Requiere Python 3.8 y Poetry para empezar.

Para instalar nuevos paquetes, ejecutar:
poetry add <NOMBRE-DEL-PAQUETE>

Para generar el archivo de requerimientos con las dependencias:
poetry export -f requirements.txt --output requirements.txt
Nota: Heroku requiere este archivo. Ejecutar luego de instalar nuevos paquetes.

Para ejecución local:
pip install -r requirements.txt 
Nota: solo si hay nuevas dependencias. Si hay que desinstalar paquetes se debe realizar a mano, pip uninstall <NOMBRE-DEL-PAQUETE>.
heroku local web

Enviar cambios a heroku:
git push heroku main:main

Para ejecución local con Poetry:
poetry run python -m seminario1_api.app

Para ver los logs:
heroku logs --tail
