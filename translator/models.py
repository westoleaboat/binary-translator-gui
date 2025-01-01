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
        
    def is_binary(self, data):
        '''check if data is binary'''
        return all(char in '01' for char in data) and len(data) % 8 == 0
        # try:
        #     int(data, 2)
        #     return True
        # except ValueError:
        #     return False

        
    def translate_to_text(self, data):
        '''Translate binary into text'''
        binary_input = data['Input']
        try:
            characters = [chr(int(binary_input[i:i+8], 2)) for i in range(0, len(binary_input), 8)]
            # return ''.join(characters)
            trad = ''.join(characters)
            return trad
        except ValueError:
            # return "Invalid binary input."
            pass

    def translate_to_binary(self, data):
        """Translate text into binary"""
        trad = ''.join(format(ord(i), '08b') for i in data['Input'])
        # if no text to convert
        if data == '':
            pass  # do nothing

        return trad

    def translate(self, data):
        """Handle translation based on input type"""
        input_text=data['Input']
        if data['Input'] == '':
            pass
        
        if self.is_binary(input_text):
            return self.translate_to_text(data)
        else:
            return self.translate_to_binary(data)

        # elif v.MyForm.is_binary(input_text):
        #     return v.MyForm.translate_to_text(data)
        # else:
        #     return v.MyForm.translate_to_binary(data)
