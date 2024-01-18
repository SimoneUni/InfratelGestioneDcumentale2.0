from odoo import models, fields, api

class GenertedDocuments(models.Model):
    _name = 'generated.documents'
    _description = 'Generated Documents'
    

    
    name = fields.Char(string="Tipo documenti")
    all_documents_ids = fields.One2many('document.all', 'document_category', string="Categoria documento")
    documents_count = fields.Integer("Counter", compute="_compute_all_documents_count", store=True)
    #_______________Ho aggiunto questo_____________________________
    # configuration_id = fields.Many2one('document.configuration', string="Configurazione")
    
    
    @api.depends("all_documents_ids")
    def _compute_all_documents_count(self):
        for r in self:
            r.documents_count = len(r.all_documents_ids)

    def action_view_partner_all_documents(self):
        for r in self:
            return {
                "name": "Documenti associati",
                "type": "ir.actions.act_window",
                "view_mode": "tree,form",
                # "views": [(False, 'tree'), (False, 'form')],
                'res_model': 'document.all',
                'domain': [('document_category', '=', r.id)],
                'context': {'default_document_category': r.id},
            }