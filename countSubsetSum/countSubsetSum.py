# problem statement: 
# https://www.geeksforgeeks.org/count-of-subsets-with-sum-equal-to-x-using-recursion/


def getCountOfSubset():
    for i in range(1,n+1):
        for j in range(1,x+1):
            if(arr[i-1] <= j):
                dp[i][j] = dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1] # return last element

n = int(input())
arr= list(map(int,input().split(" ")))
x =int(input())
# tabulization
dp=[[0 for i in range(x+1)]for j in range(n+1)]
# intialization
for i in range(n+1): 
    dp[i][0]=1
print(getCountOfSubset())