def calcular_percentual(faturamento_estado, faturamento_total):
    return (faturamento_estado / faturamento_total) * 100

distribuidora = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(distribuidora.values())
for estado, valor in distribuidora.items():
    percentual = calcular_percentual(valor, faturamento_total)
    print(f"{estado}: {percentual:.2f}%")
