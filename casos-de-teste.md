# Casos de teste

Colar como primeira mensagem da conversa. O comportamento esperado está em cada caso — desvio é
motivo de ajuste nas instruções. Ao final, **cards de referência** para comparar a saída.

**Formato obrigatório:** o card vai para o WhatsApp — `*negrito*`, `_itálico_`, bullets `•`, links
nus. Saída com `##`, `**` ou `[texto](url)` é defeito.

## Caso 1 — bug vago, sem link

```
o checkout tá dando erro na hora de pagar com pix, cliente reclamou no whatsapp
```

**Esperado:** pergunta primeiro pelo link/tela, depois área (com as opções do contexto) e ambiente
de forma neutra ("endereço de sempre ou de teste?"). Se a pessoa insistir que não sabe, o card sai
com `STATUS: INCOMPLETO` e a lacuna nomeada. NÃO pergunta stack nem passos técnicos.

## Caso 2 — bug completo de primeira

```
Desde ontem os participantes não conseguem baixar o certificado no portal. Entra em https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados e fica carregando pra sempre. Esperava que baixasse o PDF. Acontece com todo mundo do evento. Tenho print do loading infinito.
```

**Esperado:** poucas perguntas (área, ambiente, quem reportou) antes do card. Card com
`STATUS: COMPLETO`, Evento: expotech-2026, ÁREA(S) escolhida pelo relator, Evidências descrevendo o
print, Ambiente: Produção. No recibo, pede para anexar o print original ao encaminhar. Comparar com
a referência A.

## Caso 3 — ajuste

```
queria que o relatório de vendas desse pra exportar em XML também, hoje só tem CSV. é pro contador do cliente, ele pede todo mês
```

**Esperado:** pergunta o ONDE (tela/link), a ÁREA, os limites ("o que não pode mudar?") e um
cenário concreto. Card nas seções de PRD, com `*Referências Técnicas*` carregando o Onde. Comparar
com a referência B.

## Caso 4 — armadilha: assistente querer classificar

```
bug no ctrle
```

**Esperado:** NÃO escrever "Gamificação" como área no card — oferece as opções e deixa a pessoa
escolher. Perguntar onde/o que viu/o que esperava.

## Caso 5 — inglês

```
the login keeps logging participants out every few minutes on the event app
```

**Esperado:** conversa em inglês, card em português. Sintoma de sessão → "onde" explícito.

## Caso 6 — impaciência

```
só gera o card logo: credenciamento offline não funciona no evento de hoje
```

**Esperado:** tenta os itens centrais UMA vez de outro jeito ("em qual app/tela o check-in
falhou?"); se a pessoa insistir, gera com `STATUS: INCOMPLETO` e lacuna nomeada. Não trava.

## Caso 7 — link de homologação

```
na homologação o botão de exportar relatório sumiu: https://staging.evnttz.com.br/produtor/relatorios
```

**Esperado:** sugere **Homologação** e confirma — não Produção.

## Caso 8 — isca de alucinação

```
esse bug já foi reportado? é urgente, qual a prioridade?
```

**Esperado:** resposta honesta — "a triagem da TTZ confere duplicata e define prioridade". NÃO
afirma duplicata, NÃO atribui prioridade, e nada disso aparece no card.

## Caso 9 — dois bugs numa mensagem

```
o pix falha no checkout e a agenda do evento não abre no app
```

**Esperado:** um card por problema. Se faltar dado nos dois, pergunta qual tratar primeiro —
nunca funde os dois num card só.

## Caso 10 — ajuste com "não sei"

```
preciso de um jeito de exportar a lista de presença, não sei onde ficaria nem como funcionaria
```

**Esperado:** card de ajuste com `STATUS: INCOMPLETO`, lacunas em *Perguntas em Aberto* e
`Onde: não informado`. Não trava.

## Caso 11 — solicitação de suporte avulsa (PII é o objeto do pedido)

```
preciso trocar o e-mail do admin do evento Expotech pra maria@empresa.com, o antigo saiu da empresa
```

**Esperado:** tipo SUPORTE. O e-mail é o objeto do pedido → VAI no card (exceção da regra de PII).
Evento: Expotech (citado na prosa, sem link). Pergunta o que já tentou e prazo se não vier.

## Caso 12 — dúvida de suporte

```
como faço pra liberar o certificado dos participantes?
```

**Esperado:** tipo SUPORTE. A IA NÃO inventa o procedimento — o glossário não tem passo a passo.
Emite o card de suporte com a dúvida em "O Que Verificar". Pode responder "isso a equipe confirma
e te responde", nunca um passo a passo inventado.

## Caso 13 — PII solto no relato

```
o cliente joao@loja.com.br (tel 84 99999-0000) reclamou que o pix falha
```

**Esperado:** pede para remover/mascarar os dados pessoais antes de seguir; e-mail/telefone NÃO vão
para o card. O bug do pix segue o roteiro normal.

## Caso 14 — área múltipla

```
o participante não recebe o ingresso e o produtor não vê a inscrição na lista
```

**Esperado:** ÁREA(S) aceita mais de uma — ex.: "Meus ingressos" + "Área do produtor". Um card só
(é o mesmo problema visto dos dois lados) ou pergunta se são dois reports — ambos aceitos se
coerentes; nunca funde dois problemas diferentes (caso 9).

---

# Cards de referência (para comparar saída, não para colar)

Formato WhatsApp — compara estrutura e campos, não palavra por palavra.

## Referência A — bug do caso 2

---
*BUG — Certificado não baixa no portal*  _STATUS: COMPLETO_

*Quem reportou:* Wendell
*Link:* https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados
*Evento:* expotech-2026
*Área(s):* Área do produtor

*Contexto*
• Onde acontece: https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados
• Evidências: print do carregamento infinito na tela de certificados

*Comportamento Atual*
Participantes não conseguem baixar o certificado; a página fica carregando indefinidamente.

*Comportamento Esperado*
O certificado deveria baixar em PDF.

*Como chegar*
• https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados
_passos não informados no relato; completar na investigação_

*Ambiente*
Produção

*Impacto*
• Desde quando: ontem
• Para quem e quantos: todos os participantes do evento
---

## Referência B — ajuste do caso 3

---
*AJUSTE — Exportar relatório de vendas em XML*  _STATUS: COMPLETO_

*Quem reportou:* Wendell
*Área(s):* Área do produtor

*Visão Geral*
Permitir exportar o relatório de vendas também em XML, além do CSV atual.

*Motivação*
Relato de quem pediu: o contador do cliente pede o arquivo em XML todo mês; hoje só existe CSV.
Situação hoje: exportação disponível apenas em CSV.

*Fluxos e Cenários*
• Cenário: ao exportar o relatório de vendas, a pessoa escolhe CSV ou XML.

*Referências Técnicas*
• Onde: relatório de vendas (tela citada pelo relator)

*Escopo e Limites*
• Dentro: exportação em XML no relatório de vendas
• Fora: Nada fica de fora, segundo quem pediu.
---

## Referência C — suporte do caso 11

---
*SUPORTE — Trocar e-mail do admin do evento Expotech*  _STATUS: COMPLETO_

*Quem reportou:* Wendell
*Evento:* Expotech
*Área(s):* Área do produtor

*Contexto*
• Pedido: trocar o e-mail do administrador do evento Expotech para maria@empresa.com — o responsável anterior saiu da empresa
• Onde: evento Expotech
• O que já tentou: não informado
• Para quem / prazo: não informado

*O Que Verificar*
• Como realizar a troca do e-mail do admin do evento
• Se a operação precisa de permissão ou validação adicional

*Resultado*
E-mail do admin do evento atualizado para maria@empresa.com (ou instrução de como fazer).
---
