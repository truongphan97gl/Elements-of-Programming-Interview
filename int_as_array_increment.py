from test_framework import generic_test


def plus_one(A):
    # remainder = 0
    # for i in reversed(range(len(A))):
    #     if A[i] < 9:
    #         A[i] = A[i] + 1
    #         break
    #     if A[i] == 9 and i == 0:
    #         A[i] = 0
    #         A.insert(0,1)
    #     if A[i] == 9:
    #         A[i] = 0
    #         remainder = 1
    A[-1] += 1
    if A[0] == 10:
        return [0,1]
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
        if A[0] == 10:
            A[0] = 1
            A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
