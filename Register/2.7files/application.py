from Tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
import datetime
import time
import sys

#driver = webdriver.Firefox()
#driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp')
#AutoItSetOption("WinTitleMatchMode",2)
#WinSetState(driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp'),"",SW_HIDE)

TITLE_FONT = ("Comic Sans", 18, "bold")
terms = ["Spring 2015-16","Summer 2015-16","Fall 2016-17","Spring 2016-17",
         "Summer 2016-17","Fall 2017-18","Spring 2017-18"]
totalClasses = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"]

#new_display = Display(visible=0,size=(800, 600))
#new_display.start()

global user_name
global pass_word
global term_sem
global search_numbs
global date_now
global time_now
global full_date

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

        u = StringVar(self)
        p = StringVar(self)
        d = StringVar(self)
        t = StringVar(self)
        self.cb = IntVar(self)
        
        self.un = Label(self,text='Username(6+2)')
        self.un.grid(row=3,column=0)
        self.pw = Label(self,text='Password(6+2)')
        self.pw.grid(row=4,column=0)
        self.the_date = Label(self,text='Date of class registration start (M/D/YYYY)')
        self.the_date.grid(row=5,column=0)
        self.the_time = Label(self,text='Time of class registration start (10:00)')
        self.the_time.grid(row=6,column=0)
        self.username = Entry(self,textvariable=u)
        self.username.grid(row=3,column=1,padx=15)
        self.password = Entry(self, show = '*', textvariable=p)
        self.password.grid(row=4,column=1)
        self.dateEntry = Entry(self,textvariable=d)
        self.dateEntry.grid(row=5,column=1)
        self.timeEntry = Entry(self,textvariable=t)
        self.timeEntry.grid(row=6,column=1)
        
        self.quitButton = Button(self,text='Quit', command=self.endIt)
        self.quitButton.grid(row=7,pady=10,ipadx=10,padx=15,sticky='SW',column=1)

        self.newsButton = Button(self,text='Submit', command=self.combineFunc)
        self.newsButton.grid(row=7,pady=10,padx=15,sticky='SE',column=1)

        self.amButton = Checkbutton(self,text='AM',variable=self.cb)
        self.amButton.grid(row=7,column=0)


    def combineFunc(self):
        self.getInfo()
        self.controller.show_frame(Term)

    def toTerm(self,controller):
        lambda: self.controller.show_frame(Term)

    def getInfo(self):
        global user_name
        global pass_word
        global date_now
        global time_now
        global full_date
        global time_now
        the_time = ""
        time_now = self.timeEntry.get()
        if(self.cb.get() != 1):
            self.convertTo24(time_now)
        else:
            time_now = datetime.datetime.strptime(time_now,"%H:%M").time()
        user_name = self.username.get()
        pass_word = self.password.get()
        date_now = datetime.datetime.strptime(self.dateEntry.get(),"%m/%d/%Y")
        date_now
        full_date = date_now.combine(date_now,time_now)
        return user_name,pass_word,date_now,time_now,full_date

    def endIt(self):
        self.controller.destroy()

    def convertTo24(self,number):
        global time_now
        firstnumbs = int(number[:2])
        ending = number[2:]
        newnumbs = 12 + firstnumbs
        retnumb = str(newnumbs) +ending
        time_now = datetime.datetime.strptime(retnumb,"%H:%M").time()
        return time_now
        
        
class Term(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        Frame.configure(self,width=10,height=10)
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
        self.value = int(value)
        if(self.value >= 0):
            if(self.value != self.cur_value):
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
                    for i in range(self.value,self.cur_value):
                        index = self.value
                  
                        self.arrayOfLabels[index].grid_forget()
                        del self.arrayOfLabels[index]
                        self.arrayOfEntries[index].grid_forget()
                        del self.arrayOfEntries[index]

        self.cur_value = self.value

    def combineFunc(self):
        self.getNumbs()
        doMagic()

    def getNumbs(self):
        value = int(self.w.cget('text'))
        arr = [None] * value
        for i in range(0,value):
            arr[i] = self.arrayOfEntries[i].get()
        global search_nums
        search_nums = arr
        return arr
            
class doMagic():

    def __init__(self):
        global user_name
        global pass_word
        global term_sem
        global search_nums
        print(user_name)
        print(pass_word)
        print(term_sem)
        print(search_nums)
        self.StartSelenium()

    def StartSelenium(self):
        regcheck = 0
        while regcheck == 0:
            now = datetime.datetime.now()
            if(now >= full_date):
                print(now)
                print(full_date)
                check = 0
                check_counter = 0
                driver = webdriver.Firefox()
                driver.get('https://ixpress-server2.uc.edu/Registration/Register.asp')
                time.sleep(3)
                user = driver.find_element_by_name("Username")
                passw = driver.find_element_by_name("Password")
                user.send_keys(user_name)
                passw.send_keys(pass_word)
                # Clicks log in
                log = driver.find_element_by_xpath("//input[@value='Log In']").click()
                # Hits register
                time.sleep(3)
                regbut = driver.find_element_by_xpath("//input[@value='Register']").click()
                # Finds drop down
                time.sleep(1)
                termcode = driver.find_element_by_name("TermCode")
                selection = Select(termcode.find_element_by_xpath("//select[@name='TermCode']"))
                # Clicks semester
                selection.select_by_visible_text(term_sem)
                conbut = driver.find_element_by_xpath("//input[@value='Continue']").click()
                # Writes numbers into search boxes
                count = 7
                for i in search_nums:
                    print (i)
                    inp = '//input[@name=\''
                    callnumb = 'CallNumber'
                    endBrack = '\']'
                    call = inp+callnumb+(str(count))+endBrack
                    numb1 = driver.find_element_by_xpath(call)
                    numb1.send_keys(i)
                    count += 1
                while check != 50:
                    sub = driver.find_element_by_xpath("//input[@value='Submit']").click()
                    time.sleep(7)
                    check += 1

                driver.close()
                regcheck = 1
            
		
if __name__ == "__main__":
    app = theApplication()
    app.title('SUBMISSION')
    app.mainloop()
