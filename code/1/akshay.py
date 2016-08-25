import utest

@utest.ok
def add_custom():
    '''First program'''
    print '2 + 3 = ' + str(2 + 3)


@utest.ok
def fail_case():
    '''Failure test case'''
    assert 1 == 2
