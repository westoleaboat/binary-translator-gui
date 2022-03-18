from tkinter import *
from tkinter import Tk

class Content:
    def __init__(self, root):

        def convert():
            string_to_convert = input_text.get("1.0", "end-1c")
            trad = ''.join(format(ord(i), '08b') for i in string_to_convert)
            if string_to_convert == '':
                pass
            else:
                binary_output.insert(END, trad)

        def clear_text():
            input_text.delete("1.0", "end")
            binary_output.delete("1.0", "end")

        input_lf = LabelFrame(text='TEXT INPUT')
        input_lf.pack(pady=10)

        button_lf = LabelFrame(text='')
        button_lf.pack()

        input_text = Text(input_lf, height=10)
        input_text.pack()

        btn_convert = Button(button_lf, text='convert', command=convert)
        btn_convert.pack(side='left')

        btn_clear = Button(button_lf, text='clear', command=clear_text)
        btn_clear.pack(side='right')

        output_lf = LabelFrame(text='BINARY OUTPUT')
        output_lf.pack()

        binary_output = Text(output_lf, height=10)
        binary_output.pack()



def main():
    root = Tk()
    root.geometry('600x450+800+300')
    root.resizable(0, 0)
    root.title('BINARY CONVERTER')
    cnt = Content(root)
    root.mainloop()

if __name__ == '__main__':
    main()
