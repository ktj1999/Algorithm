def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2+1):
        compressed = ""
        prev = s[0:step]    # 첫번째 문자부터 step만큼의 문자열 추출
        count = 1
        
        for j in range(step, len(s), step):     # step 만큼씩 증가하면서 검사
            if s[j:j+step] == prev:     # prev에 저장된 문자열과 동일한 문자이면
                count += 1
            else:   # 다른 문자열이 나와 압축할 수 없는 형태이면 (압축 종료)
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]  # 다시 상태 초기화
                count = 1
        
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    
    return answer