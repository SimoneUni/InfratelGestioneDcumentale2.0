from odoo import api, fields, models 
from jinja2 import Template


class AllDocuments(models.Model):
    _inherit = 'document.all'

    # foreign key to the res.partner model;
    # on partner_id remove, record with this foreign key will be deleted
    document_category = fields.Many2one('generated.documents', string="Categoria documento associato",
        required=True, ondelete='cascade')
    type_documents_rel = fields.Char(related ='document_category.name' , string="mento")
    
    
    #campi booleandi da attivare nella sezione 'voci'
    
    code_deal = fields.Boolean('Codice Tratta')
    pippi = fields.Char('provapippi')
    point_a = fields.Boolean('Punto A')
    point_z = fields.Boolean('Punto Z')
    contract_name = fields.Boolean('Nome contratto')
    date_contract = fields.Boolean('Data contratto')
    cig = fields.Boolean('CIG')
    cup = fields.Boolean('CUP')
    shop_assistant_code = fields.Boolean('Codice commessa')
    contracting_entity = fields.Boolean('Ente appaltante')
    dl = fields.Boolean('DL')
    contracting_company = fields.Boolean('Impresa appaltatrice')
    netAmount_WorksContract = fields.Boolean('Importo netto lavori contratto')
    approval_date_oda = fields.Boolean('Data approvazione (OdA)')
    approval_date_frameworkAgreement = fields.Boolean('Data approvazione (Accordo quadro)')
    deadline = fields.Boolean('Deadline')
    
    #campo html relativa alla sezione 'testo'
    
    nome_campo_html = fields.Html(string='Nome Campo HTML', help='Descrizione del campo HTML')

    nome_campo_html_2 = fields.Html(string='Nome Campo HTML', help='Descrizione del campo HTML')
    
    @api.model
    def _compile_html_template(self, template_string, context):
        template = Template(template_string)
        compiled_html = template.render(context)
        return compiled_html


    #funzione per eseguire il parsing
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