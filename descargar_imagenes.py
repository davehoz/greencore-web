"""
GreenCore Nutrition — Descargador de imágenes
Ejecuta este script UNA VEZ para descargar todas las imágenes al disco.
Requiere Python 3 y conexión a internet.

Cómo ejecutarlo:
  1. Abre Terminal (o símbolo del sistema)
  2. Navega a la carpeta greencore-web:
       cd "~/Library/Mobile Documents/com~apple~CloudDocs/Daniel Vélez/EMBA EDEM/TFM/greencore-web"
  3. Ejecuta:
       python3 descargar_imagenes.py
"""

import urllib.request
import os
import sys

# Carpeta donde se guardarán las imágenes
IMG_DIR = os.path.join(os.path.dirname(__file__), "assets", "img")
os.makedirs(IMG_DIR, exist_ok=True)

IMAGENES = [
    # (nombre_local, url, descripción)
    ("hero-planta.jpg",        "https://images.unsplash.com/photo-1581093458791-9f58c68f6c31?w=900&q=80",  "Planta procesado agroalimentario (hero)"),
    ("hero-fondo.jpg",         "https://images.unsplash.com/photo-1625246333195-78d9c38ad449?w=1600&q=70", "Campo cereal fondo hero"),
    ("protinova-harina.jpg",   "https://images.unsplash.com/photo-1509358271058-acd22cc93458?w=800&q=80",  "Harina/polvo proteico ProtiNova"),
    ("petfood-perro.jpg",      "https://images.unsplash.com/photo-1450778869180-c3a35beb73b2?w=700&q=80",  "Perro/petfood premium"),
    ("acuicultura-peces.jpg",  "https://images.unsplash.com/photo-1534043464-7e2f0e29c1d4?w=700&q=80",    "Peces/acuicultura salmón"),
    ("inversores.jpg",         "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=700&q=80",    "Reunión inversores"),
    ("laboratorio-fcr.jpg",    "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=700&q=80",  "Laboratorio análisis FCR"),
    ("csrd-datos.jpg",         "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=700&q=80",  "Datos ESG/CSRD"),
    ("mercado-grafica.jpg",    "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=700&q=80",  "Gráfica mercado proteína insecto"),
    ("sostenibilidad.jpg",     "https://images.unsplash.com/photo-1464938050520-f8b6f7b9b3d3?w=900&q=80",  "Naturaleza/sostenibilidad"),
    ("application-lab.jpg",    "https://images.unsplash.com/photo-1576086135395-3b93e6fc53e5?w=800&q=80",  "Application Lab laboratorio"),
    ("equipo.jpg",             "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&q=80",  "Equipo trabajo colaborativo"),
    ("teruel-campo.jpg",       "https://images.unsplash.com/photo-1500651424-b8729e7e977a?w=800&q=80",    "Campo cereal Teruel/Aragón"),
    ("esg-analisis.jpg",       "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=700&q=80",    "Dashboard análisis ESG"),
    ("director.jpg",           "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=500&q=80",    "Retrato Director General"),
    ("directora-tecnica.jpg",  "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500&q=80",  "Retrato Directora Técnica"),
    ("kam.jpg",                "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=500&q=80",  "Retrato KAM"),
]

print(f"\n📁 Carpeta de destino: {IMG_DIR}\n")
errores = []

for nombre, url, desc in IMAGENES:
    ruta = os.path.join(IMG_DIR, nombre)
    if os.path.exists(ruta):
        print(f"  ✓ Ya existe: {nombre}")
        continue
    try:
        print(f"  ⬇ Descargando {nombre} ({desc})...", end=" ", flush=True)
        urllib.request.urlretrieve(url, ruta)
        size_kb = os.path.getsize(ruta) // 1024
        print(f"{size_kb} KB ✓")
    except Exception as e:
        print(f"✗ ERROR: {e}")
        errores.append(nombre)

print(f"\n{'='*50}")
if errores:
    print(f"⚠ {len(errores)} imagen(es) fallaron: {', '.join(errores)}")
    print("  Verifica tu conexión a internet e inténtalo de nuevo.")
else:
    descargadas = len([f for f in os.listdir(IMG_DIR) if f.endswith('.jpg')])
    print(f"✅ ¡Listo! {descargadas} imágenes descargadas en assets/img/")
    print("\nPróximo paso: abre index.html en tu navegador.")
