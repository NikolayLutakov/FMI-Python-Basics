from tests.test_1 import create_test_1, test_1
from tests.test_2 import create_test_2, test_2
from tests.test_3 import create_test_3, test_3
from tests.test_4 import create_test_4, test_4
import sys

arguments = sys.argv[1:]


def one():
    test_1()


def two():
    test_2()


def three():
    test_3()


def four():
    test_4()


def switch(argument):
    switcher = {
        "test_1": one,
        "test_2": two,
        "test_3": three,
        "test_4": four,
    }
    func = switcher.get(argument)
    func()


def create_tests():
    create_test_1()
    create_test_2()
    create_test_3()
    create_test_4()


create_tests()

for arg in range(len(arguments)):
    switch(arguments[arg])
