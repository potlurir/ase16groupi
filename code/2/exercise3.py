""" Write a function named right_justify that takes a string named s as a
parameter and prints the string with enough leading spaces so that the last
letter of the string is in column 70 of the display. """


def exercise3():
    def right_justify(s):
        print "%s%s" % (70*" ", s)

    right_justify("team I")
