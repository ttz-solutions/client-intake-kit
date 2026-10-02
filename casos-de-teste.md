# Casos de teste

Colar como primeira mensagem da conversa. O comportamento esperado está em cada caso — desvio é
motivo de ajuste nas instruções. Ao final, **cards de referência** para comparar a saída.

## Caso 1 — bug vago, sem link

```
o checkout tá dando erro na hora de pagar com pix, cliente reclamou no whatsapp
```

**Esperado:** pergunta primeiro pelo link/tela, depois ambiente de forma neutra ("endereço de
sempre ou de teste?"). Se a pessoa insistir que não sabe, o card sai com `STATUS: INCOMPLETO` e a
lacuna nomeada. NÃO pergunta stack nem passos técnicos.

## Caso 2 — bug completo de primeira

```
Desde ontem os participantes não conseguem baixar o certificado no portal. Entra em https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados e fica carregando pra sempre. Esperava que baixasse o PDF. Acontece com todo mundo do evento. Tenho print do loading infinito.
```

**Esperado:** card quase direto (confirma ambiente se faltar) com `STATUS: COMPLETO`, Evento:
expotech-2026, Evidências descrevendo o print, Ambiente: Produção. No recibo, pede para anexar o
print original ao encaminhar. Comparar com o card de referência A.

## Caso 3 — ajuste

```
queria que o relatório de vendas desse pra exportar em XML também, hoje só tem CSV. é pro contador do cliente, ele pede todo mês
```

**Esperado:** pergunta o ONDE (tela/link do relatório), limites ("o que não pode mudar?") e um
cenário concreto. Card nas seções de PRD, com `## Referências Técnicas` carregando o **Onde**.
Comparar com o card de referência B.

## Caso 4 — armadilha: assistente querer classificar

```
bug no ctrle
```

**Esperado:** NÃO escrever "Produto: Gamificação" no card. No máximo "Produto/módulo nas palavras
do relator: ctrle" no bloco da triagem. Perguntar onde/o que viu/o que esperava.

## Caso 5 — inglês

```
the login keeps logging participants out every few minutes on the event app
```

**Esperado:** conversa em inglês, card em português. Sintoma de sessão → "onde" explícito é
obrigatório antes de emitir.

## Caso 6 — impaciência

```
só gera o card logo: credenciamento offline não funciona no evento de hoje
```

**Esperado:** pergunta o "onde" UMA vez de outro jeito ("em qual app/tela o check-in falhou?"); se
a pessoa insistir, gera com `STATUS: INCOMPLETO`, "link não informado" e lacuna nomeada.

## Caso 7 — link de homologação

```
na homologação o botão de exportar relatório sumiu: https://staging.evnttz.com.br/produtor/relatorios
```

**Esperado:** sugere **Homologação** e confirma — não Produção. Card com o link e Ambiente
preenchido depois do ok.

## Caso 8 — isca de alucinação

```
esse bug já foi reportado? é urgente, qual a prioridade?
```

**Esperado:** resposta honesta — "a triagem da TTZ confere duplicata e define prioridade". NÃO
afirma duplicata, NÃO atribui prioridade. No card, severidade fica "a definir na triagem".

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

**Esperado:** card de ajuste com `STATUS: INCOMPLETO`, lacunas em **Perguntas em Aberto** e
`Referências Técnicas → Onde: não informado`. Não trava.

---

# Cards de referência (para comparar saída, não para colar)

## Referência A — bug do caso 2

---
TIPO: Bug
STATUS: COMPLETO
TÍTULO SUGERIDO: Certificado não baixa no portal
LINK: https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados
EVENTO: expotech-2026

## Contexto
**Onde acontece**: https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados
**Evento**: expotech-2026
**Evidências**: print do carregamento infinito na tela de certificados

## Comportamento Atual
Participantes não conseguem baixar o certificado; a página fica carregando indefinidamente.

## Comportamento Esperado
O certificado deveria baixar em PDF.

## Passos para Reproduzir
**Como chegar**
- https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados
_passos não informados no relato; completar na investigação_

## Ambiente
Produção

## Impacto
**Desde quando**: ontem
**Para quem e quantos**: todos os participantes do evento

**Para a triagem (não faz parte do card)**
- Checar duplicata buscando por: certificado, download, loading, portal, expotech
- Produto/módulo nas palavras do relator: portal, certificados
- Severidade e prioridade: a definir na triagem
---

## Referência B — ajuste do caso 3

---
TIPO: Ajuste
STATUS: COMPLETO
TÍTULO SUGERIDO: Exportar relatório de vendas em XML

## Visão Geral
Permitir exportar o relatório de vendas também em XML, além do CSV atual.

## Motivação
Relato de quem pediu: o contador do cliente pede o arquivo em XML todo mês; hoje só existe CSV.
Situação hoje: exportação disponível apenas em CSV.

## Fluxos e Cenários
**Cenários**
- Ao exportar o relatório de vendas, a pessoa escolhe CSV ou XML.

## Referências Técnicas
**Onde**: relatório de vendas (tela citada pelo relator)

## Escopo e Limites
**Dentro**
- Exportação em XML no relatório de vendas
**Fora**
- Nada fica de fora, segundo quem pediu.

**Para a triagem (não faz parte do card)**
- Checar duplicata buscando por: exportar, XML, relatório, vendas
- Produto/área nas palavras do relator: relatório de vendas
- Prioridade: a definir na triagem
---
