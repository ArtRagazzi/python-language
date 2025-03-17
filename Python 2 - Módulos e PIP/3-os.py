import os

# 1 - Limpar terminal

os.system("clear")


# 2 - Retornar a pasta atual
print(os.getcwd())

# 3 - Listar arquivos e pastas
print(os.listdir())

# 4 - Apresentar versao do SO Windows
os.system('ver')
# 4 - Apresentar versao do SO Linux
os.system("uname -a")
# 5 - Apresentar informações da Maquina Windows
os.system('systeminfo')
# 5 - Apresentar informações detalhadas da máquina
os.system("lsb_release -a")  # Para distribuições Debian/Ubuntu