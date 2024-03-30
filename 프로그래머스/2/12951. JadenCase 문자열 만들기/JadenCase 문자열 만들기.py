def solution(s):
    answer = ''
    cnt = 0
    num = [str(i) for i in range(10)]
    for i in s:
        if i != " ":
            if i in num:
                answer += i
            elif cnt == 0:
                answer += i.upper()
            else:
                answer += i.lower()
            cnt = 1
        else:
            answer += i
            cnt = 0
    return answer