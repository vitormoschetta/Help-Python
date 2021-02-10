host = "DB:MySql"

print(host[0])          #print 'D'

print(len(host))        #print 8 (qtd de letras)

host_list = host.split(':')
print(host_list)        #separa a string criando uma lista ['DB', 'MySql']


host02 = ':'.join(host_list)
print(host02)           #print DB:MySql


print('Teste\tTeste')   #tab

print('Outro\nOutro')   #line break







