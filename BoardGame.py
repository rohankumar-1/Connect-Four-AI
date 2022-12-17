
def four_in_a_row(colrow, checker):
    counter = 0
    for i in colrow:
        if i==checker:
            counter += 1
        else:
            counter = 0
        if counter == 4:
            break
    
    if counter >= 4:
        return True
    else:
        return False
    
def all_diagonals(tdlist):
    diags = []
    buffer = 'B'
    buff_list_right = []
    buff_list_left = []
    for r in range(len(tdlist)):
        buff_list_right += [r*[buffer] + tdlist[r][:] + (len(tdlist)-1-r)*[buffer]]
        buff_list_left += [(len(tdlist)-1-r)*[buffer] + tdlist[r][:] + r*[buffer]]
    
    for i in range(len(buff_list_right[0])):
        diags += [[buff_list_right[x][i] for x in range(len(buff_list_right)) if buff_list_right[x][i] != 'B']]
        diags += [[buff_list_left[x][i] for x in range(len(buff_list_left)) if buff_list_left[x][i] != 'B']]
                  
        
    return diags
    
    
class Board:
    
    def __init__(self, row_param, col_param):
        self.row = row_param
        self.col = col_param
        self.slots = [[' ' for a in range(self.col)] for b in range(self.row)]
        
    
    def __repr__(self):
        s = ''
        for a in range(self.row):
            s += '|'
            for b in range(self.col):
                s += self.slots[a][b] + '|'
            s += '\n'
        
        for c in range(self.col*2 +1):
            s += '-'
        s += '\n '
        for d in range(self.col):
            s += str(d+1)+' '
        
        return s
    
    def add_checker(self, checker, column):
        
        target_row = -1
        for i in range(self.row):
            if self.slots[i][column]== ' ':
                target_row = i
        
        self.slots[target_row][column] = checker
        
    def clear(self):
        self.slots = [[' ' for a in range(self.col)] for b in range(self.row)]
        
    def is_win_for(self, checker):
        win = False
        
        #checking verticals
        for i in range(self.col):
            temp_col_list = [self.slots[x][i] for x in range(self.row)]
            win = four_in_a_row(temp_col_list, checker)
            if win==True:
                return win
                break
            
        #checking horizontals
        for j in range(self.row):
            temp_row_list = [self.slots[j][x] for x in range(self.col)]
            win = four_in_a_row(temp_row_list, checker)
            if win==True:
                return win
                break
           
        cleandiags = [x for x in all_diagonals(self.slots) if len(x)>=4]
        for k in cleandiags:
            win = four_in_a_row(k, checker)
            if win==True:
                return win
                break
        
        return False
    
    def get_rows(self):
        return self.row
    
    def get_cols(self):
        return self.col
    
    def is_col_full(self, column):
        empty = 0
        for d in range(self.row):
            if self.slots[d][column]==' ':
                empty += 1   
        return bool(not empty)
    
    def all_full(self):
       empty = 0
       for d in range(self.col):
           if not self.is_col_full(d):
               empty += 1
       return bool(not empty)
   
    def remove_checker(self, checker, col):
        for i in range(self.row):
            if self.slots[i][col] == checker:
                self.slots[i][col] = ' '
                break
                
                
            
            
            
            
    
    
            

            
        
        
    
    