import os,sys,random

# Chessmastah, started Jan 2012 by Svein Arne Roed
#
# Available at https://sites.google.com/site/marsarsite/files
#
# Contact: svein+roed 'a+t' Gmail
#
# Version 0.5 hereby released :
#
# Castling
# En passant
# Choice between Knight and Queen when promoting a Pawn
# Game now ends in a draw if:
# * only kings are left
# * no possible moves (and isn't in check)
# * 50 consecutive moves without movement of a Pawn or a capture
# Various fixes and cleanup, thanks to cProfile - more efficient code
# Play against (random) computer
#
# "AI" not rewritten to classes yet, so computer is simply picking
# a random move.
#
# Thanks to python-forum.org's users Akavall and Micseydel
# for constructive feedback.


class Player(object):

    allsquares = [(x, y) for x in range(8) for y in range(8)]
    dullmoves = 0

    def __init__(self, colour, nature, name):

        self.colour   = colour
        self.nature   = nature
        self.name     = name
        self.can_castle_long_this_turn  = False
        self.can_castle_short_this_turn = False
        self.playedturns = 0

    def __str__(self):
        if self.nature is 'AI':
            return self.name+' ('+self.nature+')'+' as '+self.colour
        else:
            return self.name+' as '+self.colour

    def set_opponent(self, opponent):
        self.opponent = opponent

    def getpieces(self, board):
        return [pos for pos in board if board[pos].colour is self.colour]

    def potentialtargets(self, playerspieces):
        return [pos for pos in self.allsquares if pos not in playerspieces]

    def kingpos(self, board):
        for mine in self.getpieces(board):
            if board[mine].piecename is 'k':
                return mine

    def validmoves(self, board):
        self.set_castling_flags(board)

        mypieces=self.getpieces(board)
        for mine in mypieces:
            for target in self.potentialtargets(mypieces):
                if self.canmoveto(board, mine, target):
                    if not self.makesuscheck(mine, target, board):
                        yield (mine, target)

    def set_castling_flags(self, board):
        kingpos = self.kingpos(board)
        if self.king_can_castle(board, kingpos):

            if self.rook_can_castle_long(board, kingpos):
                self.can_castle_long_this_turn = True
            else:
                self.can_castle_long_this_turn = False

            if self.rook_can_castle_short(board, kingpos):
                self.can_castle_short_this_turn = True
            else:
                self.can_castle_short_this_turn = False
        else:
            self.can_castle_long_this_turn = False
            self.can_castle_short_this_turn = False

    def king_can_castle(self, board, kingpos):
        if board[kingpos].nrofmoves is 0 and not self.isincheck(board):
            return True

    def rook_can_castle_long(self, board, kingpos):
        if self.longrook in board and board[self.longrook].nrofmoves is 0:
            if self.hasclearpath(self.longrook, kingpos, board):
                tmptarget = (kingpos[0],kingpos[1]-1)
                if not self.makesuscheck(kingpos, tmptarget, board):
                    return True

    def rook_can_castle_short(self, board, kingpos):
        if self.shortrook in board and board[self.shortrook].nrofmoves is 0:
            if self.hasclearpath(self.shortrook, kingpos, board):
                tmptarget = (kingpos[0],kingpos[1]+1)
                if not self.makesuscheck(kingpos, tmptarget, board):
                    return True

    def getposition(self, move):
        startcol  = int(ord(move[0].lower())-97)
        startrow  = int(move[1])-1
        targetcol = int(ord(move[2].lower())-97)
        targetrow = int(move[3])-1
        start     = (startrow, startcol)
        target    = (targetrow, targetcol)

        return start, target

    def reacheddraw(self, board):

        if not list(self.validmoves(board)) and not self.isincheck(board):
            return True

        if len(list(self.getpieces(board))) == \
           len(list(self.opponent.getpieces(board))) == 1:
            return True

        if Player.dullmoves/2 == 50:
            if self.nature is 'AI':
                return True
            else:
                if raw_input("Call a draw? (yes/no) : ") in ['yes','y','Yes']:
                    return True

    def ischeckmate(self, board):

        if not list(self.validmoves(board)) and self.isincheck(board):
            return True

    def turn(self, board):
       
        turnstring = "\n%s's turn," % self.name
        warning = " *** Your King is in check *** "

        if self.isincheck(board):
            turnstring = turnstring + warning

        return turnstring

    def getmove(self, board):

        print "\n"
        while True:

            # If player is computer, get a move from computer
            if self.nature is 'AI':
                #return aiengine.getAImove(self, board)
                return random.choice(list(self.validmoves(board)))

            else:
                # Player is human, get a move from input
                move=raw_input("\nMake a move : ")
                if move == 'exit':
                    break

                else:
                    start, target = self.getposition(move)
                    if (start, target) in self.validmoves(board):
                        return start, target
                    else:
                        raise IndexError

    def makesuscheck(self, start, target, board):
        # Make temporary move to test for check
        self.domove(board, start, target)

        retval = self.isincheck(board)
        
        # Undo temporary move
        self.unmove(board, start, target)

        return retval

    def isincheck(self, board):
        kingpos = self.kingpos(board)
        for enemy in self.opponent.getpieces(board):
            if self.opponent.canmoveto(board, enemy, kingpos):
                return True

    def domove(self, board, start, target):

        self.savedtargetpiece = None
        if target in board:
            self.savedtargetpiece = board[target]

        board[target] = board[start]
        board[target].position = target
        del board[start]

        board[target].nrofmoves += 1

        if board[target].piecename is 'p' and not self.savedtargetpiece:

            if abs(target[0]-start[0]) == 2:
                board[target].turn_moved_twosquares = self.playedturns

            elif abs(target[1]-start[1]) == abs(target[0]-start[0]) == 1:
                # Pawn has done en passant, remove the victim
                if self.colour is 'white':
                    passant_victim = (target[0]-1, target[1])
                else:
                    passant_victim = (target[0]+1, target[1])
                self.savedpawn = board[passant_victim]
                del board[passant_victim]

        if board[target].piecename is 'k':
            if target[1]-start[1] == -2:
                # King is castling long, move longrook
                self.domove(board, self.longrook, self.longrook_target)
            elif target[1]-start[1] == 2:
                # King is castling short, move shortrook
                self.domove(board, self.shortrook, self.shortrook_target)

    def unmove(self, board, start, target):

        board[start] = board[target]
        board[start].position = start
        if self.savedtargetpiece:
            board[target] = self.savedtargetpiece
        else:
            del board[target]

        board[start].nrofmoves -= 1

        if board[start].piecename is 'p' and not self.savedtargetpiece:

            if abs(target[0]-start[0]) == 2:
                del board[start].turn_moved_twosquares

            elif abs(target[1]-start[1]) == abs(target[0]-start[0]) == 1:
                # We have moved back en passant Pawn, restore captured Pawn
                if self.colour is 'white':
                    formerpos_passant_victim = (target[0]-1, target[1])
                else:
                    formerpos_passant_victim = (target[0]+1, target[1])
                board[formerpos_passant_victim] = self.savedpawn

        if board[start].piecename is 'k':
            if target[1]-start[1] == -2:
                # King's castling long has been unmoved, move back longrook
                self.unmove(board, self.longrook, self.longrook_target)
            elif target[1]-start[1] == 2:
                # King's castling short has been unmoved, move back shortrook
                self.unmove(board, self.shortrook, self.shortrook_target)

    def pawnpromotion(self, board, target):
        if self.nature is 'AI':
            # See if Knight makes opponent checkmate
            board[target].promote('kn')
            if self.opponent.ischeckmate(board):
                return
            else:
                promoteto = 'q'
                
        else:
            promoteto = 'empty'
            while promoteto.lower() not in ['kn','q']:
                promoteto = \
                raw_input("You may promote your pawn:\n[Kn]ight [Q]ueen : ")

        board[target].promote(promoteto)

    def hasclearpath(self, start, target, board):

        startcol, startrow = start[1], start[0]
        targetcol, targetrow = target[1], target[0]

        if abs(startrow - targetrow) <= 1 and abs(startcol - targetcol) <= 1:
            # The base case
            return True
        else:
            if targetrow > startrow and targetcol == startcol:
                # Straight down
                tmpstart = (startrow+1,startcol)
            elif targetrow < startrow and targetcol == startcol:
                # Straight up
                tmpstart = (startrow-1,startcol)
            elif targetrow == startrow and targetcol > startcol:
                # Straight right
                tmpstart = (startrow,startcol+1)
            elif targetrow == startrow and targetcol < startcol:
                # Straight left
                tmpstart = (startrow,startcol-1)
            elif targetrow > startrow and targetcol > startcol:
                # Diagonal down right
                tmpstart = (startrow+1,startcol+1)
            elif targetrow > startrow and targetcol < startcol:
                # Diagonal down left
                tmpstart = (startrow+1,startcol-1)
            elif targetrow < startrow and targetcol > startcol:
                # Diagonal up right
                tmpstart = (startrow-1,startcol+1)
            elif targetrow < startrow and targetcol < startcol:
                # Diagonal up left
                tmpstart = (startrow-1,startcol-1)

            # If no pieces in the way, test next square
            if tmpstart in board:
                return False
            else:
                return self.hasclearpath(tmpstart, target, board)

    def canmoveto(self, board, start, target):

        startpiece = board[start].piecename.upper()

        if startpiece == 'R' and not self.check_rook(start, target):
            return False
        elif startpiece == 'KN' and not self.check_knight(start, target):
            return False
        elif startpiece == 'P' and not self.check_pawn(start, target, board):
            return False
        elif startpiece == 'B' and not self.check_bishop(start, target):
            return False
        elif startpiece == 'Q' and not self.check_queen(start, target):
            return False
        elif startpiece == 'K' and not self.check_king(start, target):
            return False

        # Only the 'Knight' may jump over pieces
        if startpiece in 'RPBQK':
            if not self.hasclearpath(start, target, board):
                return False

        return True

    def check_rook(self, start, target):

        # Check for straight lines of movement(start/target on same axis)
        if start[0] == target[0] or start[1] == target[1]:
            return True

    def check_knight(self, start, target):

        # 'Knight' may move 2+1 in any direction and jump over pieces
        if abs(target[0]-start[0]) == 2 and abs(target[1]-start[1]) == 1:
            return True
        elif abs(target[0]-start[0]) == 1 and abs(target[1]-start[1]) == 2:
            return True

    def check_pawn(self, start, target, board):

        # Disable backwards and sideways movement
        if 'white' in self.colour and target[0] < start[0]:
            return False
        elif 'black' in self.colour and target[0] > start[0]:
            return False
        if start[0] == target[0]:
            return False

        if target in board:
            # Only attack if one square diagonaly away
            if abs(target[1]-start[1]) == abs(target[0]-start[0]) == 1:
                return True
        else:
            # Make peasants move only one forward (except first move)
            if start[1] == target[1]:
                # Normal one square move
                if abs(target[0]-start[0]) == 1:
                    return True
                # 1st exception to the rule, 2 square move first time
                if board[start].nrofmoves is 0:
                    if abs(target[0]-start[0]) == 2:
                        return True

            # 2nd exception to the rule, en passant
            if start[0] == self.enpassantrow:
                if abs(target[0]-start[0]) == 1:
                    if abs(target[1]-start[1]) == 1:
                        if target[1]-start[1] == -1:
                            passant_victim = (start[0], start[1]-1)
                        elif target[1]-start[1] == 1:
                            passant_victim = (start[0], start[1]+1)
                        if passant_victim in board and \
                        board[passant_victim].colour is not self.colour and \
                        board[passant_victim].piecename is 'p'and \
                        board[passant_victim].nrofmoves == 1 and \
                        board[passant_victim].turn_moved_twosquares == \
                        self.playedturns-1:
                            return True

    def check_bishop(self, start, target):

        # Check for non-horizontal/vertical and linear movement
        if abs(target[1]-start[1]) == abs(target[0]-start[0]):
            return True

    def check_queen(self, start, target):

        # Will be true if move can be done as Rook or Bishop
        if self.check_rook(start, target) or self.check_bishop(start, target):
            return True

    def check_king(self, start, target):

        # King can move one square in any direction
        if abs(target[0]-start[0]) <= 1 and abs(target[1]-start[1]) <= 1:
            return True

        # ..except when castling
        if self.can_castle_short_this_turn:
            if target[1]-start[1] == 2 and start[0] == target[0]:
                return True

        if self.can_castle_long_this_turn:
            if target[1]-start[1] == -2 and start[0] == target[0]:
                return True

class Piece(object):

    def __init__(self, piecename, position, player):
        self.colour    = player.colour
        self.nature    = player.nature
        self.piecename = piecename
        self.position  = position
        self.nrofmoves = 0

    def __str__(self):
        if self.colour is 'white':
            if self.piecename is 'p':
                return 'WP'
            else:
                return self.piecename.upper()
        else:
            return self.piecename

    def canbepromoted(self):
        if str(self.position[0]) in '07':
            return True

    def promote(self, to):
        self.piecename = to.lower()


class Game(object):

    def __init__(self, playera, playerb):

        self.board = dict()
        for player in [playera, playerb]:
            if player.colour is 'white':
                brow, frow = 0, 1
                player.enpassantrow = 4
            else:
                brow, frow = 7, 6
                player.enpassantrow = 3

            player.longrook  = (brow, 0)
            player.longrook_target = \
            (player.longrook[0], player.longrook[1]+3)
            
            player.shortrook = (brow, 7)
            player.shortrook_target = \
            (player.shortrook[0], player.shortrook[1]-2)
            

            [self.board.setdefault((frow,x), Piece('p', (frow,x), player)) \
            for x in range(8)]
            [self.board.setdefault((brow,x), Piece('r', (brow,x), player)) \
            for x in [0,7]]
            [self.board.setdefault((brow,x), Piece('kn',(brow,x), player)) \
            for x in [1,6]]
            [self.board.setdefault((brow,x), Piece('b', (brow,x), player)) \
            for x in [2,5]]
            self.board.setdefault((brow,3),  Piece('q', (brow,3), player))
            self.board.setdefault((brow,4),  Piece('k', (brow,4), player))

    def printboard(self):

        topbottom=['*','a','b','c','d','e','f','g','h','*']
        sides=['1','2','3','4','5','6','7','8']
        tbspacer=' '*6
        rowspacer=' '*5
        cellspacer=' '*4
        empty=' '*3

        print
        for field in topbottom:
            print "%4s" % field,
        print

        print tbspacer+("_"*4+' ')*8

        for row in range(8):
            print(rowspacer+(('|'+cellspacer)*9))
            print "%4s" % sides[row],('|'),
            for col in range(8):
                if (row, col) not in self.board:
                    print empty+'|',
                else:
                    print "%2s" % self.board[(row, col)],('|'),
            print "%2s" % sides[row],
            print
            print rowspacer+'|'+(("_"*4+'|')*8)
        print

        for field in topbottom:
            print "%4s" % field,

        print "\n"

    def refreshscreen(self, player):
        if player.colour is 'white':
            playera, playerb = player, player.opponent
        else:
            playera, playerb = player.opponent, player
        os.system('clear')
        print "   Now playing: %s vs %s" % (playera, playerb)
        self.printboard()

    def run(self, player):

        self.refreshscreen(player)

        while True:

            print player.turn(self.board)

            try:
                start, target = player.getmove(self.board)

            except (IndexError, ValueError):
                self.refreshscreen(player)
                print "\n\nPlease enter a valid move."

            except TypeError:
                # No start, target if user exit
                break

            else:
                if target in self.board or self.board[start].piecename is 'p':
                    Player.dullmoves = 0
                else:
                    Player.dullmoves += 1

                player.domove(self.board, start, target)
                player.playedturns += 1

                # Check if there is a Pawn up for promotion
                if self.board[target].piecename is 'p':
                    if self.board[target].canbepromoted():
                        player.pawnpromotion(self.board, target)

                player = player.opponent

                if player.reacheddraw(self.board):
                    return 1, player

                elif player.ischeckmate(self.board):
                    return 2, player

                else:
                    self.refreshscreen(player)

    def end(self, player, result):

        looser = player.name
        winner = player.opponent.name

        if result == 1:
            endstring = "\n%s and %s reached a draw." % (winner, looser)
        elif result == 2:
            endstring = "\n%s put %s in checkmate." % (winner, looser)

        os.system('clear')
        self.printboard()

        return endstring

def newgame():

    os.system('clear')

    print """
      Welcome to Chessmastah, the fantastic console chess environment.
      Please type in the name of the contestants.

      If you want to play against the computer, leave one name blank
      and press [Enter].

      Or if you fancy, leave both names blank and watch the computer
      duke it out with itself.
      """

    playera, playerb = getplayers()
    playera.set_opponent(playerb)
    playerb.set_opponent(playera)

    game = Game(playera, playerb)

    infostring = \
    """
    Very well, %s and %s, let's play.
    
    Player A: %s (uppercase)
    Player B: %s (lowercase)
    (Use moves on form 'a2b3' or type 'exit' at any time.) """
    print infostring % (playera.name, playerb.name, playera, playerb)

    raw_input("\n\nPress [Enter] when ready")

    # WHITE starts
    player = playera

    try:
        result, player = game.run(player)

    except TypeError:
        # No result if user exit
        pass

    else:
        print game.end(player, result)
        raw_input("\n\nPress any key to continue")

def getplayers():

    ainames = ['chesschick','foxysquare']

    name1 = raw_input("\nPlayer A (white): ")
    if not name1:
        playera = Player('white', 'AI', ainames[0])
    else:
        playera = Player('white', 'human', name1)

    name2 = raw_input("\nPlayer B (black): ")
    if not name2:
        playerb = Player('black', 'AI', ainames[1])
    else:
        playerb = Player('black', 'human', name2)

    return playera, playerb

def main():
    """ Kickstart everything. Display menu after game has ended. """
    
    menu="""
    Thanks for playing the Chessmastah, would you like to go again?
    Press [Enter] to play again or type 'exit'.  >>  """

    try:
        while True:
            newgame()

            choice=raw_input(menu)

            if choice == 'exit':
                print "\nAs you wish. Welcome back!"
                break

    except KeyboardInterrupt:
        sys.exit("\n\nOkok. Aborting.")


if __name__ == '__main__':
    #cProfile.run('main()')
    main()
