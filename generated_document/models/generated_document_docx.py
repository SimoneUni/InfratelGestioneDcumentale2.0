from odoo import models, fields, api
from docx import document
from io import BytesIO
import base64


class DocumentTemplate(models.Model):
    _name = 'document.template'
    _description = 'Document Template'

    name = fields.Char("Name")
    template_file = fields.Binary("Carica Documento")
    processed_file = fields.Binary("Documento Finale")
    

    @api.multi
    def button_generate_document(self):
        self.ensure_one()  # Assicurati che il metodo sia chiamato su un singolo record
        # Qui va la logica per generare il documento
        # Ad esempio, puoi chiamare il metodo process_template qui
        self.process_template()
        
    def process_template(self):
        if not self.template_file:
            raise Exception("No template file uploaded")
        current_user = self.env.user
        user_name = current_user.name  # Ottieni il nome dell'utente corrente

        file_content = BytesIO(base64.b64decode(self.template_file))
        doc = document(file_content)

        for paragraph in doc.paragraphs:
            if "{{ nome }}" in paragraph.text:
                paragraph.text = paragraph.text.replace("{{ nome }}", user_name)

        # Salva il file modificato
        file_stream = BytesIO()
        doc.save(file_stream)
        self.processed_file = base64.b64encode(file_stream.getvalue())
        