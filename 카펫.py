# 먼저 조합 추출
# 조합에서 가능한지 확인
# 가능하면 return

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    sqrt = int(total ** (0.5))
    
    # 3부터 해야 yellow가 가능함
    for i in range(3, sqrt+1):
        if total % i == 0:
            if is_possible([total//i, i], brown):
                return [total//i, i]
    return answer

def is_possible(size, brown):
    h, w = size
    num_brown = h * 2 + (w-2) * 2    
    if brown == num_brown:
        return True
    else:
        return False
