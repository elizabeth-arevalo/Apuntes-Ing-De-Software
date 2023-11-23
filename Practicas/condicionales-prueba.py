#Ejercicio 1:
x=5
y=10
z=8

print('****Ejercicio 1*****')
print(x>y)
print(y>z)
print('*********')
####### Ejercicio 2:
x, y, z= 5, 10, 8
print('****Ejercicio 2*****')
print(x>z)
print((y-5)==x)
print('*********')

####### Ejercicio 3:
x= 10

print('****Ejercicio 3*****')
if x==10:
    print(x==10)
if x>5:
    print(x>5)
if x<10:
    print(x<10)
else:
    print('else')
print('*********')

####### Ejercicio 4:
x, y, z= 5, 10, 8
x, y, z= z, y, x

print('****Ejercicio 4*****')
print(x>z)
print((y-5)==x)
print('*********')

####### Ejercicio 5:
x= "1"

print('****Ejercicio 5*****')
if x==1:
    print("one")
elif x=="1":
    if int(x) >1:
        print("two")
    elif int(x) <1:
        print("three")
    else:
        print("four")
if int(x) ==1 :
    print("five")
else:
    print("six")

print('*********')

####### Ejercicio 6:
x= 1
y=1.0
z="1"

print('****Ejercicio 6*****')
if x==y:
    print("one")
if y == int(z):
    print("two")
elif x==y:
    print("three")
else:
    print("four")
print('*********')
