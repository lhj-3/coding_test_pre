def solution(sizes):
    first = []
    second = []
    for i in range(len(sizes)):
        
        if sizes[i][0] >= sizes[i][1]:
            first.append(sizes[i][0])
            second.append(sizes[i][1])
        else:
            first.append(sizes[i][1])
            second.append(sizes[i][0])
            
    return max(first)*max(second)
