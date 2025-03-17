times = {}

def listarTimes():
    for time in times:
        print(time)
    
def listarJogadores(nomeTime):
    print(times[nomeTime])
        
def cadastrarTime():
    nomeTime = str(input("Digite o nome do time: "))
    times[nomeTime] = []
    
def cadastrarJogador(nomeTime):
    nomeJogador = str(input("Digite o nome do jogador: "))
    times[nomeTime].append(nomeJogador)

while True:
    print("-"*10)
    print("Escolha uma opção [0 - 4]")
    print("0 - Sair")
    print("1 - Listar Times")
    print("2 - Listar Jogadores")
    print("3 - Cadastrar Time")
    print("4 - Cadastrar Jogador")

    resposta = int(input("Opção: "))
    if(resposta <= 0 or resposta >4):
        break
    else:
        match resposta:
            case 1:
                listarTimes()
                
            case 2:
                nomeTime = str(input("Qual o nome do time? "))
                listarJogadores(nomeTime)
                
            case 3:
                cadastrarTime()
                
            case 4:
                nomeTime = str(input("Qual o nome do time? "))
                cadastrarJogador(nomeTime)
                
    


    