# ICEbot-dgt

ICEbot-dgt (Incidentes en Carreteras españolas) es un script hecho en python que recopila toda la información relacionada con accidentes e incidentes de tráfico en las carreteras españolas
a partir de la página web de la [DGT](http://infocar.dgt.es/etraffic/Incidencias?ca=&provIci=&caracter=acontecimiento&accion_consultar=Consultar&IncidenciasRETENCION=IncidenciasRETENCION&IncidenciasPUERTOS=IncidenciasPUERTOS&IncidenciasMETEOROLOGICA=IncidenciasMETEOROLOGICA&IncidenciasEVENTOS=IncidenciasEVENTOS&IncidenciasOTROS=IncidenciasOTROS&IncidenciasRESTRICCIONES=IncidenciasRESTRICCIONES&ordenacion=fechahora_ini-DESC) (Dirección General de Tráfico)


## Dependencias
Necesitarás: 
- [selenium library](https://pypi.org/project/selenium/): automatiza la interacción del navegador web desde Python.
```
pip3 install selenium
```

- [chromedriver](http://chromedriver.chromium.org): herramienta de código libre para pruebas automatizadas de aplicaciones web en muchos navegadores.



## Ejecución
ICEbot-dgt tiene dos funcionalidades principales relacionadas con la búsqueda de incidencias: 
-  Búsquedas de incidencias en toda España. 
- Búsqueda de incidencias en una carretera en concreto. 

A la hora de ejecutar el programa será necesario asignar una ruta al driver si no se ha asigando directamente en el código. 
A continuación se describe: 

##### Command Line 
```
$ python3 ICEbot-dgt.py -h
usage: ICEbot-dgt.py [-h] [-p PATH_CHROMEDRIVER] [-c]
optional arguments:
    -h, --help show this help message and exit
    -p PATH_CHROMEDRIVER, --path-chromedriver PATH_CHROMEDRIVER Path where chromedriver is stored 
    -c, --carretera Indica la carretera a buscar incidencias, por defecto se buscan en todas las carreteras
```

## Salida
Se muestra por consola un _array_ con la siguiente información: 
```
[hora de inicio, fecha de inicio, hora de finalziación*, fecha de finalización, provincia, población, carretera, descripción, localización]
```

> **Nota***: Estos campos no se muestran siempre.

##### Ejemplo: 
```python
['16:19', '15/02/2019', 'VALENCIA/VALÈNCIA', 'LUZ (BARRIO DE LA)', 'A-3', 'OBSTÁCULO FIJO en:', '- La carretera A-3 en el km 351.8 en LUZ (BARRIO DE LA) (VALENCIA/VALÈNCIA) hacia madrid, en gasolinera repsol, saliendo de avenida del cid']
```

