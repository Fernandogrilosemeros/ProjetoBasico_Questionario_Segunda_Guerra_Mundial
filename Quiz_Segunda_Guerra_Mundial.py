print("Seja bem-vindo ao questionário sobre a Segunda Guerra Mundial.\n\nEste teste tem como tema central os antecedentes, o desenvolvimento militar e os desdobramentos geopolíticos e sociais do conflito global ocorrido entre 1939 e 1945.\n\nO principal propósito deste material é avaliar seu conhecimento histórico e aprimorar sua capacidade de interpretação de texto, por meio de questões elaboradas no mesmo formato e nível de exigência do ENEM, servindo como uma ferramenta direta de revisão e preparação para exames.")

score = 0

iniciar_questionario = input("\nDeseja iniciar o questionário? (sim/não): ").lower()
if iniciar_questionario != "sim":
    quit()

print("\nÓtimo! Vamos começar o questionário.\n\nLembre-se de ler atentamente cada pergunta e suas alternativas antes de responder. Boa sorte!")
print("\nQuestão 1: O Tratado de Versalhes, assinado em 1919, impôs duras sanções à Alemanha após a Primeira Guerra Mundial. O país perdeu territórios, teve seu exército reduzido e foi obrigado a pagar indenizações altíssimas aos vencedores. Nas décadas seguintes, esse cenário de humilhação e crise econômica profunda serviu como terreno fértil para mudanças políticas drásticas.\n\nO contexto histórico descrito no texto foi um dos fatores determinantes para:\n\nA) a consolidação de regimes democráticos em toda a Europa Central.\nB) o surgimento da Guerra Fria e a divisão da Alemanha em duas repúblicas.\nC) a ascensão do nazifascismo e a eclosão da Segunda Guerra Mundial.\nD) a criação imediata da Organização das Nações Unidas (ONU) para evitar conflitos.\nE) o fortalecimento da Liga das Nações como órgão apaziguador europeu.")
resposta1 = input("Resposta: ").upper()
if resposta1 == "B":
    print("Correto!")
    score = score + 1 
    print(f"Seu score atual é de {score}/5")
else:
    print("Incorreto. A resposta correta é B.") 
    print(f"Seu score atual é de {score}/5")

print("\nQuestão 2: Em agosto de 1939, a Alemanha nazista e a União Soviética assinaram o Pacto de Não Agressão (Pacto Molotov-Ribbentrop). Do ponto de vista estratégico de Adolf Hitler, o principal objetivo prático desse acordo era:\n\nA) Estabelecer o comunismo nos territórios ocupados da Europa Ocidental.\nB) Garantir uma paz definitiva e duradoura com as potências aliadas.\nC) Evitar uma guerra em duas frentes durante a invasão e anexação da Polônia.\nD) Dividir o controle e a exploração do Oceano Pacífico com Stalin.\nE) Promover a integração econômica e o livre comércio entre Berlim e Moscou.")
resposta2 = input("Resposta: ").upper()
if resposta2 == "C":
    print("Correto!")
    score = score + 1 
    print(f"Seu score atual é de {score}/5")
else:
    print("Incorreto. A resposta correta é C.") 
    print(f"Seu score atual é de {score}/5")

print("\nQuestão 3: A entrada dos Estados Unidos na Segunda Guerra Mundial, no final de 1941, alterou o equilíbrio de forças no conflito. O estopim para a declaração de guerra americana foi:\n\nA) A invasão da França pelas tropas nazistas e a queda de Paris.\nB) A descoberta da política de extermínio nos campos de concentração europeus.\nC) O afundamento sistemático de navios mercantes americanos por submarinos alemães no Atlântico.\nD) O ataque surpresa da aviação militar japonesa à base naval de Pearl Harbor, no Havaí.\nE) O apelo diplomático direto da União Soviética após a quebra do pacto germano-soviético.")
resposta3 = input("Resposta: ").upper()
if resposta3 == "D":
    print("Correto!")
    score = score + 1 
    print(f"Seu score atual é de {score}/5")
else:
    print("Incorreto. A resposta correta é D.") 
    print(f"Seu score atual é de {score}/5")

print("\nQuestão 4: A Batalha de Stalingrado (1942-1943) é amplamente considerada pelos historiadores como o principal ponto de virada da Segunda Guerra Mundial na Europa. Seu desdobramento militar mais importante foi:\n\nA) A derrota do Exército Alemão e o início da contraofensiva soviética ininterrupta em direção a Berlim.\nB) A queda do governo de Joseph Stalin e a fragmentação do território soviético.\nC) A assinatura de um armistício que dividiu o Leste Europeu entre Alemanha e URSS.\nD) O primeiro uso de armas nucleares táticas no teatro de operações europeu.\nE) A entrada formal do Japão no conflito terrestre asiático contra as forças russas.")
resposta4 = input("Resposta: ").upper()
if resposta4 == "A":
    print("Correto!")
    score = score + 1 
    print(f"Seu score atual é de {score}/5")
else:
    print("Incorreto. A resposta correta é A.") 
    print(f"Seu score atual é de {score}/5")

print("\nQuestão 5: O 'Dia D' (6 de junho de 1944) marcou o início da Operação Overlord, uma das maiores mobilizações militares conjuntas da história. O objetivo central dessa operação era:\n\nA) Invadir as ilhas principais do Japão através do Oceano Pacífico.\nB) Libertar a Península Itálica do regime fascista de Benito Mussolini.\nC) Destruir as fábricas de armas químicas no interior do território alemão.\nD) Desembarcar tropas aliadas nas praias da Normandia para iniciar a libertação da França do domínio nazista.\nE) Resgatar prisioneiros políticos em campos de concentração localizados na Polônia.")
resposta5 = input("Resposta: ").upper()
if resposta5 == "D":
    print("Correto!")
    score = score + 1 
    print(f"Seu score atual é de {score}/5")
else:
    print("Incorreto. A resposta correta é D.") 
    print(f"Seu score atual é de {score}/5")

print(f"\nParabéns! Chegamos ao final do questionário!\nSua taxa de aproveitamento foi de {score}/5, ou seja, {(score/5)*100:.2f}%")