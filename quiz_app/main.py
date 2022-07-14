# QUIZ application using tkinter

#importing libraries
from tkinter import *
from PIL import Image, ImageTk

from tkinter import messagebox as mb

import json
import sqlite3

from matplotlib import image

####################################################################################################################

def loginPage(logindata):
    sup.destroy()
    global login
    login = Tk()
    login.title('PYTHON QUIZ')
    
    user_name = StringVar()
    password = StringVar()
    
    img = PhotoImage(file="bg3.png")
    
    login_canvas = Canvas(login,width=720,height=440)
    login_canvas.create_image(0,0,image=img,anchor=NW)
    login_canvas.pack()

    login_frame = Frame(login_canvas,bg="white")
    login_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(login_frame,text="Quiz App Login",fg="black",bg="white")
    heading.config(font=('Times New Roman',40))
    heading.place(relx=0.2,rely=0.1)

    #USER NAME
    ulabel = Label(login_frame,text="Username",fg='black',bg='white')
    ulabel.place(relx=0.21,rely=0.4)
    uname = Entry(login_frame,bg='#d3d3d3',fg='black',textvariable = user_name)
    uname.config(width=42)
    uname.place(relx=0.31,rely=0.4)

    #PASSWORD
    plabel = Label(login_frame,text="Password",fg='black',bg='white')
    plabel.place(relx=0.215,rely=0.5)
    pas = Entry(login_frame,bg='#d3d3d3',fg='black',show="*",textvariable = password)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.5)

    def check():
        for a,b,c in logindata:
            if b == uname.get() and c == pas.get():
                menu() 
                break
        else:
            error = Label(login_frame,text="Wrong Username or Password!",fg='black',bg='white')
            error.place(relx=0.37,rely=0.7)
    
    #LOGIN BUTTON
    log = Button(login_frame,text='Login !!!',padx=5,pady=5,width=5,bd='5',command=check)
    log.config(width = 15,height=1, bg='khaki')
    log.place(relx=0.4,rely=0.6)
    
    
    login.mainloop()
#####################################################################################################################
def signUpPage():
    root.destroy()
    global sup
    sup = Tk()
    sup.title('PYTHON QUIZ')
    
    fname = StringVar()
    uname = StringVar()
    passW = StringVar()
    
    
    img = PhotoImage(file="bg3.png")
    
    sup_canvas = Canvas(sup,width=720,height=440)
    sup_canvas.create_image(0,0,image=img,anchor=NW)
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas,bg="white")
    sup_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    heading = Label(sup_frame,text="SignUp To Start",fg="black",bg="white")
    heading.config(font=('Times New Roman',40))
    heading.place(relx=0.2,rely=0.1)

    #full name
    f_label = Label(sup_frame,text="Full Name ",fg='black',bg='white')
    f_label.place(relx=0.20,rely=0.4)
    f_name = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = fname)
    f_name.config(width=42)
    f_name.place(relx=0.31,rely=0.4)

    #username
    u_label = Label(sup_frame,text="Username ",fg='black',bg='white')
    u_label.place(relx=0.20,rely=0.5)
    user = Entry(sup_frame,bg='#d3d3d3',fg='black',textvariable = uname)
    user.config(width=42)
    user.place(relx=0.31,rely=0.5)
    
    
    #password
    plabel = Label(sup_frame,text="Password ",fg='black',bg='white')
    plabel.place(relx=0.21,rely=0.6)
    pas = Entry(sup_frame,bg='#d3d3d3',fg='black',show="*",textvariable = passW)
    pas.config(width=42)
    pas.place(relx=0.31,rely=0.6)
    
    
    
# defining database for signup
    def addUserToDataBase():
        
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        
        
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        create.execute('CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, USERNAME text,PASSWORD text)')
        create.execute("INSERT INTO userSignUp VALUES (?,?,?)",(fullname,username,password)) 
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        print(z)

        conn.close()
        loginPage(z)
    def gotoLogin():
        conn = sqlite3.connect('quiz.db')
        create = conn.cursor()
        conn.commit()
        create.execute('SELECT * FROM userSignUp')
        z=create.fetchall()
        loginPage(z)
    #signup BUTTON
    sp = Button(sup_frame,text='SignUp !!!',padx=5,pady=5,width=5, bd='7',command = addUserToDataBase,bg='khaki')
    sp.config(width = 15,height=1)
    sp.place(relx=0.4,rely=0.7)

    log = Button(sup_frame,text='Already have an Account?',padx=5,pady=5,width=5,command = gotoLogin,bg="white",fg='blue')
    log.config(width = 16,height=1, relief = FLAT)
    log.place(relx=0.4,rely=0.9)

    sup.mainloop()
##########################################################################################################################################

def menu():
    login.destroy()
    global menu 
    menu = Tk()
    menu.title('PYTHON QUIZ')
    
    img = PhotoImage(file="back5.png")

    menu_canvas = Canvas(menu,width=720,height=440,bg="blue")
    menu_canvas.create_image(0,0,image=img,anchor=NW)
    menu_canvas.pack()

    menu_frame = Frame(menu_canvas,bg="white")
    menu_frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

    my_img = ImageTk.PhotoImage(Image.open('logo.png'))
    my_label = Label( image= my_img,anchor= CENTER)
    my_label.place(x=120,y=60)

    wel = Label(menu_canvas,text=' W E L C O M E  T O  Q U I Z  S T A T I O N ',fg="white",bg="midnight blue") 
    wel.config(font=('Broadway 22'))
    wel.place(relx=0.1,rely=0.02)


    letsgo = Button(menu_frame,text="       Let's Go !        ",bg="gold2",font="calibri 12",width=20,height=1,bd='8',command=mainwindow)
    letsgo.place(relx=0.35,rely=0.85)
    menu.mainloop()



################################################################################################################################################
#defining class for quiz mainwindow
class Quiz:
	def __init__(self):
		
		# set question 
		self.q_no=0
		
		# assigns questions
		self.display_title()
		self.display_question()
		
		# selected otions
		self.opt_selected=IntVar()
		
		# options
		self.opts=self.radio_buttons()
		
		# display options for the current question
		self.display_options()
		
		# displays the button for next and exit.
		self.buttons()
		
		# no of questions
		self.data_size=len(question)
		self.correct=0


	# Result display using messagebox
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# function for checking answer
	def check_ans(self, q_no):		
		if self.opt_selected.get() == answer[q_no]:
			
			return True


	def next_btn(self):
		
		# Check if the answer is correct
		if self.check_ans(self.q_no):
			self.correct += 1
		self.q_no += 1
		
		# counting questions
		if self.q_no==self.data_size:
			self.display_result()
			gui.destroy()
		else:
			# shows the next question
			self.display_question()
			self.display_options()



	def buttons(self):
		
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(gui, text= "   Next  ",command=self.next_btn,width=10,bg="powder blue",fg="black",bd='5',font=("ariel",16,"bold"))
		next_button.place(x=350,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(gui, text=" Quit ", command=gui.destroy,width=5,fg="black", bg="white",font=("ariel",16," bold"))
		quit_button.place(x=700,y=50)



	def display_options(self):
		val=0
		
		# deselecting the options
		self.opt_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			val+=1


	# This method shows the current Question 
	def display_question(self):
		
		# Question
		q_no = Label(gui, text=question[self.q_no], width=60,font=( 'ariel' ,16, 'bold' ), anchor= 'w',bg='white',fg='black' )
		
		#placing the option 
		q_no.place(x=70, y=100)


	# This method is used to Display Title
	def display_title(self):
		
		
		title = Label(gui, text="PYTHON QUIZ",width=50, bg="misty rose",fg="black", font=("ariel", 20, "bold"))
		title.place(x=0, y=2)



	def radio_buttons(self):
		
		# initialize the list with an empty list of options
		q_list = []
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button
			radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,fg='black',bg='white',value = len(q_list)+1,font = ("ariel",14))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list

##############################################################################################################################################

def mainwindow():
# Create a GUI Window
    global question, options,answer
    menu.destroy()
    global gui
    gui = Tk()

    gui.geometry("800x450")

    gui.title("Python Quiz")
    gui.configure(bg='black')

# get the data from the json file
    with open('data.json') as f:
	    data = json.load(f)

# set the question, options, and answer
    question = (data['question'])
    options = (data['options'])
    answer = (data[ 'answer'])

    quiz = Quiz()
    gui.mainloop()

#############################################################################################################################################

def start():
    global root 
    root = Tk()
    root.title('PYTHON QUIZ')
    canvas = Canvas(root,width = 640,height = 360)
    canvas.grid(column = 0 , row = 1)
    img = PhotoImage(file="back4.png")
    canvas.create_image(0,0,image=img,anchor=NW)

    button = Button(root, text='START !!!',command = signUpPage) 
    button.config(width = 100,height=2,bd = '5', activebackground = "#33B5E5", bg ='black',fg='alice blue', relief = RAISED,font =("Arial", 10,'bold'))
    button.grid(column = 0 , row = 2)

    root.mainloop()


if __name__=='__main__':
    start()

############################################################################################################################

