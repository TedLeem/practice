

def getPrimaryNum_Eratos(N): 
    nums = [True] * (N + 1) 
    for i in range(2, len(nums) // 2 + 1): 
        if nums[i] == True: 
            for j in range(i+i, N, i): 
                nums[j] = False 
    return [[i for i in range(2, N) if nums[i] == True], nums] 

primary_nums = getPrimaryNum_Eratos(1000000)[0] 
primary_bools = getPrimaryNum_Eratos(1000000)[1] 
while(True): 
    N = int(input()) 
    if N == 0: 
        break 
    for i in range(N // 2): 
        if primary_bools[N-primary_nums[i]] == True: 
            print("{} = {} + {}".format(N, primary_nums[i], N-primary_nums[i])) 
            break

