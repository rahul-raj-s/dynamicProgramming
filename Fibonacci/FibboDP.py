def fibbo(n):
    global arr
    if(arr[n-1]!=-1):
        return arr[n-1]
    else:
        temp=fibbo(n-1)+fibbo(n-2)
        arr[n-1]=temp
        return temp

num = int(input("Enter a number"))
count =0
arr = [-1]*num
arr[0]=0
arr[1]=1
print("Fibbo: ",fibbo(num))

""" 
        function_calls
num     DP      Recursion

10      17      109
20      37      13529
5       7       9
50      97      NO RESULT
100     197     NO RESULT
"""