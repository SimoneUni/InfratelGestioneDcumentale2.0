from odoo import fields, models, _, api
# import os
# import pypandoc
# import base64


class DocumentList(models.Model):
    _name = 'document.list'
    _description = 'Document List'
    
    
    name = fields.Char('Nome documento')
    reference = fields.Char('Codice Documento', required=True, copy=False, 
                            readonly=True, default=lambda self: _('New'))
    order_many = fields.Many2one('sale.order', string="prova")
    cig_rel = fields.Char(related='order_many.cig', string="CIG")
    
    
   
    
    #Campi relativi a 'sale.order'
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
    is_purchase = fields.Boolean('Acquisto', default=False)
    document_associato = fields.Many2one('generated.documents', string='docc')
    
    

    # state = fields.Selection([
    #     ('draft','Bozza'), ('approval_1','Approvazione Fase 1'),
    #     ('approval_2', 'Approvazione Fase 2')
    # ], string='Stato', compute='_compute_state', store=True)
    
    phases_names_selection = fields.Selection(
        selection=[('draft', 'Bozza'), ('approval_1', 'Approvazione 1')],
        string='Fasi del Documento',
    )
    
    # state = fields.Selection([('draft','Bozza'), ('approval_1','Approvazione Fase 1'),
    #                           ('approval_2', 'Approvazione Fase 2'),('signature','Firma'),('signature_1','Firma 1'),
    #                           ('signature_2', 'Firma 2')], string="Fasi", default='draft', readonly=True)
    
    
    upload_file = fields.Binary('Carica File')
    download_file = fields.Binary('Scarica File')
    associate_document = fields.Char('Documento Associato')
    tipo_configurazione = fields.Char('Connf')
    configurazione_prova = fields.Char('conf')
    
    

    
    # @api.depends('ponte_collegamento')
    # def _compute_config_info(self):
    #     for record in self:
    #         config_info = {
    #             'name': record.ponte_collegamento.name,
    #             'note': record.ponte_collegamento.note,
    #             'phase_ids': [(phase.id, phase.name) for phase in record.ponte_collegamento.phase_ids],
    #             # 'document_category_id': (record.document_configuration_id.document_category_id.id, record.document_configuration_id.document_category_id.name),
    #             'start_process': record.ponte_collegamento.start_process,
    #             'presence_dl': record.ponte_collegamento.presence_dl,
    #             'show_presence_dl': record.ponte_collegamento.show_presence_dl,
    #             # Aggiungi altri campi come document_lines, ecc.
    #         }
    #         record.update(config_info)
    
    
    def approva(self):
        # if self.state == 'draft':
        #     self.write({'state': 'approval_1'})
        # elif self.state == 'approval_1':
        #     self.write({'state': 'approval_2'})
        # elif self.state == 'approval_2':
        #     self.write({'state': 'signature'})
        # elif self.state == 'signature':
        #     self.write({'state': 'signature_1'})
        # elif self.state == 'signature_1':
        #     self.write({'state': 'signature_2'})
        return
    
    def indietro(self):
        # if self.state == 'approval_1':
        #     self.write({'state': 'draft'})
        # elif self.state == 'approval_2':
        #     self.write({'state': 'approval_1'})
        # elif self.state == 'signature':
        #     self.write({'state': 'approval_2'})
        # elif self.state == 'signature_1':
        #     self.write({'state': 'signature'})
        # elif self.state == 'signature_2':
        #     self.write({'state': 'signature_1'})
        return
    
    
    
            
            
    # @api.onchange('html_content')
    # def convert_html_to_docx(self):
    #     if self.html_content:
    #         try:
    #             # Salva il contenuto HTML in un file temporaneo
    #             html_path = 'C:\\Users\\simone\\Desktop\\contenitore'
    #             with open(html_path, 'w', encoding='utf-8') as html_file:
    #                 html_file.write(self.html_content)

    #             # Converti il file HTML in un file DOCX
    #             docx_path = '/path/to/temporary/file.docx'
    #             pypandoc.convert_file(html_path, 'docx', outputfile=docx_path)

    #             # Leggi il contenuto del file DOCX e salvalo nel campo binary_file
    #             with open(docx_path, 'rb') as docx_file:
    #                 self.download_file = base64.b64encode(docx_file.read())

    #         except Exception as exc:
    #             print(exc)

    #         finally:
    #             # Pulisci i file temporanei
    #             if html_path:
    #                 os.remove(html_path)
    #             if docx_path:
    #                 os.remove(docx_path)

    # def clear_binary_file(self):
    #     self.download_file = False