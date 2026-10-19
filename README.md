# Trabalho Computacional - Otimização de Tanque Cilíndrico

📐 Otimização do projeto de um tanque cilíndrico de armazenamento.

Este trabalho computacional foi desenvolvido para a disciplina de Métodos Numéricos / Computação Aplicada. O objetivo é determinar as dimensões ideais de um tanque cilíndrico que minimizam o custo total de material, respeitando a restrição de volume.

## Objetivo

Minimizar a função de custo total:

$$
f(r, h) = 150(\pi r^2) + 100(2\pi r h) + 200(\pi r^2)
= 350\pi r^2 + 200\pi r h
\]

onde:
- $r$ é o raio da base do tanque;
- $h$ é a altura do tanque.

A restrição de capacidade é dada por:

$$
g(r, h) = 500 - \pi r^2 h \le 0
$$

ou seja, o volume do tanque não pode ultrapassar 500 unidades de volume.

## Metodologia Numérica

Para resolver o problema de otimização não linear restrita, foram combinadas três técnicas fundamentais:

### 1. Função de Penalização

A restrição foi incorporada à função objetivo por meio de uma penalização:

$$
P(r, h) = f(r, h) + \mu \cdot [\max(0, g(r, h))]^2
$$

Essa estratégia penaliza soluções inviáveis, forçando o algoritmo a buscar pontos admissíveis.

### 2. Diferenças Finitas

As derivadas parciais foram aproximadas numericamente usando diferenças finitas simples adiantadas:

$$
\frac{\partial P}{\partial r} \approx \frac{P(r + \Delta, h) - P(r, h)}{\Delta},
\quad
\frac{\partial P}{\partial h} \approx \frac{P(r, h + \Delta) - P(r, h)}{\Delta}
$$

com $\Delta = 10^{-5}$.

### 3. Método do Gradiente Descendente

A busca da solução ótima foi conduzida pelo método do gradiente descendente:

$$
r^{(k+1)} = r^{(k)} - \alpha \frac{\partial P}{\partial r}\Big|^{(k)}
$$

$$
h^{(k+1)} = h^{(k)} - \alpha \frac{\partial P}{\partial h}\Big|^{(k)}
$$

onde $\alpha$ é a taxa de aprendizado.

## Resultados Ótimos

A solução do problema foi obtida numericamente por meio da combinação das técnicas acima, considerando a penalização da restrição e a atualização iterativa das variáveis.

O resultado final fornece a configuração ótima de raio e altura que minimiza o custo do tanque, respeitando o limite de volume imposto.

## Como executar

```bash
git clone https://github.com/seu-usuario/otimizacao-tanque-cilindrico.git

# Entrar na pasta do projeto
cd otimizacao-tanque-cilindrico

# Executar o código em Python
python tanque_otimizacao.py
```

## Estrutura do Repositório

```text
.
├── Otimizacao_TanqueCilindrico.py   # Código-fonte principal em Python
├── README.md              # Documentação do repositório
└── .gitignore
```

## Licença

Este projeto é de livre utilização para fins acadêmicos e educacionais.
