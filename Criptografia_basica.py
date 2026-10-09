senha = "123456"
senha_criptografada = ""

for numero in senha:
    numero = int(numero) + 1
    senha_criptograda += str(numero)
    
print(senha_criptografada)
