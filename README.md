# O que é?

Este projeto diz respeito a um script, desenvolvido em Python, para ataque de senhas que estão em hash. 
Como sabemos, existem diversas modalidades de hash, como md5, sha1, sha256, sha384 e muitos outros. Este script pode ser utilizado em qualquer um destes cenários, porquanto definimos
o tipo de algoritmo na chamada do algoritmo. 

## Como usar o attackHash.py

Hash Attack Tool
Modo de uso: python attackHash.py wordlistDeSenhas arquivoVazio hashsEncontradosNoPentest algoritmo
Exemplo: python attackHash.py wordlist.txt wordlistEmHash.txt senhasEmHash.txt sha256

Este algoritmo recebe, no total, 5 parâmetros, contando com o nome do script.
São eles:
--> O nome do script
--> Uma wordlist pessoal de senhas, uma senha por linha.
--> Um arquivo vazio, para armazenar os hashes gerados da wordlist definida anteriormente
--> Um arquivo com os hashs que desejamos descobrir, um hash por linha.
--> O algoritmo que desejamos utilizar, como sha256, sha512, md5 e outros...

### Como funciona?
Este script faz a leitura da sua wordlist e aplica o algoritmo definido na chamada dele para todas as senhas. Ele salva o resultado dessa operação no formato "senha - hash" dentro do arquivo
vazio, que passamos como terceiro parâmetro. O resultado é similar a este:

admin - 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
password - 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8
manager - 6ee4a469cd4e91053847f5d3fcb61dbcc91e8f0ef10be7748da4c4a1ba382d17
letmein - 1c8bfe8f801d79745c4631d09fff36c82aa37fc4cce4fc946683d7b336b63032


Em seguida, o script faz a leitura deste arquivo, fazendo split (separação) pelo sinal de '-' e captura a primeira parte, que são as senhas, e a segunda, que são os hashes, em duas variáveis diferentes.
Por fim, ele itera o 5º parâmetro, que é o arquivo que contém os hashes que queremos descobrir, e caso ele encontre alguma correspondencia, ele retorna a senha encontrada e o hash dela.
