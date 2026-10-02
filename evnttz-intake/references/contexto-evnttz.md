# Vocabulário do EVNTTZ — contexto para o assistente de intake

Use este arquivo para ENTENDER o relato e fazer perguntas melhores. Não copie termos daqui para o card se quem relatou não os usou — o card registra as palavras da pessoa.

## O que é o EVNTTZ

Plataforma de eventos da TTZ. Quem usa: produtores de evento, participantes, parceiros (patrocinadores e expositores) e a operação interna (admin).

## Personas

- **Produtor**: dono/organizador do evento. Usa a área do produtor no portal.
- **Participante**: quem se inscreve e participa do evento (portal, app, credenciamento).
- **Parceiro**: patrocinador ou expositor. Área do parceiro e gamificação.
- **Admin**: operação interna / backoffice.

## Áreas (o que cada endereço é)

| endereço começa com | área |
|---|---|
| `checkout.` ou `eventos.` | checkout de inscrição e páginas públicas de evento |
| `app.` ou `portal.` | portal do produtor e do participante |
| `api.` | backend (a pessoa quase nunca cita; aparece em erro técnico) |
| `codes.` | área de códigos |
| `ctrle.` ou `gamificacao.` | gamificação do evento |

Outros endereços citados em chamados: `credenciamento`, `gorn`.

## URL com nome do evento

Links como `/produtor/eventos/<nome-do-evento>/` ou `/evento/<nome-do-evento>/` trazem o nome do evento na URL — extraia para o campo Evento do card.

## Áreas do produto (oferecer como opções na pergunta — nunca afirmar)

- **Área do produtor** — portal onde o organizador gerencia o evento (`/produtor/...`)
- **Área gamificada do evento** — jornadas, quests, lojinha, prêmios do participante
- **Área do parceiro** — patrocinador/expositor
- **Meus ingressos / área do participante** — inscrições e ingressos de quem participa
- **Checkout de inscrição** — compra/inscrição (`checkout.`, `eventos.`)
- **Credenciamento** — check-in no dia do evento
- **Site do evento** — página pública/landing
- **Mini Checkout** — checkout simplificado

## Módulos (o nome que as pessoas usam)

Credenciamento (check-in), Checkout, Quests, Quizzes, Missões, Jornadas, Prêmios, Lojinha, Pedidos, Ingressos, Participantes, Relatórios, Usuários, Networking, Matchmaking, Feed social, Agenda inteligente, Construtor de navegação, Produtos digitais, Gestão de eventos, Gestão da gamificação, Gestão da lojinha, Clientes de produtos digitais.

## Ambiente

- **Produção**: os endereços normais do produto.
- **Homologação**: endereços com `staging.` ou `homolog` no link — nesse caso não pergunte, é fato derivado do link.

## Como o link vira ambiente e área

O link vem do relator — o que ele deriva é quase-fato. Ambiente casa → não pergunte. Área casa →
ofereça como opção marcada e confirme ("pelo link, parece a Área do Produtor — é isso?").

| padrão no link | ambiente | área sugerida |
|---|---|---|
| host tem `staging.` ou `homolog` | Homologação (não pergunta) | — |
| host começa `checkout.` ou `eventos.`, ou caminho `/sales/` | — | Checkout de inscrição |
| caminho tem `/produtor/` | — | Área do produtor |
| host começa `app.` ou `portal.` (outros caminhos) | — | Meus ingressos / área do participante |
| host começa `ctrle.` ou `gamificacao.`, ou caminho `/-gamification/` ou `/jornadas/` | — | Área gamificada do evento |
| subdomínio de evento (`<nome-do-evento>.evnttz.com.br`) com `/jornadas/` ou gamificação | — | Área gamificada do evento |
| caminho tem `/parceiro` | — | Área do parceiro |
| host começa `codes.` | — | Credenciamento |
| host começa `api.` | — | (técnico — pergunte em aberto) |
| site público sem nenhum padrão | — | Site do evento |

Sem casar padrão nenhum → pergunta em aberto com a lista de áreas.

## Sintomas que atravessam áreas

Login, sessão caindo, senha, cadastro, token — aparecem em qualquer área. Quando vier um desses, o "onde aconteceu" é a pergunta que destrava o relato.

## Produtos

- **EVNTTZ** — plataforma de eventos.
- **Mini Checkout** — checkout simplificado.
