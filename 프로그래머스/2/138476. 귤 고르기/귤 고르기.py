def solution(k, tangerine):
    answer = 1
    lst1 = [0] * max(tangerine)
    dict1 = {}

    for i in tangerine:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    lst1 = list(dict1.values())
    lst1.sort()

    max_sum = 0

    for i in range(len(lst1) - 1, -1, -1):
        max_sum+=lst1[i]

        if max_sum >=k:
            return answer
        answer += 1

    return answer
