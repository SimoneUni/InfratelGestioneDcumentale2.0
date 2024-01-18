{
    'name': 'Infratel List Document',
    'license': 'AGPL-3',
    'author': 'Simone Tullino',
    'website': 'www.unitiva.it',
    'category': '',
    'version': '1.1.0',
    'depends': [
        'base',
        'infratel_sale_ext',
        'container_file',
        
        
        
        
        
    ],
    # 'external_dependencies': {"python": ["pypandoc"]},
    'data': [
        'security/ir.model.access.csv',
        'views/document_list_views.xml',
        'views/menu_views.xml',
        # 'data/sequence_data.xml'
        
    ],
    'application': True,
    'installable': True
 
}