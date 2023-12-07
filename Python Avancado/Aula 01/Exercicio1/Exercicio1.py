def boas_vindas():
    print("Bem-vindo(a) ao curso de Python!")

def exibir_informacoes(nome, idade=None):
    if idade is None:
        print(f"Nome: {nome}, Idade não informada")
    elif idade < 18:
        print(f"Desculpe, {nome}, você não atende à idade mínima de 18 anos.")
    else:
        print(f"Nome: {nome}, Idade: {idade} anos")

def cadastrar_aluno(nome, idade, endereco, cep):
    numero_matricula = 123456  
    turma = "PY-2024-001" 

    return numero_matricula, turma

exibir_informacoes("José Silveira", 18)
exibir_informacoes("Ana Moreira")  

nome = "José Silveira"
idade = 18
endereco = "Jose Geraldo Rodrgiues, 100"
cep = "88888-789"

numero_matricula, turma = cadastrar_aluno(nome, idade, endereco, cep)

print(f"Olá {nome}, sua matrícula é {numero_matricula} na turma {turma}.")
