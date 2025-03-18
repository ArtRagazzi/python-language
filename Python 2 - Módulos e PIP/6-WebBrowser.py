import webbrowser

done = False

while not done:
    print("O Que voce Deseja fazer? ")
    print("1- Aprender Python")
    print("2- Aprender Java")
    print("3- Aprender Javascript")
    print("4- Sair")
    choice = int(input(">"))
    
    if choice == 1:
        webbrowser.open("http://www.python.org")
    elif choice == 2:
        webbrowser.open("https://www.java.com/pt-BR/")
    elif choice == 3:
        webbrowser.open("https://developer.mozilla.org/pt-BR/docs/Web/JavaScript")
    else:
       print("Opção invalida") 
       done = True