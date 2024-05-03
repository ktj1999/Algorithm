def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    # 배열을 뒤에서부터 순회
    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()  # 스택에서 원소를 제거하여 뒷 큰수를 찾음
        if stack:  # 스택이 비어있지 않으면 현재 원소의 뒷 큰수를 찾은 것
            answer[i] = stack[-1]
        stack.append(numbers[i])  # 현재 원소를 스택에 추가하여 다음 원소의 뒷 큰수를 찾을 때 활용
    
    return answer