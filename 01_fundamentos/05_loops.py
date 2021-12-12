# for

words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w)


print('\n')


for n in [1, 15, 58, 977, 1001, 5000]:
    if n % 2 == 0:
        print("{} é par".format(n))    
    else:
        print("{} é ímpar".format(n))


print('\n')


# for + range

for i in range(len(words)):
    print(words[i])


for i in range(5,10):
    print(i)


print('\n')


# break

for n in [1, 15, 58, 977, 1001, 5000]:
    if n > 100:
        print("Os proximos números são maires que 100")
        break
    else:
        print(n)


print('\n')


# continue

for n in [1, 15, 58]:
    if n == 15:
        continue
    else:
        print(n)


print('\n')


# while

texto = "programador"
indice = 0

while indice < len(texto):
    print(texto[indice])
    indice += 1
    

print('\n')


# do while

texto = "desenvolvedor"
indice = 0

while True:
    print(texto[indice])
    indice += 1
    if indice >= len(texto):
        break

