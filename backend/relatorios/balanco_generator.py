
def gerar_balanco(empresa_id, dados):
    balanco = f"Balanço Patrimonial - Empresa {empresa_id}\n"
    balanco += "-"*35 + "\n"
    balanco += f"Ativos: {dados.get('ativos', 0)}\n"
    balanco += f"Passivos: {dados.get('passivos', 0)}\n"
    balanco += f"Patrimônio Líquido: {dados.get('pl', 0)}\n"
    return balanco
