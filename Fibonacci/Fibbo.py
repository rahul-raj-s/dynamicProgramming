def fibbo(n):
    global count
    count+=1
    if(n<=1):
        return 0
    if(n==2):
        return 1
    return fibbo(n-1)+fibbo(n-2)      
count  =0
num = int(input("Enter a number"))
print("Output",fibbo(num))
print(count)

# Order = 2^n 