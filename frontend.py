from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
import backend
from PIL import ImageTk, Image

def choosefile():
    try:
         file = askopenfilename(filetype = [(('image files'),('*.jpg')),(('image files'),('*.jpeg')),(('image files'),('*.png'))])
         backend.choosefile(file)
  
         img = Image.open(file)
         img = img.resize((250,250),Image.ANTIALIAS)
         img = ImageTk.PhotoImage(img)
                                       
         l3 = Label(window, image = img)
         l3.image = img
         l3.grid(row = 0 , column = 2 , rowspan = 5 , columnspan = 2)
         l4 = Label(window,text = backend.dimention())
         l4.grid(row = 1 , column = 0 , columnspan = 2)
         l4.configure(background = '#E8E8E4')
         l5.configure(text = '')
         l6.configure(text = '')
    except:
        pass

def convertfile():
    try:
         width = int(width_data.get())
         height = int(height_data.get())
         backend.convert(width,height)
         messagebox.showinfo("success","File resized successfully")
         
         global l5
         l5 = Label(window,text = 'resized dimention of the image is '+str(width)+'x'+str(height))
         l5.grid(row = 2 , column = 0 , columnspan = 2)
         l5.configure(background = '#E8E8E4')

         global l6
         l6 = Label(window,text = 'save your image as jpg, jpeg or png')
         l6.grid(row = 5 , column = 2)
         l6.configure(background = '#E8E8E4')
    except:
        messagebox.showerror("error","Please input the dimentions first")

def savefile():
    try:
         directory = asksaveasfilename(defaultextension = '.jpg', filetypes = [('file type',('*.*')),('1',('*.jpg')),('2',
         ('*.jpeg')),('3',('*.png'))])

         backend.save(directory)

         l6.configure(text = 'image saved')
    except:
        messagebox.showerror("error","an error occured while saving")
    
def about_command():
    newWindow = Toplevel()
    p1 = PhotoImage(file = 'ico.png')
    newWindow.iconphoto(False,p1)
    newWindow.resizable(0,0)
    newWindow.title("About")
    newWindow.geometry("+600+300")
    nl1 = Label(newWindow,text = "Developer: Ayush Mandal\nProgram Developed in Python\nWhatsapp: +919105604725\nEmail: ayush.mandal11@gmail.com")
    nl1.pack()

window = Tk()
window.geometry("+500+200")
window.resizable(0,0)
window.configure(background = '#E8E8E4')
window.title('Image manipulator')

p1 = PhotoImage(file = 'ico.png')
window.iconphoto(False,p1)

menubar = Menu(window)
file = Menu(menubar, tearoff = 0)
about = Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File', menu = file )
menubar.add_cascade(label = 'about', menu = about )
file.add_command(label = 'choose file' , command = choosefile)
file.add_separator()
file.add_command(label = "exit", command = window.destroy)
about.add_command(label = 'about', command = about_command)
window.config(menu = menubar)

b1 = Button(window,text = 'choose file',bd ='4', command = choosefile , font = ("Arial",12,"") , width = 12)
b1.grid(row = 0 , column = 0 )
b1.configure(background = '#EDF6F9')

l1 = Label(window,text = 'set width', font = ("Arial",14))
l1.grid(row = 3 , column = 0,  rowspan = 1)
l1.configure(background = '#E8E8E4')

width_data = StringVar()
e1 = Entry(window,textvariable = width_data, font = ("Arial",12))
e1.grid(row = 3 , column = 1,  rowspan = 1)

l2 = Label(window,text = 'set height', font = ("Arial",14))
l2.grid(row = 4 , column = 0 )
l2.configure(background = '#E8E8E4')

height_data = StringVar()
e2 = Entry(window,textvariable = height_data, font = ("Arial",12))
e2.grid(row = 4 , column = 1)

b2 = Button(window,text = 'resize',pady = 5,bd ='4',padx = 5, command = convertfile , font = ("Arial",12) , width = 12)
b2.grid(row = 5 , column = 0)
b2.configure(background = '#EDF6F9')

b3 = Button(window,text = 'save', pady = 5,bd ='4',padx = 5, command = savefile , font = ("Arial",12) , width = 12)
b3.grid(row = 5 , column = 1)
b3.configure(background = '#EDF6F9')

window.mainloop()