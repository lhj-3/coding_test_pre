# ""으로 aws를 만들면 문자열 불변 속성으로 인한 재할당 비용이 듬
# append는 O(1)이고, 마지막에 O(N)이므로 위보다 짧게 듬 

import sys

N = int(input())
aws = []
for _ in range(N):
    S, T = input().split()
    for j in range(len(S)):
        if 'x' == S[j] or 'X' == S[j]:
            aws.append(T[j].upper())
            break
print(''.join(aws))
