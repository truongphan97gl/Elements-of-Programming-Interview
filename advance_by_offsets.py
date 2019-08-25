from test_framework import generic_test


def can_reach_end(A):
    farest, last_index = 0, len(A) - 1
    
    i = 0
    while i <= farest and farest <= last_index:
        farest = max(farest, A[i] + i)
        i += 1
    return farest >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
