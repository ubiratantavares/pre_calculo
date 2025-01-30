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

* **Problema 3**: Qual das expressões a seguir dá a quantidade de dinheiro que Benjamim espera ganhar se ele plantar batatas em **a** acres de terra?

$$
M(P(a)) = 0,2\times(25.000a - 1.000) - 200 = 5.000a - 200 - 200 = 5.000a - 400
$$ 

## 2. Funções compostas

Dadas duas funções, podemos combiná-las de maneira que as saídas de uma função se tornem as entradas da outra. Isso define uma **função composta**. Vamos ver o que isso significa!

## 3. Resolução de funções compostas

## 4. Avalie funções compostas

## 5. Cálculo de funções compostas usando tabelas

## 6. Cálculo de funções compostas usando gráficos

## 7. Calcule funções compostas - gráficos e tabelas

## 8. Como encontrar funções compostas

## 9. Encontre funções compostas

## 10. Cálculo de funções compostas
