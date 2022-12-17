
def all_diagonals(tdlist):
    diags = []
    buffer = 'B'
    buff_list_right = []
    buff_list_left = []
    for r in range(len(tdlist)):
        buff_list_right += [r*[buffer] + tdlist[r][:] + (len(tdlist)-1-r)*[buffer]]
        buff_list_left += [(len(tdlist)-1-r)*[buffer] + tdlist[r][:] + r*[buffer]]
    
    for i in range(len(buff_list_right[0])):
        diags += [[buff_list_right[x][i] for x in range(len(buff_list_right)) if buff_list_right[x][i] is not 'B']]
        diags += [[buff_list_left[x][i] for x in range(len(buff_list_left)) if buff_list_left[x][i] is not 'B']]
                  
        
    return diags



tester = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

all_diagonals(tester)