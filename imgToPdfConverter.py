"""docs

import img2pdf

# opening from filename
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert('test.jpg'))

# opening from file handle
with open("name.pdf","wb") as f1, open("test.jpg") as f2:
    f1.write(img2pdf.convert(f2))

# using in-memory image data
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert("\x89PNG...")

# multiple inputs (variant 1)
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert("test1.jpg", "test2.png"))

# multiple inputs (variant 2)
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert(["test1.jpg", "test2.png"]))

# convert all files ending in .jpg inside a directory
dirname = "/path/to/images"
with open("name.pdf","wb") as f:
    imgs = []
    for fname in os.listdir(dirname):
        if not fname.endswith(".jpg"):
            continue
        path = os.path.join(dirname, fname)
        if os.path.isdir(path):
            continue
        imgs.append(path)
    f.write(img2pdf.convert(imgs))

# convert all files ending in .jpg in a directory and its subdirectories
dirname = "/path/to/images"
with open("name.pdf","wb") as f:
    imgs = []
    for r, _, f in os.walk(dirname):
        for fname in f:
            if not fname.endswith(".jpg"):
                continue
            imgs.append(os.path.join(r, fname))
    f.write(img2pdf.convert(imgs))


# convert all files matching a glob
import glob
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert(glob.glob("/path/to/*.jpg")))

# writing to file descriptor
with open("name.pdf","wb") as f1, open("test.jpg") as f2:
    img2pdf.convert(f2, outputstream=f1)

# specify paper size (A4)
a4inpt = (img2pdf.mm_to_pt(210),img2pdf.mm_to_pt(297))
layout_fun = img2pdf.get_layout_fun(a4inpt)
with open("name.pdf","wb") as f:
    f.write(img2pdf.convert('test.jpg', layout_fun=layout_fun))

"""

from tkinter import filedialog
import tkinter as tk
from tkinter import Label, Button, Entry, messagebox

import img2pdf


class App():
    
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Img to PDF")
        self.master.geometry("300x200")
        
        Label(self.master, text='').grid(row=0, column=0)
        self.filenames = None
        Label(self.master, text='Select Images:').grid(row=1, column=0)
        button = Button(self.master, text='Select Files', width=25, command=self.getfilenames) 
        button.grid(row=1, column=1)
        
        Label(self.master, text='').grid(row=2, column=0)
        Label(self.master, text='PDF File Name').grid(row=3, column=0) 
        self.output_field = Entry(self.master,width=20) 
        self.output_field.grid(row=3, column=1)
        
        Label(self.master, text='').grid(row=4, column=0)
        converter_button = Button(self.master, text='Convert', width=25, command=self.converter) 
        converter_button.grid(row=5, column=1)
        
        Label(self.master, text='').grid(row=6, column=0)
        Exitbutton = Button(self.master, text='Exit', width=25, command=self.exitApplication) 
        Exitbutton.grid(row=7, column=1)
        
        self.master.mainloop()
        

    def converter(self):
        
        img_files = list(self.filenames)
        output = self.output_field.get().strip(".pdf")+".pdf"
        # multiple inputs (variant 1)
        try:
            converted = img2pdf.convert(img_files)
            with open(output,"wb") as f:
                f.write(converted)
            messagebox.showinfo('Success',
                                f"Images Converted Successfully!\n{output} file has been created.")
        except Exception as e:
            messagebox.showerror('Error..',f"Exception Caught: \n======\n{e}")
        
        
        
    def getfilenames(self):
        self.filenames =  filedialog.askopenfilenames(
                                                    initialdir = "/",title = "Select file",
                                                    filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
                                                    )
        print (list(self.filenames))


    def exitApplication(self):
        MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
        if MsgBox == 'yes':
           self.master.destroy()    

    
    
if __name__ == "__main__":    
    
    app = App()