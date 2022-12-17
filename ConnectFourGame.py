
from BoardGame import Board
from PlayerGame import Player, RandomPlayer, AIPlayer


def letsplay():
    r = int(input('Enter rows: '))
    c = int(input('Enter columns: '))
    print('(1) Human opponent')
    print('(2) Random opponent')
    print('(3) AI opponent')
    typeofop = int(input('Enter the number corresponding to the wanted opponent: '))
    
    if typeofop == 3:
        look = int(input('How much lookahead? Enter number of moves:'))                
    
    b = Board(r, c)
    print(repr(b))
    
    p1 = Player('X')
    
    if typeofop == 1:
        p2 = Player('O')
    elif typeofop == 2:
        p2 = RandomPlayer('O')
    elif typeofop == 3:
        p2 = AIPlayer('O', look)
    
    while True:
        print('It is Player',p1.checker,'\'s turn.')
        p1.next_move(b)
        print(repr(b))
        if b.is_win_for(p1.checker):
            print('Player', p1.checker,'has won.')
            break
        if b.all_full():
            print('It\'s a tie!')
            break
        print('It is Player',p2.checker,'\'s turn.')

        p2.next_move(b)
        
        print(repr(b))
        if b.is_win_for(p2.checker):
            print('Player', p2.checker,'has won.')
            break
        if b.all_full():
            print('It\'s a tie!')
            break
        
        
        
    
    
 
    
