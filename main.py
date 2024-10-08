import flet as ft
import yt_dlp
import os
import webbrowser
import http.server
import socketserver
import socket
import threading

def main(page: ft.Page):
    page.title = "Simple Youtube Downloader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLUE_100

    link_download = ft.TextField(
        label="Cole o link aqui",
        label_style=ft.TextStyle(color=ft.colors.BLACK),
        text_style=ft.TextStyle(color=ft.colors.BLACK),
        border_color=ft.colors.BLACK,
    )

    downloads_concluidos = []
    lista_downloads = ft.Column([], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    progresso_download = ft.Text("", size=16, color=ft.colors.GREEN)
    diretorio_download = ""  # Variável para armazenar o diretório

    # Diálogo para escolher o diretório (sem dialog_title)
    dlg_escolher_diretorio = ft.FilePicker()

    def abrir_seletor_diretorio(e):
        nonlocal diretorio_download  # Acessa a variável externa
        dlg_escolher_diretorio.get_directory_path()
        page.update()

    def download_video(e):
        if not link_download.value:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, insira um link."), open=True)
            page.update()
            return

        if not diretorio_download:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, selecione um diretório de download."), open=True
            )
            page.update()
            return

        ydl_opts = {
            "progress_hooks": [atualizar_progresso],
            "outtmpl": os.path.join(diretorio_download, "%(title)s.%(ext)s"),
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([link_download.value])
                info_dict = ydl.extract_info(link_download.value, download=False)
                nome_arquivo = ydl.prepare_filename(info_dict)
                caminho_completo = os.path.join(diretorio_download, nome_arquivo)
                downloads_concluidos.append({"nome": nome_arquivo, "caminho": caminho_completo})
                atualizar_lista_downloads()
                page.snack_bar = ft.SnackBar(ft.Text("Download concluído!"), open=True)
                progresso_download.value = ""
                link_download.value = ""
                page.update()
            except Exception as ex:
                print(f"Erro no download: {ex}")
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro no Download: {ex}"), open=True)
                page.update()

    def encontrar_porta_livre():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("", 0))
            return s.getsockname()[1]

    def serve_file():
        Handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", encontrar_porta_livre()), Handler) as httpd:
            print(f"Servidor HTTP iniciado na porta {httpd.server_address[1]}")
            httpd.serve_forever()

    threading.Thread(target=serve_file, daemon=True).start()

    def atualizar_progresso(d):
        if d["status"] == "downloading":
            percentual = d["_percent_str"]
            progresso_download.value = f"Baixando: {percentual}"
            page.update()

    def atualizar_lista_downloads():
        lista_downloads.controls = []
        for download in downloads_concluidos:
            texto_download = ft.Text(download["nome"], color=ft.colors.BLACK, size=12)
            texto_download.on_click = lambda e, download=download: abrir_arquivo(
                download["caminho"]
            )
            lista_downloads.controls.append(texto_download)
        page.update()

    def abrir_arquivo(caminho):
        try:
            webbrowser.open(caminho)
        except Exception as e:
            print(f"Erro ao abrir o arquivo: {e}")
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao abrir o arquivo."), open=True)
            page.update()
    
    def diretorio_selecionado(e: ft.FilePickerResultEvent):
        nonlocal diretorio_download
        diretorio_download = e.path if e.path else ""
        page.update()

    dlg_escolher_diretorio.on_result = diretorio_selecionado

    retangulo = ft.Container(
        height=800,
        bgcolor=ft.colors.BLUE_100,
        alignment=ft.alignment.center,
        padding=20,
    )

    retangulo.content = ft.Column(
        [
            ft.Text("Simple YouTube Downloader", size=20, color=ft.colors.BLACK),
            link_download,
            ft.ElevatedButton(
                text="Escolher Diretório", on_click=abrir_seletor_diretorio
            ),
            ft.ElevatedButton(text="Download", on_click=download_video),
            progresso_download,
            lista_downloads,
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.overlay.append(dlg_escolher_diretorio)
    page.add(retangulo)


ft.app(main)
