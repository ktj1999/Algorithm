def solution(cards1, cards2, goal):
    answer = "Yes"
    c1, c2 = 0, 0
    usedc1, usedc2 = set(), set()
    for i in goal:
        if i in usedc1 and i in usedc2:
            answer = "No"
            break
        elif c1 < len(cards1) and i == cards1[c1]:
            c1 += 1
            usedc1.add(i)
        elif c2 < len(cards2) and i == cards2[c2]:
            c2 += 1
            usedc2.add(i)
        else:
            answer = "No"
            break
    return answer