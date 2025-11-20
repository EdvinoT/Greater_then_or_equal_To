def sum():
    sum_list=[1,6,4,8,10,-4,-7,4,6,-6,]
    total = 0
    for number in sum_list:
        if number > 0:
            total += number
    print(sum_list)
    print("Sum of positive numbers is:")
    return total 
    
print(sum())

