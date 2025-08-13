import sys
import os

# Añadimos la carpeta raíz del proyecto al sys.path para que Python encuentre backend/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.scraping import save_raw_data, scrape_reuters_with_selenium

def main():
    articles = scrape_reuters_with_selenium()
    if articles:
        save_raw_data("santander_reuters_news.json", articles)
        print(f"{len(articles)} datos guardados en santander_reuters_news.json")
    else:
        print("No se encontraron noticias")

if __name__ == "__main__":
    main()