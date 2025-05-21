from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[x] = i
        return []


"""
    - Problema:
    É passado dois parametros uma lista de números inteiros e um alvo inteiro.
    É preciso achar dois indexes dentro de uma lista que a soma dos números é igual ao alvo
    
    - Explicação:
    É possível fazer este problema de duas formas, a forma bruta com a complexidade O(n^2)
    ou fazer da forma mais inteligente com a complexidade O(n)

        - Forma bruta: 
            Consiste em utilizar dois laços aninhados para percorrer todos os pares possíveis de números na lista.

            Para cada elemento, comparamos sua soma com todos os outros elementos seguintes.
            Se a soma for igual ao valor alvo, retornamos os índices correspondentes.

            Essa abordagem é direta e fácil de entender, mas pouco eficiente para listas grandes, pois tem complexidade 
            de tempo O(n^2) — ou seja, o tempo de execução cresce rapidamente conforme o tamanho da lista aumenta.

        - Forma inteligente: 
            Utiliza um hash map (dicionário) para armazenar os valores já percorridos da lista junto com seus respectivos índices.

            A ideia é simples: para cada número na lista, calculamos o complemento, que é alvo - número atual.
            Em seguida, verificamos se esse complemento já foi armazenado no dicionário.

            Se estiver, significa que já encontramos dois números cuja soma é igual ao alvo — basta retornar os índices:

            o índice do complemento (já armazenado no dicionário)

            o índice atual do número sendo analisado

            Se não estiver, adicionamos o número atual ao dicionário com seu índice.

            Essa abordagem permite encontrar a solução em tempo linear O(n), evitando comparações desnecessárias.
"""

# Caso 1
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target)) # [0, 1]

# Caso 2
nums = [3,2,4]
target = 6
print(Solution().twoSum(nums, target)) # [1, 2]

# Caso 3
nums = [3,3]
target = 6
print(Solution().twoSum(nums, target)) # [0, 1]