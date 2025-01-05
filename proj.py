
from tkinter import *
from tkinter.messagebox import*
from tkinter.scrolledtext import *
from sqlite3 import*
import requests 
import matplotlib.pyplot as plt

#=============================Functions==============================

def f1():
    mw.withdraw()
    aw.deiconify()

def f2():
    aw.withdraw()
    mw.deiconify()

def f3():
    mw.withdraw()
    uw.deiconify()

def f4():
    uw.withdraw()
    mw.deiconify()

def f5():
    mw.withdraw()
    dw.deiconify()

def f6():
    dw.withdraw()
    mw.deiconify()

def f7():
    mw.withdraw()
    vw.deiconify()
    vw_st_data.delete(1.0,END)
    con = None
    try:
        con = connect("ems1.db")
        cursor = con.cursor()
        sql = "select * from emp"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info = info +"EMP ID: "+str(d[0])+"\nNAME: "+str(d[1])+"\nAge: "+str(d[2])+"\nPhone NO: "+str(d[3])+"\nSalary: "+str(d[4])+"\n******************************"
        vw_st_data.insert(INSERT,info)
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()

def f8():
    vw.withdraw()
    mw.deiconify()

def add():
    sp = "!@#$%^&*()_+-{}|[]:;'<>/."
    con = None
    try:
        con = connect("ems1.db")
        cursor = con.cursor()
        sql = "insert into emp values('%d','%s','%d','%d','%d')"
        try:
            eid = int(aw_e_id.get())
            if eid<1:
                raise Exception("Id should not be 0 or negative")
        except ValueError:
            showerror("Issue","Invalid ID!")
        except Exception as e:
            showerror("Issue",e)      
            return  
        try:
            name = aw_e_nme.get()
            if len(name)<2:
                raise Exception("Invalid Name")
            for i in name:
                if i.isnumeric():
                    raise Exception("Name should be only contain alphabates")
                elif i in sp:
                    raise Exception("Name should not contain Special Characters")
        except Exception as e:
            showerror("Issue",e)   
            return
        try:
            age = int(aw_e_age.get())
            if age<18:
                raise Exception("Employee is below 18 years ")
            elif age>65:
                raise Exception("Employee is too old ")
        except ValueError:
            showerror("Issue","Invalid Age")
        except Exception as e:
            showerror("Issue",e)
            return
        try:
            phn = int(aw_e_phn.get())
            if len(str(phn))<10:
                raise Exception("Phone Nuber must be of 10 digits")
            elif len(str(phn))>11:
                raise Exception("Phone Nuber must be of 10 digits")
        except ValueError:
            showerror("Issue","Invalid Phone Number")
        except Exception as e:
            showerror("Issue",e)
            return
        try:
            sal = int(aw_e_sal.get())
            if sal<8000:
                raise Exception("Salary must be more than 8K")
        except ValueError:
            showerror("Issue","Invalid Salary")
        except Exception as e:
            showerror("Issue",e)
            return
        cursor.execute(sql %(eid,name,age,phn,sal))
        con.commit()
        showinfo("Sucess","Information Saved")
    except Exception as e:
        if type(e).__name__ == "IntegrityError":
            showerror("Issue","Id is already Preesent")
        else:
            showerror("Issue",e)
    finally:
        if con is not None:
            con.close()
        aw_e_id.delete(0,END)
        aw_e_nme.delete(0,END)
        aw_e_age.delete(0,END)
        aw_e_phn.delete(0,END)
        aw_e_sal.delete(0,END)
        aw_e_id.focus() 

        
def update():
    sp = "!@#$%^&*()_+-{}|[]:;'<>/."
    con = None
    try:
        con = connect("ems1.db")
        cursor = con.cursor()
        sql = "update emp set name = '%s',age = '%d',phn = '%d',sal = '%d' where eid = '%d'"
        try:
            eid = int(uw_e_id.get())
            if eid<0:
                raise Exception("Id should not be 0 or negative")
        except ValueError:
            showerror("Issue","Invalid ID!")
        except Exception as e:
            showerror("Issue",e)
            return
        
        try:
            name = uw_e_nme.get()
            if len(name)<2:
                raise Exception("Invalid Name")
            for i in name:
                if i.isnumeric():
                    raise Exception("Name should be only contain alphabates")
                elif i in sp:
                    raise Exception("Name should not contain Special Characters")
        except Exception as e:
            showerror("Issue",e)
            return
        try:
            age = int(uw_e_age.get())
            if age<18:
              raise Exception("Employee is below 18 years ")
            elif age>65:
              raise Exception("Employee is too old ")
           
        except ValueError:
            showerror("Issue","Invalid Age")
        except Exception as e:
            showerror("Issue",e)
            return
        try:
            phn = int(uw_e_phn.get())
            if len(str(phn))<10:
                raise Exception("Phone Nuber must be of 10 digits")
            elif len(str(phn))>11:
                raise Exception("Phone Nuber must be of 10 digits")
        except ValueError:
            showerror("Issue","Invalid Phone Number")
        except Exception as e:
            showerror("Issue",e)
            return
        try:
            sal = int(uw_e_sal.get())
            if sal<8000:
                raise Exception("Salary must be more than 8K")
        except ValueError:
            showerror("Issue","Invalid Salary")
        except Exception as e:
            showerror("Issue",e)
            return
        cursor.execute("select eid from emp where eid = ?",(eid,))
        r = cursor.fetchone()
        if r is None:
            raise Exception("Id does not Exist ")
        else:
            cursor.execute(sql %(name,age,phn,sal,eid))
            con.commit()
            showinfo("Success","Info Updated")
    except Exception as e:
        if type(e).__name__ == "IntegrityError":
            showerror("Issue","Id is already Preesent")
        else:
            showerror("Issue",e)
    finally:
        if con is not None:
            con.close()
        uw_e_id.delete(0,END)
        uw_e_nme.delete(0,END)
        uw_e_age.delete(0,END)
        uw_e_phn.delete(0,END)
        uw_e_sal.delete(0,END)
        uw_e_id.focus()

def dele():
    con = None
    try:
        con = connect("ems1.db")
        cursor = con.cursor()
        sql = "DELETE FROM emp WHERE eid = '%d'"
        try:
            eid = int(dw_e_id.get())
            cursor.execute("select eid from emp where eid = ?",(eid,))
            r = cursor.fetchone()
            if r is None:
              raise Exception("Id does not Exist")
            if eid<1:
             raise Exception("Id should not be 0 or negative")
            else:
                cursor.execute(sql %(eid))
                con.commit()
            showinfo("Success","Info Deleted")
        except ValueError:
            showerror("issue","Invalid ID")
        except Exception as e:
            showerror("Issue",e) 
            return 
    finally:
        if con is not None:
            con.close()
        dw_e_id.delete(0,END)
        dw_e_id.focus()


def chart():
    mw.withdraw()
    con = None
    try:
        con = connect("ems1.db")
        cursor = con.cursor()
        sql = "select name,sal from emp order by sal desc limit 6;"
        cursor.execute(sql)
        data = cursor.fetchall()
        con.commit()
        ids=[]
        sal=[]
        i,j=0,0
        try:
            if len(data)<5:
                raise Exception("Database is too less (Min 5 Employees)")
            while(i<5):
                ids.append(data[i][0])
                i+=1
            while(j<5):
                sal.append(data[j][1])
                j+=1
        except Exception as e:
            showerror("Issue",e)
            return
        try:
            plt.bar(ids,sal,color = ['blue','green','yellow','orange','red'])
            plt.xlabel("EMP Name")
            plt.ylabel("SALARY")
            plt.title("Performance chart")
            plt.show()
        except Exception as e:
            showerror("Issue",e)
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()
        mw.deiconify()



def close():
    if askyesno("Exit","Are you sure you want to exit? "):
        mw.destroy()

#==============================TEMP AND LOC===============================
try:
    wa="https://ipinfo.io/"
    res = requests.get(wa)
    data = res.json()
    city_name = data["city"]
    a1 = "https://api.openweathermap.org/data/2.5/weather"
    a2 = "?q="+city_name
    a3 = "&appid=" + "c6e315d09197cec231495138183954bd"
    a4 = "&units="+"metric"
    wa2 = a1+a2+a3+a4
    res1 = requests.get(wa2)
    data1 =  res1.json()
    tempr = data1["main"]["temp"]  
except Exception as e:
    showerror("Issue",e)

#=================================MAIN WINDOW=======================================
mw = Tk()
mw.title("Employee Management System")
mw.geometry("800x750+20+20")
mw.configure(bg="khaki")
f=("arial",20,"bold")
fo1 =("arial",20,"bold")
mw_button_add=Button(mw,text="ADD",font=f,bg="ivory",width=10,command=f1)
mw_button_update=Button(mw,text="UPDATE",font=f,bg="ivory",width=10,command=f3)
mw_button_delete=Button(mw,text="DELETE",font=f,bg="ivory",width=10,command=f5)
mw_button_view=Button(mw,text="VIEW",font=f,bg="ivory",width=10,command=f7)
mw_button_chart=Button(mw,text="CHART",font=f,bg="ivory",width=10,command=chart)
mw_loc_lab = Label(mw,text = "Location: "+city_name,font=fo1,bg="khaki")
mw_temp_lab = Label(mw,text = "Temperature:"+str(tempr)+"°C",font=fo1,bg="khaki")
mw_button_add.pack(pady=20)
mw_button_update.pack(pady=20)
mw_button_delete.pack(pady=20)
mw_button_view.pack(pady=20)
mw_button_chart.pack(pady=20)
mw_loc_lab.place(x=30,y=700)
mw_temp_lab.place(x=450,y=700)
mw.protocol("WM_DELETE_WINDOW",close)

#=============================ADD WINDOW==================================
aw = Toplevel(mw)
aw.title("Add Employees")
aw.geometry("800x750+20+20")
aw.configure(bg="khaki")
aw_id_lab = Label(aw,text="Employee ID: ",font=f,bg="khaki")
aw_e_id=Entry(aw,font = f)
aw_nme_lab = Label(aw,text="Name: ",font=f,bg="khaki")
aw_e_nme=Entry(aw,font = f)
aw_age_lab = Label(aw,text="Age: ",font=f,bg="khaki")
aw_e_age=Entry(aw,font = f)
aw_phn_lab = Label(aw,text="Phone No: ",font=f,bg="khaki")
aw_e_phn=Entry(aw,font = f)
aw_sal_lab = Label(aw,text="Salary: ",font=f,bg="khaki")
aw_e_sal=Entry(aw,font = f)
aw_bt_save = Button(aw,text="Save",font = f,bg="ivory",command=add)
aw_bt_back = Button(aw,text="Back",font = f,bg="ivory",command=f2)
aw_id_lab.pack(pady=10)
aw_e_id.pack(pady=10)
aw_nme_lab.pack(pady=10)
aw_e_nme.pack(pady=10)
aw_age_lab.pack(pady=10)
aw_e_age.pack(pady=10)
aw_phn_lab.pack(pady=10)
aw_e_phn.pack(pady=10)
aw_sal_lab.pack(pady=10)
aw_e_sal.pack(pady=10)
aw_bt_save.pack(pady=10)
aw_bt_back.pack(pady=10)
aw.protocol("WM_DELETE_WINDOW",close)
aw.withdraw()

#==============================UPDATE WINDOW=================================
uw = Toplevel(mw)
uw.title("Update Employees")
uw.geometry("800x750+20+20")
uw.configure(bg="khaki")
uw_id_lab = Label(uw,text="Employee ID: ",font=f,bg="khaki")
uw_e_id=Entry(uw,font = f)
uw_nme_lab = Label(uw,text="Name: ",font=f,bg="khaki")
uw_e_nme=Entry(uw,font = f)
uw_age_lab = Label(uw,text="Age: ",font=f,bg="khaki")
uw_e_age=Entry(uw,font = f)
uw_phn_lab = Label(uw,text="Phone No: ",font=f,bg="khaki")
uw_e_phn=Entry(uw,font = f)
uw_sal_lab = Label(uw,text="Salary: ",font=f,bg="khaki")
uw_e_sal=Entry(uw,font = f)
uw_bt_save = Button(uw,text="Save",font = f,bg="ivory",command=update)
uw_bt_back = Button(uw,text="Back",font = f,bg="ivory",command=f4)
uw_id_lab.pack(pady=10)
uw_e_id.pack(pady=10)
uw_nme_lab.pack(pady=10)
uw_e_nme.pack(pady=10)
uw_age_lab.pack(pady=10)
uw_e_age.pack(pady=10)
uw_phn_lab.pack(pady=10)
uw_e_phn.pack(pady=10)
uw_sal_lab.pack(pady=10)
uw_e_sal.pack(pady=10)
uw_bt_save.pack(pady=10)
uw_bt_back.pack(pady=10)
uw.protocol("WM_DELETE_WINDOW",close)
uw.withdraw()

#============================DELETE WINDOW=============================
dw = Toplevel(mw)
dw.title("Delete Employees")
dw.geometry("800x750+20+20")
dw.configure(bg="khaki")
dw_id_lab = Label(dw,text="Employee ID: ",font=f,bg="khaki")
dw_e_id=Entry(dw,font = f)
dw_bt_del = Button(dw,text="Delete",font = f,bg="ivory",command=dele)
dw_bt_back = Button(dw,text="Back",font = f,bg="ivory",command=f6)
dw_id_lab.pack(pady=20)
dw_e_id.pack(pady=20)
dw_bt_del.pack(pady=20)
dw_bt_back.pack(pady=20)
dw.protocol("WM_DELETE_WINDOW",close)
dw.withdraw()

#=============================VIEW WINDOW================================
vw = Toplevel(mw)
vw.title("View Employees")
vw.geometry("800x750+20+20")
vw.configure(bg="khaki")
vw_st_data = ScrolledText(vw, width=22, height=15, font=f)
vw_btn_back = Button(vw,text="Back", font=f, command=f8,bg="ivory")
vw_st_data.pack(pady=10)
vw_btn_back.pack(pady=10)
vw.protocol("WM_DELETE_WINDOW",close)
vw.withdraw()
    
mw.mainloop()