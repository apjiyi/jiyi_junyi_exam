def filter_multiple(n):
    new_lst = [i for i in range(1,n+1) if (i%3!=0 and i%5!=0) or (i%3==0 and i%5==0)]
    return len(new_lst)

# Driver Code
n = 15
print(filter_multiple(n))