# Sistema de Login e Cadastro com Kivy 🚀

Este é um projeto desenvolvido em Python utilizando o framework **Kivy**, focado na criação de uma interface de usuário (UI) moderna, limpa e responsiva para sistemas de autenticação (Login, Cadastro de Contas e Painel do Usuário).

O projeto demonstra a separação prática entre a lógica de programação (em Python) e o design visual (usando a linguagem Kivy `.kv`), além de persistência de dados local.

## 🎨 Características do Projeto
* **Design Dark Moderno:** Interface elegante com paleta de cores escuras e detalhes em roxo vibrante (estilo Material/Flat).
* **Componentes Customizados:** Caixas de texto (`TextInput`) e botões com cantos arredondados. Os inputs mudam de cor automaticamente ao receber o foco do clique.
* **Layout Responsivo:** Desenvolvido usando `BoxLayout` e `FloatLayout` estruturados, garantindo que a tela se ajuste perfeitamente se a janela for maximizada ou redimensionada.
* **Gerenciamento de Fluxo:** Transições fluidas de tela (deslizar para os lados/cima/baixo) controladas por um `ScreenManager`.
* **Banco de Dados Local:** Módulo independente (`database.py`) para gravação, leitura e validação de e-mails e senhas criptografadas/estruturadas em um arquivo local (`users.txt`).

## 🛠️ Tecnologias Utilizadas
* **Python** (Lógica do sistema e manipulação de arquivos)
* **Kivy Framework** (Interface gráfica e gerenciamento de janelas)

## 📁 Estrutura do Repositório
* `main.py`: Código principal que gerencia o ciclo de vida do app e as ações dos botões.
* `my.kv`: Arquivo de estilo contendo todo o design, cores, fontes e posições dos elementos visuais.
* `database.py`: Classe responsável por gerenciar o carregamento, cadastro e validação dos usuários.

## 🚀 Como Executar o Aplicativo

### 1. Clonar o repositório
Abra o seu terminal (PowerShell ou Bash) e clone o projeto para a sua máquina:
```bash
git clone https://
cd REPOSITORIO
```

### 2. Criar e Ativar o Ambiente Virtual
É altamente recomendado rodar o projeto dentro de um ambiente isolado:
```powershell
# Criar o ambiente virtual
python -m venv .venv

# Ativar no Windows (PowerShell)
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar o Kivy
Com o ambiente ativado, instale a biblioteca do Kivy:
```bash
pip install kivy
```

### 4. Rodar o projeto
Agora, basta iniciar o arquivo principal:
```bash
python main.py
```
### Imagem Main
<img width="1918" height="1022" alt="MyMain" src="https://github.com/user-attachments/assets/3f807446-0528-463b-9a8a-dfa72c0f3c63" />
