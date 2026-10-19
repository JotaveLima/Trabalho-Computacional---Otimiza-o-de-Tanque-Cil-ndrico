"""
TRABALHO COMPUTACIONAL - OTIMIZAÇÃO DE TANQUE CILÍNDRICO
Disciplina: Modelagem Computacional
Alunos: Eduardo Woyames Cardoso e João Victor B. Lima
Método: Gradiente Descendente com Penalização e Diferenças Finitas.
"""

import math



# 1. DEFINIÇÃO DO MODELO FÍSICO E DA FUNÇÃO OBJETIVO

def custo_real(r: float, h: float) -> float:
    """
    Calcula o custo total de fabricação do tanque cilíndrico sem penalidades.
    
    f(r, h) = 150*(pi*r^2) + 100*(2*pi*r*h) + 200*(pi*r^2) = 350*pi*r^2 + 200*pi*r*h
    
    Parâmetros:
        r (float): Raio da base (m)
        h (float): Altura do tanque (m)
    Retorna:
        float: Custo em R$
    """
    area_base = math.pi * (r ** 2)
    area_lateral = 2.0 * math.pi * r * h
    area_teto = math.pi * (r ** 2)
    
    custo = (150.0 * area_base) + (100.0 * area_lateral) + (200.0 * area_teto)
    return custo


def restricao_g(r: float, h: float, v_min: float = 500.0) -> float:
    """
    Calcula a restrição de desigualdade g(r, h) <= 0.
    
    g(r, h) = V_min - pi*r^2*h <= 0
    
    Parâmetros:
        r (float): Raio da base (m)
        h (float): Altura do tanque (m)
        v_min (float): Volume mínimo exigido (m^3)
    Retorna:
        float: Valor de g(r, h). Positivo se inviável, negativo ou zero se viável.
    """
    volume = math.pi * (r ** 2) * h
    return v_min - volume


def funcao_penalizada_P(r: float, h: float, mu: float, v_min: float = 500.0) -> float:
    """
    Calcula a Função de Penalização P(r, h) = f(r, h) + mu * [max(0, g(r, h))]^2
    """
    f = custo_real(r, h)
    g = restricao_g(r, h, v_min)
    penalidade = max(0.0, g) ** 2
    return f + mu * penalidade



# 2. CÁLCULO DAS DERIVADAS PARCIAIS NUMÉRICAS (DIFERENÇAS FINITAS)

def gradiente_numerico(r: float, h: float, mu: float, delta: float = 1e-5):
    """
    Aproxima o vetor gradiente [dP/dr, dP/dh] utilizando Diferenças Finitas.
    
    dP/dr ≈ (P(r + delta, h) - P(r, h)) / delta
    dP/dh ≈ (P(r, h + delta) - P(r, h)) / delta
    """
    P_atual = funcao_penalizada_P(r, h, mu)
    
    P_r_delta = funcao_penalizada_P(r + delta, h, mu)
    dP_dr = (P_r_delta - P_atual) / delta
    
    P_h_delta = funcao_penalizada_P(r, h + delta, mu)
    dP_dh = (P_h_delta - P_atual) / delta
    
    return dP_dr, dP_dh



# 3. ALGORITMO DO MÉTODO DO GRADIENTE

def otimizar_tanque(r_init: float, h_init: float, alpha: float, mu: float, 
                    max_iter: int = 100000, tol: float = 1e-6, delta: float = 1e-5):
    """
    Executa a minimização pelo Método do Gradiente Descendente.
    
    Parâmetros:
        r_init, h_init: Chutes iniciais para r e h
        alpha: Taxa de aprendizado (passo)
        mu: Coeficiente de penalidade
        max_iter: Número máximo de iterações
        tol: Tolerância para critério de parada (norma do gradiente)
        delta: Passo do cálculo da derivada numérica
    """
    r, h = r_init, h_init
    historico = []
    
    for k in range(max_iter):
        # 1. Calcula o gradiente numérico no ponto atual
        grad_r, grad_h = gradiente_numerico(r, h, mu, delta)
        norma_grad = math.sqrt(grad_r**2 + grad_h**2)
        
        # Guarda o histórico da convergência
        custo = custo_real(r, h)
        vol = math.pi * (r ** 2) * h
        historico.append((k, r, h, custo, vol, norma_grad))
        
        # 2. Critério de parada por convergência
        if norma_grad < tol:
            print(f"--> Convergência atingida na iteração {k}!")
            break
            
        # 3. Atualização das variáveis pelo método do gradiente descendente
        r_novo = r - alpha * grad_r
        h_novo = h - alpha * grad_h
        
        # Garante que raio e altura não podem ser negativos
        r = max(1e-4, r_novo)
        h = max(1e-4, h_novo)
    else:
        print("--> Número máximo de iterações atingido sem convergência completa.")
        
    return r, h, historico



# 4. EXECUÇÃO PRINCIPAL E TESTES COMPARATIVOS

if __name__ == "__main__":
    print("=======================================================================")
    print("          OTIMIZAÇÃO DO PROJETO DE UM TANQUE CILÍNDRICO                ")
    print("=======================================================================\n")
    
    # Parâmetros Iniciais Padrão
    r0, h0 = 5.0, 10.0  # Chutes iniciais (metros)
    
    print("--- CASO BASE DE EXECUÇÃO ---")
    alpha_base = 1e-6
    mu_base = 1e4
    
    r_otimo, h_otimo, hist = otimizar_tanque(r0, h0, alpha=alpha_base, mu=mu_base)
    custo_otimo = custo_real(r_otimo, h_otimo)
    vol_otimo = math.pi * (r_otimo ** 2) * h_otimo
    
    print(f"\nResultados Obtidos (Alpha = {alpha_base}, Mu = {mu_base}):")
    print(f"  > Raio Ótimo (r*):   {r_otimo:.4f} m")
    print(f"  > Altura Ótima (h*): {h_otimo:.4f} m")
    print(f"  > Volume Final:      {vol_otimo:.2f} m³ (Mínimo exigido: 500 m³)")
    print(f"  > Custo Mínimo:      R$ {custo_otimo:,.2f}")
    print(f"  > Iterações:         {len(hist)}")
    
    print("\n" + "="*70)
    print("--- ESTUDO DE SENSIBILIDADE E VARIABILIDADE DOS PARÂMETROS (MU e ALPHA) ---")
    print("="*70)
    
    testes_mu = [1e2, 1e4, 1e6]
    testes_alpha = [1e-7, 1e-6, 5e-6]
    
    print(f"{'Alpha':<10} | {'Mu':<10} | {'r* (m)':<8} | {'h* (m)':<8} | {'Vol (m³)':<10} | {'Custo (R$)':<12} | {'Iterações':<10}")
    print("-" * 78)
    
    for a in testes_alpha:
        for m in testes_mu:
            r_f, h_f, h_list = otimizar_tanque(r0, h0, alpha=a, mu=m, max_iter=150000)
            c_f = custo_real(r_f, h_f)
            v_f = math.pi * (r_f ** 2) * h_f
            print(f"{a:<10.1e} | {m:<10.1e} | {r_f:<8.3f} | {h_f:<8.3f} | {v_f:<10.1f} | R$ {c_f:<9.2f} | {len(h_list):<10}")