import csv
import functions
import random

files = [] # Abre o csv e guarda na variável files
with open('alunos.csv', 'r') as student_archive:
    student_info = csv.reader(student_archive)
    for line in student_info:
        files.append(line)

currentLine = functions.getLines(files) # Função pra identificar em que linha do arquivo está a matrícula

check = 0
if currentLine == 0:
    print("O aluno nao pode ser encontrado")
else:
    if (files[currentLine][5] == "Ativo") and (files[currentLine][4] == ''): 
        check = True
        student_name = files[currentLine][0].split(" ")
        options = functions.getEmail(student_name) # Função pra criar opções de uffmail
    else:
        if files[currentLine][5] == "Inativo":
            print("A sua matricula está Inativa. \n")
        if files[currentLine][4]:
            print("Voce ja possui um UFFmail, que é : " + files[currentLine][4])


if check:
    print(student_name[0]+", por favor escolha uma das opcoes abaixo: \n") # Escolha do indice de uffmail
    for i in range(6):
        print(str(i+1)+" - "+options[i])

    choice = int(input())

    if choice > 6 or choice < 1:
        print("Escolha inválida")
    else:
        files[currentLine][4] = options[choice-1] # Criação do uffmail e sms
        print("A criação de seu e-mail (" + options[choice - 1] + ") será feita nos próximos minutos. \nUm SMS foi enviado para " + files[currentLine][2] + " com a sua senha de acesso.\n")

with open("alunos.csv", 'w', newline= '') as fileWriter: # Abrir o csv pra atualizar com o novo uffmail
    writer = csv.writer(fileWriter)
    for line in files:
        writer.writerow(line)
