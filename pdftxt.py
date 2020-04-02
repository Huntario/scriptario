# https://pdfminersix.readthedocs.io/en/latest/tutorials/composable.html
from io import StringIO
import re

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

text_file = open("output.txt", "w")
text_file.write(screenplay_text)
text_file.close()
# print(screenplay_text)


with open("output.txt") as f:
    lines = []
    for line in f:
        lines.append(line)

scene_list = []
scene_dict = {}
for line in lines:
    scene_start_int = 'INT' in line
    scene_start_ext = 'EXT' in line
    if scene_start_int == True or scene_start_ext == True:
        scene_dict['location'] = line
        scene_list.append(scene_dict)
        # print(scene_dict)
        # scene_dict.location.append(line)
# print(scene_list)

screenplay = {}

screenplay['scenes'] = scene_list
print(type(screenplay))
print(type(scene_list))
print(screenplay)


# if its new line, ' \n' , then skip it and keep going
# first chracters (letters/numbers, etc) = title
# if you don't understand, skip it and keep going


# print(x)
# look for INT. or EXT.
# then we want location = INT. or EXT. + whatever until this dash -
# drop the dash, and time = whatever is after the dash

# all caps 1-3 words, with no other words on the line --> type = dialogue
# else --> type = action
# if the type is action, then the content = whatever the text is until a new line
# if the type is dialogue, character = the all caps 1-3 words before the new empty line
#   AND the content = everything until the line
# the character is a list of all the all caps words in the action, otherwise null
# later we can make a list of characters, and if its on that list then it may be a sound,
# character = a list of all the characters in that paragraph (before the empty line)

screenplay_rough = {
    'title': 'Di·gi·tol',
    'written_by': 'Some person',
    'scenes': [
        {
            'location': 'WHATEVER LOCATION',
            'time': 'DAY',
            'dialogue_action': [
                {
                    'characters': ['PETER'],
                    'type': 'dialogue',
                    'content': 'Blah blah'
                },
                {
                    'characters': ['PETER'],
                    'type': 'action',
                    'content': 'Peter walks to the door'
                },
                {
                    'characters': ['JANE'],
                    'type': 'dialogue',
                    'content': 'Hey there'
                }
            ]
        }
    ]
}
screenplay = {
    'scenes': [
    ]
}
