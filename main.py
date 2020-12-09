from tkinter import*
import sqlite3

#creating the main window
root=Tk()
root.configure(background="#6495ED")
root.title("Address book 1.1-Main window")
root.iconbitmap(r'icon.ico')
root.geometry('650x500')

#creating the database

connect=sqlite3.connect('address_book.db')
cursor=connect.cursor()

#creating a table
#cursor.execute(""" CREATE TABLE addresses (
                #first_name text,
                #last_name text,
                #address text,
                #city text,
                #state text,
                #zipcode integer
                #)""")



#functions


#creating a function for deleting a record


def delete():
    connect = sqlite3.connect('address_book.db')
    cursor = connect.cursor()
    cursor.execute("DELETE from addresses WHERE oid= "+ select_id.get() )

    select_id.delete(0,END)


    connect.commit()
    connect.close()

#creating submit function


def submit():
    connect = sqlite3.connect('address_book.db')
    cursor = connect.cursor()
    cursor.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
                   {
                       'f_name': f_name.get(),
                       'l_name': l_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get()
                   })


    connect.commit()
    connect.close()


    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#creating edit function

def edit():
    global root2
    root2=Toplevel()
    root2.configure(background="#6495ED")
    root2.title("Address book 1.1 - Editing")
    root2.iconbitmap(r'icon.ico')
    root2.geometry('400x300')

    connect = sqlite3.connect('address_book.db')
    cursor = connect.cursor()
    record_id=select_id.get()
    cursor.execute("SELECT* from addresses WHERE oid ="+ record_id)
    records = cursor.fetchall()

    connect.commit()
    connect.close()

    #creating same entry boxes and labels and buttons

    #creating save button
    save_button=Button(root2,text="Save",bg="#8B0000",fg="white",font=("mv boli",10),width=22,command=save)


    # creating labels for our gui
    f_name_label = Label(root2, text="Enter the First name ", bg="#6495ED", fg="white", font=("mv boli", 10))
    l_name_label = Label(root2, text="Enter the Last name ", bg="#6495ED", fg="white", font=("mv boli", 10))
    address_label = Label(root2, text="Enter the Adress", bg="#6495ED", fg="white", font=("mv boli", 10))
    city_label = Label(root2, text="Enter the City", bg="#6495ED", fg="white", font=("mv boli", 10))
    state_label = Label(root2, text="Enter the State", bg="#6495ED", fg="white", font=("mv boli", 10))
    zipcode_label = Label(root2, text="Enter the Zipcode", bg="#6495ED", fg="white", font=("mv boli", 10))

    global f_name
    global l_name
    global address
    global city
    global state
    global zipcode

    #creating entry boxes
    f_name = Entry(root2, width=30)
    l_name = Entry(root2, width=30)
    address = Entry(root2, width=30)
    city = Entry(root2, width=30)
    state = Entry(root2, width=30)
    zipcode = Entry(root2, width=30)

    for record in records:
        f_name.insert(0, record[0])
        l_name.insert(0, record[1])
        address.insert(0, record[2])
        city.insert(0, record[3])
        state.insert(0, record[4])
        zipcode.insert(0, record[5])

    #save button griding
    save_button.grid(column=1,row=7,columnspan=6,pady=10)

    # labels griding
    f_name_label.grid(column=0, row=1, sticky=W)
    l_name_label.grid(column=0, row=2, sticky=W)
    address_label.grid(column=0, row=3, sticky=W)
    city_label.grid(column=0, row=4, sticky=W)
    state_label.grid(column=0, row=5, sticky=W)
    zipcode_label.grid(column=0, row=6, sticky=W)

    # entry boxes griding

    f_name.grid(column=2, row=1, pady=10)
    l_name.grid(column=2, row=2, pady=10)
    address.grid(column=2, row=3, pady=10)
    city.grid(column=2, row=4, pady=10)
    state.grid(column=2, row=5, pady=10)
    zipcode.grid(column=2, row=6, pady=10)


#creating function for save button

def save():
    #global root2
    connect = sqlite3.connect('address_book.db')
    cursor = connect.cursor()
    record_id1=select_id.get()

    cursor.execute(""" UPDATE addresses SET 
                    first_name = :first,
                    last_name = :last ,
                    address = :address ,
                    city = :city ,
                    state = :state ,
                    zipcode = :zipcode
                    
                    WHERE oid = :oid""",
                   {'first':f_name.get(),
                    'last': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get(),
                    'oid': record_id1} )

    connect.commit()
    connect.close()
    root2.destroy()


#creating a function for display button


def display():
    connect = sqlite3.connect('address_book.db')
    cursor = connect.cursor()
    cursor.execute("SELECT*,oid from addresses")
    records=cursor.fetchall()
    print_records=""
    for record in records:
        print_records+= str(record[0]) + "  " + str(record[1]) +" \t "+ str(record[6]) +"\n"


    display_label=Label(root,text=print_records,font=("mv boli",15),bg="#6495ED",fg="white")
    display_label.grid(column=6,row=2,sticky=W,rowspan=6)

    connect.commit()
    connect.close()


#creating labels for our gui
f_name_label=Label(root,text="Enter the First name ", bg="#6495ED" , fg="white", font=("mv boli",10))
l_name_label=Label(root,text="Enter the Last name ", bg="#6495ED" , fg="white", font=("mv boli",10))
address_label=Label(root,text="Enter the Adress", bg="#6495ED" , fg="white", font=("mv boli",10))
city_label=Label(root,text="Enter the City", bg="#6495ED" , fg="white", font=("mv boli",10))
state_label=Label(root,text="Enter the State" , bg="#6495ED" , fg="white", font=("mv boli",10))
zipcode_label=Label(root,text="Enter the Zipcode", bg="#6495ED" , fg="white", font=("mv boli",10))
select_id_label=Label(root,text="Select ID",bg="#6495ED",fg="white",font=("mv boli",10))

#entry boxes

f_name=Entry(root, width=30)
l_name=Entry(root, width=30)
address=Entry(root, width=30)
city=Entry(root, width=30)
state=Entry(root, width=30)
zipcode=Entry(root, width=30)
select_id=Entry(root,width=30)

#buttons
submit_button=Button(root,text="Submit",bg="#8B0000",fg="white",font=("mv boli",10) , width=22,command=submit)
display_button=Button(root,text="Display Data", bg="#8B0000",fg="white",font=("mv boli",10,),width=22,command=display)
delete_record_button=Button(root,text="Delete",bg="#8B0000",fg="white",font=("mv boli",10),width=22,command=delete)
edit_record_button=Button(root,text="Edit or Update ",bg="#8B0000",fg="white",font=("mv boli",10),width=22,command=edit)
#griding

#button griding

submit_button.grid(column=2,row=8,columnspan=3,pady=10)
display_button.grid(column=2,row=9,columnspan=3,pady=10)
delete_record_button.grid(column=2,row=10,columnspan=3,pady=10)
edit_record_button.grid(column=2,row=11,columnspan=3,pady=10)

#labels griding
f_name_label.grid(column=0,row=1,sticky=W)
l_name_label.grid(column=0,row=2,sticky=W)
address_label.grid(column=0,row=3,sticky=W)
city_label.grid(column=0,row=4,sticky=W)
state_label.grid(column=0,row=5,sticky=W)
zipcode_label.grid(column=0,row=6,sticky=W)
select_id_label.grid(column=0,row=7,sticky=W)

#entry boxes griding

f_name.grid(column=2,row=1,pady=10)
l_name.grid(column=2,row=2,pady=10)
address.grid(column=2,row=3,pady=10)
city.grid(column=2,row=4,pady=10)
state.grid(column=2,row=5,pady=10)
zipcode.grid(column=2,row=6,pady=10)
select_id.grid(column=2,row=7,pady=10)


connect.commit()
connect.close()

root.mainloop()
