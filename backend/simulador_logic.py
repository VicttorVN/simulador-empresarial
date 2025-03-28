
def processar_rodada(decisoes, rodada_numero):
    resultados = []
    for decisao in decisoes:
        lucro = (
            sum(decisao.get("comercial", {}).values())
            - sum(decisao.get("rh", {}).values())
            - sum(decisao.get("producao", {}).values())
            - sum(decisao.get("financas", {}).values())
        )
        resultados.append({
            "empresa_id": decisao.get("empresa_id"),
            "rodada": rodada_numero,
            "lucro": lucro,
            "ranking": 0
        })
    resultados.sort(key=lambda x: x["lucro"], reverse=True)
    for i, r in enumerate(resultados):
        r["ranking"] = i + 1
    return resultados
