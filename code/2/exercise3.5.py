""" This exercise can be done using only the statements and other features
we have learned so far. Write a function that draws a grid like the
following:

+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
Hint: to print more than one value on a line, you can print a comma-separated
sequence: print '+', '-' If the sequence ends with a comma, Python leaves
the line unfinished, so the value printed next appears on the same line.
print '+', 
print '-'
The output of these statements is '+ -'.
A print statement all by itself ends the current line and goes to the
next line.

Write a function that draws a similar grid with four rows and four columns.

"""


def plusBorder(cols):
    print cols*("+" + 4*" - "), "+"

def verticalBorder(cols):
    for x in xrange(0, 4):
        print cols*("|" + 4*"   "), "|"

def printGrids(m, n):
    for i in xrange(0, m):
        plusBorder(n)
        verticalBorder(n)
        if i == m - 1:
            plusBorder(n)

printGrids(4, 4)