def solution(nums):
    
    store = dict()
    
    for i in nums:
        if i in store.keys():
            store[i] = store[i] + 1
        else:
            store[i] = 1

    full_nums = len(nums) // 2
    class_num = len(store.keys())
    
    if full_nums > class_num:
        return class_num
    else:
        return full_nums