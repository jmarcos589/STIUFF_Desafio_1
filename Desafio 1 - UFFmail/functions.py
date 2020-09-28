import random
def getLines(files):
    matricula = input("Digite o número da sua matricula: \n")
    temp = 0 
    student_line = 0 
    for line in files:
        if line[1] == matricula: 
            student_line = temp
        temp += 1
    return student_line

def getEmail(student_name):
    optionsList = []
    optionsList.append(student_name[0] + student_name[1] + "@id.uff.br") 
    optionsList.append(student_name[0 ]+ student_name[2] + "@id.uff.br") 
    optionsList.append(student_name[0] + str(random.randint(0,100)) + "@id.uff.br")
    optionsList.append(student_name[0][0] + student_name[1][0]+'_' + student_name[2] +"@id.uff.br")
    optionsList.append(student_name[0] + '_' + student_name[1][0]+ student_name[2] + "@id.uff.br")
    optionsList.append(student_name[0][0] + student_name[2] + str(random.randint(0,100)) + "@id.uff.br")

    return optionsList
