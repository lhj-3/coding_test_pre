input_string = input()

N = len(input_string)

for i in range(N // 10+1):
    if len(input_string[i:]) >= 10:
        print(input_string[i * 10: i * 10  + 10])
    else:
        print(input_string[i * 10:])