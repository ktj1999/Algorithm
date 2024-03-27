def solution(elements):
    ele_set = set()
    for i in range(len(elements)):
        tmp = elements[i]
        ele_set.add(elements[i])
        for j in range(i+1, i+len(elements)):
            tmp += elements[j%len(elements)]
            ele_set.add(tmp)
    answer = len(ele_set)
    return answer