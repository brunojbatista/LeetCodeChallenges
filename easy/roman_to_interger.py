class Solution:
    ROMAN_NUMERALS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    """
        A lógica de converter um número romano em inteiro é a seguinte:
        leia as letras da direita para a esquerda, então faça:
            Se o valor da letra atual for maior ou igual da ultima letra lida, some ao valor final
            Caso contrário, subtraia o valor da letra pelo valor final
    """
    def romanToInt(self, s: str) -> int:
        totalLetters = len(s)
        lastNumber = 0
        value = 0
        """
            A cada iteração, é lido a ultima letra e extraido o valor dele,
            caso o valor atual seja maior ou igual ao anterior soma-se ao 
            valor final, caso contrário subtrai-se do valor final.
        """
        for i in range(totalLetters - 1, -1, -1):
            currentValue = Solution.ROMAN_NUMERALS[s[i]]
            if currentValue >= lastNumber:
                value += currentValue
            else:
                value -= currentValue
            lastNumber = currentValue
        return value

print(Solution().romanToInt("III")) # 3

print(Solution().romanToInt("LVIII")) # 58

print(Solution().romanToInt("MCMXCIV")) # 1994
