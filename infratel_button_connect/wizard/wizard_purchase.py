from odoo import models, fields, api, _

class WizardPurchase(models.Model):
    _name = 'wizard.purchase'
    _description = 'Wizard Purchase'
    
    categoria_documento = fields.Many2one('document.all',
                                          string="Categoria documento",
                                          required=True,
                                          ondelete='cascade')
    
    reference = fields.Char('Codice Documento', required=True, copy=False,
                            readonly=True, default=lambda self: _('New'))
    
    def generate_documents(self):
        active_id = self.env.context.get('active_id')
        purchase_record = self.env['purchase.order'].browse(active_id)
        
        
        project_request_id_value = purchase_record.project_request_id
        infr_order_value = purchase_record.infr_order
        framework_agreement_id_value = purchase_record.framework_agreement_id
        sla_policy_id_rel_value = purchase_record.sla_policy_id_rel
        cig_value = purchase_record.cig
        cup_valu = purchase_record.cup
        request_type_value = purchase_record.request_type
        contact_referent_id_value = purchase_record.contact_referent_id
        email_rel_value = purchase_record.email_rel
        pec_rel_value = purchase_record.pec_rel
        phone_rel_value = purchase_record.phone_rel
        joint_testing_value = purchase_record.joint_testing
        expiration_date_value = purchase_record.expiration_date
        actual_delivery_date_value = purchase_record.actual_delivery_date
        
        delivery_employee_id_value = purchase_record.delivery_employee_id
        works_director_id_value = purchase_record.works_director_id
        execution_security_coordinator_id_value = purchase_record.execution_security_coordinator_id
        design_safety_coordinator_id_value = purchase_record.design_safety_coordinator_id
        
        DocumentList = self.env['document.list']
        
        sequence_code = 'document.list.purchase' 
        # Ottieni il prossimo numero della sequenza
        next_sequence = self.env['ir.sequence'].next_by_code(sequence_code)
        
        new_document = DocumentList.create({
            'project_request_id_purchase': project_request_id_value.name,
            'infr_order_purchase': infr_order_value,
            'framework_agreement_id_purchase': framework_agreement_id_value.name,
            'sla_policy_id_rel_purchase': sla_policy_id_rel_value.name,
            'cig_purchase': cig_value,
            'cup_purchase': cup_valu,
            'request_type_purchase': request_type_value,
            'contact_referent_id_purchase': contact_referent_id_value.name,
            'email_rel_purchase': email_rel_value,
            'pec_rel_purchase': pec_rel_value,
            'phone_rel_purchase': phone_rel_value,
            'joint_testing_purchase': joint_testing_value,
            'expiration_date_purchase': expiration_date_value,
            'actual_delivery_date_purchase': actual_delivery_date_value,
            'delivery_employee_id_purchase': delivery_employee_id_value.name,
            'works_director_id_purchase': works_director_id_value.name,
            'execution_security_coordinator_id_purchase': execution_security_coordinator_id_value.name,
            'design_safety_coordinator_id_purchase': design_safety_coordinator_id_value.name,
            'reference': next_sequence,
            'is_purchase': True
        })
        
        ParsingDocument = self.env['file.parsing']
        
        new_parsing_document = ParsingDocument.create({
            'project_request_id_purchase': project_request_id_value.name,
            'infr_order_purchase': infr_order_value,
            'framework_agreement_id_purchase': framework_agreement_id_value.name,
            'sla_policy_id_rel_purchase': sla_policy_id_rel_value.name,
            'cig_purchase': cig_value,
            'cup_purchase': cup_valu,
            'request_type_purchase': request_type_value,
            'contact_referent_id_purchase': contact_referent_id_value.name,
            'email_rel_purchase': email_rel_value,
            'pec_rel_purchase': pec_rel_value,
            'phone_rel_purchase': phone_rel_value,
            'joint_testing_purchase': joint_testing_value,
            'expiration_date_purchase': expiration_date_value,
            'actual_delivery_date_purchase': actual_delivery_date_value,
            'delivery_employee_id_purchase': delivery_employee_id_value.name,
            'works_director_id_purchase': works_director_id_value.name,
            'execution_security_coordinator_id_purchase': execution_security_coordinator_id_value.name,
            'design_safety_coordinator_id_purchase': design_safety_coordinator_id_value.name,
        })
        return True
    
    