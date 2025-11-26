import os
import time

# Dicionário global para armazenar os dados do organismo
organismo = {}

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa():
    """Pausa o programa até o usuário pressionar ENTER"""
    input('\nPressione ENTER para continuar...')

def exibir_menu():
    """Exibe o menu principal"""
    print('=' * 50)
    print(f"{'CLASSIFICAÇÃO DE ORGANISMOS POR REINO':^50}")
    print('=' * 50)
    print(' 1 - Cadastro do organismo')
    print(' 2 - Classificação')
    print(' 3 - Consultar informações sobre o reino')
    print(' 4 - Sair')
    print('=' * 50)

def cadastro_organismo():
    """Coleta informações sobre o organismo"""
    print('=' * 50)
    print(f"{'CADASTRO DE ORGANISMO':^50}")
    print('=' * 50)
    
    organismo['tipoCelula'] = input('Tipo de célula (procarionte/eucarionte): ').lower()
    organismo['numeroCelula'] = input('Número de células (unicelular/pluricelular): ').lower()
    organismo['formaNutricao'] = input('Forma de nutrição (autótrofo/heterótrofo): ').lower()
    organismo['paredeCelular'] = input('Possui parede celular? (sim/não): ').lower()
    organismo['mobilidade'] = input('Forma de mobilidade: ').lower()
    organismo['ambiente'] = input('Ambiente de vida: ').lower()
    
    print('\n Organismo cadastrado com sucesso!')
    print('=' * 50)

def classificar_organismo():
    """Classifica o organismo com base nas características cadastradas"""
    if not organismo:
        return None
    
    # Lógica de classificação
    tipo = organismo.get('tipoCelula', '')
    numero = organismo.get('numeroCelula', '')
    nutricao = organismo.get('formaNutricao', '')
    parede = organismo.get('paredeCelular', '')
    
    # Monera (Bactérias)
    if 'procarionte' in tipo:
        return 'Monera'
    
    # Plantae (Plantas)
    elif 'eucarionte' in tipo and 'pluricelular' in numero and 'autótrofo' in nutricao and 'sim' in parede:
        return 'Plantae (Vegetal)'
    
    # Fungi (Fungos)
    elif 'eucarionte' in tipo and 'heterótrofo' in nutricao and 'sim' in parede:
        return 'Fungi'
    
    # Animalia (Animais)
    elif 'eucarionte' in tipo and 'pluricelular' in numero and 'heterótrofo' in nutricao and 'não' in parede:
        return 'Animalia (Animal)'
    
    # Protista
    elif 'eucarionte' in tipo and 'unicelular' in numero:
        return 'Protista'
    
    else:
        return 'Classificação inconclusiva'

def classificacao():
    """Exibe a classificação do organismo cadastrado"""
    print('=' * 50)
    print(f"{'CLASSIFICAÇÃO DO ORGANISMO':^50}")
    print('=' * 50)
    
    if not organismo:
        print('⚠ Nenhum organismo cadastrado ainda!')
        print('Por favor, cadastre um organismo primeiro (opção 1).')
        return
    
    print('\nProcessando os dados', end='')
    for i in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    
    reino = classificar_organismo()
    print(f'\n\nDe acordo com as informações fornecidas,')
    print(f'a classificação do organismo é: {reino}')
    print('=' * 50)

def consultar_info():
    """Consulta informações sobre um reino específico"""
    print('=' * 50)
    print(f"{'CONSULTAR INFORMAÇÕES':^50}")
    print('=' * 50)
    reino = input('Digite o reino do organismo: ').lower()
    print()
    
    if reino in ['animal', 'animalia']:
        print('REINO ANIMALIA (ANIMAL)')
        print(' - Descrição: Organismos multicelulares que não produzem seu próprio alimento.')
        print(' - Características: Eucariontes, heterotróficos, geralmente possuem locomoção,')
        print('   sistema nervoso e órgãos complexos.')
        print(' - Exemplos: Humanos, aves, peixes, insetos, mamíferos.')
    
    elif reino in ['vegetal', 'plantae', 'planta']:
        print('REINO PLANTAE (VEGETAL)')
        print(' - Descrição: Seres vivos que produzem seu próprio alimento por fotossíntese.')
        print(' - Características: Eucariontes, multicelulares, autotróficos,')
        print('   possuem parede celular de celulose.')
        print(' - Exemplos: Árvores, flores, samambaias, musgos.')
    
    elif reino in ['fungi', 'fungo']:
        print('REINO FUNGI')
        print(' - Descrição: Organismos que atuam como decompositores no ambiente.')
        print(' - Características: Eucariontes, heterotróficos por absorção,')
        print('   não fazem fotossíntese. Muitos são multicelulares.')
        print(' - Exemplos: Cogumelos, bolores, leveduras.')
    
    elif reino in ['protista', 'protoctista']:
        print('REINO PROTISTA')
        print(' - Descrição: Organismos geralmente unicelulares, mas com células complexas.')
        print(' - Características: Possuem núcleo (eucariontes). Podem ser autotróficos')
        print('   ou heterotróficos.')
        print(' - Exemplos: Amebas, paramécios, algas unicelulares.')
    
    elif reino in ['monera', 'bacteria']:
        print('REINO MONERA')
        print(' - Descrição: Organismos unicelulares e microscópicos.')
        print(' - Características: Não possuem núcleo organizado (procariontes).')
        print('   Podem viver em diversos ambientes.')
        print(' - Exemplos: Bactérias e cianobactérias.')
    
    else:
        print('Reino não reconhecido. Tente: animal, vegetal, fungi, protista ou monera.')
    
    print('=' * 50)

def sair():
    """Encerra o programa"""
    print('\n Saindo do programa', end='')
    for i in range(5):
        print('.', end='', flush=True)
        time.sleep(0.5)
    print('\n\n Programa encerrado com sucesso!')

def main():
    """Função principal que controla o fluxo do programa"""
    while True:
        limpar_tela() 
        exibir_menu()  
        opcao = input('\nDigite a opção desejada: ')
        
        if opcao == '1':
            cadastro_organismo()
            pausa()
        elif opcao == '2':
            classificacao()
            pausa()
        elif opcao == '3':
            consultar_info()
            pausa()
        elif opcao == '4':
            sair()
            break
        else:
            print('\n Opção inválida. Tente novamente.')
            pausa()

# Inicia o programa
if __name__ == '__main__':
    main()