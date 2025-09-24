max_value = 0
for i in range (999 , 1 , -1):
    for j in range(999 , 1 , -1):
        current_value = i*j
        List = list(str(current_value))
        if List == List[::-1] and  current_value > max_value:
            max_value = current_value
print (max_value)
