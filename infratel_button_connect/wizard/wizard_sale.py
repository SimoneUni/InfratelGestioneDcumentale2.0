from odoo import fields, models, api, _
from jinja2 import Template


class WizardSale(models.Model):
    _name = 'wizard.sale'
    _description = 'Wizard Sale'
    
    
    categoria_documento = fields.Many2one('document.all',
                                          string="Tipo documento",
                                          required=True,
                                          ondelete='cascade',
                                          domain="[('document_category', '=', cat_document)]")
   
    cat_document = fields.Many2one('generated.documents',
                                    string="Categeria documento",
                                    required=True,
                                    ondelete='cascade')
    
    yaaa = fields.Many2one('document.configuration',
                           string="Configurazione Relazione",
                           domain="[('document_category_id', '=', cat_document)]")
    
    # def _get_selection(self):
    #         selection = []
    #         for line in self.yaaa.document_lines:
    #             selection += [line.phases_id.name]
    #         return selection

    @api.onchange('cat_document')
    def _onchange_cat_document(self):
        # Aggiorna il dominio di categoria_documento in base al valore selezionato in cat_document
        if self.cat_document:
            return {'domain': {'categoria_documento': [('document_category', '=', self.cat_document.id)]}}
        else:
            return {'domain': {'yaaa': []}}
    
    @api.onchange('cat_document')
    def _onchange_cat_document(self):
        # Aggiorna il dominio di yaaa in base al valore selezionato in cat_document
        if self.cat_document:
            return {'domain': {'yaaa': [('document_category_id', '=', self.cat_document.id)]}}
        else:
            return {'domain': {'yaaa': []}}
    
    
    reference = fields.Char('Codice Documento', required=True, copy=False,
                            readonly=True, default=lambda self: _('New'))
    
    testo = fields.Html('Testo')
    
                
    @api.model
    def _compile_html_template(self, template_string, context):
        template = Template(template_string)
        compiled_html = template.render(context)
        return compiled_html
    
    def generate_documents(self):
        
        active_id = self.env.context.get('active_id')
        sale_order_record = self.env['sale.order'].browse(active_id)
        # model_name = self._name
         
        project_request_id_value = sale_order_record.project_request_id
        infr_order_value = sale_order_record.infr_order
        framework_agreement_id_value = sale_order_record.framework_agreement_id
        cig_value = sale_order_record.cig
        cup_value = sale_order_record.cup
        request_type_value = sale_order_record.request_type
        contact_referent_id_value = sale_order_record.contact_referent_id
        email_rel_value = sale_order_record.email_rel
        pec_rel_value = sale_order_record.pec_rel
        phone_rel_value = sale_order_record.phone_rel
        joint_testing_value = sale_order_record.joint_testing
        is_quadrature_possible_value = sale_order_record.is_quadrature_possible
        business_developer_id_value = sale_order_record.business_developer_id
        delivery_employee_id_value = sale_order_record.delivery_employee_id
        
        document_associated = self.categoria_documento
        
        
        testo_value = document_associated.nome_campo_html
        
        result_list = []

        # Itera attraverso le linee del documento
        for line in self.yaaa.document_lines:
            result_list.append(line.phases_id.sequence)

        # Mappa i valori di sequence ai valori di state
        sequence_to_state_mapping = {
            1: 'draft',
            2: 'approval_1',
            3: 'approval_2',
            # Aggiungi altri mapping se necessario
        }
        default_state = 'default_state'  # Sostituisci con lo stato predefinito desiderato
        state_values = [sequence_to_state_mapping.get(sequence, default_state) for sequence in result_list]

        

        # Alla fine dell'iterazione, avrai una lista di tuple con ('sequence', 'name') tra apici
        print('Risultato finale',result_list)
        
        DocumentList = self.env['document.list']
        
        
        sequence_code = 'document.list' 
        # Ottieni il prossimo numero della sequenza
        next_sequence = self.env['ir.sequence'].next_by_code(sequence_code)

        
        # Ottieni il prossimo numero della sequenza
        
       
        
        # map(lambda item: item.phases_id.name ,self.yaaa.document_lines)
        
        # Crea un nuovo record in DocumentList con i dati desiderati
        new_document = DocumentList.create({
            'project_request_id_list': project_request_id_value.name,
            'infr_order_list': infr_order_value,
            'framework_agreement_id_list': framework_agreement_id_value.name,
            'cig_list': cig_value,
            'cup_list': cup_value,
            'request_type_list': request_type_value,
            'contact_referent_id_list': contact_referent_id_value.name,
            'email_rel_list': email_rel_value,
            'pec_rel_list': pec_rel_value,
            'phone_rel_list': phone_rel_value,
            'joint_testing_list': joint_testing_value,
            'is_quadrature_possible_list': is_quadrature_possible_value,
            'business_developer_id_list': business_developer_id_value.name,
            'delivery_employee_id_list': delivery_employee_id_value.name,
            'reference': next_sequence,
            'is_sale': True,
            'associate_document': self.cat_document.name,
            'configurazione_prova' : self.yaaa.name,
            'tipo_configurazione': self.yaaa.document_category_id.name,
            
                # ', '.join(list(map(lambda item: item.phases_id.name, self.yaaa.document_lines)))
        })
        
        print(', '.join(list(map(lambda item: item.phases_id.name, self.yaaa.document_lines))))
        # print(map(lambda item: item.phases_id.name ,self.yaaa.document_lines))
        # print(self.yaaa.document_lines)
        # print(self.yaaa.document_lines.phases_id.name)
        
        # def _get_selection(self):
        #     selection = []
        #     for line in self.yaaa.document_lines:
        #         selection += [line.phases_id.name]
        #     return selection
        # lista = []
        # listaseq = []
        # for line in self.yaaa.document_lines:
        #     lista.append(line.phases_id.name)
        #     listaseq.append(line.phases_id.sequence)
        # print("listaaaaaaaaaa", lista.append(line.phases_id.name))
        # print("vuota?", lista)
        # print("sequenza", listaseq)
        
                # Inizializza la lista vuota


        # new_document._compute_config_info()

        # new_document.onchange_cig_list()
           
            
        ParsingDocument = self.env['file.parsing']
        
        new_parsing_document = ParsingDocument.create({
            'project_request_id_list': project_request_id_value.name,
            'infr_order_list': infr_order_value,
            'framework_agreement_id_list': framework_agreement_id_value.name,
            'cig_list': cig_value,
            'cup_list': cup_value,
            'request_type_list': request_type_value,
            'contact_referent_id_list': contact_referent_id_value.name,
            'email_rel_list': email_rel_value,
            'pec_rel_list': pec_rel_value,
            'phone_rel_list': phone_rel_value,
            'joint_testing_list': joint_testing_value,
            'is_quadrature_possible_list': is_quadrature_possible_value,
            'business_developer_id_list': business_developer_id_value.name,
            'delivery_employee_id_list': delivery_employee_id_value.name,
            'is_sale':True,
            'testo' : testo_value  
        })
        
        # 'nome_campo' è quello che deve essere scritto in {{nome_campo}}
        # self.campo è il campo ch vado a prelevare.
        
        context = {}
        
        #gestione del campo vuoto, quano esso non è presente sarà vuoto e non uscirà il 'False'
        # if self.pippi:
        #     context['pippi'] = self.pippi
            
        if cig_value:
            context['cig'] = cig_value
                
        

        # Carica il template HTML dal campo e compila i segnaposto
        compiled_html = self._compile_html_template(testo_value, context)

        # Aggiorna il campo HTML con la versione compilata
        new_parsing_document.write({'testo': compiled_html})
        
        
        
        return True

    
   
    # @api.depends('yaaa')
    # def _compute_config_info(self):
    #     for record in self:
    #         config_info = {
    #             'name': record.yaaa.name,
    #             'note': record.yaaa.note,
    #             'phase_ids': [(phase.id, phase.name) for phase in record.yaaa.phase_ids],
    #             # 'document_category_id': (record.document_configuration_id.document_category_id.id, record.document_configuration_id.document_category_id.name),
    #             'start_process': record.yaaa.start_process,
    #             'presence_dl': record.yaaa.presence_dl,
    #             'show_presence_dl': record.yaaa.show_presence_dl,
    #             # Aggiungi altri campi come document_lines, ecc.
    #         }
    #         record.update(config_info)
            
    #         record.phase_status = config_info.get('phase_ids', [])
        
    # print(phase_status)
            
    