# 방법 1

input_string = input()

A, B = input_string.split()

print(int(A) + int(B))


# 방법 2

A, B = map(int, input().split())
print(A + B)

# map(func, interable)