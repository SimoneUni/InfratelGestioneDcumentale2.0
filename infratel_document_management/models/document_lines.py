from odoo import fields, models

class DocumentLines(models.Model):
    _name= 'document.lines'
    _description = 'Document Lines'
    
    phases_id = fields.Many2one('document.phases', string="Fasi")
    approvers_id = fields.Many2one('res.groups', string="Approvatori")
    
    phase_approvers = fields.Many2one('document.configuration', string='Rif.') 