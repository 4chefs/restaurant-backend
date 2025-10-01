# Restaurant Backend #

## Introduction ##

Este projeto tem como objetivo o desenvolvimento do backend para um sistema de restaurante, oferecendo funcionalidades de gerenciamento de usuários, cardápio, agendamentos e mais.

## Funcionalidades ##

1. CRUD de Usuários
2. CRUD de Cardápio
3. CRUD de Agendamentos
4. Controle de Estoque e Registro de Ações (Log)
5. Pagamentos e Sistema de Bonificação
6. Personalização do Perfil do Usuário

## Rotas / Endpoints ##

Veja uma descrição melhor em [Endpoints](ENDPOINTS.md)

### Usuário ###

- Criar usuário: /user/create
- Atualizar usuário: /user/update/(id)
- Deletar usuário: /user/delete/(id)
- Efetuar login: /user/login
- Usuários por ID: /user/id/(id)
- Usuários por Nome: /user/name/(name)
- Usuários por Tipo: /user/role/(role)
