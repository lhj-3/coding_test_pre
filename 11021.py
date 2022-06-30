repeat_num = int(input())
for i in range(repeat_num):
    A, B = map(int, input().split())
    print("Case #%d: %d" %(i + 1, A + B))