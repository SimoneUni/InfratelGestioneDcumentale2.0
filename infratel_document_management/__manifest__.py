{
    'name': 'Infratel Document Manager',
    'license': 'AGPL-3',
    'author': 'Simone Tullino',
    'website': 'www.unitiva.it',
    'category': '',
    'version': '1.1.0',
    'depends': [
        'base',
        'infratel_document_list',
        'sale'
                
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/document_configuration_views.xml',
        'views/menu_views.xml',
        'views/generated_documents_views.xml',
        'views/document_all_views.xml',
        'views/document_lines_views.xml',
        'views/reports.xml',
        'views/template_esempio.xml'
    ],
    'application': True,
    'installable': True
 
}