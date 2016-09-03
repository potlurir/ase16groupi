""" Move the last line of this program to the top, so the function call
appears before the definitions. Run the program and see what error message you
get. """


def exercise1():

    repeat_lyrics()

    def print_lyrics():
        print "I'm a lumberjack, and I'm okay."
        print "I sleep all night and I work all day."

    def repeat_lyrics():
        print_lyrics()
        print_lyrics()

if __name__ == '__main__':
    exercise1()
