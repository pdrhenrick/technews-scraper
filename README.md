# 🕷️ TechNews Scraper

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scrapy](https://img.shields.io/badge/Scrapy-Framework-60A839?style=for-the-badge&logo=scrapy&logoColor=white)
![Data](https://img.shields.io/badge/Data-Engineering-blue?style=for-the-badge)

Projeto de Engenharia de Dados focado em **Web Scraping**. O objetivo é extrair notícias de tecnologia do site [TabNews](https://www.tabnews.com.br/), estruturar os dados e exportá-los para análise.

Este projeto demonstra o uso de **Frameworks Profissionais de Crawling** e estratégias de extração de dados resilientes (XPath/CSS Selectors).

---

## 🚀 Funcionalidades

* **Coleta Automatizada:** Navega pelo site e identifica postagens.
* **Extração Precisa:** Captura Título, Autor e Link de cada notícia.
* **Limpeza de Dados:** Tratamento de strings (strip) para garantir dados limpos.
* **Exportação JSON:** Gera arquivos estruturados prontos para consumo por outras APIs ou Bancos de Dados (MongoDB).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.12:** Linguagem base.
* **Scrapy:** Framework de alto desempenho para crawling.
* **XPath & CSS Selectors:** Para navegação na árvore DOM do HTML.

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos
* Python 3.10 ou superior instalado.

### 1. Instalação

```bash
# Clone o repositório
git clone [https://github.com/pdrhenrick/technews-scraper.git](https://github.com/pdrhenrick/technews-scraper.git)

# Entre na pasta
cd technews-scraper

# Crie e ative o ambiente virtual (Windows)
python -m venv venv
.\venv\Scripts\activate

# Instale as dependências
pip install scrapy pymongo