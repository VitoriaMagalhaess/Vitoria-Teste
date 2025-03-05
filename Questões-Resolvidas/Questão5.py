def inverter_string(s):
    invertida =""
    for char in s:
        invertida = char + invertida
        return invertida
string_original = input("Digite uma string para inverter:")
print("String invertida:", inverter_string(string_original))
