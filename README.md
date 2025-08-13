# Dashboard - Presentación para Banco Santander

Aplicación interactiva en Streamlit para mostrar mi perfil profesional, habilidades y propuesta para Banco Santander.

## Instalación y ejecución en Linux
```bash
# Clonar repositorio
git clone https://github.com/usuario/santander_dashboard.git
cd santander_dashboard

# Crear entorno
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
streamlit run app.py

## Organización recomendada de carpetas y archivos
```

mydashboard/
│
├── app.py                      # Punto de entrada con menú
├── requirements.txt            # Dependencias
├── .env
├── .gitignore
├── README.md
│
├── data/                       # Archivos dinamicos Datos obtenidos por scraping (por ejemplo, análisis de  noticias, indicadores financieros, feeds de LinkedIn o Twitter).Resultados de modelos que entrenes (predicciones, clasificaciones, etc).Datos almacenados y consultados en la base de datos (formulario de contacto).
│   ├── static                      # Archivos estáticos (texto de presentacion, archivos markdown)
│   ├── processed
│   └── raw
│
├── assets/                       # Archivos estáticos (imagenes)
│
├── sections/                   # Código modular por sección
│   ├── portada.py
│   ├── habilidades.py
│   ├── experiencia.py
│   ├── santander.py
│   └── contacto.py
│
├── backend/                    # Código de backend: scraping, base de datos, modelado
│   ├── database.py
│   ├── scraping.py
│   ├── modelo.py
│   └── utils.py
|
├── scripts/                    # Código de backend: scraping, base de datos, modelado
│   ├── bootstrap.py
│   ├── listar_contacts.py
│
└── certs/                      # Certificados SSL para la base de datos (Aiven)

