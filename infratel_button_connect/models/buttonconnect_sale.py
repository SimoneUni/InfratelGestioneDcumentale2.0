from odoo import models, fields

class buttonconnectSale(models.Model):
    _inherit = 'sale.order'
    
    def buttonSale(self):
        return {
            'name': 'Genera Documento',
            'type': 'ir.actions.act_window',
            'res_model':'wizard.sale',
            'view_mode': 'form',
            'view_id': self.env.ref('infratel_button_connect.wizard_sale_form_view').id,
            'target': 'new'            
        }