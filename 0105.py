import math

def isPrime(numTemp,arr):
    for i in range(len(arr)):
        if numTemp <= arr[i] :
            if numTemp%arr[i] == 0:
                return False
        else:
            break
    return True

while(True) :
    num = int(input())
    arr = [2]
    for i in range(3, int(math.sqrt(num)) +1 ):
        j=0
        for j in range(len(arr)):
            if i % arr[j] == 0 :
                break
        if j== len(arr)-1 : 
            arr.append(i)
    ## 루트 n까지 소수 구하기
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
        if isPrime(2*array[i][0]+1,arr) and isPrime(2*array[i][1]+1,arr):
            # 둘다 소수라면
            index = i 
            break
        else:
            if(i== rows -1) :
                print("Goldbach's conjecture is wrong")
    resultStr = "{} = {} + {}"
    print(resultStr.format(num,2*array[index][0] + 1 ,2*array[index][1] + 1))