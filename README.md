# ckanext-abrircon

Esta extensión permite abrir los recursos de determinado tipo con Plotly, Carto y Geojson.io.
Con Plotly se habilitará el enlace "Abrir con" con los siguientes tipos de ficheros:

- CSV
- TSV
- XLS
- XLSX
	
Con Carto se habilitará el enlace "Abrir con" con los siguientes tipos de ficheros:

- CSV
- XLS
- XLSX
- KML
- KMZ
- GeoJSON
- SHP

Con Geojson.io se habilitará el enlace "Abrir con" con los siguientes tipos de ficheros:

- GeoJSON

## Requisitos


Para usar el "Abrir con" con Carto se deberá estar registrado previamente.

## Instalación

Para instalar ckanext-abrircon:

1. Activa tu medio virtual CKAN, por ejemplo::

     . /usr/lib/ckan/default/bin/activate

2. Vaya a la carpeta de instalación del plugin::

     cd /usr/lib/ckan/default/src

3. Clone este repositorio::

     git clone https://bitbucket.org/ciudadesabiertas/ckanext-abrircon.git

4. Entre en la carpetarecien clonada::

     cd ckanext-abrircon

5. Instale la extensión ckanext-abrircon::

     python setup.py develop

6. Añada ``abrircon`` en ``ckan.plugins`` de la configuración de CKAN (por defecto alojado en  ``/etc/ckan/default/production.ini``). Si usa un plugin que haga cambios visuales sobre el core de CKAN y dicho plugin sobreescribe el bloque 'resource_item_explore' del fichero resource_item.html, habrá que añadir ``abrircon`` delante de dicho plugin.

7. En configuración habrá que rellenar los siguientes parámetros::

	abrircon.plotly = ('csv', 'xls', 'xlsx', 'text/csv', 'text/tab-separated-values', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' )
	abrircon.carto = ('csv', 'xls', 'xlsx', 'kml', 'geojson', 'shp' ,'kmz', 'text/csv','application/vnd.ms-excel','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.google-earth.kml+xml','application/geo+json', 'application/octet-stream', 'application/vnd.google-earth.kmz')
	abrircon.geojson.io = ('geojson', 'application/geo+json')
	abrircon.plotly_url = https://plot.ly/external/?url=
	abrircon.carto_url = http://oneclick.cartodb.com/?file=
	abrircon.geojson_io_url = http://geojson.io/#data=data:text/x-url,
	
8. Explicación de los parámetros de configuración::

	abrircon.plotly = Conjuntos de tipos de archivos y tipo de MIME entrecomillados, que se van a usar en Plotly
	abrircon.carto = Conjuntos de tipos de archivos y tipo de MIME entrecomillados que se van a usar en Carto 
	abrircon.geojson.io = Conjuntos de tipos de archivos y tipo de MIME entrecomillados que se van a usar en geojson.io
	abrircon.plotly_url = URL que se usará para abrir el recurso en Plotly
	abrircon.carto_url = URL que se usará para abrir el recurso en Carto 
	abrircon.geojson_io_url = URL que se usará para abrir el recurso en geojson.io

7. Renicie CKAN. Por ejemplo con Apache y NGINX en Ubuntu::

     sudo service apache2 reload
     sudo service nginx reload

## Autores

A continuación se indica el listado de autores de la extensión "Abrir con" para CKAN, desarrollada dentro del proyecto Ciudades Abiertas.

Ayuntamiento de A Coruña
Ayuntamiento de Madrid
Ayuntamiento de Santiago de Compostela
Ayuntamiento de Zaragoza
Entidad Pública Empresarial Red.es

## Licencia

La extensión "Abrir con" para CKAN forma parte de las actuaciones que se llevan a cabo dentro del proyecto "Plataforma de Gobierno Abierto, Colaborativa e Interoperable",
presentado por los ayuntamientos de A Coruña, Madrid, Santiago de Compostela y Zaragoza, que fue seleccionado como beneficiario de la
"II Convocatoria de Ciudades Inteligentes" del Ministerio de Economía y Empresa lanzado a través de la Entidad Pública Empresarial Red.es
adscrita a la Secretaría de Estado de Avance Digital de dicho Ministerio.

Los derechos de autor de esta aplicación pertenecen a © 2018 Ayuntamiento de A Coruña, Ayuntamiento de Madrid, Ayuntamiento de Santiago de Compostela, Ayuntamiento de Zaragoza, Entidad Pública Empresarial Red.es
Licencia cedida con arreglo a la EUPL.
Por favor, tenga en cuenta asimismo las demás menciones de derechos de autor presentes en todos los componentes usados.
