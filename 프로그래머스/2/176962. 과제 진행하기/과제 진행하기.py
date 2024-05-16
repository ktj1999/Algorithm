def solution(plans):
    stk = []
    answer = []
    
    # 시간을 int로 변경
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60 + m
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key=lambda x: x[1]) # 오름차순
    
    for i in range(len(plans)-1):
        stk.append([plans[i][0], plans[i][2]])
        diff = plans[i+1][1] - plans[i][1]
        
        while stk and diff:
            if stk[-1][1] <= diff:
                name, time = stk.pop() # pop
                diff -= time # 다음과제까지 남은 시간
                answer.append(name) # 과제완료
            else: # 다음 과제시간까지 못 끝내면
                stk[-1][1] -= diff # 남은 과제 시간 저장
                diff = 0 # 다음과제 해야하니까 0
                
    answer.append(plans[-1][0])
    
    for i in range(len(stk)):
        answer.append(stk[~i][0]) # 역순 append
        
    return answer