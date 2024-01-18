from odoo import models, fields,api

class DocumentConfiguration(models.Model):
    _name = 'document.configuration'
    _description = 'Document Configuration'
    
    name = fields.Char(string='Name', required=True)
    note = fields.Text('Dscrizione')
    phase_ids = fields.Many2many('document.phases', string='Fase')
    document_category_id = fields.Many2one('generated.documents', string="Categoria documento")
    #document_template_id = fields.Many2one('ir.attachment', string='Template')
    document_lines = fields.One2many('document.lines', 'phase_approvers', string="Fase-Approvatori")
    start_process = fields.Selection([('oda', 'Ordine di acquisto'),('odv', 'Ordine di vendita')], string="Inizio del processo", required=True)
    presence_dl = fields.Boolean('Presenza DL')
    show_presence_dl = fields.Boolean(compute='_compute_show_presence_dl', default=False)
    
    
    
    
    
    @api.depends('document_category_id')
    def _compute_show_presence_dl(self):
        for record in self:
            # Sostituisci queste condizioni con le tue condizioni specifiche
            # modello_b_record = self.env['generated.documents'].sudo().browse(1)
            # print("f prova ", modello_b_record)
            
            record.show_presence_dl = record.document_category_id.name.lower() in ['lavoro','consegna del cantiere al fornitore',
                                                                                   'lavori','intervento fornitore' ,'misure' ,'manutenzione', 'cai' ]
    
    def _compute_config_info(self):
        # Funzione per calcolare e restituire le informazioni di configurazione
        config_info = {
            'name': self.name,
            'note': self.note,
            'phase_ids': [(phase.id, phase.name) for phase in self.phase_ids],
            'document_category_id': (self.document_category_id.id, self.document_category_id.name),
            'start_process': self.start_process,
            'presence_dl': self.presence_dl,
            'show_presence_dl': self.show_presence_dl,
            # Aggiungi altri campi come document_lines, ecc.
        }
        return config_info
    
    
    