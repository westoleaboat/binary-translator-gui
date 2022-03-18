from tkinter import *
from tkinter import Tk

class Content:
    def __init__(self, root):
        """
        Translate text input to binary output
        """

        # Convert text into binary
        def convert():
            # fetch input text
            string_to_convert = input_text.get("1.0", "end-1c")
            # format into binary
            trad = ''.join(format(ord(i), '08b') for i in string_to_convert)
            # if no text to convert
            if string_to_convert == '':
                pass # do nothing
            else:
                # activate text widget
                binary_output['state']='normal'
                # add binary to output
                binary_output.insert(END, trad)
                # deactivate text widget
                binary_output['state']='disabled'

        # delete input text when convert button is clicked
        def clear_text():
            # delete input text
            input_text.delete("1.0", "end")
            # activate output text widget
            binary_output['state']='normal'
            # delete binary text
            binary_output.delete("1.0", "end")

        # LabelFrame contain the input text
        input_lf = LabelFrame(text='TEXT INPUT')
        input_lf.pack(pady=10)

        # LabelFrame for buttons
        button_lf = LabelFrame(text='')
        button_lf.pack()

        # input text widget
        input_text = Text(input_lf, height=10)
        input_text.pack()

        # convert into binary button
        btn_convert = Button(button_lf, text='convert', command=convert)
        btn_convert.pack(side='left')

        # delete all text button
        btn_clear = Button(button_lf, text='clear', command=clear_text)
        btn_clear.pack(side='right')

        # LabelFrame contains the binary output
        output_lf = LabelFrame(text='BINARY OUTPUT')
        output_lf.pack()

        # binary output text widget
        binary_output = Text(output_lf, height=10, state='disabled')
        binary_output.pack()


# define root, call content class
# infinite loop
def main():
    root = Tk()
    root.geometry('600x450+800+300')
    root.resizable(0, 0)
    root.title('BINARY CONVERTER')
    cnt = Content(root)
    root.mainloop()


if __name__ == '__main__':
    main()
