""" translator.py: Translate text to binary

The code is organized in the following classes:

    -BoundText: Text widget with a bound variable
    -LabelInput: Widget containing a label and input together
    -MyForm: Input form for widgets
    -Application: Application root window

TODO:
    -option to translate binary into text
    -buttons: improve inter-object communication

Author: Tomas C. 
"""


from translator.application import Application

app = Application()
app.mainloop()
