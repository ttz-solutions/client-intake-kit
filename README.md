# Client intake kit — Skill do Gemini + Project do ChatGPT

Alternativa interim enquanto o conector de intake (conecttz) não está pronto: o cliente fala com a
IA em linguagem livre, do jeito que quiser, e recebe de volta um **card pronto em markdown**. Quem
cadastra no board é um humano da TTZ — a IA não registra, não classifica e não decide prioridade.

## Arquivos

| arquivo | uso |
|---|---|
| `evnttz-intake/SKILL.md` | skill do Gemini: frontmatter (`name` slug + `description`) + instruções |
| `evnttz-intake/references/contexto-evnttz.md` | vocabulário real do produto, carregado sob demanda |
| `evnttz-intake.zip` | pacote pronto pra upload no Gemini (SKILL.md + references) |
| `chatgpt-project/instrucoes.md` | campo Instructions do Project — **gerado**, não editar |
| `scripts/build.py` | gera `instrucoes.md` e o zip a partir do `SKILL.md` (fonte única) |
| `casos-de-teste.md` | 10 prompts de teste + 2 cards de referência para comparar a saída |

## Baixar sem saber git

Dois links diretos, um clique cada:

- **Gemini:** [baixar evnttz-intake.zip](https://github.com/ttz-solutions/client-intake-kit/releases/latest/download/evnttz-intake.zip) — é só isso que precisa.
- **ChatGPT:** [baixar contexto-evnttz.md](https://github.com/ttz-solutions/client-intake-kit/releases/latest/download/contexto-evnttz.md) — e as instruções se copiam do GitHub: abra `chatgpt-project/instrucoes.md` aqui no site e copie o texto.

## Setup — Gemini (skill)

Skills pedem conta Google **pessoal** (18+, Keep Activity on) — em rollout, pode não aparecer em
conta de trabalho ainda. Dois caminhos:

**Upload (recomendado — leva o contexto junto):**

1. `gemini.google.com` → sidebar → **Settings → Skills** → **Upload**.
2. Envie `evnttz-intake.zip` (ou a pasta `evnttz-intake/`).
3. Revise e clique **Create**.

**Manual (3 campos, sem contexto anexo):**

1. **Create manually**.
2. Nome: `evnttz-intake` (slug, minúsculas com hífen).
3. Descrição: `Reportar bug ou pedir ajuste no EVNTTZ — entrevista breve e emite card pronto em markdown.`
4. Instruções: cole o corpo do `SKILL.md` (tudo abaixo do frontmatter `---`). A seção CONTEXTO
   ANEXO é condicional ("se houver arquivo"), então funciona sem o anexo — mas a skill fica sem o
   vocabulário.

Para usar: em qualquer chat, digite `/` e escolha a skill — ou deixe o Gemini ativar sozinho pela
descrição.

## Setup — ChatGPT (Project)

1. **New Project** → nome: `EVNTTZ · Reports`.
2. **Instructions**: cole `chatgpt-project/instrucoes.md` inteiro.
3. **Files**: anexe `evnttz-intake/references/contexto-evnttz.md`.
4. Toda conversa de report deve começar dentro do projeto.

## Como usar (quem reporta)

1. Abra o chat com a skill (`/` → `evnttz-intake`) ou dentro do Project.
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
3. Se o card cita evidência (print, anexo), **confira se o arquivo original veio junto** — a imagem
   fica no chat da IA e não viaja com o texto. Peça ao relator se faltar.
4. Lê o bloco **Para a triagem**: busca duplicata pelas palavras-chave sugeridas, define produto,
   severidade e sprint.
5. Cola o corpo no card (Boardz/ClickUp). As seções são as mesmas que o `support_file` do conecttz
   produz — quando o conector estiver pronto, a migração é trocar "colar no board" por "colar na
   conversa do Claude App".

## Manutenção

`evnttz-intake/SKILL.md` é a fonte única. `chatgpt-project/instrucoes.md` e `evnttz-intake.zip`
são gerados — depois de editar o SKILL.md ou o `references/`:

```bash
python3 scripts/build.py
git add -A
```

No Gemini, arquivo de skill não edita no lugar: **More → Replace skill** com o zip novo.

## Limites conhecidos (por desenho)

- **Sem dedup real** — a IA não vê o board; a checagem de duplicata é sugestão de palavras-chave
  para o humano.
- **Sem classificação** — produto/módulo nunca é afirmado pela IA; fica nas palavras do relator e
  na decisão da triagem.
- **Regra em texto fura** — instrução de prompt não é portão. Por isso a IA é propositalmente
  proibida de decidir: tudo que exigiria acesso a dados reais fica com o humano.
- **Evidência não viaja** — print/anexo fica no chat da IA; o card carrega só a descrição. O humano
  confere o anexo original na triagem.
- **Deriva** — a fonte é o `SKILL.md` + `scripts/build.py`. No Gemini, edição de arquivos exige
  re-upload do pacote.
