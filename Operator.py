#Arithmatic Op
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a**b)     #exponentiation - 10^5  - power
print(a//b)     #floor operation - removes the fraction value
print(a%b)      #modulus % - remainder

#assignment op
x=5
x+=3
print(x)

#logical op
c=5
d=7
print(c&d)                  #converts both in binary (bitwise), then does and(&) operation
print(c<d and c>d)          #converts it to boolean
print(not(c<d and c>d))     #not op - reversed the result