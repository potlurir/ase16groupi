from __future__ import print_function

""" http://www.greenteapress.com/thinkpython/html/thinkpython004.html
Exercise 1  
Move the last line of this program to the top, so the function call appears
before the definitions. Run the program and see what error message you get.

Ans >>
We get a NameError because, repeat_lyrics is not defined when it is called

--------------------------------------------------------------------------
Exercise 2
Move the function call back to the bottom and move the definition of
print_lyrics after the definition of repeat_lyrics.
What happens when you run this program?

Ans>>
The program runs successfully because when the actual function call
happens both functions "repeat_lyrics" and "print_lyrics" are defined.
"""


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


def print_lyrics():
    print ("I'm a lumberjack, and i'm okay")
    print ("I sleep all night and I work all day.")

repeat_lyrics()

""" Exercise 3.3
Python provides a built-in function called len that returns the length of a
string, so the value of len('allen') is 5.
Write a function named right_justify that takes a string named s as a
parameter and prints the string with enough leading spaces so that the last
letter of the string is in column 70 of the display.

>>> right_justify('allen')
"""
print("\n\n%s Exercise 3.3 %s" % ('-' * 10, '-' * 10))


def right_justify(s):
    print(s.rjust(70))

right_justify("pritesh")

print("\n\n%s Exercise 3.4 %s" % ('-' * 10, '-' * 10))


def do_twice(f, val):
    f(val)
    f(val)


def print_spam():
    print('spam')


def print_twice(inp_str):
    print(inp_str)
    print(inp_str)

do_twice(print_twice, 'spam')


def do_four(fn, val):
    do_twice(fn, val)
    do_twice(fn, val)

print("\n")
do_four(print_twice, 'NOTspam')


""" Exercise 3.5 """
print("\n\n%s Exercise 3.5 %s" % ('-' * 10, '-' * 10))

line_1 = ('+' + (''.join(' - '*4))) * 2 + '+'
line_2 = '/'.ljust(13) + '/' + '/'.rjust(13)


def draw_2by2():
    a = line_1 + '\n'
    b = line_2 + '\n'
    print("{0}{1}{1}{1}{1}{0}{1}{1}{1}{1}{0}".format(a, b))


def draw_2by4():
    a = line_1[:-1] * 2 + '+'
    b = line_2[:-1] * 2 + '/'
    for _ in range(4):
        print (a)
        for _ in range(4):
            print (b)
    print (a)

draw_2by2()
print('\n\n')
draw_2by4()
