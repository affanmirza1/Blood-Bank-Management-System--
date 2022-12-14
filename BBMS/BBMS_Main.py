from tkinter import *
import defaultmysql
import mysql.connector
from tkcalendar import *
from tkinter import ttk,font
from PIL import Image,ImageTk
from tkinter import messagebox
import builtins
import importlib.util as iu

window=Tk()
window.resizable(width=False, height=False)
window.title("Password and Username Required")
window.geometry("300x160+450+240")
window.resizable(0,0)
name=Label(window,text="Enter Your MySql Username",font=('Gabriola',13,'bold')).place(x=65,y=5)
e_name=Entry(window,bd=4)
e_name.place(x=89,y=35)
password=Label(window,text="Enter Your MySql Password",font=('Gabriola',13,'bold')).place(x=65,y=65)
e1=Entry(window,bd=4,show='*')
e1.place(x=89,y=95)
def check():
    mydb = mysql.connector.connect(host="127.0.0.1",
                                   port="3306",
                                   user=e_name.get(),
                                   password=e1.get(),
                                   auth_plugin="mysql_native_password")
    window.destroy()
def fun(a,b):
    if a=="(NULL)" and b=="(NULL)":
        builtins.pas = ''
        builtins.username=''
        check()      
    else:
        builtins.pas = a
        builtins.username= b
        check()
b=Button(window,text="Submit",command=lambda:fun(e1.get(),e_name.get()),bd=3,bg="orange",activeforeground="orange").place(x=125,y=125)
window.bind('<Return>',lambda x:fun(e1.get(),e_name.get()))
window.mainloop()
m = mysql.connector.connect(host='127.0.0.1',
                            user=username,
                            port='3306',
                            password=pas,
                            auth_plugin="mysql_native_password")
mc =m.cursor()
mc.execute('create database if not exists BloodBank')
mc.close()
mydb = mysql.connector.connect(host='127.0.0.1',
                               user=username,
                               port="3306",
                               password=pas,
                               auth_plugin="mysql_native_password",
                               database='BloodBank')
mc = mydb.cursor()
root=Tk()
root.title("BLOOD BANK")
root.geometry('1180x720')
root.title("Blood Bank Management System")
root.resizable(0,0)
root.configure(background='white')
load = Image.open('Background.png')
render = ImageTk.PhotoImage(load)
img = Label(image=render)
img.image = render
img.place(x=0,y=0)
width=1180
height=720
root.resizable(width=False, height=1920)
root.geometry("%sx%s"%(width, height))
l3=Label(root,text="BLOOD BANK SYSTEM",bg='#00CDCD',font = ('Bauhaus 93',20),fg='#A00000').place(x=450,y=200,w=300,h=40)
l1=Label(root,text="Click to enter the details of the donor :",bg='#00CDCD',font="Papyrus 12 bold").place(x=300,y=300,w=300,h=40)
b1=Button(root,text="Donor Details",command=lambda : donor(),bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=650,y=310)
l3=Label(root,text="Click to make a request for blood :",bg='#00CDCD',font="Papyrus 12 bold").place(x=300,y=350,w=300,h=40)
b3=Button(root,text="Request Blood",command=lambda : requestblood(),bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=650,y=350)

l3=Label(root,text="Click to see the donor List :",bg='#00CDCD',font="Papyrus 12 bold").place(x=300,y=400,w=300,h=40)
b3=Button(root,text="Donor List",command=lambda : donor_list(),bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=650,y=400)

l4=Label(root,text="Click to see the blood details :",bg='#00CDCD',font="Papyrus 12 bold").place(x=300,y=450,w=300,h=40)
b4=Button(root,text="Blood Details",command=lambda : blood(),bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=650,y=450)

l5=Label(root,text="Click to see the donation :",bg='#00CDCD',font="Papyrus 12 bold").place(x=300,y=500,w=300,h=40)
b5=Button(root,text="Donation",command=lambda : blood_donor(),bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=650,y=500)

l5=Label(root,text="Donor who donated or not :",bg='#00CDCD',font="Papyrus 12 bold").place(x=300,y=550,w=300,h=40)
b5=Button(root,text="Donated or not",command=lambda : donated_not(),bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=650,y=550)

b2=Button(root,text="Exit",command=lambda : stop(root),padx=11,pady=4,bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=400,y=600)
b4=Button(root,text="Help",command=lambda : HELP(),padx=11,pady=4,bg='#FAF0E6',font=("Lucida Calligraphy",10,'bold')).place(x=700,y=600)
v = StringVar()

def donated_not():
    dark=Toplevel()
    dark.title("Result")
    dark.configure(background='#c21d1d')
    dark.resizable(0,0)
    cmd=("SELECT * FROM donor LEFT JOIN blood ON donor.Donor_ID=blood.Donor_ID;")

    mc.execute(cmd)
    donors = mc.fetchall()
    a=1

    for row in donors:
        l_DonorId=Label(dark,text="Id",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_DonorId.grid(row=0,column=0,padx=15,pady=8)
        l_name=Label(dark,text="Name",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_name.grid(row=0,column=1,padx=15,pady=8)
        l_age=Label(dark,text="Age",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_age.grid(row=0,column=2,padx=15,pady=8)
        l_DOB=Label(dark,text="Gender",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_DOB.grid(row=0,column=3,padx=15,pady=8)
        l_gender=Label(dark,text="Date Of Birth",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_gender.grid(row=0,column=4,padx=15,pady=8)
        l_con=Label(dark,text="Contact No",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_con.grid(row=0,column=5,padx=15,pady=8)
        l_email=Label(dark,text="Email",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_email.grid(row=0,column=6,padx=15,pady=8)
        l_blood=Label(dark,text="Blood Group",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_blood.grid(row=0,column=7,padx=15,pady=8)
        l_address=Label(dark,text="Address",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_address.grid(row=0,column=8,padx=15,pady=8)

        l_bb=Label(dark,text="Bloodbag_number",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_bb.grid(row=0,column=9,padx=15,pady=8)

        
        l_bb=Label(dark,text="Donor_ID",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_bb.grid(row=0,column=10,padx=15,pady=8)
        
        
        l_hc=Label(dark,text="HEAMOGLOBIN_CONTENT",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_hc.grid(row=0,column=11,padx=15,pady=8)

        l_ba=Label(dark,text="Blood_Amount",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_ba.grid(row=0,column=12,padx=15,pady=8)

        l_bc=Label(dark,text="Blood_Group",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_bc.grid(row=0,column=13,padx=15,pady=8)

        l_c=Label(dark,text="Cost",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_c.grid(row=0,column=14,padx=15,pady=8)


        l0=Label(dark,text=row[0],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l0.grid(row=a,column=0,padx=13,pady=8)
        l1=Label(dark,text=row[1],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l1.grid(row=a,column=1,padx=13,pady=8)
        l2=Label(dark,text=row[2],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l2.grid(row=a,column=2,padx=13,pady=8)
        l3=Label(dark,text=row[3],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l3.grid(row=a,column=3,padx=13,pady=8)
        l4=Label(dark,text=row[4],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l4.grid(row=a,column=4,padx=13,pady=8)
        l5=Label(dark,text=row[5],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l5.grid(row=a,column=5,padx=13,pady=8)
        l6=Label(dark,text=row[6],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l6.grid(row=a,column=6,padx=13,pady=8)
        l7=Label(dark,text=row[7],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l7.grid(row=a,column=7,padx=10,pady=8)
        add=(row[8]+"  ,  "+row[9]+"  ,  "+row[10]+"  ,  "+row[11])
        l8=Label(dark,text=add,bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l8.grid(row=a,column=8,padx=13,pady=8)

        l9=Label(dark,text=row[12],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l9.grid(row=a,column=9,padx=10,pady=8)

        l10=Label(dark,text=row[13],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l10.grid(row=a,column=10,padx=10,pady=8)

        l11=Label(dark,text=row[14],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l11.grid(row=a,column=11,padx=10,pady=8)

        
        l12=Label(dark,text=row[15],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l12.grid(row=a,column=12,padx=10,pady=8)
                
        l13=Label(dark,text=row[16],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l13.grid(row=a,column=13,padx=10,pady=8)
        
        l14=Label(dark,text=row[17],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l14.grid(row=a,column=14,padx=10,pady=8)


        
   
        
        a += 1

def blood_donor():
    dark=Toplevel()
    dark.title("Result")
    dark.configure(background='#c21d1d')
    dark.resizable(0,0)
    cmd=("SELECT * FROM donor INNER JOIN blood ON donor.Donor_ID=blood.Donor_ID;")

    mc.execute(cmd)
    donors = mc.fetchall()
    a=1

    for row in donors:
        l_DonorId=Label(dark,text="Id",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_DonorId.grid(row=0,column=0,padx=15,pady=8)
        l_name=Label(dark,text="Name",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_name.grid(row=0,column=1,padx=15,pady=8)
        l_age=Label(dark,text="Age",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_age.grid(row=0,column=2,padx=15,pady=8)
        l_DOB=Label(dark,text="Gender",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_DOB.grid(row=0,column=3,padx=15,pady=8)
        l_gender=Label(dark,text="Date Of Birth",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_gender.grid(row=0,column=4,padx=15,pady=8)
        l_con=Label(dark,text="Contact No",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_con.grid(row=0,column=5,padx=15,pady=8)
        l_email=Label(dark,text="Email",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_email.grid(row=0,column=6,padx=15,pady=8)
        l_blood=Label(dark,text="Blood Group",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_blood.grid(row=0,column=7,padx=15,pady=8)
        l_address=Label(dark,text="Address",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_address.grid(row=0,column=8,padx=15,pady=8)

        l_bb=Label(dark,text="Bloodbag_number",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_bb.grid(row=0,column=9,padx=15,pady=8)

        
        l_bb=Label(dark,text="Donor_ID",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_bb.grid(row=0,column=10,padx=15,pady=8)
        
        
        l_hc=Label(dark,text="HEAMOGLOBIN_CONTENT",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_hc.grid(row=0,column=11,padx=15,pady=8)

        l_ba=Label(dark,text="Blood_Amount",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_ba.grid(row=0,column=12,padx=15,pady=8)

        l_bc=Label(dark,text="Blood_Group",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_bc.grid(row=0,column=13,padx=15,pady=8)

        l_c=Label(dark,text="Cost",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
        l_c.grid(row=0,column=14,padx=15,pady=8)


        l0=Label(dark,text=row[0],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l0.grid(row=a,column=0,padx=13,pady=8)
        l1=Label(dark,text=row[1],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l1.grid(row=a,column=1,padx=13,pady=8)
        l2=Label(dark,text=row[2],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l2.grid(row=a,column=2,padx=13,pady=8)
        l3=Label(dark,text=row[3],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l3.grid(row=a,column=3,padx=13,pady=8)
        l4=Label(dark,text=row[4],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l4.grid(row=a,column=4,padx=13,pady=8)
        l5=Label(dark,text=row[5],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l5.grid(row=a,column=5,padx=13,pady=8)
        l6=Label(dark,text=row[6],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l6.grid(row=a,column=6,padx=13,pady=8)
        l7=Label(dark,text=row[7],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l7.grid(row=a,column=7,padx=10,pady=8)
        add=(row[8]+"  ,  "+row[9]+"  ,  "+row[10]+"  ,  "+row[11])
        l8=Label(dark,text=add,bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l8.grid(row=a,column=8,padx=13,pady=8)

        l9=Label(dark,text=row[12],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l9.grid(row=a,column=9,padx=10,pady=8)

        l10=Label(dark,text=row[13],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l10.grid(row=a,column=10,padx=10,pady=8)

        l11=Label(dark,text=row[14],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l11.grid(row=a,column=11,padx=10,pady=8)

        
        l12=Label(dark,text=row[15],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l12.grid(row=a,column=12,padx=10,pady=8)
                
        l13=Label(dark,text=row[16],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l13.grid(row=a,column=13,padx=10,pady=8)
        
        l14=Label(dark,text=row[17],bg="#c21d1d",font=("Segoe Print",10,'bold'))
        l14.grid(row=a,column=14,padx=10,pady=8)


        
   
        
        a += 1

def donor_list():
    dark=Toplevel()
    dark.title("Result")
    dark.configure(background='#c21d1d')
    dark.resizable(0,0)
    cmd=("select * from donor")

    mc.execute(cmd)
    donors = mc.fetchall()
    a=1
    print(donors)
    for row in donors:
                l_DonorId=Label(dark,text="Id",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_DonorId.grid(row=0,column=0,padx=15,pady=8)
                l_name=Label(dark,text="Name",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_name.grid(row=0,column=1,padx=15,pady=8)
                l_age=Label(dark,text="Age",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_age.grid(row=0,column=2,padx=15,pady=8)
                l_DOB=Label(dark,text="Gender",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_DOB.grid(row=0,column=3,padx=15,pady=8)
                l_gender=Label(dark,text="Date Of Birth",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_gender.grid(row=0,column=4,padx=15,pady=8)
                l_con=Label(dark,text="Contact No",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_con.grid(row=0,column=5,padx=15,pady=8)
                l_email=Label(dark,text="Email",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_email.grid(row=0,column=6,padx=15,pady=8)
                l_blood=Label(dark,text="Blood Group",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_blood.grid(row=0,column=7,padx=15,pady=8)
                l_address=Label(dark,text="Address",bg="#c21d1d",font=("Kristen ITC",12,'bold'))
                l_address.grid(row=0,column=8,padx=15,pady=8)

                l0=Label(dark,text=row[0],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l0.grid(row=a,column=0,padx=13,pady=8)
                l1=Label(dark,text=row[1],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l1.grid(row=a,column=1,padx=13,pady=8)
                l2=Label(dark,text=row[2],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l2.grid(row=a,column=2,padx=13,pady=8)
                l3=Label(dark,text=row[3],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l3.grid(row=a,column=3,padx=13,pady=8)
                l4=Label(dark,text=row[4],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l4.grid(row=a,column=4,padx=13,pady=8)
                l5=Label(dark,text=row[5],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l5.grid(row=a,column=5,padx=13,pady=8)
                l6=Label(dark,text=row[6],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l6.grid(row=a,column=6,padx=13,pady=8)
                l7=Label(dark,text=row[7],bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l7.grid(row=a,column=7,padx=10,pady=8)
                add=(row[8]+"  ,  "+row[9]+"  ,  "+row[10]+"  ,  "+row[11])
                l8=Label(dark,text=add,bg="#c21d1d",font=("Segoe Print",10,'bold'))
                l8.grid(row=a,column=8,padx=13,pady=8)
                a += 1
            


def HELP():
    Help=Tk()
    Help.title("HELP")
    Help.resizable(0,0)
    f=open("help.txt",'r')
    txt=f.read()
    f.close()
    label=Label(Help,text=txt,
                font='Chiller 25 bold',bg="#ff7f50",
                fg="#5B0E2D",anchor='w',justify=LEFT)
    label.grid(row=0,column=0,sticky=W)
def stop(*a):
    for i in range(len(a)):
        a[i].destroy()
        i=i+1
def tables():
    cmd=("CREATE TABLE IF NOT EXISTS receiver(Name varchar(50) NOT NULL,Blood_group char(4),Contact_No char(10) NOT NULL)")
    mc.execute(cmd)
    mydb.commit()
    cmd=("""CREATE TABLE IF NOT EXISTS donor(   Donor_ID int not null auto_increment,
                                                Name varchar(50) NOT NULL,
                                                 Age int NOT NULL, Gender char(10) NOT NULL,
                                                 Date_of_Birth char(20) NOT NULL,
                                                 Contact_no char(20) NOT NULL, Email varchar(50) NOT NULL,
                                                  Blood_Group varchar(10),Address varchar(50) NOT NULL,
                                                 City varchar(50) NOT NULL,
                                                 District varchar(50) NOT NULL,
                                                 State varchar(50) NOT NULL)""")
    mc.execute(cmd)
    mydb.commit()
tables()
def requestblood():
    master=Toplevel()
    master.geometry('600x350')
    master.title("Receiver Details")
    master.configure(background='#7fff7f')
    master.resizable(0,0)
    lab1=Label(master,text="Name:",bg="#7fff7f",font=("Monotype Corsiva",17, "bold")).place(x=80,y=40)
    entry_name=Entry(master,width=50,fg='#003366',borderwidth=5)
    entry_name.place(x=205,y=40,height=30)
    lab2=Label(master,text="Contact No:",bg="#7fff7f",font=("Monotype Corsiva",15, "bold")).place(x=80,y=90)
    entry_contact=Entry(master,width=50,fg='#003366',borderwidth=5)
    entry_contact.place(x=205,y=90,height=30)
    lab3=Label(master,text="Blood Group:",bg="#7fff7f",font=("Monotype Corsiva",15, "bold")).place(x=80,y=140)
    variable = StringVar(master)
    Blood_Group=['A+','A-','B+','B-','O+','O-','AB+','AB-']
    variable.set(Blood_Group[0])
    q=OptionMenu(master,variable,'A+','A-','B+','B-','O+','O-','AB+','AB-')
    q.config(bg='#7fff7f',fg="black",font=("Verdana",10, "bold italic"))
    q.place(x=220,y=140)
    b_submit=Button(master,text="Search",command=lambda:Submit_Details(),bd=3,bg="#F5FFFA",activeforeground="#7fff7f",font=("Lucida Calligraphy",10,'bold'),padx=10,pady=5).place(x=200,y=210)
    b_submit=Button(master,text="Back",command=lambda:stop(master),bd=3,bg="#F5FFFA",activeforeground="#7fff7f",font=("Lucida Calligraphy",10,'bold'),padx=10,pady=5).place(x=350,y=210)
    def Submit_Details():
        def receiver():
            cmd=("INSERT INTO receiver values(%s,%s,%s)")
            val=[entry_name.get(),variable.get(),entry_contact.get(),]
            mc.execute(cmd,val)
            mydb.commit()
        def search():
            cmd=("select * from donor where Blood_Group=%s")
            val=[variable.get()]
            mc.execute(cmd,val) 
            records = mc.fetchall()
            dark=Toplevel()
            dark.title("Result")
            dark.configure(background='#EFFD5F')
            dark.resizable(0,0)
            a=1
            for row in records:
                l_DonorId=Label(dark,text="Id",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_DonorId.grid(row=0,column=0,padx=15,pady=8)
                l_name=Label(dark,text="Name",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_name.grid(row=0,column=1,padx=15,pady=8)
                l_age=Label(dark,text="Age",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_age.grid(row=0,column=2,padx=15,pady=8)
                l_DOB=Label(dark,text="Gender",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_DOB.grid(row=0,column=3,padx=15,pady=8)
                l_gender=Label(dark,text="Date Of Birth",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_gender.grid(row=0,column=4,padx=15,pady=8)
                l_con=Label(dark,text="Contact No",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_con.grid(row=0,column=5,padx=15,pady=8)
                l_email=Label(dark,text="Email",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_email.grid(row=0,column=6,padx=15,pady=8)
                l_blood=Label(dark,text="Blood Group",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_blood.grid(row=0,column=7,padx=15,pady=8)
                l_address=Label(dark,text="Address",bg="#EFFD5F",font=("Kristen ITC",12,'bold'))
                l_address.grid(row=0,column=8,padx=15,pady=8)

                l0=Label(dark,text=row[0],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l0.grid(row=a,column=0,padx=13,pady=8)
                l1=Label(dark,text=row[1],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l1.grid(row=a,column=1,padx=13,pady=8)
                l2=Label(dark,text=row[2],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l2.grid(row=a,column=2,padx=13,pady=8)
                l3=Label(dark,text=row[3],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l3.grid(row=a,column=3,padx=13,pady=8)
                l4=Label(dark,text=row[4],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l4.grid(row=a,column=4,padx=13,pady=8)
                l5=Label(dark,text=row[5],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l5.grid(row=a,column=5,padx=13,pady=8)
                l6=Label(dark,text=row[6],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l6.grid(row=a,column=6,padx=13,pady=8)
                l7=Label(dark,text=row[7],bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l7.grid(row=a,column=7,padx=10,pady=8)
                add=(row[8]+"  ,  "+row[9]+"  ,  "+row[10]+"  ,  "+row[11])
                l8=Label(dark,text=add,bg="#EFFD5F",font=("Segoe Print",10,'bold'))
                l8.grid(row=a,column=8,padx=13,pady=8)
                a=a+1

        
        if entry_name.get()=='' or len(entry_contact.get())!=10 or variable.get()=='' :
            messagebox.showerror("BBMS", "Please Enter all details correctly!!!")
            stop(master)
            requestblood()
        else:
            receiver()
            res=messagebox.askquestion("BBMS", "Are you sure you want to Submit receiver details?")
            if res=='yes':
                search()
                stop(master)
            else:
                messagebox.showwarning("BBMS", "All the entered data will be cleared!!!")
                stop(master)
                requestblood()
    master.mainloop()
def donor():
    global r
    window= Toplevel()
    window.geometry('1000x700')
    window.configure(background='#ff3232')
    window.title("Donor Details")
    window.resizable(0,0)   
    lab0=Label(window,text="Id:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=10)
    entry_id=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_id.place(x=205,y=10,height=30)
    lab1=Label(window,text="Name:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=60)
    entry_name=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_name.place(x=205,y=60,height=30)
    lab2=Label(window,text="Age:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=100)
    entry_age=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_age.place(x=205,y=100,height=30)
    lab3=Label(window,text="Gender:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=150)
    r=StringVar()
    r1=Radiobutton(window,text="Male",bg="#ff3232",variable=r,value="Male",padx=20,pady=5,font=("Monotype Corsiva",12, "bold"))
    r1.place(x=200,y=160) 
    r2=Radiobutton(window,text="Female",variable=r,bg="#ff3232",value="Female",padx=20,pady=5,font=("Monotype Corsiva",12, "bold"))
    r2.place(x=200,y=185) 
    r3=Radiobutton(window,text="Others",variable=r,value="Others",bg="#ff3232",padx=20,pady=5,font=("Monotype Corsiva",12, "bold"))
    r3.place(x=200,y=215)
    lab4=Label(window,text="Contact No:",bg="#ff3232",font=("Monotype Corsiva",15, "bold")).place(x=550,y=40)
    entry_contact=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_contact.place(x=650,y=40,height=30)
    lab5=Label(window,text="Address:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=330)
    entry_address=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_address.place(x=205,y=330,height=30)
    lab6=Label(window,text="City",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=390)
    entry_city=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_city.place(x=205,y=390,height=30)
    lab7=Label(window,text="District",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=550,y=330)
    entry_district=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_district.place(x=650,y=330,height=30)
    lab9=Label(window,text="State",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=550,y=390)
    entry_state=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_state.place(x=650,y=390,height=30)
    variable = StringVar(window)
    Blood_Group=['A+','A-','B+','B-','O+','O-','AB+','AB-']
    variable.set(Blood_Group[0])
    w=OptionMenu(window,variable,'A+','A-','B+','B-','O+','O-','AB+','AB-')
    w.config(bg='#ff3232',fg="black",font=("Verdana",10, "bold"))
    w.place(x=700,y=180)
    lab10=Label(window,text="Blood Group :",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=550,y=180)
    lab8=Label(window,text="Email:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=550,y=100)
    entry_email=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_email.place(x=650,y=100,height=30)
    lab11=Label(window,text="Date Of Birth:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=550,y=230)
    frame=Frame(window,width=200,height=25,relief=SUNKEN,bd=4,bg='white')
    frame.place(x=700,y=230)
    cal=DateEntry(frame,date_pattern="yyyy/mm/dd",width=12, background='darkblue',
                    foreground='white', borderwidth=4,Calendar=2020)
    cal.pack()
    def insertdonor():
        no=len(str(entry_contact.get()))
        if entry_name.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif entry_age.get()==None:
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif r.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif cal.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif no!=10:
            messagebox.showerror("BBMS", "Invalid phone number!!!Try Again!!!")
            stop(window)
            donor()    
        elif entry_email.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif variable.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
                
        elif entry_address.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif entry_city.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif entry_district.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        elif entry_state.get()=="" :
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            donor()
        else:    
            res=messagebox.askquestion("BBMS", "Are you sure you want to Submit?")
            if res=='yes':
                cmd=("INSERT INTO donor VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
                val=[entry_id.get(),entry_name.get(),entry_age.get(),
                     r.get(),
                     cal.get(),entry_contact.get(),
                     entry_email.get(),variable.get(),
                     entry_address.get(),entry_city.get(),
                     entry_district.get(),entry_state.get()]
                mc.execute(cmd,val)
                mydb.commit()
                window.destroy()
            else:
                messagebox.showwarning("BBMS", "All the entered data will be cleared!!!")
                donor()

    b_submit=Button(window,text="Submit",command=lambda:insertdonor(),bd=3,bg="#FFFAF0",activeforeground="#ff3232",font=("Lucida Calligraphy",12,'bold'),padx=12,pady=7).place(x=400,y=450)
    b_submit=Button(window,text="Back",command=lambda:stop(window),bd=3,bg="#FFFAF0",activeforeground="#ff3232",font=("Lucida Calligraphy",12,'bold'),padx=12,pady=7).place(x=600,y=450)
    window.mainloop()
def table1():
    cmd=("""CREATE TABLE IF NOT EXISTS blood(   Bloodbag_number int not null auto_increment,
    primary key (Bloodbag_number),
	Donor_ID int,
    foreign key(Donor_ID) References donor(Donor_ID),
	HEAMOGLOBIN_CONTENT int,
	Blood_Amount int,
	Blood_Group varchar(50),
	Cost int)""")
    mc.execute(cmd)
    mydb.commit()

table1()

def blood():
    
    window= Toplevel()
    window.geometry('1000x700')
    window.configure(background='#ff3232')
    window.title("Blood Details")
    window.resizable(0,0)   

    lab1=Label(window,text="Heamoglobin Content:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=60)
    entry_heamo=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_heamo.place(x=205,y=60,height=30)
    lab2=Label(window,text="Blood Amount",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=100)
    entry_bloodamount=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_bloodamount.place(x=205,y=100,height=30)
    lab4=Label(window,text="Cost:",bg="#ff3232",font=("Monotype Corsiva",15, "bold")).place(x=550,y=40)
    entry_cost=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_cost.place(x=650,y=40,height=30)
    lab5=Label(window,text="Donor ID:",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=80,y=330)
    entry_did=Entry(window,width=50,fg='#003366',borderwidth=5)
    entry_did.place(x=205,y=330,height=30)
    variable = StringVar(window)
    Blood_Group=['A+','A-','B+','B-','O+','O-','AB+','AB-']
    variable.set(Blood_Group[0])
    w=OptionMenu(window,variable,'A+','A-','B+','B-','O+','O-','AB+','AB-')
    w.config(bg='#ff3232',fg="black",font=("Verdana",10, "bold"))
    w.place(x=700,y=180)
    lab10=Label(window,text="Blood Group :",bg="#ff3232",font=("Monotype Corsiva",17, "bold")).place(x=550,y=180)
    cmd=("select Donor_ID from donor")

    mc.execute(cmd)
    donor_id = mc.fetchall()
    print(donor_id)
    for i in donor_id:
        print(i[0])
    
    def insertblood():
      
        
        if entry_heamo.get()==None:
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            blood()
    
        elif entry_bloodamount.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            blood()   
        elif entry_cost.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            blood()
        elif variable.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            blood()
                
        elif entry_did.get()=="":
            messagebox.showerror("BBMS", "Please Enter all details!!!Try Again!!!")
            stop(window)
            blood()
        
        else:    
            res=messagebox.askquestion("BBMS", "Are you sure you want to Submit?")
            if res=='yes':
                cmd=("INSERT INTO blood(Donor_ID, HEAMOGLOBIN_CONTENT, Blood_Amount, Blood_Group, Cost) VALUES(%s,%s,%s,%s,%s)")
                val=[entry_did.get(),entry_heamo.get(),
                entry_bloodamount.get(),variable.get(),
                    entry_cost.get()
                     
                     ]
            
                mc.execute(cmd,val)
                mydb.commit()
                window.destroy()
            else:
                messagebox.showwarning("BBMS", "All the entered data will be cleared!!!")
                blood()
    b_submit=Button(window,text="Submit",command=lambda:insertblood(),bd=3,bg="#FFFAF0",activeforeground="#ff3232",font=("Lucida Calligraphy",12,'bold'),padx=12,pady=7).place(x=400,y=450)
    b_submit=Button(window,text="Back",command=lambda:stop(window),bd=3,bg="#FFFAF0",activeforeground="#ff3232",font=("Lucida Calligraphy",12,'bold'),padx=12,pady=7).place(x=600,y=450)
    window.mainloop()



root.mainloop()
    
    
    
    
    
    


 








	
    



