# Client intake kit — Gem do Gemini + Project do ChatGPT

Alternativa interim enquanto o conector de intake (conecttz) não está pronto: o cliente fala com a
IA em linguagem livre, do jeito que quiser, e recebe de volta um **card pronto em markdown**. Quem
cadastra no board é um humano da TTZ — a IA não registra, não classifica e não decide prioridade.

## Arquivos

| arquivo | uso |
|---|---|
| `instrucoes.md` | campo de instruções (mesmo texto nos dois) — ~6.200 chars, dentro do limite de 8.000 do ChatGPT |
| `contexto-evnttz.md` | anexar como knowledge do Gem / file do Project — vocabulário real do produto |
| `casos-de-teste.md` | 6 prompts de teste com comportamento esperado, para validar depois de montar |

## Setup — Gemini (Gem)

1. Abra o Gemini → **Gems** → **New Gem**.
2. Nome: `EVNTTZ — Reportar bug/ajuste`.
3. **Instructions**: cole o bloco de `instrucoes.md` (só o conteúdo dentro do cercado de código).
4. **Knowledge**: anexe `contexto-evnttz.md`.
5. Salve e compartilhe o link com quem reporta.

## Setup — ChatGPT (Project)

1. **New Project** → nome: `EVNTTZ · Reports`.
2. **Instructions**: cole o bloco de `instrucoes.md`.
3. **Files**: anexe `contexto-evnttz.md`.
4. Toda conversa de report deve começar dentro do projeto.

## Como usar (quem reporta)

1. Abra o Gem ou o Project.
2. Descreva o problema ou o pedido do seu jeito, em qualquer idioma — pode ser uma frase solta
   ("o checkout trava no pix") ou um relato completo com link e print.
3. A IA faz até 3 perguntas curtas por vez, só sobre o que você sabe: onde aconteceu, o que você
   viu, o que esperava, desde quando, quem é afetado. Nunca pergunta nada técnico.
   - "Não sei" vale em qualquer pergunta.
4. Quando tiver o suficiente — ou se você pedir para gerar logo — ela emite o **card em markdown**.
5. Copie o texto do card e mande para o contato da TTZ (ou cole direto onde for combinado).

Pronto. Você não precisa saber nome de produto, módulo, ambiente técnico nem formato — a IA
organiza e a triagem da TTZ classifica.

## O que o humano que cadastra faz (TTZ)

1. Recebe o markdown do relator.
2. Confere o `STATUS`: `INCOMPLETO` significa que algum item ficou "não informado" — decida se
   cadastra assim ou devolve ao relator.
3. Lê o bloco **Para a triagem**: busca duplicata pelas palavras-chave sugeridas, define produto,
   severidade e sprint.
4. Cola o corpo no card (Boardz/ClickUp). As seções são as mesmas que o `support_file` do conecttz
   produz — quando o conector estiver pronto, a migração é trocar "colar no board" por "colar na
   conversa do Claude App".

## Limites conhecidos (por desenho)

- **Sem dedup real** — a IA não vê o board; a checagem de duplicata é sugestão de palavras-chave
  para o humano.
- **Sem classificação** — produto/módulo nunca é afirmado pela IA; fica nas palavras do relator e
  na decisão da triagem.
- **Regra em texto fura** — instrução de prompt não é portão. Por isso a IA é propositalmente
  proibida de decidir: tudo que exigiria acesso a dados reais fica com o humano.
- **Deriva** — se as instruções mudarem, mudar nos dois lugares (Gem + Project). A fonte é este
  repositório.
