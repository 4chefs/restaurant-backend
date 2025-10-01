# 📌 Endpoints - Usuário

Base URL: `/user`

---

## Autenticação

| Rota | Método | Descrição | Autenticação |
|------|--------|-----------|--------------|
| `/login` | `POST` | Efetua login e retorna token JWT | ❌ Pública |

**Request Body**

```json
{
  "email": "usuario@exemplo.com",
  "senha": "123456"
}
```

**Response (200)**

```json
{
  "data": {
    "token": "<jwt_token>",
    "user": { ...dados_do_usuario }
  },
  "message": "Login efetuado com sucesso"
}
```

---

## Gestão de Usuários

| Rota | Método | Descrição | Autenticação |
|------|--------|-----------|--------------|
| `/create` | `POST` | Cria um novo usuário | ❌ Pública |
| `/update/{id}` | `PUT` | Atualiza um usuário existente | ✅ JWT |
| `/delete/{id}` | `DELETE` | Remove um usuário | ✅ JWT |

---

### Criar Usuário

`POST /user/create`

**Request Body (exemplo)**

```json
{
  "nome": "João Silva",
  "email": "joao@exemplo.com",
  "senha": "123456",
  "role": "aluno"
}
```

**Response (200)**

```json
{
  "data": { ...usuario_criado },
  "message": "Usuário criado com sucesso"
}
```

---

### Atualizar Usuário

`PUT /user/update/{id}`

**Headers**

```json
Authorization: Bearer <jwt_token>
```

**Request Body (exemplo)**

```json
{
  "nome": "João Silva Atualizado"
}
```

**Response (200)**

```json
{
  "data": { ...usuario_atualizado },
  "message": "Usuário 3 atualizado com sucesso"
}
```

---

### Deletar Usuário

`DELETE /user/delete/{id}`

**Headers**
```
Authorization: Bearer <jwt_token>
```

**Response (200)**

```json
{
  "data": { ...usuario_removido },
  "message": "Usuário 3 apagado com sucesso"
}
```

---

## Consultas

| Rota | Método | Descrição | Retorno |
|------|--------|-----------|---------|
| `/id/{id}` | `GET` | Retorna usuário por ID | Objeto |
| `/name/{name}` | `GET` | Lista usuários com nome | Lista |
| `/role/{role}` | `GET` | Lista usuários por tipo (role) | Lista |

---

### Buscar por ID

`GET /user/id/3`

**Response**

```json
{
  "data": { ...usuario },
  "message": "Usuário encontrado"
}
```

---

### Buscar por Nome

`GET /user/name/João`

**Response**

```json
{
  "data": [
    { ...usuario1 },
    { ...usuario2 }
  ],
  "message": "2 Usuários com nome João encontrados"
}
```

---

### Buscar por Role

`GET /user/role/admin`

**Response**

```json
{
  "data": [
    { ...usuario1 },
    { ...usuario2 }
  ],
  "message": "2 Usuários com role admin encontrados"
}
```
