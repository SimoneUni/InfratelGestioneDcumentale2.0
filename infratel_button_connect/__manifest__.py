{
    'name': 'Infratel Button Connect',
    'license': 'AGPL-3',
    'author': 'Simone Tullino, Unitiva',
    'website': 'www.unitiva.it',
    'category': '',
    'version': '1.1.0',
    'depends': [
        'base',
        'sale',
        'purchase',
        'infratel_document_management',
        'infratel_document_list',
        'infratel_sale_ext',
        'sale',
        
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/buttonconnect_sale_views.xml',
        'views/buttonconnect_purchase_views.xml',
        'views/wizard_sale_views.xml',
        'views/wizard_purchase_views.xml',
        'data/sequence_data.xml'
    ],
    'application': False,
    'installable': True
 
}