# problem 
# hackerrank: https://www.hackerrank.com/challenges/fibonacci-modified/problem

def modFibbo(n):
    if(arr[n]!=-1):
        return arr[n]
    else:
        temp = modFibbo(n-2) + modFibbo(n-1)**2
        arr[n]= temp
        return temp

t1,t2,n = map(int,input().split(" "))
arr = [-1 for i in range(n+1)]
arr[1]=t1
arr[2]=t2
print(modFibbo(n))