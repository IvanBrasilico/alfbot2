'''Place your configs here. No need to code if dicttlak supports
your needs. DRY principle. Just cloning bdicttalk and puting
rules here can make a new application'''
import json
import os
import botteryext.bdicttalk.localizations

URL_APP = 'http://localhost:5000'
URL = 'http://localhost:5000'

if os.path.exists('rules.json'):
    with open('rules.json', 'r') as json_config:
        RULES = json.load(json_config)
else:
    RULES = {}
    RULES['pattern_list'] = ['lacre', 'tec']
    RULES['rules'] = \
        {'tec': {'rank': {'type': 'json_api',
                          'method': 'GET',
                          'resource': URL + '/_rank',
                          'params': [{'name': 'words', 'required': True}]
                          },
                 'filtra': {'type': 'json_api',
                            'method': 'GET',
                            'resource': URL + '/_filter_documents',
                            'params': [{'name': 'afilter', 'required': True}]
                            },
                 'capitulo': {'type': 'json_api',
                              'method': 'GET',
                              'resource': URL + '/_document_content',
                              'params': None},
                 '_message': 'Informe o comando: '
                 },
         'lacre': {'ll': {'type': 'json_api',
                          'method': 'GET',
                          'resource': URL + '/_lacre/lacre',
                          'params': [{'name': 'pk', 'required': True}]
                          },
                   'cc': {'type': 'json_api',
                          'method': 'GET',
                          'resource': URL + '/_lacre/container',
                          'params': [{'name': 'pk', 'required': True}]
                          },
                   'log': {'type': 'json_api',
                           'method': 'GET',
                           'resource': URL + '/_lacre/list/log',
                           'params': None
                           },
                   '_message': 'Escolha uma das opções: '
                   }
         }
