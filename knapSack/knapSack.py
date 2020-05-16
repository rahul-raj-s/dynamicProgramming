# problem :
# https://www.hackerrank.com/contests/srin-aadc03/challenges/classic-01-knapsack/submissions/code/1323624149
# knapSack problem top-down approach

def getMaxProfit():
    for i in range(1,n+1):
        for j in range(1,w+1):
            if(weight[i]<=j):
                dp[i][j]= max(value[i]+dp[i-1][j-weight[i]],dp[i-1][j])    
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]

test= int(input())
for i in range(test):
    w,n = map(int,input().split(" "))
    weight = [0 for i in range(n+1)]
    value = [ 0 for i in range(n+1)]
    for i in range(1,n+1):
        weight[i],value[i] = map(int,input().split(" "))
    dp =[[0 for i in range(w+1)] for j in range(n+1)]
    print(getMaxProfit())

