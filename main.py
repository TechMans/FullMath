from utils.utils.Resolvedor_equacao import resolver_equação_simples
from utils.utils.incógnitas import separar_incógnitas_e_funções

import webview


class BackEnd:   #Esta classe conterá todas as funções as quais serão expostas para o Front End

    resolver_equação_simples = resolver_equação_simples

    separar_incógnitas_e_funções = separar_incógnitas_e_funções



def iniciar_aplicacao(titulo: str, url: str, largura: int = 800, altura: int = 600, resizable: bool = True):
    """
    Inicializa uma janela PyWebView com API Python exposta para o JavaScript.

    Args:
        titulo (str): Título da janela.
        url (str): URL ou caminho para o arquivo HTML a ser exibido.
        largura (int, optional): Largura da janela. Padrão é 800.
        altura (int, optional): Altura da janela. Padrão é 600.
        resizable (bool, optional): Define se a janela pode ser redimensionada. Padrão é True.
    """
    backend = BackEnd()  # Instância do backend
    janela = webview.create_window(
        titulo,
        url,
        width=largura,
        height=altura,
        resizable=resizable,
        js_api=backend  # Aqui estamos expondo a API para o JavaScript
    )
    webview.start()  # Inicia o loop da aplicação

iniciar_aplicacao("FullMath", "Front_End\Paginas\Pagina_Inicial\index.html")