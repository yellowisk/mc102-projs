with open('./sobrenome.txt', 'r') as s:
    sobrenomes = [line.strip() for line in s]


with open('./primeiro_nome.txt', 'r') as n:
    nomes = [line.strip() for line in n]


sobrenomes = sobrenomes[::-1]
nomes_completos = []

for _ in range(len(nomes)):
    nomes_completos.append(nomes[_] + ' ' + sobrenomes[_])

nomes_completos.sort()

with open('membros.md', 'w') as f:
    f.write('# Organizacao\n')
    f.write('1. Membros da organizacao\n')
    for _ in range(len(nomes_completos)):
        if _ < len(nomes_completos) - 1:
            f.write(f'    1. {nomes_completos[_]}\n')
        else:
            f.write(f'    1. {nomes_completos[_]}')