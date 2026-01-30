# 🎮 Jogo das Palavras - Flask

![Jogo das Palavras](https://img.shields.io/badge/Jogo%20das%20Palavras-Flask-blue?style=flat-square)

Um jogo divertido de palavras feito em **Python com Flask**, onde vários jogadores podem se desafiar a criar palavras que comecem com uma letra específica.  
O projeto inclui uma interface web estilizada, funcionalidade multiplayer e gerenciamento de turnos. ✨

---

## 💡 Funcionalidades

- 🧑‍🤝‍🧑 Cadastro de múltiplos jogadores.
- 🔄 Turnos alternados entre jogadores.
- ✅ Validação de palavras:  
  - Deve começar com a letra da rodada.  
  - Não pode repetir palavras já inseridas na rodada.
- ❌ Opção de desistir, mantendo os demais jogadores no jogo.
- 📜 Ao final de cada rodada, exibe a lista de palavras digitadas.
- 🔤 Opção de nova letra ou encerrar o jogo, mantendo a lista de jogadores.
- 🎨 Interface bonita e responsiva com CSS moderno.

---

## 🛠 Tecnologias

- 🐍 Python 3  
- ⚡ Flask  
- 🌐 HTML5 & CSS3 (gradiente animado e design responsivo)  

---

## 🚀 Como rodar

1. Clone o repositório:  
```bash
git clone https://github.com/seu-usuario/jogo-das-palavras-flask.git
cd jogo-das-palavras-flask
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):  
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale o Flask:  
```bash
pip install Flask
```

4. Execute o aplicativo:  
```bash
python app.py
```

5. Abra seu navegador e acesse:  
```
http://127.0.0.1:5000/
```

---

## 🎨 Layout

- 🏠 **Página inicial:** cadastro dos jogadores e escolha da letra da rodada.  
- 🎯 **Página do jogo:** mostra a letra da rodada, vez do jogador atual, campo para digitar a palavra, lista de palavras adicionadas, e botões de **nova letra** e **parar o jogo**.  
- 🏁 **Página final:** mostra a lista completa das palavras digitadas durante o jogo.

---

## 📁 Estrutura do projeto

```text
jogo-das-palavras-flask/
│
├── app.py            # Arquivo principal do Flask
├── templates/
│   ├── index.html    # Página inicial
│   ├── jogo.html     # Página do jogo
│   └── fim.html      # Página final
├── static/
│   ├── style.css     # Estilo CSS moderno
│   └── img/          # Favicon e ícones opcionais
└── README.md         # Este arquivo
```

---

## 👥 Contribuição

Contribuições são bem-vindas!  
Se você quiser adicionar recursos, melhorar o design ou corrigir bugs, fique à vontade para abrir um Pull Request. 🤝

---

## 📝 Licença

Este projeto é **livre para uso e aprendizado**.  
Use, estude, adapte, e se divirta! 🎉

---

## ⚡ Nota

Este projeto foi desenvolvido como **um exercício pessoal de Flask e Python**, com apoio de ferramentas de IA para acelerar o desenvolvimento.  

---

## 💖 Obrigado por conferir este projeto!

Divirta-se jogando, aprendendo e compartilhando com os amigos.
