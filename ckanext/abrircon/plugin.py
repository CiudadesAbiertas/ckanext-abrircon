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


import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation


class AbrirconPlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'abrircon')

    ## ITemplateHelpers
    def get_helpers(self):
        from ckanext.abrircon import helpers as abrircon_helpers
        return {
            'is_cartodb_format': abrircon_helpers.is_cartodb_format,
            'is_plotly_format': abrircon_helpers.is_plotly_format,
            'is_geojson_io_format': abrircon_helpers.is_geojson_io_format,
            'abrircon_plotly_url': abrircon_helpers.abrircon_plotly_url,
            'abrircon_carto_url': abrircon_helpers.abrircon_carto_url,
            'abrircon_geojson_io_url': abrircon_helpers.abrircon_geojson_io_url,
}
