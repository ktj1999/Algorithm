import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
answer = 0
for i in range(N):
    tmp = arr[:i] + arr[i + 1:]
    lt, rt = 0, len(tmp) - 1
    while lt < rt:
        t = tmp[lt] + tmp[rt]
        if t == arr[i]:
            answer += 1
            break
        if t < arr[i]: 
            lt += 1 
        else: 
            rt -= 1 
print(answer)