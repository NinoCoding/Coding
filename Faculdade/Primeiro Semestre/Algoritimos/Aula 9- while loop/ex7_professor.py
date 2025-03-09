#primeiro digite a quantidade de profesores
#depois digite a quantidade de turmas que cada professor ministra
#nao deve ter mensagem
#deve ser igual ao caso de teste

i = 0
turmas_total = 0

professor = int(input())

if professor == 0:
    print("NÃO HOUVE PROCESSAMENTO")
    

else:
    while i < professor:
        turmas = int(input())     
        turmas_total += turmas
        i += 1

        if turmas > 6:
            print("VOCÊ TEM MUITAS TURMAS")
            
    print(f"{turmas_total / professor:.2f}")
    