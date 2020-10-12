'''
Created on 2020 Oct 9

@author: timothy
'''

import string


"""
----------------------------------------------------
Parameters:   filename (str)
Return:       contents (str)
Description:  Utility function to read contents of a file
              Can be used to read plaintext or ciphertext
---------------------------------------------------
"""
def file_to_text(filename):
    infile = open(filename,'r', encoding="ISO-8859-15")
    contents = infile.read()
    infile.close()
    return contents

"""
----------------------------------------------------
Parameters:   text (str)
              filename (str)            
Return:       no returns
Description:  Utility function to write any given text to a file
              If file already exist, previous content will be erased
---------------------------------------------------
"""
def text_to_file(text, filename):
    outfile = open(filename,'w', encoding="ISO-8859-15")
    outfile.write(text)
    outfile.close()
    return

"""
----------------------------------------------------
Parameters:   r: #rows (int)
              c: #columns (int)
              fill (str,int,double)
Return:       empty matrix (2D List)
Description:  Create an empty matrix of size r x c
              All elements initialized to fill
---------------------------------------------------
"""
def new_matrix(r,c,fill):
    r = r if r >= 2 else 2
    c = c if c>=2 else 2
    return [[fill] * c for i in range(r)]

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       None
# Description:  prints a matrix each row in a separate line
                items separated by a tab
#               Assumes given parameter is a valid matrix
---------------------------------------------------
"""
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='\t')
        print()
    return

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       text (string)
# Description:  convert a 2D list of characters to a string
#               left to right, then top to bottom
#               Assumes given matrix is a valid 2D character list
---------------------------------------------------
"""
def matrix_to_string(matrix):
    text = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            text+=matrix[i][j]
    return text

"""
----------------------------------------------------
# Parameters:   marix (2D List)
# Return:       h1 (heuristic 1)
# Description:  Checks to see how many values are not
#               correct space
---------------------------------------------------
"""
def check_h1_eight(matrix):
     
    h1 = 0
    
    if matrix[0][0] != 1:
        h1 += 1
    
    if matrix[0][1] != 2:
        h1 += 1
        
    if matrix[0][2] != 3:
        h1 += 1
        
    if matrix[1][0] != 4:
        h1 += 1
    
    if matrix[1][1] != 5:
        h1 += 1
        
    if matrix[1][2] != 6:
        h1 += 1
        
    if matrix[2][0] != 7:
        h1 += 1
    
    if matrix[2][1] != 8:
        h1 += 1
        
    if matrix[2][2] != '':
        h1 += 1
        
    return h1

                      
        