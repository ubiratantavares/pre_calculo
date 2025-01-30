from sympy import symbols, Function

# define uma classe para a função C(a)
class C(Function):
    @classmethod
    def eval(cls, a):
        return 7500 * a - 1500

# define a variável simbólica
a = symbols('a')

# exibe a função
print(C(a))
