from sympy import symbols, Function, simplify

# define a classe para a função P(a)
class P(Function):
    @classmethod
    def eval(cls, a):
        return 25000 * a - 1000

# define a classe para a função M(p)
class M(Function):
    @classmethod
    def eval(cls, p):
        return 0.2 * p - 200

# define a classe para a função MoP(a) = M(P(a))
class MoP(Function):
    @classmethod
    def eval(cls, a):
        return simplify(M(P(a)))  # aplica M sobre P(a) e simplifica

# define a variável simbólica
a = symbols('a')

# avalia a função P em a = 3
P_value = P(3)

# avalia a função M em P_value
M_value = M(P_value)

# avalia a função Mop em a = 3
MoP_value = MoP(3)

# exibe a função MoP em a
print(MoP(a))

# exibe o valor da função MoP avaliado em a = 3 com duas casas decimais
print(f'M(3)= {M_value:.2f}')
print(f'MoP(3) = {MoP_value:.2f}')
