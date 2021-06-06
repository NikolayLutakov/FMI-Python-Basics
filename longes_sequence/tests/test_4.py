from solution_logic import solution

rows = 0
cols = 0

test_matrix_4 = []


def fill_test_matrix_4():
    for row in range(rows):
        str_arr = input().split(' ')
        line = [str(num) for num in str_arr]
        test_matrix_4.append(line)


def create_test_4():
    str_arr = input().split(' ')
    dimensions = [int(num) for num in str_arr]
    global rows
    rows = dimensions[0]
    global cols
    cols = dimensions[1]
    fill_test_matrix_4()


def test_4():
    solution(test_matrix_4)
