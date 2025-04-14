#Sem typeHint
def hello1(name):
    return f'Olá {name}'

#Com typeHint
def hello2(name:str) -> str:
    return f'Olá {name}'


#Sem TypeHint 
list_user =[
    "fulano","sicrano"
]

#Com TypeHit
list_user_2:list[str]=[
    "fulano","sicrano"
]

#sem TH
dict_users={
    1:"Fulano",
    2:"Sicrano"
}

#Com TH

dict_users_2:dict[str,str]={
    "1":"Fulano",
    "2":"Sicrano"
}


print(hello2(12312))

#Necessario MyPY mypy ...