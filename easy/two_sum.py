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

        - Forma bruta: Criar dois laços aninhados onde percorrerá valor a valor e ir comparando
        se a soma deles é igual ao alvo

        - Forma inteligente: Usar o conceito de hash map para criar um histórico dos valores 
        já acessados e seus indexes, para isso calcula-se um complemento para cada valor
        na lista e verifica se existe no dicionário, caso sim os valores dos indexes são o index
        do valor do complemento no dicionário e o index do valor atual.
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