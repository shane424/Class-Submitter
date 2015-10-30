from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#driver = webdriver.Firefox()
#driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp')
#AutoItSetOption("WinTitleMatchMode",2)
#WinSetState(driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp'),"",SW_HIDE)

TITLE_FONT = ("Helvetica", 14, "bold")
terms = ["Spring 2015-16","Summer 2015-16","Fall 2016-17","Spring 2016-17",
         "Summer 2016-17","Fall 2017-18","Spring 2017-18"]
totalClasses = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
'''
class containName(username):
    user = username

class containPass(password):
    passw = password

class containTerm(term):
    term = term

class containNumbers(numbers):
    searchNumbers = numbers
'''

global user_name
global pass_word
global term_sem
global search_numbs


class theApplication(Tk):

    def __init__(self):
        Tk.__init__(self)
        

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self,width=50,height=50)
        container.grid(row=0,column=0)
        Grid.grid_rowconfigure(self,0, weight=1)
        Grid.grid_columnconfigure(self,0, weight=1)

        self.frames = {}
        for F in (Login, Term, SearchNumbers):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
            #container.grid_rowconfigure(0, weight=1)
            #container.grid_columnconfigure(0, weight=1)

        self.show_frame(Login)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]

        frame.tkraise()


class Login(Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        Frame.__init__(self, parent)

        label = Label(self, text="The Class Submitter", font=TITLE_FONT)
        label.grid()
        #Frame.grid()
       #Grid.grid_rowconfigure(self,0, weight=1)
        #Grid.grid_columnconfigure(self,0, weight=1)
        
        u = StringVar(self)
        p = StringVar(self)
        
        self.un = Label(self,text='Username(6+2)')
        self.un.grid(row=3,column=0)
        self.pw = Label(self,text='Password(6+2)')
        self.pw.grid(row=4,column=0)
        self.username = Entry(self,textvariable=u)
        self.username.grid(row=3,column=1,padx=15)
        self.password = Entry(self,textvariable=p)
        self.password.grid(row=4,column=1)
        
        #Login.passw = self.password.get()
        self.quitButton = Button(self,text='Quit', command=self.destroy)
        self.quitButton.grid(row=6,pady=10,ipadx=10,padx=15,sticky='SW',column=1)

        self.newsButton = Button(self,text='Submit', command=self.combineFunc)
        self.newsButton.grid(row=6,pady=10,padx=15,sticky='SE',column=1)

        #test= Button(self,text='thetesting',command=self.getPass)
        #test.pack()

    def combineFunc(self):
        self.getName()
        self.getPass()
        self.controller.show_frame(Term)

    def toTerm(self,controller):
        lambda: self.controller.show_frame(Term)

    def getName(self):
        print(self.username.get())
        global user_name
        user_name = self.username.get()        
        return self.username.get()
    def getPass(self):
        print(self.password.get())
        global pass_word
        pass_word = self.password.get()
        return self.password.get()

class Term(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Frame.configure(self,width=10,height=10)
        #Frame.grid_rowconfigure(0, weight=1)
        #Frame.grid_columnconfigure(0, weight=1)
        self.controller = controller
        label = Label(self, text="The Term Page", font=TITLE_FONT)
        label.grid()
        button = Button(self, text="Back",
                           command=lambda: controller.show_frame(Login))
        button.grid(row=6,column=0,ipadx=15,sticky='e',pady=23)
        self.newsButton = Button(self,text='Submit', command=self.combineFunc)
        self.newsButton.grid(row=6,column=2,pady=21,ipadx=8)
        variable = StringVar(self)
        variable.set(terms[0])
        self.w = OptionMenu(self, variable,*terms)
        self.w.grid(row=3,column=1)

    def combineFunc(self):
        self.getTerm() 
        self.controller.show_frame(SearchNumbers)
        
    def getTerm(self):
        global term_sem
        term_sem = self.w.cget('text')
        return self.w.cget('text')

class SearchNumbers(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        self.arrayOfEntries = []
        self.arrayOfLabels = []
        self.cur_value = 0
        self.count = 0
        self.controller = controller
        #self.frame = Frame(self)
        #self.frame.grid()
        label = Label(self, text="Your Call Numbers", font=TITLE_FONT)
        label.grid()
        button = Button(self, text="Back",
                           command=lambda: controller.show_frame(Term))
        button.grid(column=1,row=3,padx=10,ipadx=10)
        self.newsButton = Button(self,text='Submit', command=self.combineFunc)
        self.newsButton.grid(column=2,row=3,padx=50)
        
        variable = StringVar(self)
        variable.set(totalClasses[0])

        self.w = OptionMenu(self, variable,*totalClasses,command=self.optUpdate)
        self.w.grid(row=3)
        self.frame = Frame(self)
        self.frame.grid(row=4)
        Grid.rowconfigure(self.frame,2,weight=1)
        Grid.columnconfigure(self.frame,6,weight=1)




    def optUpdate(self,value):
        print("--------UPDATE--------")
        self.value = int(value)
        #self.first_frame = Frame(self)
        #self.first_frame.grid()
        print ('value: ' + str(self.value))
        print ('count: ' + str(self.count))
        print('currentValue: ' + str(self.cur_value))
        if(self.value >= 0):
            if(self.value != self.cur_value):
               # self.frame = Frame(self.first_frame)
                #self.frame.grid()

                if (self.cur_value < self.value):
                    for i in range(self.cur_value,self.value):
                        self.label = Label(self.frame, text='Call Number ' + str(i+1))
                        self.label.grid(row=i,column=0)
                        self.e = Entry(self.frame)
                        self.e.grid(row=i,column=1)
                        self.arrayOfEntries.append(self.e)
                        self.arrayOfLabels.append(self.label)
                        self.count += 1
                        
                elif(self.cur_value > self.value):
                    print('in Second elif')
                    print('cur_val: ')
                    print(self.cur_value)
                    print('value: ')
                    print(self.value)

                    for i in range(self.value,self.cur_value):
                        index = self.value
                        print('i: ')
                        print(i)
                  
                        self.arrayOfLabels[index].grid_forget()
                        del self.arrayOfLabels[index]
                        self.arrayOfEntries[index].grid_forget()
                        del self.arrayOfEntries[index]

        print('Exits If Statement')

        print(self.arrayOfEntries)
        print(self.arrayOfLabels)
        
        self.cur_value = self.value
        print('currentValueAfterIf: ' + str(self.cur_value))
        print ('afterIfcount: ' + str(self.count))
        #print('sizeOfFrameAfterIf: ' + str(len(self.frame.winfo_children())/2))
        print("--------ENDOFUPDATE--------")

    def combineFunc(self):
        self.getNumbs()
        doMagic()

    def getNumbs(self):
        value = int(self.w.cget('text'))
        print (value)
        arr = [None] * value
        for i in range(0,value):
            print (arr[i])
            arr[i] = self.e.get()
            print ('after arr[i] placed')
            print (arr[i])
        global search_nums
        search_nums = arr
        return arr
            
class doMagic():

    def __init__(self):
        #app.quit()
        #username = Login.getName()
        #password = Login.getPass()
        #term = Term.getTerm()
        #callNumbs = SearchNumbers.getNumbs()
        
        print (user_name)
        print (pass_word)
        print (term_sem)
        print (search_nums)

    #def info(self):
        #driver = webdriver.Firefox()
        #driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp')
        #time.sleep(3)
        #user = driver.find_element_by_name("Username")
        #passw = driver.find_element_by_name("Password")
        #user.send_keys(un.get())
        #passw.send_keys(pw.get())
        

if __name__ == "__main__":
    #root = Tk()
    app = theApplication()
    app.title('SUBMISSION')
    app.mainloop()
    doMagic()
