from solution_logic import solution

rows = 0
cols = 0

test_matrix_1 = []


def fill_test_matrix_1():
    for row in range(rows):
        str_arr = input().split(' ')
        line = [str(num) for num in str_arr]
        test_matrix_1.append(line)


def create_test_1():
    str_arr = input().split(' ')
    dimensions = [int(num) for num in str_arr]
    global rows
    rows = dimensions[0]
    global cols
    cols = dimensions[1]
    fill_test_matrix_1()


def test_1():
    solution(test_matrix_1)
