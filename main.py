from functools import partial
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import custom as cs

class Management:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        self.window.geometry("780x480")
        self.window.config(bg="white")

        # Customization
        self.color_1 = cs.color_1
        self.color_2 = cs.color_2
        self.color_3 = cs.color_3
        self.color_4 = cs.color_4
        self.font_1 = cs.font_1
        self.font_2 = cs.font_2

        # Database connection
        self.conn = sqlite3.connect('student_management.db')
        self.c = self.conn.cursor()

        # Left Frame
        self.frame_1 = Frame(self.window, bg=self.color_1)
        self.frame_1.place(x=0, y=0, width=540, relheight=1)

        # Right Frame
        self.frame_2 = Frame(self.window, bg="black")
        self.frame_2.place(x=540, y=0, relwidth=1, relheight=1)

        # Buttons
        self.add_bt = Button(self.frame_2, text='Add New', font=(self.font_1, 12), bd=2, cursor="hand2", bg="grey", fg=self.color_3, command=self.AddStudent)
        self.add_bt.place(x=68, y=50, width=100)

        self.view_bt = Button(self.frame_2, text='View Details', font=(self.font_1, 12), bd=2, cursor="hand2", bg="grey", fg=self.color_3, command=self.GetContact_View)
        self.view_bt.place(x=68, y=120, width=100)

        self.update_bt = Button(self.frame_2, text='Update', font=(self.font_1, 12), bd=2, cursor="hand2", bg="grey", fg=self.color_3, command=self.GetContact_Update)
        self.update_bt.place(x=68, y=190, width=100)

        self.delete_bt = Button(self.frame_2, text='Delete', font=(self.font_1, 12), bd=2, cursor="hand2", bg="red", fg=self.color_3, command=self.GetContact_Delete)
        self.delete_bt.place(x=68, y=260, width=100)

        self.clear_bt = Button(self.frame_2, text='Clear', font=(self.font_1, 12), bd=2, cursor="hand2", bg="grey", fg=self.color_3, command=self.ClearScreen)
        self.clear_bt.place(x=68, y=330, width=100)

        self.exit_bt = Button(self.frame_2, text='Exit', font=(self.font_1, 12), bd=2, cursor="hand2", bg="grey", fg=self.color_3, command=self.Exit)
        self.exit_bt.place(x=68, y=400, width=100)

        # Widgets for adding student data
    def AddStudent(self):
        self.ClearScreen()

        self.name = Label(self.frame_1, text="First Name", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.name.place(x=40, y=30)
        self.name_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.name_entry.place(x=40, y=60, width=200)

        self.surname = Label(self.frame_1, text="Last Name", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.surname.place(x=300, y=30)
        self.surname_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.surname_entry.place(x=300, y=60, width=200)

        self.course = Label(self.frame_1, text="Degree", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.course.place(x=40, y=100)
        self.course_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.course_entry.place(x=40, y=130, width=200)

        self.subject = Label(self.frame_1, text="Subject", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.subject.place(x=300, y=100)
        self.subject_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.subject_entry.place(x=300, y=130, width=200)

        self.year = Label(self.frame_1, text="Session Year", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.year.place(x=40, y=170)
        self.year_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.year_entry.place(x=40, y=200, width=200)

        self.age = Label(self.frame_1, text="Age", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.age.place(x=300, y=170)
        self.age_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.age_entry.place(x=300, y=200, width=200)

        self.gender = Label(self.frame_1, text="Gender", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.gender.place(x=40, y=240)
        self.gender_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.gender_entry.place(x=40, y=270, width=200)

        self.birth = Label(self.frame_1, text="DOB", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.birth.place(x=300, y=240)
        self.birth_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.birth_entry.place(x=300, y=270, width=200)

        self.contact = Label(self.frame_1, text="Contact", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.contact.place(x=40, y=310)
        self.contact_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.contact_entry.place(x=40, y=340, width=200)

        self.email = Label(self.frame_1, text="Email", font=(self.font_2, 15, "bold"), bg=self.color_1)
        self.email.place(x=300, y=310)
        self.email_entry = Entry(self.frame_1, bg=self.color_4, fg=self.color_3)
        self.email_entry.place(x=300, y=340, width=200)

        self.submit_bt_1 = Button(self.frame_1, text='Submit', font=(self.font_1, 12), bd=2, command=self.Submit, cursor="hand2", bg="black", fg="white")
        self.submit_bt_1.place(x=200, y=389, width=100)

    '''Get the contact number to show a student details'''
    def GetContact_View(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Contact Number", font=(self.font_2, 18, "bold"), bg=self.color_1)
        self.getInfo.place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_2 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, command=self.CheckContact_View, cursor="hand2", bg="black", fg="white")
        self.submit_bt_2.place(x=220, y=150, width=80)

    '''To update a student details, get the contact number'''
    def GetContact_Update(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Contact Number", font=(self.font_2, 18, "bold"), bg=self.color_1)
        self.getInfo.place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_3 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, command=self.CheckContact_Update, cursor="hand2", bg="black", fg="white")
        self.submit_bt_3.place(x=220, y=150, width=80)

    '''To delete a student details, get the contact number'''
    def GetContact_Delete(self):
        self.ClearScreen()

        self.getInfo = Label(self.frame_1, text="Enter Contact Number", font=(self.font_2, 18, "bold"), bg=self.color_1)
        self.getInfo.place(x=140, y=70)
        self.getInfo_entry = Entry(self.frame_1, font=(self.font_1, 12), bg=self.color_4, fg=self.color_3)
        self.getInfo_entry.place(x=163, y=110, width=200, height=30)
        self.submit_bt_4 = Button(self.frame_1, text='Submit', font=(self.font_1, 10), bd=2, command=self.CheckContact_Delete, cursor="hand2", bg="black", fg="white")
        self.submit_bt_4.place(x=220, y=150, width=80)

    '''Clear screen'''
    def ClearScreen(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()

    '''Submit new student details to the database'''
    def Submit(self):
        first_name = self.name_entry.get()
        last_name = self.surname_entry.get()
        course = self.course_entry.get()
        subject = self.subject_entry.get()
        year = self.year_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        birthday = self.birth_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()

        self.c.execute("INSERT INTO students (first_name, last_name, course, subject, year, age, gender, birthday, contact, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (first_name, last_name, course, subject, year, age, gender, birthday, contact, email))
        self.conn.commit()
        messagebox.showinfo("Success", "Student details added successfully!")

    '''Check contact for viewing details'''
    def CheckContact_View(self):
        contact = self.getInfo_entry.get()
        self.c.execute("SELECT * FROM students WHERE contact=?", (contact,))
        student = self.c.fetchone()
        if student:
            self.ClearScreen()
            details = f"First Name: {student[1]}\nLast Name: {student[2]}\nCourse: {student[3]}\nSubject: {student[4]}\nYear: {student[5]}\nAge: {student[6]}\nGender: {student[7]}\nBirthday: {student[8]}\nContact: {student[9]}\nEmail: {student[10]}"
            details_label = Label(self.frame_1, text=details, font=(self.font_2, 15), bg=self.color_1, justify=LEFT)
            details_label.place(x=20, y=20)
        else:
            messagebox.showerror("Error", "No student found with this contact number!")

    '''Check contact for updating details'''
    def CheckContact_Update(self):
        contact = self.getInfo_entry.get()
        self.c.execute("SELECT * FROM students WHERE contact=?", (contact,))
        student = self.c.fetchone()
        if student:
            self.ClearScreen()
            self.AddStudent()

            self.name_entry.insert(0, student[1])
            self.surname_entry.insert(0, student[2])
            self.course_entry.insert(0, student[3])
            self.subject_entry.insert(0, student[4])
            self.year_entry.insert(0, student[5])
            self.age_entry.insert(0, student[6])
            self.gender_entry.insert(0, student[7])
            self.birth_entry.insert(0, student[8])
            self.contact_entry.insert(0, student[9])
            self.email_entry.insert(0, student[10])

            self.submit_bt_1.config(text='Update', command=lambda: self.UpdateStudent(student[0]))
        else:
            messagebox.showerror("Error", "No student found with this contact number!")

    '''Check contact for deleting details'''
    def CheckContact_Delete(self):
        contact = self.getInfo_entry.get()
        self.c.execute("SELECT * FROM students WHERE contact=?", (contact,))
        student = self.c.fetchone()
        if student:
            self.c.execute("DELETE FROM students WHERE contact=?", (contact,))
            self.conn.commit()
            messagebox.showinfo("Success", "Student details deleted successfully!")
        else:
            messagebox.showerror("Error", "No student found with this contact number!")

    '''Update student details'''
    def UpdateStudent(self, student_id):
        first_name = self.name_entry.get()
        last_name = self.surname_entry.get()
        course = self.course_entry.get()
        subject = self.subject_entry.get()
        year = self.year_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        birthday = self.birth_entry.get()
        contact = self.contact_entry.get()
        email = self.email_entry.get()

        self.c.execute("UPDATE students SET first_name=?, last_name=?, course=?, subject=?, year=?, age=?, gender=?, birthday=?, contact=?, email=? WHERE id=?",
                       (first_name, last_name, course, subject, year, age, gender, birthday, contact, email, student_id))
        self.conn.commit()
        messagebox.showinfo("Success", "Student details updated successfully!")

    '''Exit the application'''
    def Exit(self):
        self.conn.close()
        self.window.quit()

if __name__ == "__main__":
    root = Tk()
    app = Management(root)
    root.mainloop()
