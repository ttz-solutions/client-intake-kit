# Casos de teste

Colar como primeira mensagem da conversa. O comportamento esperado está em cada caso — desvio é motivo de ajuste nas instruções.

## Caso 1 — bug vago, sem link

```
o checkout tá dando erro na hora de pagar com pix, cliente reclamou no whatsapp
```

**Esperado:** assistente pergunta primeiro pelo link/tela, depois ambiente. Se a pessoa insistir que não sabe, o card sai com `STATUS: INCOMPLETO` e "onde" como lacuna nomeada. NÃO pergunta stack nem passos técnicos.

## Caso 2 — bug completo de primeira

```
Desde ontem os participantes não conseguem baixar o certificado no portal. Entra em https://app.evnttz.com.br/produtor/eventos/expotech-2026/certificados e fica carregando pra sempre. Esperava que baixasse o PDF. Acontece com todo mundo do evento. Tenho print do loading infinito.
```

**Esperado:** pergunta no máximo ambiente (confirmação) — tudo o resto já veio. Card sai com Evento: expotech-2026, Contexto com o link, Impacto "todo mundo", Evidências com o print descrito, Ambiente: Produção.

## Caso 3 — ajuste

```
queria que o relatório de vendas desse pra exportar em XML também, hoje só tem CSV. é pro contador do cliente, ele pede todo mês
```

**Esperado:** roteiro de ajuste — pergunta limites ("o que não pode mudar?") e um cenário concreto se não vier. Card sai nas seções de PRD (Visão Geral, Motivação, Escopo e Limites, Fluxos e Cenários, Perguntas em Aberto). NÃO afirma produto nem diz que o CSV já existe — quem disse foi o relator.

## Caso 4 — armadilha: assistente querer classificar

```
bug no ctrle
```

**Esperado:** NÃO escrever "Produto: Gamificação" no card. No máximo "Produto/módulo nas palavras do relator: ctrle" no bloco da triagem. Perguntar onde/o que viu/o que esperava.

## Caso 5 — inglês

```
the login keeps logging participants out every few minutes on the event app
```

**Esperado:** conversa em inglês, card em português. Sintoma de sessão → "onde" explícito é obrigatório.

## Caso 6 — impaciência

```
só gera o card logo: credenciamento offline não funciona no evento de hoje
```

**Esperado:** pergunta o "onde" UMA vez de outro jeito ("em qual app/tela o check-in falhou?"); se a pessoa insistir, gera com `STATUS: INCOMPLETO`, "link não informado" e lacuna nomeada. Não trava.
