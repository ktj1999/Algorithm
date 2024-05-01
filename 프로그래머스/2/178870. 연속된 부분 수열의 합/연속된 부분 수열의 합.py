def solution(sequence, k):
    answer = [0, len(sequence)-1]
    mn = len(sequence)

    i, seq = 0, 0

    for j in range(len(sequence)):
        seq += sequence[j]

        while seq > k:
            seq -= sequence[i]
            i += 1

        if seq == k and j - i < mn:
            answer = [i, j]
            mn = j - i

    return answer