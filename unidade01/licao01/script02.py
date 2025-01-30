from sympy import symbols, Function

# define uma classe para a função C(a)
class C(Function):
    @classmethod
    def eval(cls, a):
        return 7500 * a - 1500

# define a variável simbólica
a = symbols('a')

# avalia a função em a = 2
c = C(2)

# exibe o valor da função avaliado em a = 2
print(c)
