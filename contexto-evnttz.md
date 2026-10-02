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

## Módulos (o nome que as pessoas usam)

Credenciamento (check-in), Checkout, Quests, Quizzes, Missões, Jornadas, Prêmios, Lojinha, Pedidos, Ingressos, Participantes, Relatórios, Usuários, Networking, Matchmaking, Feed social, Agenda inteligente, Construtor de navegação, Produtos digitais, Gestão de eventos, Gestão da gamificação, Gestão da lojinha, Clientes de produtos digitais.

## Ambiente

- **Produção**: os endereços normais do produto.
- **Homologação**: endereços com `staging.` ou `homolog` no link.

## Sintomas que atravessam áreas

Login, sessão caindo, senha, cadastro, token — aparecem em qualquer área. Quando vier um desses, o "onde aconteceu" é a pergunta que destrava o relato.

## Produtos

- **EVNTTZ** — plataforma de eventos.
- **Mini Checkout** — checkout simplificado.
