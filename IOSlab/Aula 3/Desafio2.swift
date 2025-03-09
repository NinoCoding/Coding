/*Gabriel é um professor e precisa acompanhar a presença dos seus alunos. No entanto, sua memória
não é tão boa e, às vezes, esquece de adicionar os novos alunos ao seu sistema. Atualmente a turma
conta com seguintes alunos:
João tem 5 presenças
Maria tem 3 presenças
Carlos tem 6 presenças
Eduardo tem 5 presenças
João, Maria e Carlos compareceram na aula de hoje e suas presenças devem ser atualizadas com +1
presença
Fábio se matriculou no curso mas ainda não compareceu, seu nome deve ser exibido com 0 presenças*/

var alunos = ["Joao": 5, "Maria": 3, "Carlos": 6, "Eduardo": 5, "Fabio": 0]

alunos["Joao"] = (alunos["Joao"] ?? 0) + 1
alunos["Maria"] = (alunos["Maria"] ?? 0) + 1
alunos["Carlos"] = (alunos["Carlos"] ?? 0) + 1

print(alunos)

