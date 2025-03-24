import json



#1- string para dicionario
person = '{"name":"Artur", "languages":["Python","JS"]}'
person_dict = json.loads(person)
print(person)
print(person_dict)

#2 - convertendo dictionary para json 
person_json = json.dumps(person_dict)
print(person_json)
print(type(person_json))
print(type(person_dict))

#3-formatando json
print(json.dumps(person_dict, indent=4, sort_keys=True))

#4-Salvando arquivo sjon em txt
with open("person.txt ", "w")as json_file:
    json.dump(person_dict, json_file)
    
