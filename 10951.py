# 못 품, 반복 횟수를 모른다? 
# 해결 방법 ,https://velog.io/@jsw8050/%EB%B0%B1%EC%A4%80-while%EB%AC%B8-10951%EB%B2%88-AB-4-Python
# try, except 활용

while True:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break