from copy import deepcopy

from dados import produtos
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
print(*produtos, "\n", sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

novos_produtos = deepcopy(produtos)
for i in novos_produtos:
    i['preco'] += i['preco'] * 0.1
 
# novos_produtos = [
#     {**p, 'preco': round(p['preco'] * 1.1, 2)}
#     for p in copy.deepcopy(produtos)
# ]

produtos_ordenados_por_nome = deepcopy(produtos)
produtos_ordenados_por_nome.sort(key=lambda x: x['nome'], reverse=True)

# produtos_ordenados_por_nome = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['nome'],
#     reverse=True
# )

produtos_ordenados_por_preco = deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda x: x["preco"])

# produtos_ordenados_por_preco = sorted(
#     copy.deepcopy(produtos),
#     key=lambda p: p['preco']
# )

print(*novos_produtos, '\n', *produtos_ordenados_por_nome, '\n', *produtos_ordenados_por_preco, sep='\n' )