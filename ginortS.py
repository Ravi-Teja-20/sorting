'''import string

s=input()
s1='abcdefghijklmnopqrstuvwxyz'
s2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s3='1234567890'
l1=[]
l2=[]
l3=[]
for i in range(len(s)):
    if s[i] in s1:
        l1.append(s[i])
    elif s[i] in s2:
        l2.append(s[i])
    else:
        l3.append(s[i])
l1.sort()
l2.sort()
even=[]
odd=[]
for i in range(len(l3)):
    if int(l3[i])%2==0:
        even.append(l3[i])
    else:
        odd.append(l3[i])

even.sort()
odd.sort
print(*(l1+l2+odd+even),sep='')




#Your task is to sort the string  in the following manner:

#All sorted lowercase letters are ahead of uppercase letters.
#All sorted uppercase letters are ahead of digits.
#All sorted odd digits are ahead of sorted even digits.'''


