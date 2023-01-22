
from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import *
from tkinter import messagebox
from plyer import notification
import time


root=Tk()
root.geometry("500x300+430+200")
root.title("Notifier App |Developed by Sukalyan")
root.config(background="grey",bd=10,relief=RIDGE)
# ___________________________________SETTING IMAGE__________________________________
ico = Image.open('image1.ico')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# _____________________DEFINING THE FUNCTION________________________________
def function():
    get_label1=tittle.get()
    get_label2=message.get()
    get_label3=date.get()


    if get_label1==" " or get_label2==" " or get_label3==" ":
        messagebox.showerror("Alert","All Fields are Required !!")
    else:
        int_time=int(get_label3)
        min_to_sec=int_time*60
        messagebox.showinfo("notifier set","set notifier ?")
        root.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_label1,
                            message=get_label2,
                            app_name="Notifier",
                            toast=True,
                            timeout=10)


#For Tittle
label1=Label(root,text="Tittle ",background="grey",font=("poppins",16))
label1.place(x=10,y=50)
#For Tittle Entry
tittle=Entry(root,width="25",font=("poppins",16))
tittle.place(x=110,y=50)

#For message
label2=Label(root,text="Message ",background="grey",font=("poppins",16))
label2.place(x=10,y=100)
#For message Entry
message=Entry(root,width="25",font=("poppins",16))
message.place(x=110,y=100)

#For date
label3=Label(root,text="Date ",background="grey",font=("poppins",16))
label3.place(x=10,y=150)
#For date Entry
date=Entry(root,width="6",font=("poppins",16))
date.place(x=110,y=150)
#For minute
label3=Label(root,text="Min ",background="grey",font=("poppins",16))
label3.place(x=200,y=150)

#button
btn=Button(root,text="Save",command=function)
btn.place(x=200,y=200)




root.mainloop()