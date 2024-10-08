```markdown
# Simple YouTube Downloader

Um aplicativo simples para baixar vídeos do YouTube, construído com Flet e yt-dlp.

## Funcionalidades

* Baixa vídeos do YouTube em formato MP4.
* Exibe o progresso do download em tempo real.
* Lista os downloads concluídos com os nomes dos arquivos.
* Permite clicar nos nomes dos arquivos na lista para abri-los.
* Interface de usuário simples e intuitiva.

## Pré-requisitos

* Python 3.7 ou superior
* Flet
* yt-dlp

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu_usuario/simple-youtube-downloader.git
```

2. Navegue até o diretório do projeto:

```bash
cd simple-youtube-downloader
```

3. Crie um ambiente virtual (recomendado):

```bash
python -m venv .venv
```

4. Ative o ambiente virtual:

* Windows:

```bash
.venv\Scripts\activate
```

* macOS/Linux:

```bash
source .venv/bin/activate
```


5. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Execução

```bash
flet run main.py
```


## Uso

1. Cole o link do vídeo do YouTube no campo de texto.
2. Clique no botão "Download" ou pressione Enter.
3. O progresso do download será exibido abaixo do botão.
4. Após a conclusão do download, o nome do arquivo será adicionado à lista.
5. Clique no nome do arquivo na lista para abri-lo.


## Observações

* O aplicativo baixa os vídeos para o diretório em que o script está sendo executado.
* Certifique-se de ter as permissões necessárias para escrever arquivos no diretório atual.
* O uso deste aplicativo é de sua responsabilidade. Respeite os termos de serviço do YouTube e os direitos autorais.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença

[MIT](LICENSE)


## Print da aplicação
![Print](print.png) "Print da aplicação"


```

**Lembre-se de:**

* Substituir `seu_usuario` pelo seu nome de usuário do GitHub.
* Criar um arquivo `requirements.txt` na raiz do seu projeto com as dependências:

```
flet
yt-dlp
```

* Incluir uma print da sua aplicação nomeada como `print.png` para o usuário ter uma noção de como é a aplicação.


Este README fornece informações claras sobre o projeto, como instalá-lo, executá-lo e usá-lo.  Ele também inclui informações importantes sobre licença, contribuições e avisos sobre o uso responsável da aplicação.
