def getMin():
    global table
    for i in range(1,len(coins)):
        for j in range(1,amount+1):
            if(coins[i]>j):
                table[i][j]= table[i-1][j]
            else:
                table[i][j] = min([table[i-1][j],1+table[i][j-coins[i]]])
    return table[-1][-1]

coins = list(map(int,input("Enter coins").split(" ")))
amount = int(input())
table = [[0 for i in range(amount+1)]for i in range(len(coins))]
for i in range(1,amount+1):
    table[0][i] = i
print(getMin())