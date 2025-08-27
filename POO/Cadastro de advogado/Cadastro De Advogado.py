import random, os, json

ARQUIVO_DADOS = 'advogado.json'
matriculas_usadas = set()

class Advogado:
    def __init__(self, nome, OAB, cpf, matricula=None):
        self.nome = nome
        self.oab = OAB
        self.cpf = self.CPF_formatado(cpf)
        self.matricula =  matricula if matricula is not None else self.gerar_matricula()
    
    def gerar_matricula(self):
        while True:
            nova = random.randint(100000, 999999)
            if nova not in matriculas_usadas:
                matriculas_usadas.add(nova)
                return nova

    def CPF_formatado(self, cpf):
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    
    def exibir_dados(self):
        print(f"Matrícula gerada....: {self.matricula}")
        print(f'Advogado............: {self.nome}')
        print(f'Número da OAB.......: {self.oab}')
        print(f'Número do CPF.......: {self.cpf}')

        # ---------- Funções que transitam os dados em dicionários ----------

    def salvar_como_dicionario(self):
        return{
            'nome': self.nome,
            'oab': self.oab,
            'cpf': self.cpf.replace('.', '').replace('-', ''),
            'matricula': self.matricula
        }
    
    @staticmethod
    def carregar_do_dicionario(info):
        return Advogado(info['nome'], info['oab'], info['cpf'], info['matricula'])

# ---------- Funções que interagem com o arquivo json ----------

def salvar_dados(lista):
    with open(ARQUIVO_DADOS, 'w') as i:
        json.dump([adv.salvar_como_dicionario() for adv in lista], i, indent=2)

def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []
    with open(ARQUIVO_DADOS, 'r') as h:
        dados = json.load(h)
        return [Advogado.carregar_do_dicionario(j) for j in dados]


#  ---------- Inicio do programa ----------
advogados = carregar_dados()
for a in advogados:
    matriculas_usadas.add(a.matricula)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Digite 1 para cadastrar novo advogado')
    print('Digite 2 para listar os advogados registrados')
    print('Digite 3 para encerrar o programa')
    processo = input('Digite sua escolha: ')

    if processo == '1':
        nome = input('\nDigite o nome do advogado: ')
        oab = input('Digite o número da OAB: ')
        while True:
            cpf = input("Digite o CPF do advogado (somente os 11 números): ")
            if len(cpf) == 11 and cpf.isdigit():
                break
            else:
                print("CPF inválido! Digite exatamente 11 números.\n")
        
        advogado = Advogado(nome, oab, cpf)
        advogados.append(advogado)
        salvar_dados(advogados)

        print('\nAdvogado registrado com sucesso!')
        input('Pressione Enter para retornar ')

    elif processo == '2':
        if not advogados:
            print('Não há advogados registrados')
        else:
            print('\n=== Advogados registrados ===')
            for advogado in advogados:
                advogado.exibir_dados()
                print('-' * 30)
        input('\nPressione Enter para continuar...')

    elif processo == '3':
        print('Encerrando programa...')
        exit()

    else:
        print('\nOpção inválida, por favor digite um dos números acima')
        input('Pressione Enter para continuar...')