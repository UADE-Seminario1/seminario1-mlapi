Requiere Python 3.8 y Poetry para empezar.
<br>
<br>
Para instalar nuevos paquetes, ejecutar:
<br>
<code>
poetry add <i>NOMBRE-DEL-PAQUETE</i>
</code>

Para generar el archivo de requerimientos con las dependencias:
<br>
<code>
poetry export -f requirements.txt --output requirements.txt
</code>
<br>
Nota: Heroku requiere este archivo. Ejecutar luego de instalar nuevos paquetes.
<br>
<br>
Para ejecución local:
<br>
<code>
pip install -r requirements.txt 
</code>
<br>
Nota: solo si hay nuevas dependencias. Si hay que desinstalar paquetes se debe realizar a mano, 
<br>
<code>
pip uninstall <i>NOMBRE-DEL-PAQUETE</i>
</code>
<br>
<code>
heroku local web
</code>
<br>
<br>
Enviar cambios a heroku:
<br>
<code>
git push heroku main:main
</code>
<br>
<br>
Para ejecución local con Poetry:
<br>
<code>
poetry run python -m seminario1_api.app
</code>
<br>
<br>
Para ver los logs:
<br>
<code>
heroku logs --tail
</code>