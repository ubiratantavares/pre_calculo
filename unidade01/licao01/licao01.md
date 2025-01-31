# Lição 1 - Funções Compostas

## 1. Introdução à composição de funções

Caio é um fazendeiro. Todo ano ele planta sementes que virarão milho. 

A função abaixo nos dá a quantidade de milho, **C**, em quilogramas (kg), que ele espera produzir se ele plantar milho em certa quantidade **a** de acres de terra.

$$
C(a) = 7500a - 1500
$$

Definindo a função em Python:

* **script01.py**

```Python
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
```

Por exemplo, se Caio planta sementes de milho em dois acres de terra, ele espera produzir 

$$
C(2) = 7.500(2) - 1.500 = 15.000 - 1.500 = 13.500
$$

Avaliando a função no valor de $a = 2$.

* **script02.py**

```Python
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
print(C(a))

```

**Resposta: 13.500 kg de milho.**

O que Caio quer realmente saber é o quanto de dinheiro ele conseguirá vendendo este milho. 

Então, ele utiliza a seguinte função para estimar a quantidade de dinheiro, **M**, em reais, que ele ganhará vendendo **c** quilogramas de milho.

$$
M(c) = 0,9c - 50
$$

Então, se Caio produzir 13.500 kg de milho, ele pode estimar que vai ganhar:

$$
M(13.500) = 0,9 \times 13.500 - 50 = 12.100
$$

Definindo a função M e avaliando em c = 13.500 na linguagem Python:

* **script03.py**

```Python
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
```

**Resposta: 12.100 kg de milho.**

Observe que Caio tem que usar duas funções separadas para converter acres plantados em ganhos esperados. 

A primeira função, **C**, transforma acres em milho, enquanto a segunda função, **M**, transforma milho em dinheiro.

![Figura 1](https://github.com/ubiratantavares/pre_calculo/blob/main/unidade01/licao01/figura01.png)

Não seria ótimo se Caio pudesse escrever uma função que transformasse diretamente acres plantados em ganhos esperados?

![Figura 2](https://github.com/ubiratantavares/pre_calculo/blob/main/unidade01/licao01/figura02.png)

* **Como criar uma nova função**

De fato, podemos encontrar a função que leva diretamente de acres plantados para ganhos esperados! 

Para encontrar essa nova função, vamos pensar sobre a questão mais geral. 

Quanto dinheiro Caio espera ganhar se ele plantar sementes de milho em **a** acres de terra?

Se Caio planta milho em **a** acres, ele espera produzir **C(a)** quilogramas de milho. 

E, se ele produz **C(a)** quilogramas de milho, ele espera ganhar **M(C(a))** reais.

![Figura 3](https://github.com/ubiratantavares/pre_calculo/blob/main/unidade01/licao01/figura03.png)

Então, para encontrar uma regra geral que converta **a** acres diretamente em ganhos esperados, podemos encontrar a expressão **M(C(a))**.

Mas como fazemos isso? 

Observe que na expressão **M(C(a))**, a entrada da função **M** é **C(a)**. 

Então, para encontrar essa expressão, podemos substituir **c** por **C(a)** na função **M**.

$$
M(C(a)) = 0,9C(a) - 50 = 0,9\times(7.500a - 1.500) - 50 = 6.750a - 1.350 - 50 = 6.750a - 1.400
$$

Definindo e avaliando a função composta M(C(a)) em a = 2 usando Python

* **script04.py**

```Python
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
V_value = V(2)

# Exibe o valor da função V avaliado em a = 2 com duas casas decimais
print(f'V(2) = {V_value:.2f}')
```

Sendo assim, a função acima converte diretamente acres plantados em ganhos esperados. 

Vamos utilizar esta nova função para estimar a quantidade de dinheiro que Caio conseguirá plantando milho em dois acres.

$$
M(C(2)) = 6.750\times2 - 1.400 = 13.500 - 1.400 = 12.100
$$

Caio pode esperar lucrar **12.100** plantando milho em dois acres, o que está consistente com nosso trabalho anterior!

* **Como definir funções compostas**

Acabamos de descobrir o que é uma função composta. 

Ao invés de substituirmos acres plantados em uma função de milho e, em seguida, substituir a quantidade de milho produzido na função de ganhos, 
encontramos uma função que converte diretamente os acres plantados em ganhos esperados.

Fizemos isso substituindo **C(a)** na função **M**, ou encontrando **M(C(a))**. 

Vamos chamar essa nova função:

$$
(M\circ C)(a)=M(C(a))
$$

Que é lida como "M composta com C".

Isto é, na verdade, a definição formal de composição de função.

* **Visualização dos dois métodos**

Temos aqui uma ajuda visual para interpretar a definição acima.

![Figura 4](https://github.com/ubiratantavares/pre_calculo/blob/main/unidade01/licao01/figura04.png)

Ao utilizarmos ambas as funções **C** e **M**, a função **C**, a função do milho que converte dois em 13.500. 

Então, a função **M**, a função dos ganhos que converte os 13.500 em 12.100 reais.

Ao utilizarmos a função composta, vemos que a função MoC.
 
Converte dois diretamente em 12.100 reais.

* **Problema 1**: Utilizando as funções apresentadas no exemplo, quanto Caio pode esperar ganhar se ele vender todo o milho produzido em 1,5 acre?

**Resposta:** 8.725 reais

* **Problema 2**: Benjamim é um produtor de batatas. A função:

$$
P(a) = 25.000a - 1.000
$$

Nos dá a quantidade de batatas, **P**, em quilogramas, que ele espera produzir plantando batatas em **a** acres de terra. 

A função:

$$
M(p) = 0,2p - 200
$$

Nos dá a quantidade de dinheiro, **M**, em reais, que Benjamim espera conseguir se ele produzir **p** quilogramas de batatas.

Quanto, em dinheiro, Benjamim pode esperar ganhar se ele vender todas as batatas produzidas em 3 acres?

**Resposta:**  reais

* **Problema 3**: Qual das expressões a seguir dá a quantidade de dinheiro que Benjamim espera ganhar se ele plantar batatas em **a** acres de terra?

**Resposta:**

$$
M(P(a)) = 0,2\times(25.000a - 1.000) - 200 = 5.000a - 200 - 200 = 5.000a - 400
$$ 

Definindo as funções P, M e MoP e avaliando em a = 3 usando Python

* **script05.py**

```Python
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
```

## 2. Funções compostas

Dadas duas funções, podemos combiná-las de maneira que as saídas de uma função se tornem as entradas da outra. Isso define uma **função composta**. 

Vamos ver o que isso significa!

* **Calculando funções compostas**

* **Exemplo**

Se $f(x) = 3x - 1$ e $g(x) = x^{3} + 2$, então quanto é f(g(3))?

* **Solução**

Uma forma de calcular f(g(3)) é fazer os cálculos de "dentro para fora". Em outras palavras, vamos calcular g(3) primeiro e então substituir esse resultado em f para encontrar nossa resposta.

Vamos calcular g(3):

$$
g(3) = 3^{3} + 2 = 27 + 2 = 29
$$

Como $g(3) = 29$, então $f(g(3)) = f(29)$.

Agora, vamos calcular f(29):

$$
f(29) = 3\times29- 1 = 87 - 1 = 86
$$

* **Encontrando a função composta**

No exemplo acima, a função g levou de 3 para 29, e então a função f levou de 29 para 86. Vamos encontrar a função que leva 3 diretamente em 86.

Para isso, precisamos compor as duas funções e encontrar f(g(x)).

* **Exemplo**

Quanto é f(g(x))?

* **Solução**

Se analisarmos a expressão f(g(x)), veremos que g(x) é a entrada da função f. Então, vamos substituir g(x) sempre que virmos x na função f.

$$
f(g(x)) = 3g(x) - 1 = 3(x^{3} + 2) - 1 = 3x^{3} + 6 - 1 = 3x^{3} + 5
$$

Essa nova função deve levar 3 diretamente para 86. Vamos verificar!

$$
	f(g(3)) = 3 \times 3^{3} + 5 = 81 + 5 = 86
$$

* **Vamos praticar**

* **Problema 1**

$f(x) = 3x - 1$ e $g(x) = x^{3} + 2$. Calcule g(f(1)).

* **Problema 2**

$m(x) = 3x - 2** e $n(x) = x + 4$. Encontre m(n(x)).

* **Funções Compostas: uma definição formal**

No exemplo acima, encontramos e calculamos uma função composta.

Em geral, para indicar a função f composta com a função g, podemos escrever fog, que é lido como "f composta com g". Essa composição é definida pela seguinte regra: (fog)(x) = f(g(x)).

O diagrama abaixo mostra a relação entre (fog)(x) e f(g(x)).

![Figura 5](https://github.com/ubiratantavares/pre_calculo/blob/main/unidade01/licao01/figura05.png)

Agora, vamos ver outro exemplo com essa nova definição em mente.

* **Exemplo**

$g(x) = x = 4$ e $h(x) = x^{2} - 2x$. Encontre (hog)(x) e (hog)(-2).


Agora, vamos praticar com alguns problemas

* **Problema 3**

$f(x) = 3x - 5$ e $g(x) = 3 - 2x$. Calcule (gof)(3).

Nos problemas 4 e 5, sejam $f(t) = t - 2$ e $g(t) = t^{2} + 5$. 

* **Problema 4**

Encontre (gof)(t).

* **Problema 5**

Encontre (fog)(t)

* **Desafio**

Os gráficos das equações $y = f(x)$ e $y = g(x)$ são mostradas na malha abaixo:

![Figura 6](https://github.com/ubiratantavares/pre_calculo/blob/main/unidade01/licao01/figura06.png)

Qual das seguintes opçóes melhor aproxima-se ao valor de (fog)(8)?

a) -12

b) -3

c) 0

d) 2

## 3. Resolução de funções compostas

## 4. Avalie funções compostas

## 5. Cálculo de funções compostas usando tabelas

## 6. Cálculo de funções compostas usando gráficos

## 7. Calcule funções compostas - gráficos e tabelas

## 8. Como encontrar funções compostas

## 9. Encontre funções compostas

## 10. Cálculo de funções compostas
