def dfs(numbers, visited, current, result):
    if current != "":
        num = int(current)
        if num not in result and is_decimal(num):
            result.add(num)
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            dfs(numbers, visited, current + numbers[i], result)
            visited[i] = False
            
def is_decimal(num):
    if num == 1 or num == 0:
        return False
    if num == 2:
        return True
    tmp_num = int((num**(0.5)))
    for i in range(2, tmp_num+1):
        if num % i == 0:
            return False
    return True
    
def solution(numbers):
    result = set()
    visited = [False] * len(numbers)
    dfs(numbers, visited, "", result)
    return len(result)
