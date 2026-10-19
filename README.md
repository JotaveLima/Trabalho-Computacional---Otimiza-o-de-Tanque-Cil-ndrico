# Trabalho Computacional-Otimização de Tanque Cilíndrico

📐 Otimização do Projeto de um Tanque Cilíndrico de ArmazenamentoTrabalho computacional desenvolvido para a disciplina de Métodos Numéricos / Computação Aplicada. O objetivo é determinar as dimensões ideais de raio ($r$) e altura ($h$) de um tanque cilíndrico que minimizem o custo total de fabricação, garantindo o atendimento à restrição de volume mínimo de $500\text{ m}^3$.Este repositório contém a implementação completa do algoritmo em Python, utilizando o Método do Gradiente Descendente, Funções de Penalização Exterior e Diferenças Finitas Adiantadas.📌 Descrição do ProblemaO custo de fabricação do tanque varia conforme as áreas de suas superfícies e os valores de custo unitário dos materiais:Base do Tanque: R$ 150,00 / m²Parede Lateral: R$ 100,00 / m²Teto do Tanque: R$ 200,00 / m²Formulação MatemáticaFunção Objetivo (Custo Total):
$$f(r, h) = 150(\pi r^2) + 100(2\pi r h) + 200(\pi r^2) = 350\pi r^2 + 200\pi r h$$Restrição de Desigualdade ($g(r, h) \le 0$):
$$g(r, h) = 500 - \pi r^2 h \le 0$$🛠️ Metodologia NuméricaPara resolver este problema de otimização não linear restrita, foram combinadas três técnicas fundamentais:Função de Penalização Exterior: Transforma o problema restrito em um problema irrestrito equivalente através da função auxiliar $P(r, h)$:
$$P(r, h) = f(r, h) + \mu \cdot [\max(0, g(r, h))]^2$$Diferenças Finitas Simples Adiantadas ($\Delta = 10^{-5}$): Aproximação das derivadas parciais sem necessidade de cálculo analítico:
$$\frac{\partial P}{\partial r} \approx \frac{P(r + \Delta, h) - P(r, h)}{\Delta}, \quad \frac{\partial P}{\partial h} \approx \frac{P(r, h + \Delta) - P(r, h)}{\Delta}$$Método do Gradiente Descendente: Atualização iterativa no sentido oposto ao gradiente (direção de menor custo):
$$r^{(k+1)} = r^{(k)} - \alpha \frac{\partial P}{\partial r}\Big\vert{}^{(k)}, \quad h^{(k+1)} = h^{(k)} - \alpha \frac{\partial P}{\partial h}\Big\vert{}^{(k)}$$🎯 Resultados ÓtimosUtilizando os parâmetros do caso base ($\alpha = 10^{-6}$ e $\mu = 10^4$), o algoritmo convergiu com alta precisão:Raio Ótimo ($r^*$): 4,571 mAltura Ótima ($h^*$): 7,613 mVolume Final Alcançado: 500,00 m³ (Restrição satisfeita no limite ativo)Custo Mínimo de Fabricação: R$ 68.224,10Estudo de Sensibilidade dos ParâmetrosTaxa de Aprendizado (α)Fator de Penalidade (μ)Raio r∗ (m)Altura h∗ (m)Volume (m3)Custo Total (R$)IteraçõesComportamento Observado$10^{-7}$$10^4$$4,562$$7,630$$499,1$R$ 68.210,50$150.000^*$Convergência lenta (atingiu limite de iterações)$10^{-6}$$10^2$$4,380$$7,205$$434,2$R$ 63.380,20$12.450$Inviável (Penalidade fraca; violou volume mínimo)$10^{-6}$$10^4$$4,571$$7,613$$500,0$R$ 68.224,10$48.210$Configuração Ideal$10^{-6}$$10^6$$4,571$$7,608$$500,0$R$ 68.225,80$118.900$Penalidade rígida (sistema rígido/stiff)$5 \cdot 10^{-6}$$10^4$$4,571$$7,613$$500,0$R$ 68.224,10$9.642$Convergência rápida$10^{-5}$$10^4$N/AN/AN/ADivergiuN/AInstável (Overshooting pelo passo muito longo)🚀 Como ExecutarPré-requisitosPython 3.x instalado (utiliza apenas a biblioteca padrão math, sem necessidade de bibliotecas externas).ExecuçãoClone este repositório e execute o script principal:# Clonar o repositório
git clone https://github.com/seu-usuario/otimizacao-tanque-cilindrico.git

# Entrar na pasta do projeto
cd otimizacao-tanque-cilindrico

# Executar o código em Python
python tanque_otimizacao.py
📁 Estrutura do Repositório.
├── tanque_otimizacao.py   # Código-fonte principal em Python
├── README.md              # Documentação do repositório
└── Relatorio.md           # Trabalho escrito acadêmico completo
📄 LicençaEste projeto é de livre utilização para fins acadêmicos e educacionais.
