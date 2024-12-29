import sys

h, w = list(map(int, input().split()))
# split의 " " 차이가 속도에 영향을 미침, " " 안하면 통과 하면 런타임 에러
grid_sum = [0] * h
for i in range(h):
    tmp = list(map(int, input().split()))
    grid_sum[i] = sum(tmp)
    
f_l, f_r = list(map(int, input().split()))
s_l, s_r = list(map(int, input().split()))

for i in range(f_l-1, f_r):
    if grid_sum[i] !=0:
        grid_sum[i] -= 1

for i in range(s_l-1, s_r):
    if grid_sum[i] !=0:
        grid_sum[i] -= 1

print(sum(grid_sum))
