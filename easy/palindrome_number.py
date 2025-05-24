class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
            Se for negativo ou número modulo por 10 é igual a 0, 
            pois todo número (exceto o 0) quando intertido o
            0 vai ficar a esquerda logo é desconsiderado e não será
            palindromo
        """
        if x < 0 or ((x % 10) == 0 and x > 0): return False

        CONST_10 = 10
        currentValue = x
        beforeValue = None
        remainderDivision = 0
        halfPart = 0

        """
            A idéia aqui é tirar o módulo e a parte inteira da divisão por 10,
            e ir montando o valor de trás pra frente até que a metade da parte
            montada seja igual ao valor inicial que está sendo retirado o último
            dígito a cada iteração (em caso de total de dígitos pares) ou verificar
            a metade com o valor anterior os calculos de remoção do último dígito
            (em caso de total de dígitos ímpares).
        """
        while True:
            beforeValue = currentValue
            remainderDivision = currentValue % CONST_10
            currentValue = currentValue // CONST_10
            halfPart = (halfPart * CONST_10) + remainderDivision
           
            if currentValue == halfPart or halfPart == beforeValue:
                return True
            if halfPart > currentValue: return False
        
        return False
    
print(Solution().isPalindrome(1221)) # True

print(Solution().isPalindrome(12121)) # True

print(Solution().isPalindrome(122)) # False

print(Solution().isPalindrome(-121)) # False

print(Solution().isPalindrome(1001)) # True

print(Solution().isPalindrome(100)) # False

print(Solution().isPalindrome(110)) # False

print(Solution().isPalindrome(101)) # True

print(Solution().isPalindrome(0)) # True

print(Solution().isPalindrome(999)) # True