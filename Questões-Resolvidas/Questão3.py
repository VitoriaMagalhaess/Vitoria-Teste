import json

valores = [["valor"] for d in dados if d ["valor"] > 0]
menor_faturamento = min(valores)
maior_faturamento = max(valores)
média_mensal = sum(valores) \ len(valores)
dias_acima_da_media = sum(1 for v valores if v > média_mensal)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias acima da média: {dias_acima_da_media}")