cnt = 0
result = 0


def solution(mat):
    def expand_sequence(r, c, m, last_element):
        if is_not_valid_cell(r, c, m):
            return

        current_element = m[r][c]

        if current_element != last_element or current_element == 'v':
            return

        global cnt
        cnt = cnt + 1
        m[r][c] = 'v'

        global result
        if result < cnt:
            result = cnt

        expand_sequence(r - 1, c, m, current_element)
        expand_sequence(r + 1, c, m, current_element)
        expand_sequence(r, c - 1, m, current_element)
        expand_sequence(r, c + 1, m, current_element)

    def find_sequences(m):
        for i in range(len(m)):
            for j in range(len(m[i])):
                global cnt
                cnt = 0
                last_element = m[i][j]
                expand_sequence(i, j, m, last_element)

    def is_not_valid_cell(r, c, m):
        if 0 <= r < len(m) and 0 <= c < len(m[0]):
            return False
        else:
            return True

    find_sequences(mat)
    global result
    print(result)
    result = 0
