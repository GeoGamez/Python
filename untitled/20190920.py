s=input("please enter a string")
if len(s)< 2 :
    print("this string is too short")
else:
    s2= s[:2] + s[len(s)-2:]
    print("the new string is", s2)
s3=s[0]+s[1:0].replace(s[0],"$")
print("the replaced string is", s3)
