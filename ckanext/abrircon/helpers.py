# -*- coding: utf-8 -*-
# Copyright 2018 Ayuntamiento de A Coruña, Ayuntamiento de Madrid, Ayuntamiento de Santiago de Compostela, Ayuntamiento de Zaragoza, Entidad Pública Empresarial Red.es
#
# This file is part of the CKAN "Abrir con" extension, developed within the "Ciudades Abiertas" project.
# 
# Licensed under the EUPL, Version 1.2 or – as soon they will be approved by the European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at:
# 
# https://joinup.ec.europa.eu/software/page/eupl
# 
# Unless required by applicable law or agreed to in writing, software distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and limitations under the Licence.


import re
import logging
log = logging.getLogger(__name__)

def is_plotly_format(resource):
    log.debug('is_plotly_format')
    if(resource and (abrircon_plotly()!=None or abrircon_plotly()!="")):
        format = resource.get('format', 'data').lower()
        mimetype = resource.get('mimetype')
        if(format is not None):
            format="'"+format+"'"
        if(mimetype is not None):
            mimetype="'"+mimetype+"'"
        if mimetype:
            mimetype = mimetype.lower()
        if str(format) in abrircon_plotly() or str(mimetype) in abrircon_plotly():
            log.debug('return True')
            return True
        else:
            log.debug('return False')
            return False
    return False

def is_cartodb_format(resource):
    log.debug('is_cartodb_format')
    if(resource and (abrircon_carto()!=None or abrircon_carto()!="")):
        format = resource.get('format', 'data').lower()
        mimetype = resource.get('mimetype')
        if(format is not None):
            format="'"+format+"'"
        if(mimetype is not None):
            mimetype="'"+mimetype+"'"
        if mimetype:
            mimetype = mimetype.lower()
        if str(format) in abrircon_carto() or str(mimetype) in abrircon_carto():
            log.debug('return True')
            return True
        else:
            log.debug('return False')
            return False
    return False

def is_geojson_io_format(resource):
    log.debug('is_geojson_io_format')
    if(resource and (abrircon_geojson_io()!=None or abrircon_geojson_io()!="")):
        format = resource.get('format', 'data').lower()
        mimetype = resource.get('mimetype')
        if(format is not None):
            format="'"+format+"'"
        if(mimetype is not None):
            mimetype="'"+mimetype+"'"
        if mimetype:
            mimetype = mimetype.lower()
        if str(format) in abrircon_geojson_io() or str(mimetype) in abrircon_geojson_io():
            log.debug('return True')
            return True
        else:
            log.debug('return False')
            return False
    return False

def abrircon_plotly():	
    import pylons.config as config 
    return config['abrircon.plotly']

def abrircon_carto():	
    import pylons.config as config 
    return config['abrircon.carto']

def abrircon_geojson_io():	
    import pylons.config as config 
    return config['abrircon.geojson.io']

def abrircon_plotly_url():	
    import pylons.config as config 
    return config['abrircon.plotly_url']

def abrircon_carto_url():	
    import pylons.config as config 
    return config['abrircon.carto_url']

def abrircon_geojson_io_url():	
    import pylons.config as config 
    return config['abrircon.geojson_io_url']

