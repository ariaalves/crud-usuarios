# crud-usuarios

API simples em **Flask** para cadastro e gerenciamento de usuários.  

## Grupo
-**Ariany Alves**
-**Erik Paulino**
-**Heitor dos Santos**

## Operações disponíveis  
- **Cadastrar usuário**  
- **Consultar todos os usuários**  
- **Consultar usuário por ID**  
- **Deletar usuário por ID**  

---

## Endpoints  

| Método | Rota             | Descrição                       |
|--------|------------------|---------------------------------|
| POST   | `/users`         | Cadastrar usuário               |
| GET    | `/users`         | Consultar todos os usuários     |
| GET    | `/users/<id>`    | Consultar usuário por ID        |
| DELETE | `/users/<id>`    | Deletar usuário por ID          |

## Instalação e configuração  

### 1. Criar e ativar ambiente virtual  

**Windows (PowerShell):**  
```powershell
python -m venv venv
.\venv\Scripts\activate
````

**Linux/MacOS (bash):**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Flask e dependências

```bash
pip install flask
pip install -r requirements.txt
```

### 3. Iniciar a API
**Windows (PowerShell):**  
```bash
python run.py
```
**Linux/MacOS (bash):**

```bash
python3 run.py
```

---