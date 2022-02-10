try:
    students = open("arquivo.txt", "r")
except OSError:
    print("not found this file")
else:
    alunos_reprovados = []
    for student in students:
        if int(student.split(" ")[1]) <= 5:
            aluno = student.split(" ")[0]
            alunos_reprovados.append(f"{aluno}\n")

reprovedFile = open("reproveds.txt", "w")
reprovedFile.writelines(alunos_reprovados)
students.close()
