
import random
from pygame import * 

def choose_random_max_column(scores):
    indexlist = []
    for i in range(len(scores)):
        if scores[i] == max(scores):
            indexlist += [i]
    choice = random.choice(indexlist)
    return choice
            

class Player:
    
    def __init__(self, checker):
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        s = 'Player has ' + self.checker + ' checker and has made ' + self.num_moves
        return s
    
    def next_move(self, b, column):
        self.num_moves += 1
        b.add_checker(self.checker, column)
        
    def opponent_checker(self):
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        

class RandomPlayer(Player):
    
    def __init__(self, checker):
        super().__init__(checker)
        
    def next_move(self,b):
        self.num_moves += 1
        while True:
            column_choice = random.choice(range(b.get_cols()))
            if not b.is_col_full(column_choice):
                break
            
        b.add_checker(self.checker, column_choice)
   
class AIPlayer(Player):
    
    def __init__(self, checker, lookahead):
        super().__init__(checker)
        self.lookahead = lookahead
    
    def scores_for(self, b):
        scores = [50]*b.get_cols()
        for i in range(b.get_cols()):
            if b.is_col_full(i):
                scores[i] = -1
            elif self.lookahead == 0:
                scores = [50] * b.get_cols()
            elif self.lookahead == 1:
                b.add_checker(self.checker, i)
                if b.is_win_for(self.checker):
                    scores[i] = 100
                else:
                    scores[i] = 50
                b.remove_checker(self.checker,i)
                
                
            elif self.lookahead > 1:
                b.add_checker(self.checker, i)
                tempop = AIPlayer(self.opponent_checker(), self.lookahead-1)
                opp_scores = tempop.scores_for(b)
                
                max_scores = max(opp_scores)
                
                if max_scores == 100:
                    scores[i] = 0
                elif max_scores == 0:
                    scores[i] = 100
                else:
                    scores[i] = 50
                    
                if b.is_win_for(self.checker):
                    scores[i] = 100

                b.remove_checker(self.checker,i)
        
        return scores
        
    def next_move(self, b):
        scores = self.scores_for(b)
        #max_score_list = max(scores)
        #max_col = scores.index(max_score_list)
        
        max_col = choose_random_max_column(scores)
        #b.add_checker(self.checker, max_col)
        b.add_checker(self.checker, max_col)
    
    
        
    
    
    
