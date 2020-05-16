# Problem
# Given Diffrent type(dominations) of coins, 
# Find Out: Total no. of ways you can make change of a given amount using \n
# given coins
# test Cases @Hackerrank : https://www.hackerrank.com/challenges/coin-change/problem

def noOfWaysForChange():
    global table
    for i in range(1,len(types)):
        for j in range(1,amount+1):
            if(types[i]>j):
                table[i][j]= table[i-1][j]
            else:
                table[i][j] = table[i-1][j]+table[i][j-types[i]]

    return table[-1][-1]

types = list(map(int,input("Enter types of coins: ").split(" ")))
amount = int(input("Enter amount"))
table = [[0 for i in range(amount+1)] for j in range(len(types))] 
for i in range(len(types)):
    table[i][0]=1
for i in range(amount+1):
    table[0][i] = 1 if i%types[0]==0 else 0
print("Possible ways to change: ",noOfWaysForChange())
