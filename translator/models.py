""" translator/models.py"""

from .constants import FieldTypes as FT
import tkinter as tk


from . import views as v


class TextToBinary:
    """
    Translate Texto into Binary.

    fields dictionary is a class member variable that 
    contains all the fields in our model

    """

    fields = {
        "Input": {'req': True, 'type': FT.long_string},
        "Output": {'req': True, 'type': FT.long_string}
    }

    # def __init__(self):

    def translate(self, data):
        """Translate text into binary"""
        trad = ''.join(format(ord(i), '08b') for i in data['Input'])
        # if no text to convert
        if data == '':
            pass  # do nothing

        return trad
