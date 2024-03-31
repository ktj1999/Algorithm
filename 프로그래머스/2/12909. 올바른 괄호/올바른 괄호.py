def solution(s):
    answer = True
    stk = []
    
    if s[0] == ")":
        return False
    
    for i in s:
        if len(stk) == 0:
            if i == "(":
                stk.append(i)
            else:
                return False
        else:
            if i == "(":
                stk.append(i)
            else:
                stk.pop()
    if len(stk) > 0:
        return False

    return True