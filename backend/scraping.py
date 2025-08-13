import os
import json

# Directorio para guardar datos raw
RAW_DATA_DIR = "data/raw"

def save_raw_data(filename: str, data):
    """Guarda los datos crudos en un archivo JSON."""
    if not os.path.exists(RAW_DATA_DIR):
        os.makedirs(RAW_DATA_DIR)
    file_path = os.path.join(RAW_DATA_DIR, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"[INFO] Datos guardados en {file_path}")

import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_reuters_with_selenium():
    url = "https://www.reuters.com/companies/SAN.MC/news"

    options = uc.ChromeOptions()
    # Puedes agregar opciones para headless si quieres
    # options.add_argument("--headless")

    driver = uc.Chrome(options=options, version_main=125)
    print(f"[INFO] Abriendo navegador en {url}")
    driver.get(url)

    articles = []

    try:
        # Esperar a que carguen los artículos
        WebDriverWait(driver, 15).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "li.story-collection__list-item__j4SQe")
            )
        )
        time.sleep(2)  # Pequeña espera para carga JS adicional

        # Obtener HTML de la página principal
        main_html = driver.page_source
        main_soup = BeautifulSoup(main_html, 'html.parser')

        # Seleccionar las estadísticas
        statistics = main_soup.select_one(".company-profile-maximizer__statistics-wrapper__3CEhz")

        # 1. Extraer textos sueltos (ej. "1.96 mean rating - 24 analysts")
        rating_info = statistics.select_one(".company-profile-maximizer__info__StXBc")
        if rating_info:
            print("Rating info:", rating_info.get_text(strip=True))

        # 2. Extraer todas las estadísticas de pares <dt> / <dd>
        stats_data = {}
        rows = statistics.select(".company-profile-maximizer__row__3SOn6")
        for row in rows:
            key = row.select_one("dt").get_text(strip=True)
            value = row.select_one("dd").get_text(strip=True)
            stats_data[key] = value

        print(stats_data)
        # Seleccionar todos los artículos
        article_items = main_soup.select("li.story-collection__list-item__j4SQe")

        print(f"[INFO] Encontrados {len(article_items)} artículos en la página principal")

        for idx, item in enumerate(article_items):
            # Extraer datos visibles en la página principal
            title_tag = item.select_one("h3[data-testid='Heading'] a")
            date_tag = item.select_one("time[data-testid='Body']")
            category_tag = item.select_one("span[data-testid='Label'] a span")

            title = title_tag.get_text(strip=True) if title_tag else "Sin título"
            link = title_tag['href'] if title_tag else ""
            if link.startswith("/"):
                link = f"https://www.reuters.com{link}"
            date = date_tag['datetime'] if date_tag and date_tag.has_attr('datetime') else ""
            category = category_tag.get_text(strip=True) if category_tag else ""

            print(f"[{idx+1}] {title} ({date}) - Categoría: {category}")
            print(f"Enlace: {link}")

            # Visitar la página del artículo para extraer más info
            driver.get(link)

            # Esperar que cargue contenido específico del artículo (puede variar según la web)
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "div.article-body__content__17Yit")
                )
            )

            article_html = driver.page_source
            article_soup = BeautifulSoup(article_html, 'html.parser')

            # Extraer el texto completo del artículo o detalles que quieras
            content_div = article_soup.select_one("div.article-body__content__17Yit")
            content = content_div.get_text(separator="\n", strip=True) if content_div else "Sin contenido adicional"
            if (content != "Sin contenido adicional"):
                content_split = content.split('\n')
            else:
                ["Sin contenido adicional"]

            # Guardar toda la info en el diccionario
            articles.append({
                "titulo": title,
                "categoria": category,
                "fecha": date,
                "link": link,
                "contenido_completo": content_split
            })

            # Volver a la página principal para continuar el scraping
            driver.back()
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "li.story-collection__list-item__j4SQe")
                )
            )
            time.sleep(1)  # Espera para estabilizar la carga

        print(f"[INFO] Total artículos extraídos con contenido completo: {len(articles)}")
        return articles

    finally:
        driver.quit()


if __name__ == "__main__":
    resultados = scrape_reuters_with_selenium()
    for r in resultados:
        print(f"Título: {r['titulo']}\nFecha: {r['fecha']}\nCategoría: {r['categoria']}\nLink: {r['link']}\nContenido:\n{r['contenido_completo'][:300]}...\n{'-'*50}")
