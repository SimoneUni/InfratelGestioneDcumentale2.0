from odoo import models, fields

class FileParsing(models.Model):
    _name = 'file.parsing'
    _description = 'File Parsing'
    
    name  = fields.Char('Documento di riferimento')
    
    
    
    # *********campi parsing*********
    
    #campi sale.oder
    cig_list = fields.Char('CIG')
    cup_list = fields.Char('CUP')
    project_request_id_list = fields.Char('Progetto relativo a')
    infr_order_list = fields.Char('Commessa')
    framework_agreement_id_list = fields.Char('Accordo quadro')
    request_type_list = fields.Char('Tipo richiesta')
    contact_referent_id_list = fields.Char('Referente')
    email_rel_list = fields.Char('E-mail')
    pec_rel_list = fields.Char('E-mail PEC')
    phone_rel_list = fields.Char('Telefono')
    joint_testing_list = fields.Char('Collaudo congiunto')
    is_quadrature_possible_list = fields.Char('Quadratura possibile')
    business_developer_id_list = fields.Char('Business Developer')
    delivery_employee_id_list = fields.Char('Dipendente delivery')
    is_sale = fields.Boolean('Vendita', default=False)
    
    #Campi relativi a 'purchase.order'
    project_request_id_purchase = fields.Char('Progetto relativo a')
    infr_order_purchase = fields.Char('Commessa')
    framework_agreement_id_purchase = fields.Char('Accordo quadro')
    sla_policy_id_rel_purchase = fields.Char('Politica SLA')
    cig_purchase = fields.Char('CIG')
    cup_purchase = fields.Char('CUP')
    request_type_purchase = fields.Char('Tipo richiesta')
    contact_referent_id_purchase = fields.Char('Referente')
    email_rel_purchase = fields.Char('E-mail')
    pec_rel_purchase = fields.Char('E-mail PEC')
    phone_rel_purchase = fields.Char('Telefono')
    joint_testing_purchase = fields.Char('Collaudo congiunto')
    expiration_date_purchase = fields.Char('Deadline')
    actual_delivery_date_purchase = fields.Text('Data di consegna effettiva')
    delivery_employee_id_purchase = fields.Char('Dipendente delivery')
    works_director_id_purchase = fields.Char('Direttore lavori')
    execution_security_coordinator_id_purchase = fields.Char('Coordinatore sicurezza esecuzione')
    design_safety_coordinator_id_purchase = fields.Char('Coordinatore sicurezza progettazione')
    
    testo = fields.Html('testo')
    
    
    
    
    
    
    
    
    
    
    def parse_and_update_html(self):
        # Qui puoi recuperare i dati necessari per compilare il template
        partner = self.env['res.partner'].browse(1)  # Sostituisci con il tuo effettivo record di res.partner
        
        # 'nome_campo' è quello che deve essere scritto in {{nome_campo}}
        # self.campo è il campo ch vado a prelevare.
        
        context = {'nome': self.code_deal,
                
                   }
        
        #gestione del campo vuoto, quano esso non è presente sarà vuoto e non uscirà il 'False'
        if self.pippi:
            context['pippi'] = self.pippi
            
        
        
        

        # Carica il template HTML dal campo e compila i segnaposto
        compiled_html = self._compile_html_template(self.nome_campo_html, context)

        # Aggiorna il campo HTML con la versione compilata
        self.write({'nome_campo_html': compiled_html})