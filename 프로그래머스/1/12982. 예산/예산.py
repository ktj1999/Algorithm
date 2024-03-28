def solution(d, budget):
    d.sort()
    for i, j in enumerate(d):
        budget -= j
        if budget < 0:
            return i
        
    answer = len(d)
    
    return answer