def solution(answers):
    aws = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    one_acc = 0
    two_acc = 0
    three_acc = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i%5]:
            one_acc += 1
        if answers[i] == two[i%8]:
            two_acc += 1
        if answers[i] == three[i%10]:
            three_acc += 1
            
    total_acc = [one_acc, two_acc, three_acc]
    max_value = max(total_acc)
    
    for i in range(3):
        if max_value == total_acc[i]:
            aws.append(i+1)
    return aws
