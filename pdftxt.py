# https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

output_string = StringIO()
with open('pdfs/Digitol-1579920145.pdf', 'rb') as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)

screenplay_text = output_string.getvalue()

print(screenplay_text)

screenplay = {
    'scenes': [
        {
            'location': 'WHATEVER LOCATION',
            'time': 'DAY',
            'dialogue-action': [
                    {
                        'character': 'PETER',
                        'type': 'dialogue',
                        'content': 'Blah blah'
                    },
                {
                        'character': 'PETER',
                        'type': 'action',
                        'content': 'Peter walks to the door'
                },
                {
                        'character': 'JANE',
                        'type': 'dialogue',
                        'content': 'Hey there'
                }
            ]
        }
    ]
}
