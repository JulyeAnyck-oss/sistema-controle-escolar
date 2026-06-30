usuarios = []
alunos = []

def cadastrar_usuario():
    print("Cadastro de novo usuário")
    email = input("qual o email do usuario? ")
    confirmacao_email = input("confirme o email: ")
    if email != confirmacao_email:
        print("os emails não coincidem!")
        return
    nome = input("qual o nome do usuario? ")
    senha = input("qual a sua senha? ")
    confirmacao_senha = input("confirme a senha: ")
    if senha != confirmacao_senha:
        print("as senhas não coincidem!")
        return
    papel = input("qual o seu papel? (aluno/professor) ")
    if papel not in ["aluno", "professor"]:
        print("papel inválido! escolha entre 'aluno' ou 'professor'.")
        return
    usuario = {"nome": nome, "senha": senha, "papel": papel, "email": email}
    usuarios.append(usuario)
    print(f"Usuário cadastrado com sucesso! Bem-vindo, {nome}!")

def cadastrar_aluno():
    nome_aluno = input("Digite o nome do aluno: ")
    aluno = {"nome": nome_aluno, "notas": [], "frequencias": []}
    alunos.append(aluno)
    print(f"Aluno {nome_aluno} cadastrado com sucesso!")
    
def listar_aluno():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Alunos cadastrados:")
        for aluno in alunos:
            print(f"- {aluno['nome']}")

def lancar_nota():
    nome_aluno = input("Digite o nome do aluno para lançar a nota: ")
    aluno_encontrado = None
    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            aluno_encontrado = aluno
            break
    if aluno_encontrado is None:
        print(f"Aluno {nome_aluno} não encontrado.")
    else:
        nota1 = float(input("Digite a nota 1: "))
        if nota1 < 0 or nota1 > 10:
            print("Nota inválida! Digite entre 0 e 10.")
            return
        nota2 = float(input("Digite a nota 2: "))
        if nota2 < 0 or nota2 > 10:
            print("Nota inválida! Digite entre 0 e 10.")
            return
        aluno_encontrado["notas"] = [nota1, nota2]
        print(f"Notas lançadas para o aluno {nome_aluno}.")
        media_notas = sum(aluno_encontrado["notas"]) / len(aluno_encontrado["notas"])
        print(f" Média das notas: {media_notas:.2f}")

def lancar_frequencia():
    nome_aluno = input("Digite o nome do aluno para lançar a frequência: ")
    aluno_encontrado = None
    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            aluno_encontrado = aluno
            break
    if aluno_encontrado is None:
        print(f"Aluno {nome_aluno} não encontrado.")
    else:
        frequencia = int(input("Digite a frequência (0-100): "))
        aluno_encontrado["frequencias"].append(frequencia)
        print(f"Frequência lançada para o aluno {nome_aluno}.")

def calcular_media(notas):
    return sum(notas) / len(notas) if notas else 0

def calcular_situacao(media):
    if media >= 7: 
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def boletim_completo():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(f"\nAluno: {aluno['nome']}")
        if not aluno["notas"]:
            print("  Notas ainda não lançadas.")
        else:
            print(f"  Nota 1: {aluno['notas'][0]}")
            print(f"  Nota 2: {aluno['notas'][1]}")
        media = calcular_media(aluno["notas"])
        print(f"  Média: {media:.2f}")
        situacao = calcular_situacao(media)
        print(f"  Situação: {situacao}")

def lancar_nota_extra():
    nome_aluno = input("Digite o nome do aluno para lançar a nota extra: ")
    aluno_encontrado = None
    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            aluno_encontrado = aluno
            break
    if aluno_encontrado is None:
        print(f"Aluno {nome_aluno} não encontrado.")
    else:
        nota_extra = float(input("Digite a nota extra: "))
        if nota_extra < 0 or nota_extra > 10:
            print("Nota inválida! Digite entre 0 e 10.")
            return
        aluno_encontrado["notas"].append(nota_extra)
        print(f"Nota extra lançada para o aluno {nome_aluno}.")

def buscar_aluno():
    nome_aluno = input("Digite o nome do aluno: ")
    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            print(f"\nAluno: {aluno['nome']}")
            if not aluno["notas"]:
                print("  Notas ainda não lançadas.")
            else:
                media = calcular_media(aluno["notas"])
                situacao = calcular_situacao(media)
                for i, nota in enumerate(aluno["notas"], 1):
                    print(f"  Nota {i}: {nota}")
                print(f"  Média: {media:.2f}")
                print(f"  Situação: {situacao}")
                
            return
    print(f"Aluno {nome_aluno} não encontrado.")

def remover_aluno():
    nome_aluno = input("Nome do aluno a remover: ")
    for aluno in alunos:
        if aluno["nome"] == nome_aluno:
            alunos.remove(aluno)
            print(f"Aluno {nome_aluno} removido!")
            return
    print(f"Aluno {nome_aluno} não encontrado.")

def ordenar_por_media():
    com_notas = [a for a in alunos if len(a["notas"]) >= 2]
    if not com_notas:
        print("Nenhum aluno com notas.")
        return
    ordenados = sorted(com_notas, key=lambda a: sum(a["notas"])/2, reverse=True)
    for aluno in ordenados:
        media = sum(aluno["notas"]) / 2
        print(f"{aluno['nome']}: {media:.2f}")

def salvar_em_arquivo():
    with open("boletim.txt", "w", encoding="utf-8") as f:
        for aluno in alunos:
            f.write(f"Aluno: {aluno['nome']}\n")
            if aluno["notas"]:
                media = sum(aluno["notas"]) / 2
                f.write(f"Notas: {aluno['notas']}\n")
                f.write(f"Média: {media:.2f}\n")
            f.write("\n")
    print("Boletim salvo em boletim.txt!")

def fazer_login():
    print("Entrar no sistema")
    nome = input("qual o nome do usuario? ")
    senha = input("qual a sua senha? ")
    usuario_encontrado = False
    for usuario in usuarios:
        if usuario["nome"] == nome and usuario["senha"] == senha:
            print(f"Bem-vindo, {usuario['nome']}! Você é um {usuario['papel']}.")
            if usuario["papel"] == "professor":
                while True:  
                    print("1 - Cadastrar aluno")
                    print("2 - Cadastrar nota" )
                    print("3 - Cadastrar frequência")
                    print("4 - buscar aluno por nome")
                    print("5 - ver boletim completo dos alunos")
                    print("6 - listar alunos cadastrados")
                    print("7 - Remover aluno")
                    print("8 - Lancar nota extra")
                    print("9 - Ordenar alunos por média")
                    print("10 - Salvar boletim em arquivo")
                    print("11 - sair")
                    opcao_professor = int(input("Escolha uma opção: "))
                    if opcao_professor == 1:
                        cadastrar_aluno()
                    if opcao_professor == 2:
                        lancar_nota()
                    if opcao_professor == 3:
                        lancar_frequencia()
                    if opcao_professor == 4:
                        buscar_aluno()
                    if opcao_professor == 5:
                        boletim_completo()
                    if opcao_professor == 6:
                        listar_aluno()
                    if opcao_professor == 7:
                        remover_aluno()
                    if opcao_professor == 8:
                        lancar_nota_extra()
                    if opcao_professor == 9:
                        ordenar_por_media()
                    if opcao_professor == 10:
                        salvar_em_arquivo()
                    if opcao_professor == 11:
                        break  
                    if opcao_professor < 1 or opcao_professor > 11:
                        print("Opção inválida! Por favor, escolha uma opção válida!")
            elif usuario["papel"] == "aluno":
                while True:
                    print("1 - ver notas e frequências")
                    print("2 - baixar meu boletim")
                    print("3 - sair")
                    opcao_aluno = int(input("Escolha uma opção: "))
                    if opcao_aluno == 1:
                        for a in alunos:
                            if a["nome"] == usuario["nome"]:
                                print(f"Notas: {a['notas']}")
                    if opcao_aluno == 2:
                       for a in alunos:
                           if a["nome"] == usuario["nome"]:
                                media = sum(a["notas"]) / 2 if a["notas"] else 0
                                situacao = calcular_situacao(media)
                                with open(f"boletim_{a['nome']}.txt", "w", encoding="utf-8") as f:
                                    f.write(f"Boletim de {a['nome']}\n")
                                    f.write(f"Notas: {a['notas']}\n")
                                    f.write(f"Média: {media:.2f}\n")
                                    f.write(f"Situação: {situacao}\n")
                                print(f"Boletim salvo em boletim_{a['nome']}.txt!")
                    if opcao_aluno == 3:
                        break

            usuario_encontrado = True
            break
    if not usuario_encontrado:
        print("Usuário ou senha incorretos!")

while True:
    print("Bem-vindo ao sistema de cadastro de usuários!")
    print("1 - Cadastrar novo usuário")
    print("2 - Entrar no sistema")
    print("3 - Sair")
    opcao = int(input("Escolha uma opção: "))
   
    if opcao == 1:
        cadastrar_usuario()    
    elif opcao == 2:
        fazer_login()         
    elif opcao == 3:
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")