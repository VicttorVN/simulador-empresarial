
def gerar_dre(empresa_id, dados):
    dre = f"DRE - Empresa {empresa_id}\n"
    dre += "-"*30 + "\n"
    dre += f"Receitas: {dados.get('receita', 0)}\n"
    dre += f"Custos: {dados.get('custos', 0)}\n"
    dre += f"Despesas RH: {dados.get('rh', 0)}\n"
    dre += f"Resultado: {dados.get('lucro', 0)}\n"
    return dre
