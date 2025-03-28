
fetch("/api/ranking")
    .then(r => r.json())
    .then(data => {
        const empresas = data.map(r => "Empresa " + r.empresa_id);
        const lucros = data.map(r => r.lucro);
        const ctx = document.getElementById("grafico").getContext("2d");
        new Chart(ctx, {
            type: "bar",
            data: {
                labels: empresas,
                datasets: [{
                    label: "Lucro por Empresa",
                    data: lucros,
                    backgroundColor: "#0d6efd"
                }]
            }
        });

        const rankHTML = data.map((r, i) => `<p><strong>${i+1}º:</strong> Empresa ${r.empresa_id} - Lucro: R$${r.lucro}</p>`).join("");
        document.getElementById("ranking").innerHTML = rankHTML;
    });
