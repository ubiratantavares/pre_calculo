from sympy import symbols, Function

# define uma classe para a função C(a)
class C(Function):
    @classmethod
    def eval(cls, a):
        return 7500 * a - 1500

# define uma classe para a função M(c)
class M(Function):
    @classmethod
    def eval(cls, c):
        return 0.9 * c - 50

# define a variável simbólica
a = symbols('a')
c = symbols('c')

# avalia a função C em a = 2
C_value = C(2)

# avalia a função M em c = C_Value
M_value = M(C_value)

# exibe o valor da função M avaliado em c = C_value
print(f'{M_value:.2f}')

