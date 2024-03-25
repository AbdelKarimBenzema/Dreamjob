Para arrancar la API con Apache: docker compose -f docker-composePython.yml up --build

Para arrancar la API sin Apache: docker compose -f docker-compose.yml up --build

  Ejecuta: cd web
  
  Ejecuta: virtualenv env
  
  Ejecuta: source env/bin/activate en linux o env\Scripts\activate.bat en Windows
  
  Ejecuta: pip install -r requirements.txt   (instala los paquetes necesarios)
  
  Ejecuta: python app.py
  
  Probar la aplicación con: localhost:8080/static/index.html
  
  También hay que revisar los archivos app.py descomentar cargarvariables
  
