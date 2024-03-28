def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
        return answer

    for i in s:
        if i not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            answer = False
            break

    return answer