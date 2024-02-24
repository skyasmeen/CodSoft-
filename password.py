import random

symbols='@!#$%&*()'
numbers='0123456789'
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'


string=upper+lower+numbers+symbols

length=int(input("enter the length of password:"))

password="".join(random.sample(string,length))
print("generated passsword is:",password)
