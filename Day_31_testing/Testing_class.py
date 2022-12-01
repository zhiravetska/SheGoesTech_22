# so today's class exercise is to write some tests: # TODO write at least 10 unit tests for your own functions (at least 2 different functions)
# you can use docstrings to document your functions
# or you can use unittest module

# you can use .py or .ipynb files for your tests

# TODO then run the tests and make sure they all pass

def mean(a):
    return a * a


def test_mean():

    assert mean(2) == 4
    assert mean(3) == 9

    assert mean(4) == 16
    assert mean(9) == 81


if __name__ == '__main__':
    test_mean()

if __name__ == '__main__':
    import doctest
    doctest.testmod()


def my_function(x):
    return 25 * x

    assert my_function(4) == 100


if __name__ == '__main__':
    import doctest
    doctest.testmod()
