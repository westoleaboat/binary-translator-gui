"""
translator/views.py: form containing widgets
"""

import tkinter as tk
from tkinter import ttk

from . import widgets as w
from .constants import FieldTypes as FT


class MyForm(tk.Frame):
    """Input Form for widgets

    - self._vars = Create a dictionary to hold all out variable objects 
    - _add_frame = instance method that add a new label frame. Pass in 
                   label text and optionally a number of columns.

    """

    var_types = {
        FT.string: tk.StringVar,
        FT.string_list: tk.StringVar,
        FT.short_string_list: tk.StringVar,
        FT.iso_date_string: tk.StringVar,
        FT.long_string: tk.StringVar,
        FT.decimal: tk.DoubleVar,
        FT.integer: tk.IntVar,
        FT.boolean: tk.BooleanVar
    }

    def _add_frame(self, label, cols=3):
        frame = ttk.LabelFrame(self, text=label)
        frame.grid(sticky=tk.W + tk.E)
        for i in range(cols):
            frame.columnconfigure(i, weight=1)
        return frame

    def __init__(self, parent, model, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.model = model
        fields = self.model.fields

        self._vars = {  # hold all variable objects
            key: self.var_types[spec['type']]()
            for key, spec in fields.items()
            # 'Text': tk.StringVar(),
            # 'Binary': tk.StringVar()
        }

        # disable var for Output field
        self._disable_var = tk.BooleanVar()

        # build the form
        self.columnconfigure(0, weight=1)

        w.LabelInput(
            # input,
            self,
            'Enter a Value',
            input_class=w.BoundText,
            field_spec=fields['Input'],
            var=self._vars['Input'], input_args={
                'width': 85, 'height': 6, }
        ).grid(sticky='nswe', row=0, column=0)

        w.LabelInput(
            # output,
            self,
            'Conversion',
            input_class=w.BoundText,
            field_spec=fields['Output'],
            var=self._vars['Output'], input_args={
                'width': 85, 'height': 6},
            disable_var=self._disable_var
        ).grid(row=1, column=0)

        self._disable_var.set(True)

        # text to display data from form
        self.output_var = tk.StringVar()

        ###########
        # buttons #
        ###########
        # improving inter-object communication was added to bug tracker

        buttons = ttk.Frame(self)  # add on a frame
        buttons.grid(sticky=tk.W + tk.E, row=4)
        # pass instance methods as callback commands
        self.transbutton = ttk.Button(
            buttons, text="Convert", command=self._on_trans)
        self.transbutton.pack(side=tk.RIGHT)

        self.transbutton = ttk.Button(
            buttons, text="Binary to Text", command=self._on_trans, state='disabled')
        # self.transbutton.pack(side=tk.RIGHT)

        # self.savebutton = ttk.Button(
        #     buttons, text="Save", command=self.master._on_save)  # on parent
        # self.savebutton.pack(side=tk.RIGHT)
        self.resetbutton = ttk.Button(
            buttons, text="Reset", command=self.reset)  # on this class
        self.resetbutton.pack(side=tk.RIGHT)

    def reset(self):
        """Reset entries. Set all variables to empty string"""
        # activate widget
        self._disable_var.set(False)
        # self.set_output_state(tk.NORMAL)

        # reset data
        for var in self._vars.values():
            if isinstance(var, tk.BooleanVar):
                # uncheck checkbox
                var.set(False)
            else:
                # set inputs to empty string
                var.set('')
                # set data label to empty string
                # self.output_var.set('')
        # disable widget
        self._disable_var.set(True)
        # self.set_output_state(tk.DISABLED)

    def get(self):
        """Retrieve data from the form so it can be saved or used"""
        data = {}
        for key, variable in self._vars.items():
            try:
                # retrieve from ._vars
                data[key] = variable.get()
            except tk.TclError as e:
                # create error message
                message = f'Error in field: {key}. Data not saved!'
                raise ValueError(message) from e
        # return the data
        return data

    #########################################
    # Disable widget if disable_var not used:
    #
    # def set_output_state(self, state):
    #     output_widget = self._get_widget_by_var(self._vars['Output'])
    #     if output_widget:
    #         output_widget.input.configure(state=state)

    # def _get_widget_by_var(self, var):
    #     """Return the widget associated with a given variable."""
    #     for widget in self.winfo_children():
    #         if isinstance(widget, w.LabelInput) and widget.variable == var:
    #             return widget
    #     return None
    #########################################

    def _on_trans(self):
        self.event_generate('<<TranslateText>>')
        # self._disable_var.set(False)
