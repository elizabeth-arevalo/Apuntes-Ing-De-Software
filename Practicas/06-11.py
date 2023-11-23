x=4
y=1

a=x&y
b=x|y
c=~x
e=x>>2
f=x<<2


print(a,b,c,e,f)


## Listas

numeros=[10,5,"x",2,1]
numeros2=[10,5,7,2,1]

bin_Traduccion=[4,2,1]
bin_Sin_Traduc=[0,0,1]
x=1
x=x<<1


print(numeros,"\n",numeros2,"\n",numeros[2])
numeros[2]=111
print(numeros,"\n",numeros2,"\n",numeros[2])

print(x)
numeros = [10,5,7,2,1]
print('Lista original: ', numeros)
numeros[0]=111
print('Lista modificada: ', numeros)

print('-----------Copiar el 5to elemento al 2do--------------')
print('Lista original: ', numeros)
numeros[1]=numeros[4]
print('Lista modificada: ', numeros)

print('Tamaño de la lista: ', len(numeros), 'elementos' )


print('-----------Eliminar el elemento 2--------------')
print('Lista original: ', numeros)
del numeros[2]
print('Lista modificada: ', numeros)


print('-------------Indice negativo----------------')
numeros = [10,5,7,2,1]
print(numeros[-1])
print(numeros[-2])
print(numeros[-5])