def solution(N, number):
    lst = [[] for _ in range(9)]
    for i in range(1, 9):
        comb_lst = set()
        comb_lst.add(int(str(N) * i))
        for j in range(1, i):
            for comb1 in lst[i - j]:
                for comb2 in lst[j]:
                    plus = comb1 + comb2
                    minus = comb1 - comb2
                    mul = comb1 * comb2
                    if comb2 != 0:
                        div = comb1 / comb2
                        if div % 1 == 0:
                            comb_lst.add(int(div))
                    comb_lst.update([plus,mul])
                    if minus >= 0:
                        comb_lst.add(minus)
        if number in comb_lst:
            return i
        for q in comb_lst:
            lst[i].append(q)
    return -1