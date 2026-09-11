import json
import os

ARQUIVO_DADOS = "dados_dimensionamento.json"
MESES_NOME = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro",
]

imoveis = []  


def carregar_dados():
    global imoveis
    if os.path.exists(ARQUIVO_DADOS):
        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
                imoveis = json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            print("Não foi possível ler o arquivo de dados. Iniciando com uma base vazia.\n")
            imoveis = []


def salvar_dados():
    try:
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(imoveis, arquivo, ensure_ascii=False, indent=2)
    except OSError:
        print("Não foi possível salvar os dados em disco.\n")


def ler_texto_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo é obrigatório. Tente novamente.\n")


def ler_consumo_kwh(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            kwh = float(valor)
        except ValueError:
            print("Valor inválido. Informe um número (ex: 250 ou 250.5).\n")
            continue
        if kwh <= 0:
            print("O consumo deve ser maior que zero.\n")
            continue
        return kwh


def ler_mes():
    while True:
        valor = input("Mês (1 a 12): ").strip()
        if not valor.isdigit() or not (1 <= int(valor) <= 12):
            print("Informe um mês válido, entre 1 e 12.\n")
            continue
        return int(valor)


def ler_ano():
    while True:
        valor = input("Ano (ex: 2025): ").strip()
        if not valor.isdigit() or not (2000 <= int(valor) <= 2100):
            print("Informe um ano válido, entre 2000 e 2100.\n")
            continue
        return int(valor)



def cadastrar_imovel():
    print("\n--- Cadastro de Imóvel ---")
    nome = ler_texto_obrigatorio("Identificação do imóvel (ex: Casa, Apartamento 101): ")
    endereco = ler_texto_obrigatorio("Endereço/localidade: ")
    usuario = ler_texto_obrigatorio("Nome do usuário responsável pelo imóvel: ")
    imovel = {
        "id": len(imoveis) + 1,
        "nome": nome,
        "endereco": endereco,
        "usuario": usuario,
        "consumos": [], 
    }
    imoveis.append(imovel)
    salvar_dados()
    print(f"Imóvel '{nome}' cadastrado com sucesso! (ID {imovel['id']})\n")


def listar_imoveis():
    if not imoveis:
        print("\nNenhum imóvel cadastrado ainda.\n")
        return
    print("\n--- Imóveis Cadastrados ---")
    for im in imoveis:
        print(f"[{im['id']}] {im['nome']} - {im['endereco']} | Responsável: {im['usuario']} "
              f"| {len(im['consumos'])} mês(es) registrado(s)")
    print()


def selecionar_imovel():
    listar_imoveis()
    if not imoveis:
        return None
    while True:
        valor = input("Informe o ID do imóvel: ").strip()
        if not valor.isdigit():
            print("Informe um ID numérico válido.\n")
            continue
        id_escolhido = int(valor)
        for im in imoveis:
            if im["id"] == id_escolhido:
                return im
        print("Imóvel não encontrado.\n")



def registrar_consumo_mensal():
    print("\n--- Registrar Consumo Mensal ---")
    imovel = selecionar_imovel()
    if imovel is None:
        return

    mes = ler_mes()
    ano = ler_ano()
    kwh = ler_consumo_kwh("Consumo do mês em kWh: ")

    for registro in imovel["consumos"]:
        if registro["mes"] == mes and registro["ano"] == ano:
            print(f"Já existe um registro para {MESES_NOME[mes - 1]}/{ano}. "
                  f"O valor será atualizado de {registro['kwh']:.2f} para {kwh:.2f} kWh.")
            registro["kwh"] = kwh
            salvar_dados()
            print("Registro atualizado com sucesso!\n")
            return

    imovel["consumos"].append({"mes": mes, "ano": ano, "kwh": kwh})
    salvar_dados()
    print(f"Consumo de {MESES_NOME[mes - 1]}/{ano} registrado com sucesso!\n")



def calcular_media(imovel):
    consumos = imovel["consumos"]
    if not consumos:
        return None
    total = sum(c["kwh"] for c in consumos)
    return total / len(consumos)


def exibir_media_mensal():
    print("\n--- Consumo Médio Mensal ---")
    imovel = selecionar_imovel()
    if imovel is None:
        return

    consumos = imovel["consumos"]
    if not consumos:
        print(f"O imóvel '{imovel['nome']}' ainda não possui consumo registrado.\n")
        return

    total = sum(c["kwh"] for c in consumos)
    media = total / len(consumos)

    print(f"\nImóvel: {imovel['nome']}")
    print(f"Foram somados os consumos de {len(consumos)} mês(es) registrado(s): "
          f"{total:.2f} kWh no total.")
    print(f"Média = {total:.2f} kWh ÷ {len(consumos)} mês(es) = {media:.2f} kWh/mês\n")



def identificar_maior_consumo():
    print("\n--- Maior Consumo Registrado ---")
    imovel = selecionar_imovel()
    if imovel is None:
        return

    consumos = imovel["consumos"]
    if not consumos:
        print(f"O imóvel '{imovel['nome']}' ainda não possui consumo registrado.\n")
        return

    maior = max(consumos, key=lambda c: c["kwh"])
    print(f"\nImóvel: {imovel['nome']}")
    print(f"Maior consumo registrado: {maior['kwh']:.2f} kWh, "
          f"em {MESES_NOME[maior['mes'] - 1]}/{maior['ano']}.\n")



def exibir_resumo():
    print("\n--- Resumo Energético ---")
    imovel = selecionar_imovel()
    if imovel is None:
        return

    consumos = imovel["consumos"]
    print(f"\nImóvel: {imovel['nome']} - {imovel['endereco']}")
    print(f"Responsável: {imovel['usuario']}")

    if not consumos:
        print("Nenhum consumo registrado até o momento.\n")
        return

    consumos_ordenados = sorted(consumos, key=lambda c: (c["ano"], c["mes"]))
    print(f"\nMeses registrados: {len(consumos)}")
    print("-" * 45)
    for c in consumos_ordenados:
        print(f"{MESES_NOME[c['mes'] - 1]:<10}/{c['ano']} : {c['kwh']:>8.2f} kWh")
    print("-" * 45)

    media = calcular_media(imovel)
    maior = max(consumos, key=lambda c: c["kwh"])
    print(f"Consumo médio mensal : {media:.2f} kWh/mês")
    print(f"Maior consumo        : {maior['kwh']:.2f} kWh "
          f"({MESES_NOME[maior['mes'] - 1]}/{maior['ano']})\n")



def exibir_grafico():
    print("\n--- Gráfico de Consumo Mensal ---")
    imovel = selecionar_imovel()
    if imovel is None:
        return

    consumos = imovel["consumos"]
    if not consumos:
        print(f"O imóvel '{imovel['nome']}' ainda não possui consumo registrado.\n")
        return

    consumos_ordenados = sorted(consumos, key=lambda c: (c["ano"], c["mes"]))
    maior_valor = max(c["kwh"] for c in consumos_ordenados)
    escala = 40 / maior_valor  # 40 caracteres representam o maior valor

    print(f"\nImóvel: {imovel['nome']}\n")
    for c in consumos_ordenados:
        barras = "█" * max(1, round(c["kwh"] * escala))
        rotulo = f"{MESES_NOME[c['mes'] - 1][:3]}/{c['ano']}"
        print(f"{rotulo:<9} | {barras} {c['kwh']:.2f} kWh")
    print()



def exibir_menu():
    print("""
==================================================================
   Sistema de Dimensionamento Energético Residencial
==================================================================
[1] Cadastrar imóvel
[2] Listar imóveis cadastrados
[3] Registrar consumo mensal (kWh)
[4] Calcular consumo médio mensal
[5] Identificar maior consumo e o mês/ano
[6] Exibir resumo energético completo
[7] Exibir gráfico de consumo mensal
[0] Sair
""")


def main():
    carregar_dados()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_imovel()
        elif opcao == "2":
            listar_imoveis()
        elif opcao == "3":
            registrar_consumo_mensal()
        elif opcao == "4":
            exibir_media_mensal()
        elif opcao == "5":
            identificar_maior_consumo()
        elif opcao == "6":
            exibir_resumo()
        elif opcao == "7":
            exibir_grafico()
        elif opcao == "0":
            salvar_dados()
            print("Dados salvos. Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
