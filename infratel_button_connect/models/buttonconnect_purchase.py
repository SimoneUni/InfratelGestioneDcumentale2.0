from odoo import models, fields

class buttonconnectSale(models.Model):
    _inherit = 'purchase.order'
    
    
    
    def buttonPurchase(self):
        
        return {
            'name': 'Genera Documento',
            'type': 'ir.actions.act_window',
            'res_model':'wizard.purchase',
            'view_mode': 'form',
            'view_id': self.env.ref('infratel_button_connect.wizard_purchase_form_view').id,
            'target': 'new'            
        }