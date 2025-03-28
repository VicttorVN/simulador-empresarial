
import xlsxwriter

def exportar_excel(nome_arquivo, dados):
    workbook = xlsxwriter.Workbook(nome_arquivo)
    sheet = workbook.add_worksheet("Rodadas")
    sheet.write_row(0, 0, ["Empresa", "Rodada", "Lucro", "Ranking"])
    for i, row in enumerate(dados, start=1):
        sheet.write_row(i, 0, [
            row.get("empresa_id"),
            row.get("rodada"),
            row.get("lucro"),
            row.get("ranking")
        ])
    workbook.close()
    print(f"✅ Planilha gerada: {nome_arquivo}")
