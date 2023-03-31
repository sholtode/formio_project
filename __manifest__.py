# Copyright Nova Code (http://www.novacode.nl)
# See LICENSE file for full licensing details.

{
    'name': 'Forms | Project',
    'summary': 'Forms integration with Project Tasks',
    'version': '0.1',
    'license': 'LGPL-3',
    'author': 'Sholto Douglas',
    'website': 'https://ms-systems.eu',
    'category': 'Project',
    'depends': ['project', 'formio_data_api'],
    'data': [
        'data/formio_project_data.xml',
        'views/formio_form_views.xml',
        'views/res_project_views.xml',
    ],
    'application': True,
    'images': [
        'static/description/banner.gif',
    ],
    'description': """
Forms | Project
================

"""
}
