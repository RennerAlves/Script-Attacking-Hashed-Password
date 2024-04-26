#!/usr/bin/python

import hashlib
import sys

if len(sys.argv) < 5:
    print("\nHash Attack Tool")
    print("Modo de uso: python attackHash.py wordlistDeSenhas arquivoVazio hashsEncontradosNoPentest algoritmo")
    print("Exemplo: python attackHash.py wordlist.txt wordlistEmHash.txt senhasEmHash.txt sha256")
    sys.exit(1)

wordlist = sys.argv[1]
wordlistComHash = sys.argv[2]
senhasEmHash = sys.argv[3]
algoritmo = sys.argv[4]

# Abrir arquivo para salvar palavras e hashes
try:
    with open(wordlistComHash, 'w') as output_file:
        with open(wordlist, 'r') as listaDePalavras:
            for palavra in listaDePalavras:
                palavra = palavra.strip()
                hash = hashlib.new(algoritmo, palavra.encode()).hexdigest()
                output_file.write(f"{palavra} - {hash}\n")
except Exception as e:
    print(f"Erro ao escrever no arquivo: {e}")
    sys.exit(1)

print(f"\nPalavras e hashes foram salvos em: {wordlistComHash}")

# Carregar os hashes em uma lista
hashes = []
try:
    with open(wordlistComHash, 'r') as hashesBruteForce:
        for linha_hash in hashesBruteForce:
            palavra, hash_salvo = linha_hash.strip().split(' - ')
            hashes.append((palavra, hash_salvo))
except Exception as e:
    print(f"Erro ao carregar os hashes: {e}")
    sys.exit(1)

# Comparar os hashes capturados com os hashes de senhas fornecidas
try:
    with open(senhasEmHash, 'r') as senhasHasheadas:
        for senha_hasheada in senhasHasheadas:
            senha_hasheada = senha_hasheada.strip()
            for palavra, hash_salvo in hashes:
                if hash_salvo == senha_hasheada:
                    print(f"Senha encontrada: {palavra} - {senha_hasheada}")

except Exception as e:
    print(f"Erro ao comparar hashes: {e}")
    sys.exit(1)
