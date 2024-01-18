from odoo import models, fields

class DocumentPhases(models.Model):
    _name= 'document.phases'
    _description= 'Document Phases'
    
    name = fields.Char(string="Nome della fase", help="Tipo di fase")
    sequence = fields.Integer(string='Sequenza', help="Ordina le fasi.")
    is_active = fields.Boolean(string='Active', default=True, help="Flag per indicare se la fase è attiva.")
    #approver_id = fields.Many2one('res.groups', string='Approvatore della fase')