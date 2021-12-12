# if else
x = 10

if x < 6:
    print('Reprovado')
elif x >= 6 and x < 10:
    print('Aprovado')
else:
    print('Aprovado Nota 10')


print('\n')


# switch case = match

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

http_error(400)