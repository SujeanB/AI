'''
Created on 2020 Oct 9

@author: timothy
'''

from Utilities import new_matrix, print_matrix, check_h1_eight
from random import shuffle

def task1():
    
    ran_numbers = [i for i in range(1,9)]
    ran_numbers.append('')
    shuffle(ran_numbers)
    n = 0
            
    puzzle = new_matrix(3, 3, 0)
    
    for i in range (len(puzzle)):
        for j in range (len(puzzle[i])):
            puzzle[i][j] = ran_numbers[n]
            n += 1
    
    #print(puzzle)
    #print()
    
    h1 = check_h1_eight(puzzle)
    
    print_matrix(puzzle)
    print()
    print("h1 value = ", h1)
    

def task2():
    
    ran_numbers = [i for i in range(1,16)]
    ran_numbers.append(None)
    shuffle(ran_numbers)
    n = 0
            
    eight = new_matrix(4, 4, 0)
    
    for i in range (len(eight)):
        for j in range (len(eight[i])):
            eight[i][j] = ran_numbers[n]
            n += 1
                

    print_matrix(eight)
    
task1()
#task2()