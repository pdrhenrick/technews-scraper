import scrapy

class TabNewsSpider(scrapy.Spider):
    name = "tabnews"
    start_urls = ["https://www.tabnews.com.br/"]

    def parse(self, response):
        # Percorre cada <article> encontrado
        for noticia in response.css('article'):
            
            # --- ESTRATÉGIA NOVA (Genérica) ---
            
            # TÍTULO: Pega o texto do PRIMEIRO link (<a>) que aparece no conteúdo
            # O .strip() serve para limpar espaços em branco no começo ou fim
            titulo = noticia.css('div a::text').get()
            if titulo:
                titulo = titulo.strip()

            # LINK: Pega o endereço desse mesmo primeiro link
            link_relativo = noticia.css('div a::attr(href)').get()
            
            # AUTOR: O autor geralmente está num link dentro de um <span> no rodapé do card
            # A estratégia aqui é: procure um link dentro de um span
            autor = noticia.css('div span a::text').get()

            yield {
                'titulo': titulo,
                'autor': autor,
                'link': response.urljoin(link_relativo)
            }