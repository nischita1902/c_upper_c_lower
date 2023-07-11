def cal(n):
    c_upper=0
    c_lower=0
    for i in n:
        if i.isupper():
            c_upper+=1
        elif i.islower():
            c_lower+=1
    print("No. of Upper case characters:",c_upper)
    print("No. of Lower Case characters:",c_lower)
    return ""
cal("The quick Brow Fox")

#output:
#No. of Upper case characters: 3
#No. of Lower Case characters: 12
