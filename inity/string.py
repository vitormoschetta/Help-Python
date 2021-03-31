host = "DB:MySql"

print(host[0])                  #print 'D'

print(len(host))                #print 8 (qtd de letras)


host_list = host.split(':')     #separa a string criando uma lista ['DB', 'MySql']
print(host_list)                


host02 = ':'.join(host_list)     #print DB:MySql
print(host02)                  


print('Teste\tTeste')           #tab

print('Outro\nOutro')           #line break







