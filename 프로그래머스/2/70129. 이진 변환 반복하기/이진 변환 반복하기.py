def solution(s):
    t, num = 0, 0

    while not s == "1":
        num += s.count("0")
        s = s.replace("0", "")
        s = bin(int(len(s)))[2:]
        t += 1

    answer = [t,num]
    
    return answer