from odoo import models, fields


class AllDocuments(models.Model):
    _name = 'document.all'
    _description = 'Documents All'
    
    name = fields.Char(string="Nome del documento")