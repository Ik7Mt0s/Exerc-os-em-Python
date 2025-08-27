import os, json

ARQUIVO_DADOS = 'alunos.json'

class Aluno:
    def __init__(self, nome, idade, matricula, p1, p2, p3):
        self.nome = nome
        self.idade = self.data_nascimento(idade)
        self.matricula = matricula
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.media = self.calcular_media()

    def calcular_media(self):
        return (self.p1 + self.p2 + self.p3) / 3
    
    def data_nascimento(self, idade):
        return f"{idade[:2]}/{idade[2:4]}/{idade[4:]}"
    
    def exibir_dados(self):
        print(f'Aluno................: {self.nome}')
        print(f'Data de Nascimento...: {self.idade}')
        print(f'Matrícula............: {self.matricula}')
        print(f'Média final..........: {self.media:.2f}')

    def to_dict(self):
        return {
            'nome': self.nome,
            'data': self.idade.replace('/', ''),
            'matricula': self.matricula,
            'media': self.media,
            'p1': self.p1,
            'p2': self.p2,
            'p3': self.p3
        }
    
    @staticmethod
    def from_dict(info):
        return Aluno(info['nome'], info['data'], info['matricula'], info['p1'], info['p2'], info['p3'])
    
def salvar_dados(lista):
    with open(ARQUIVO_DADOS, 'w') as i:
        json.dump([alu.to_dict() for alu in lista], i, indent=3)

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, 'r') as h:
        dados = json.load(h)
        return [Aluno.from_dict(j) for j in dados]

alunos = carregar_dados()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Digite 1 para cadastrar novo aluno')
    print('Digite 2 para listar os alunos registrados')
    print('Digite 3 para encerrar o programa')
    processo = input('\nDigite sua escolha ')

    if processo == '1':
        nome = input('Digite o nome do aluno ')
        while True:
            idade = input('Digite a data de nascimento do aluno (Somente os 8 números) ')
            if len(idade) == 8 and idade.isdigit():
                break
            else:
                print("Data inválido! Digite exatamente 8 números.\n")

        matricula = input('Digite sua matrícula ')
        p1 = float(input('Digite a nota da sua Prova 1 '))
        p2 = float(input('Digite a nota da sua Prova 2 '))
        p3 = float(input('Digite a nota do seu simulado '))
        
        aluno = Aluno(nome, idade, matricula, p1, p2, p3)
        alunos.append(aluno)
        salvar_dados(alunos)
        
        print('Aluno registrado com sucesso!')
        input('\nPressione Enter para retornar ')

    elif processo == '2':
        if not alunos:
            print('Não há alunos registrados')
        else:
            print('\n=== Alunos Casdastrados ===')
            for aluno in alunos:
                aluno.exibir_dados()
                print('-' * 30)
        input('\nPressione Enter para continuar...')

    elif processo == '3':
        print('Saindo so sistema...')
        exit()

    else:
        print('Opção inválida.')
        input('\nPressione Enter para tentar novamente...')