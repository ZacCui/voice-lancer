#!/usr/bin/python3

# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import six

"""Detects syntax in the text."""
client = language.LanguageServiceClient()

searchTrigger = 'find jobs'
searchKeyword = 'web design'
createTrigger = 'create jobs'

def search():
    # get furthur text
    pass

def create():
    pass

REQUEST_TYPE = {'search' : search, 'create' : create}

def getRequestType(text):
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')

    # Instantiates a plain text document.
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects syntax in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    tokens = client.analyze_syntax(document).tokens

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    for token in tokens:
        # print(token)
        # print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag], token.text.content))
        if pos_tag[token.part_of_speech.tag]=='VERB' and token.text.content in REQUEST_TYPE:
            return REQUEST_TYPE[token.text.content]

# entry point
def pipeline(text):
    pipefunc = getRequestType(text)
    pipefunc()


if __name__ == "__main__":
    pass
