def solution(n):
    answer = 0
    for i in range(1, n+1):
        total = 0
        j = i
        while total < n:
            total += j
            j += 1
            if total == n:
                answer += 1
                break
    return answer
