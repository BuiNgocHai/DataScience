s = input("Enter string : ")
w = int(input("Enter width : "))
k=0
t=w
while(k<len(s)):
    print(s[k:w])
    k=w
    w+=t