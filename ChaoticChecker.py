u = 'з¦Ѓ€ （0ђ¶V・$: '
g = 'GUEST: '
s = '"'
#106, 77 -> ch01
#75, 94 -> ch04
def one(nome):
    a = []
    try:
        print (u + "Abrindo arquivo " + nome + " ...")
        print()
        f = open(nome, 'r')
    except:
        print (u + "Erro ao abrir o arquivo " + nome)
        print()
    c = 0
    for linha in f:
        c += 1
        if linha.count(s) % 2 != 0:
            a.append(c)
    print(u + "Arquivo " + nome + " com erros na(s) linha(s) " + str(a))
    f.close()
    print(u + 'Arquivo ' + nome + ' fechado com sucesso')
    print()
    print()
    return a

def allfiles():
    import os
    b = []
    for x in os.listdir():
        if x.endswith(".nss"):
            b.append(one(x))
    return b

def check():
    print(u + "Seja Bem-Vindo")
    print(u+"Comandos: -one arquivo.nss, -all, -shutdown")
    print()
    cmd = input(g)
    if "-one" in cmd:
        cmd = cmd.split()
        l = one(cmd[1])
        if len(l) < 1:
            print(u + "Nenhum erro encontrado no arquivo " + cmd[1])
            print()
    elif "-shutdown" in cmd:
        exit(0)
    elif "-all" in cmd:
        allfiles()
    else:
        print( u + "Erro. Comando Inválido. Tente Novamente")
        print()
    return check()

check()

