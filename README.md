# 📦 Sistema de Pedidos - Prova Técnica

Este projeto é uma aplicação fullstack desenvolvida como prova técnica para vaga de Desenvolvedor Pleno.

---

## 🚀 Tecnologias Utilizadas

- **FastAPI** para backend assíncrono com validação via Pydantic
- **MongoDB** como banco de dados NoSQL
- **Jinja2** para renderização server-side
- **HTMX** para dinamismo sem recarregamento de página
- **Bulma CSS** para estilização responsiva
- **Docker + Docker Compose** para ambiente isolado e fácil deploy

---

## 🧱 Funcionalidades

- Cadastro de pedidos com múltiplos itens
- Listagem paginada de pedidos
- Filtros por nome do cliente e intervalo de datas
- Visualização de detalhes de pedidos
- Exclusão de pedidos com confirmação
- Interface responsiva com Bulma
- Estrutura modular respeitando princípios de Clean Architecture e SOLID

---

## 📂 Estrutura de Pastas

```
app/
├── datasources/        # Conexão com MongoDB
├── repositories/       # (Opcional) Regras de acesso a dados
├── routes/             # Rotas da aplicação
├── schemas/            # Validações e tipos com Pydantic
├── static/             # Arquivos estáticos (CSS, JS)
├── templates/          # Templates Jinja2 (HTML)
└── usecases/           # (Opcional) Regras de negócio
```

---

## 🐳 Como Rodar com Docker

```bash
# Subir aplicação com Docker Compose
docker-compose up --build
```

A aplicação estará disponível em: [http://localhost:8000](http://localhost:8000)

---

## 🧪 Testes

Testes unitários ainda não foram implementados, mas recomenda-se uso de `pytest`.

---

## 🧠 Decisões de Projeto

- Optou-se pelo MongoDB por ser leve, flexível e de fácil integração com FastAPI (via `motor`)
- A arquitetura foi separada em camadas (datasources, routes, templates, etc.)
- Toda comunicação assíncrona, respeitando boas práticas de performance

---

## ✍️ Autor

Desenvolvido por [Seu Nome Aqui]

---

## 📄 Licença

Este projeto é open-source e pode ser usado livremente para fins educacionais.

---


---

## 🚀 Como Rodar o Projeto em Qualquer Ambiente

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/orders_app.git
cd orders_app
```

### 2. Criar Ambiente Virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

### 3. Ativar Ambiente Virtual

- **Windows:**
  ```bash
  venv/Scripts/activate
  ```

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

### 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar Variáveis de Ambiente

Copie o arquivo `.env_example` e renomeie para `.env`:

```bash
cp .env_example .env  # No Linux/macOS
copy .env_example .env  # No Windows
```

Certifique-se de que o MongoDB esteja rodando localmente na porta 27017 (ou ajuste o valor de `MONGO_URL` no `.env`).

### 6. Iniciar a Aplicação

```bash
uvicorn main:app --reload
```

Abra no navegador: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Ou Subir com Docker (alternativa)

```bash
docker-compose up --build
```

---

## 🧪 Rodar Testes

```bash
pip install -r requirements-dev.txt
pytest
```

---

## 🧱 Arquitetura Utilizada

Este projeto segue os princípios da **Clean Architecture**, com separação clara entre as responsabilidades de cada camada:

### 🔹 Camadas

- `routes/` – Controladores responsáveis por lidar com requisições HTTP.
- `usecases/` – Casos de uso que encapsulam as regras de negócio (ex: criar pedido, listar com filtros, deletar).
- `repositories/` – Abstração e implementação do acesso ao banco de dados (MongoDB neste caso).
- `datasources/` – Configuração da fonte de dados (cliente MongoDB).

### 🧪 Benefícios

- Fácil manutenção e leitura
- Testes unitários podem ser feitos nos `usecases` sem depender do banco de dados
- Reduz acoplamento entre camadas e melhora a escalabilidade

### 📌 Exemplo de fluxo

> Rota POST `/orders` chama o `CreateOrderUseCase`, que utiliza o `MongoOrderRepository` para persistir os dados no MongoDB.
