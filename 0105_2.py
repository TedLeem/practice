def isPrime(numTemp):
    for i in range(2,int(numTemp)):
        if(i*i <numTemp) :
            if(numTemp%i ==0):
                return False
# 여기서 모든 i에 대해 말고 입력값 n 에 대해 루트 n까지의 소수들 구한 리스트로만 해도 될듯           
        else:
            break
    return True

while(True) :
    num = int(input())
    numTemp = int(num/2) -1
    index=0
    if(num == 0):
         break
    rows,cols = (int(numTemp/2),2)
    array = [[0 for i in range(cols)]for j in range(rows)]
    for i in range(1, rows+1):
        array[i-1][0] = i
        array[i-1][1] = numTemp-i
    for i in range(0,rows):
        if isPrime(2*array[i][0]+1) and isPrime(2*array[i][1]+1):
            # 둘다 소수라면
            index = i 
            break
        else:
            if(i== rows -1) :
                print("Goldbach's conjecture is wrong")
    resultStr = "{} = {} + {}"
    result1 = 2*array[index][0] + 1
    result2 =2*array[index][1] + 1
    print(resultStr.format(num,result1 ,result2))