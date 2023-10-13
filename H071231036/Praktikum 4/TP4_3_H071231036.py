def maksimum(*args):
    if len(args) == 0:
        return None 
    
    max_num = args[0]
    print (args)
    for num in args[1:]:
        if num > max_num:
            max_num = num 
    
    return max_num

result1 = maksimum(1, 2, 4, 6, 9, 3, 1, 9, 10)
print(result1) 

result2 = maksimum(0, 1, 90, 430, 23, 212, 34)
print(result2) 