"""
Sistema de Dimensionamento Energético Residencial
--------------------------------------------------
MVP: cadastro de imóveis, cadastro de equipamentos elétricos (catálogo),
associação de equipamentos a um imóvel (quantidade + tempo médio diário
de uso) e cálculo do consumo médio mensal estimado, por equipamento e
total do imóvel, em kWh/mês.
"""

DIAS_NO_MES = 30

# ---------------------------------------------------------------------------
# "Base de dados" em memória
# ---------------------------------------------------------------------------
imoveis = []   # cada item: {"id", "nome", "endereco", "equipamentos": [...]}
catalogo = []  # cada item: {"id", "nome", "categoria", "potencia_w"}


# ---------------------------------------------------------------------------
# Funções auxiliares de entrada validada
# ---------------------------------------------------------------------------
def ler_texto_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo é obrigatório. Tente novamente.\n")


def ler_numero_positivo(mensagem, permitir_decimal=True):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            numero = float(valor) if permitir_decimal else int(valor)
        except ValueError:
            print("Valor inválido. Informe um número.\n")
            continue
        if numero <= 0:
            print("O valor deve ser maior que zero.\n")
            continue
        return numero


def ler_horas_uso(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            horas = float(valor)
        except ValueError:
            print("Valor inválido. Informe um número.\n")
            continue
        if horas <= 0 or horas > 24:
            print("Informe um valor entre 0 e 24 horas.\n")
            continue
        return horas


# ---------------------------------------------------------------------------
# US1 - Cadastro de imóvel
# ---------------------------------------------------------------------------
def cadastrar_imovel():
    print("\n--- Cadastro de Imóvel ---")
    nome = ler_texto_obrigatorio("Identificação do imóvel (ex: Casa, Apartamento 101): ")
    endereco = ler_texto_obrigatorio("Endereço/localidade: ")
    imovel = {
        "id": len(imoveis) + 1,
        "nome": nome,
        "endereco": endereco,
        "equipamentos": [],  # {"equipamento": dict, "quantidade": int, "horas_dia": float}
    }
    imoveis.append(imovel)
    print(f"Imóvel '{nome}' cadastrado com sucesso! (ID {imovel['id']})\n")


def listar_imoveis():
    if not imoveis:
        print("\nNenhum imóvel cadastrado ainda.\n")
        return
    print("\n--- Imóveis Cadastrados ---")
    for im in imoveis:
        print(f"[{im['id']}] {im['nome']} - {im['endereco']} ({len(im['equipamentos'])} equipamento(s))")
    print()


def selecionar_imovel():
    listar_imoveis()
    if not imoveis:
        return None
    id_escolhido = int(ler_numero_positivo("Informe o ID do imóvel: ", permitir_decimal=False))
    for im in imoveis:
        if im["id"] == id_escolhido:
            return im
    print("Imóvel não encontrado.\n")
    return None


# ---------------------------------------------------------------------------
# US2 - Cadastro de equipamentos elétricos (catálogo)
# ---------------------------------------------------------------------------
def cadastrar_equipamento():
    print("\n--- Cadastro de Equipamento ---")
    nome = ler_texto_obrigatorio("Nome do equipamento (ex: Geladeira): ")
    categoria = ler_texto_obrigatorio("Categoria (ex: Cozinha, Iluminação): ")
    potencia = ler_numero_positivo("Potência nominal em watts (W): ")
    equipamento = {
        "id": len(catalogo) + 1,
        "nome": nome,
        "categoria": categoria,
        "potencia_w": potencia,
    }
    catalogo.append(equipamento)
    print(f"Equipamento '{nome}' cadastrado com sucesso! (ID {equipamento['id']})\n")


def listar_catalogo():
    if not catalogo:
        print("\nNenhum equipamento cadastrado no catálogo ainda.\n")
        return
    print("\n--- Catálogo de Equipamentos ---")
    for eq in catalogo:
        print(f"[{eq['id']}] {eq['nome']} | Categoria: {eq['categoria']} | Potência: {eq['potencia_w']:.0f} W")
    print()


def selecionar_equipamento_catalogo():
    listar_catalogo()
    if not catalogo:
        return None
    id_escolhido = int(ler_numero_positivo("Informe o ID do equipamento: ", permitir_decimal=False))
    for eq in catalogo:
        if eq["id"] == id_escolhido:
            return eq
    print("Equipamento não encontrado.\n")
    return None


# ---------------------------------------------------------------------------
# US3 - Associação de equipamentos ao imóvel
# ---------------------------------------------------------------------------
def associar_equipamento_ao_imovel():
    print("\n--- Associar Equipamento a um Imóvel ---")
    imovel = selecionar_imovel()
    if imovel is None:
        return

    equipamento = selecionar_equipamento_catalogo()
    if equipamento is None:
        return

    quantidade = int(ler_numero_positivo("Quantidade deste equipamento no imóvel: ", permitir_decimal=False))
    horas_dia = ler_horas_uso("Tempo médio diário de uso (em horas, 0-24): ")

    imovel["equipamentos"].append({
        "equipamento": equipamento,
        "quantidade": quantidade,
        "horas_dia": horas_dia,
    })
    print(f"Equipamento '{equipamento['nome']}' associado ao imóvel '{imovel['nome']}' com sucesso!\n")


# ---------------------------------------------------------------------------
# US4 e US5 - Cálculo do consumo mensal (por equipamento e total do imóvel)
# ---------------------------------------------------------------------------
def calcular_consumo_mensal_equipamento(item):
    """Consumo mensal estimado (kWh) de um equipamento associado a um imóvel."""
    potencia_w = item["equipamento"]["potencia_w"]
    quantidade = item["quantidade"]
    horas_dia = item["horas_dia"]
    consumo_wh_mes = potencia_w * quantidade * horas_dia * DIAS_NO_MES
    return consumo_wh_mes / 1000  # Wh -> kWh


def exibir_consumo_do_imovel():
    print("\n--- Consumo Médio Mensal Estimado ---")
    imovel = selecionar_imovel()
    if imovel is None:
        return

    if not imovel["equipamentos"]:
        print(f"O imóvel '{imovel['nome']}' ainda não possui equipamentos associados.\n")
        return

    print(f"\nImóvel: {imovel['nome']} - {imovel['endereco']}")
    print("-" * 64)
    consumo_total = 0.0
    for item in imovel["equipamentos"]:
        consumo = calcular_consumo_mensal_equipamento(item)
        consumo_total += consumo
        nome_eq = item["equipamento"]["nome"]
        print(f"{nome_eq:<20} | Qtd: {item['quantidade']:>3} | "
              f"Uso diário: {item['horas_dia']:>4.1f}h | "
              f"Consumo: {consumo:>8.2f} kWh/mês")
    print("-" * 64)
    print(f"CONSUMO TOTAL ESTIMADO DO IMÓVEL: {consumo_total:.2f} kWh/mês\n")


# ---------------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------------
def exibir_menu():
    print("""
==================================================================
   Sistema de Dimensionamento Energético Residencial
==================================================================
[1] Cadastrar imóvel
[2] Cadastrar equipamento no catálogo
[3] Listar equipamentos do catálogo
[4] Listar imóveis cadastrados
[5] Associar equipamento a um imóvel
[6] Calcular consumo médio mensal de um imóvel
[0] Sair
""")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_imovel()
        elif opcao == "2":
            cadastrar_equipamento()
        elif opcao == "3":
            listar_catalogo()
        elif opcao == "4":
            listar_imoveis()
        elif opcao == "5":
            associar_equipamento_ao_imovel()
        elif opcao == "6":
            exibir_consumo_do_imovel()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()
