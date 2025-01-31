from sympy import symbols, Function, simplify

# define a classe para a função C(a)
class C(Function):
    @classmethod
    def eval(cls, a):
        return 7500 * a - 1500

# define a classe para a função M(c)
class M(Function):
    @classmethod
    def eval(cls, c):
        return 0.9 * c - 50

# define a classe para a função V(a) = M(C(a))
class V(Function):
    @classmethod
    def eval(cls, a):
        return simplify(M(C(a)))  # aplica M sobre C(a) e simplifica

# define a variável simbólica
a = symbols('a')

# exibe a função V(a)
print(V(a))

# avalia a função V em a = 2
V_value = V(1.5)

# Exibe o valor da função V avaliado em a = 2 com duas casas decimais
print(f'V(1.5) = {V_value:.2f}')
