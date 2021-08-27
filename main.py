import os
from tkinter import *
from tkinter import messagebox
import time
import os


class BankSoftware:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1522x790+0+0')
        self.root.title('@Yash Bank')
        title = Label(self.root, text='@Yash Bank', bd=5, relief=GROOVE,
                      font=('times new roman', 30, 'bold'), pady=2).pack(fill=X)

        self.AccountHolderDetails = []
        self.cash = 2000
        self.f2 = Frame()
        self.f3 = Frame()
        self.f4 = Frame()

        # ----------------------------------------------------------------------------------------------------------
        self.BTN1Variable = StringVar()
        self.BTN1Variable.set('')
        self.BTN2Variable = StringVar()
        self.BTN2Variable.set('')
        self.BTN3Variable = StringVar()
        self.BTN3Variable.set('')
        self.BTN4Variable = StringVar()
        self.BTN4Variable.set('')
        self.BTN5Variable = StringVar()
        self.BTN5Variable.set('')
        self.BTN6Variable = StringVar()
        self.BTN6Variable.set('')
        self.BTN7Variable = StringVar()
        self.BTN7Variable.set('')
        self.BTN8Variable = StringVar()
        self.BTN8Variable.set('')

        self.LABEL1Variable = StringVar()
        self.LABEL1Variable.set('')
        self.LABEL2Variable = StringVar()
        self.LABEL2Variable.set('')
        self.LABEL3Variable = StringVar()
        self.LABEL3Variable.set('')
        self.LABEL4Variable = StringVar()
        self.LABEL4Variable.set('')
        self.LABEL5Variable = StringVar()
        self.LABEL5Variable.set('')
        self.LABEL6Variable = StringVar()
        self.LABEL6Variable.set('')
        self.LABEL7Variable = StringVar()
        self.LABEL7Variable.set('')

        self.LABEL2ENTRY2Variable = StringVar()
        self.LABEL3ENTRY3Variable = StringVar()
        self.LABEL4ENTRY4Variable = StringVar()
        self.LABEL5ENTRY5Variable = StringVar()
        self.LABEL6ENTRY6Variable = StringVar()
        self.LABEL7ENTRY7Variable = StringVar()

        self.AccNoTXTVariable = StringVar()
        self.AccNoTXTVariable.set('')
        self.AccHolderNameTXTVariable = StringVar()
        self.AccHolderNameTXTVariable.set('')
        self.AccHolderPhoneNoTXTVariable = StringVar()
        self.AccHolderPhoneNoTXTVariable.set('')
        self.AccHolderUniqueIDTXTVariable = StringVar()
        self.AccHolderUniqueIDTXTVariable.set('')


        # ----------------------------------------------------------------------------------------------------------
        self.f1 = Frame(self.root, bd=5, relief=GROOVE)
        self.f1.place(x=10, y=65, width=300, height=720)

        self.AccHolderLoginBTN = Button(self.f1, text='Account Holder Login', font=('Agency FB', 20, 'bold'), bd=5,
                                        relief=RAISED, command=self.AccHolderLoginFRAME)
        self.AccHolderLoginBTN.place(x=20, y=20, width=250, height=50)

        #self.EmployeeLoginBTN = Button(self.f1, text='Bank Employee Login', font=('Agency FB', 20, 'bold'), bd=5,relief=RAISED)
        #self.EmployeeLoginBTN.place(x=20, y=90, width=250, height=50)

        self.CreateNewAccBTN = Button(self.f1, text='Create New Account', font=('Agency FB', 20, 'bold'), bd=5,
                                      relief=RAISED, command=self.CreateAccountFRAME)
        self.CreateNewAccBTN.place(x=20, y=160, width=250, height=50)

        self.____ = Button(self.f1, text='---------', font=('Agency FB', 20, 'bold'), bd=5,
                                       relief=RAISED)
        self.____.place(x=20, y=230, width=250, height=50)
        # ----------------------------------------------------------------------------------------------------------

    def CreateAccountFRAME(self):
        self.f2.destroy()
        self.f3.destroy()
        self.f4.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=100, width=880, height=535)

        self.LABEL1Variable.set('Creating New Account')
        self.LABEL2Variable.set('Enter Name')
        self.LABEL3Variable.set('Enter Phone Number')
        self.LABEL4Variable.set('Enter Password')
        self.LABEL5Variable.set('Enter your city')
        self.LABEL6Variable.set('Enter Unique ID')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL1.place(x=20, y=20, width=700, height=50)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL2.place(x=20, y=90, width=400, height=50)

        self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL3.place(x=20, y=160, width=400, height=50)

        self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL4.place(x=20, y=230, width=400, height=50)

        self.LABEL5 = Label(self.f3, text=self.LABEL5Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL5.place(x=20, y=300, width=400, height=50)

        self.LABEL6 = Label(self.f3, text=self.LABEL6Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL6.place(x=20, y=370, width=400, height=50)

        self.LABEL2ENTRY2 = Entry(self.f3, text=self.LABEL2ENTRY2Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL2ENTRY2.place(x=460, y=90, width=390, height=50)

        self.LABEL3ENTRY3 = Entry(self.f3, text=self.LABEL3ENTRY3Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL3ENTRY3.place(x=460, y=160, width=390, height=50)

        self.LABEL4ENTRY4 = Entry(self.f3, text=self.LABEL4ENTRY4Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL4ENTRY4.place(x=460, y=230, width=390, height=50)

        self.LABEL5ENTRY5 = Entry(self.f3, text=self.LABEL5ENTRY5Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL5ENTRY5.place(x=460, y=300, width=390, height=50)

        self.LABEL6ENTRY6 = Entry(self.f3, text=self.LABEL6ENTRY6Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL6ENTRY6.place(x=460, y=370, width=390, height=50)

        self.SubmitBTN = Button(self.f3, text='Create Account', font=('Agency FB', 25, 'bold'), bd=5, relief=RIDGE,
                                command=self.CreateAccSubmitBTN)
        self.SubmitBTN.place(x=460, y=440, width=390, height=60)

    def CreateAccSubmitBTN(self):
        if self.LABEL2ENTRY2Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter Name')
        elif self.LABEL3ENTRY3Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter Phone Number')
        elif self.LABEL4ENTRY4Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter Password')
        elif self.LABEL5ENTRY5Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter City Name')
        elif self.LABEL6ENTRY6Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter Unique ID')
        elif len(self.LABEL3ENTRY3Variable.get()) != 10:
            messagebox.showerror('ERROR', 'Enter Valid Phone Number')
        elif len(self.LABEL4ENTRY4Variable.get()) < 6:
            messagebox.showerror('ERROR', 'Enter at least 6 digit Password')
        else:
            with open('acc no.txt') as f:
                f = f.read()
            self.accNo = int(f) + 1
            with open('acc no.txt', 'w') as f:
                f.write(str(self.accNo))
            self.CREATEACCOUNT()

    def CREATEACCOUNT(self):
        cash = self.cash
        accNo = self.accNo
        name = self.LABEL2ENTRY2Variable.get()
        phone = self.LABEL3ENTRY3Variable.get()
        password = self.LABEL4ENTRY4Variable.get()
        city = self.LABEL5ENTRY5Variable.get()
        UniqueID = self.LABEL6ENTRY6Variable.get()

        self.AccountHolderDetails = [f"Account Number: {accNo}", f"Name: {name}", f"Phone no: {phone}",
                                     f"Password: {password}", f"City: {city}", f"Unique ID: {UniqueID}",
                                     f"Balance: {cash}"]
        with open(f'Customers\\{accNo}_{name}.txt', "w") as f:
            for details in self.AccountHolderDetails:
                f.write(str(details) + "\n")

        messagebox.showinfo('SUCCESS', 'Account Created Successfully')

        self.LABEL2ENTRY2Variable.set('')
        self.LABEL3ENTRY3Variable.set('')
        self.LABEL4ENTRY4Variable.set('')
        self.LABEL5ENTRY5Variable.set('')
        self.LABEL6ENTRY6Variable.set('')
        self.f3.destroy()

    def AccHolderLoginFRAME(self):
        self.f4.destroy()
        self.f3.destroy()
        self.f2.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=100, width=880, height=395)

        self.LABEL1Variable.set('Logging In...')
        self.LABEL2Variable.set('Enter Account Number')
        self.LABEL3Variable.set('Enter Name')
        self.LABEL4Variable.set('Enter Password')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL1.place(x=20, y=20, width=700, height=50)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL2.place(x=20, y=90, width=400, height=50)

        self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL3.place(x=20, y=160, width=400, height=50)

        self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL4.place(x=20, y=230, width=400, height=50)

        self.LABEL2ENTRY2 = Entry(self.f3, text=self.LABEL2ENTRY2Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL2ENTRY2.place(x=460, y=90, width=390, height=50)

        self.LABEL3ENTRY3 = Entry(self.f3, text=self.LABEL3ENTRY3Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL3ENTRY3.place(x=460, y=160, width=390, height=50)

        self.LABEL4ENTRY4 = Entry(self.f3, text=self.LABEL4ENTRY4Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL4ENTRY4.place(x=460, y=230, width=390, height=50)

        self.SubmitBTN = Button(self.f3, text='Log In', font=('Agency FB', 25, 'bold'), bd=5, relief=RIDGE,
                                command=self.AccHolderLoginSubmitBTN)
        self.SubmitBTN.place(x=460, y=300, width=390, height=60)

    def AccHolderLoginSubmitBTN(self):
        if self.LABEL2ENTRY2Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter Account Number')
        elif self.LABEL3ENTRY3Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter Name')
        elif self.LABEL4ENTRY4Variable.get() == '':
            messagebox.showerror('ERROR', 'Enter Password')

        else:
            self.AccountLogIn()

    def AccountLogIn(self):
        try:
            self.loggedin = False
            accNo = self.LABEL2ENTRY2Variable.get()
            name = self.LABEL3ENTRY3Variable.get()
            password = self.LABEL4ENTRY4Variable.get()
            with open(f'Customers\\{accNo}_{name}.txt', "r") as f:
                details = f.read()
                self.AccountHolderDetails = details.split("\n")
                if password == str(self.AccountHolderDetails[3][10::]):
                    self.loggedin = True

                if self.loggedin == True:
                    messagebox.showinfo('SUCCESS', 'Log in Successful')
                    self.cash = int(self.AccountHolderDetails[6][9::])
                    self.name = name
                    self.accNo = accNo
                    self.phone = (self.AccountHolderDetails[2][10::])
                    self.city = self.AccountHolderDetails[4][6::]
                    self.password = self.AccountHolderDetails[3][10::]
                    self.uniqueID = self.AccountHolderDetails[5][11::]
                    self.LABEL2ENTRY2Variable.set('')
                    self.LABEL3ENTRY3Variable.set('')
                    self.LABEL4ENTRY4Variable.set('')
                    self.f3.destroy()
                    self.AccMoneyHandlingFRAME()
                else:
                    messagebox.showerror('ERROR', 'Invalid Details')

        except:
            messagebox.showerror('ERROR', 'Invalid Details Entered')

    def AccMoneyHandlingFRAME(self):

        self.AccNoTXTVariable.set(f'  {self.accNo}')
        self.AccHolderNameTXTVariable.set(f'  {self.name}')
        self.AccHolderPhoneNoTXTVariable.set(f'  {self.phone}')
        self.AccHolderUniqueIDTXTVariable.set(f'  {self.uniqueID}')

        self.f4 = Frame(self.root, bd=5, relief=GROOVE)
        self.f4.place(x=321, y=80, width=880, height=200)

        self.AccNoLBL = Label(self.f4, text='  Account Number', font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE,
                              anchor='w')
        self.AccNoLBL.place(x=10, y=10, width=200, height=50)
        self.AccNoTXT = Label(self.f4, text=self.AccNoTXTVariable.get(), font=('Agency FB', 20, 'bold'), bd=5,
                              relief=RIDGE, anchor='w')
        self.AccNoTXT.place(x=220, y=10, width=200, height=50)

        self.AccHolderUniqueIDLBL = Label(self.f4, text='  Unique ID', font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE,
                              anchor='w')
        self.AccHolderUniqueIDLBL.place(x=440, y=10, width=200, height=50)
        self.AccHolderUniqueIDTXT = Label(self.f4, text=self.AccHolderUniqueIDTXTVariable.get(), font=('Agency FB', 20, 'bold'), bd=5,
                              relief=RIDGE, anchor='w')
        self.AccHolderUniqueIDTXT.place(x=650, y=10, width=200, height=50)

        self.AccHolderNameLBL = Label(self.f4, text='  Acc Holder Name', font=('Agency FB', 20, 'bold'), bd=5,
                                      relief=RIDGE, anchor='w')
        self.AccHolderNameLBL.place(x=10, y=70, width=200, height=50)
        self.AccHolderNameTXT = Label(self.f4, text=self.AccHolderNameTXTVariable.get(), font=('Agency FB', 20, 'bold'),
                                      bd=5, relief=RIDGE, anchor='w')
        self.AccHolderNameTXT.place(x=220, y=70, width=200, height=50)

        self.AccHolderPhoneNoLBL = Label(self.f4, text='  Phone Number', font=('Agency FB', 20, 'bold'), bd=5,
                                         relief=RIDGE, anchor='w')
        self.AccHolderPhoneNoLBL.place(x=10, y=130, width=200, height=50)
        self.AccHolderPhoneNoTXT = Label(self.f4, text=self.AccHolderPhoneNoTXTVariable.get(),
                                         font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE, anchor='w')
        self.AccHolderPhoneNoTXT.place(x=220, y=130, width=200, height=50)

        self.CashPresentLBL = Label(self.f4, text='  Balance', font=('Agency FB', 20, 'bold'), bd=5,
                                    relief=RIDGE, anchor='w')
        self.CashPresentLBL.place(x=440, y=130, width=200, height=50)
        self.CashPresentTXT = Label(self.f4, text=f'  {self.cash}', font=('Agency FB', 20, 'bold'), bd=5,
                                    relief=RIDGE, anchor='w')
        self.CashPresentTXT.place(x=650, y=130, width=200, height=50)

        self.f2 = Frame(self.root, bd=5, relief=GROOVE)
        self.f2.place(x=1212, y=65, width=300, height=720)
        self.BTN1Variable.set('Add Money')
        self.BTN2Variable.set('Withdraw Money')
        self.BTN3Variable.set('Transfer Money')
        self.BTN4Variable.set('Check All Transactions')
        self.BTN5Variable.set('Account Correction')
        self.BTN6Variable.set('-------')
        self.BTN7Variable.set('-------')
        self.BTN8Variable.set('Log Out')

        BTN1 = Button(self.f2, text=self.BTN1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                      command=self.AddMoneyFRAME)
        BTN1.place(x=20, y=20, width=250, height=50)

        BTN2 = Button(self.f2, text=self.BTN2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                      command=self.WithdrawMoneyFRAME)
        BTN2.place(x=20, y=90, width=250, height=50)

        BTN3 = Button(self.f2, text=self.BTN3Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                      command=self.TransferMoneyFrame)
        BTN3.place(x=20, y=160, width=250, height=50)

        BTN4 = Button(self.f2, text=self.BTN4Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                      command=self.ShowTransactions)
        BTN4.place(x=20, y=230, width=250, height=50)

        BTN5 = Button(self.f2, text=self.BTN5Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                      command=self.AccountCorrectionFRAME)
        BTN5.place(x=20, y=300, width=250, height=50)

        BTN6 = Button(self.f2, text=self.BTN6Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED)
        BTN6.place(x=20, y=370, width=250, height=50)

        BTN7 = Button(self.f2, text=self.BTN7Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED)
        BTN7.place(x=20, y=440, width=250, height=50)

        BTN8 = Button(self.f2, text=self.BTN8Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RAISED,
                      command=self.LogOut)
        BTN8.place(x=20, y=510, width=250, height=50)

    def AddMoneyFRAME(self):
        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=300, width=880, height=250)

        self.LABEL1Variable.set('Adding Money')
        self.LABEL2Variable.set('Enter Amount To Add')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL1.place(x=20, y=20, width=700, height=50)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL2.place(x=20, y=90, width=400, height=50)

        self.LABEL2ENTRY2 = Entry(self.f3, text=self.LABEL2ENTRY2Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL2ENTRY2.place(x=460, y=90, width=390, height=50)

        self.SubmitBTN = Button(self.f3, text='Add Money', font=('Agency FB', 25, 'bold'), bd=5, relief=RIDGE,
                                command=self.AddMoneyBTN)
        self.SubmitBTN.place(x=460, y=160, width=390, height=60)

    def AddMoneyBTN(self):
        try:
            amount = int(self.LABEL2ENTRY2Variable.get())
            if amount > 0:
                self.cash += amount

                with open(f'Customers\\{self.accNo}_{self.name}.txt', "r") as f:
                    details = f.read()
                    self.AccountHolderDetails = details.split("\n")

                with open(f'Customers\\{self.accNo}_{self.name}.txt', "w") as f:
                    f.write(details.replace(str(self.AccountHolderDetails[6][9::]), str(self.cash)))

                with open(f'Customers\\{self.accNo}_{self.name}.txt', "a") as f:
                    f.write(f"\n{time.strftime('%d/%m/%y')}  {time.strftime('%H:%M:%S')}\tAdded Amount {amount}")

                self.CashPresentTXT.config(text=f'  {self.cash}')
                messagebox.showinfo("SUCCESS", 'Amount Added Successfully')
                self.LABEL2ENTRY2Variable.set('')
                self.f3.destroy()
            else:
                messagebox.showerror('ERROR', 'Enter Valid Amount')

        except:
            messagebox.showerror('ERROR', 'Enter Valid Amount')

    def WithdrawMoneyFRAME(self):
        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=300, width=880, height=250)

        self.LABEL1Variable.set('Withdrawing Money')
        self.LABEL2Variable.set('Enter Amount To Withdraw')

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL1.place(x=20, y=20, width=700, height=50)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL2.place(x=20, y=90, width=400, height=50)

        self.LABEL2ENTRY2 = Entry(self.f3, text=self.LABEL2ENTRY2Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL2ENTRY2.place(x=460, y=90, width=390, height=50)

        self.SubmitBTN = Button(self.f3, text='Withdraw Money', font=('Agency FB', 25, 'bold'), bd=5, relief=RIDGE,
                                command=self.WithdrawMoneyBTN)
        self.SubmitBTN.place(x=460, y=160, width=390, height=60)

    def WithdrawMoneyBTN(self):
        try:
            amount = int(self.LABEL2ENTRY2Variable.get())
            if amount > 0:
                if amount <= self.cash:
                    self.cash -= amount
                    with open(f'Customers\\{self.accNo}_{self.name}.txt', "r") as f:
                        details = f.read()
                        self.AccountHolderDetails = details.split("\n")
                    with open(f'Customers\\{self.accNo}_{self.name}.txt', "w") as f:
                        f.write(details.replace(str(self.AccountHolderDetails[6][9::]), str(self.cash)))

                    with open(f'Customers\\{self.accNo}_{self.name}.txt', "a") as f:
                        f.write(
                            f"\n{time.strftime('%d/%m/%y')}  {time.strftime('%H:%M:%S')}\tWithdrawn Amount {amount}")

                    self.CashPresentTXT.config(text=f'  {self.cash}')
                    messagebox.showinfo("SUCCESS", 'Amount Added Successfully')
                    self.LABEL2ENTRY2Variable.set('')
                    self.f3.destroy()

                else:
                    messagebox.showerror('ERROR', 'Insufficient Balance')

            else:
                messagebox.showerror('ERROR', 'Enter Valid Amount')
        except:
            messagebox.showerror('ERROR', 'Enter Valid Amount')

    def TransferMoneyFrame(self):
        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=300, width=880, height=390)

        self.LABEL1Variable.set('Transferring Money')
        self.LABEL2Variable.set('Enter Amount To Transfer')
        self.LABEL3Variable.set("Enter Receiver's Account Number")
        self.LABEL4Variable.set("Enter Receiver's Name")

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL1.place(x=20, y=20, width=700, height=50)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL2.place(x=20, y=90, width=400, height=50)

        self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL3.place(x=20, y=160, width=400, height=50)

        self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL4.place(x=20, y=230, width=400, height=50)

        self.LABEL2ENTRY2 = Entry(self.f3, text=self.LABEL2ENTRY2Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL2ENTRY2.place(x=460, y=90, width=390, height=50)

        self.LABEL3ENTRY3 = Entry(self.f3, text=self.LABEL3ENTRY3Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL3ENTRY3.place(x=460, y=160, width=390, height=50)

        self.LABEL4ENTRY4 = Entry(self.f3, text=self.LABEL4ENTRY4Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL4ENTRY4.place(x=460, y=230, width=390, height=50)

        self.SubmitBTN = Button(self.f3, text='Transfer Money', font=('Agency FB', 25, 'bold'), bd=5, relief=RIDGE,
                                command=self.TransferMoneyBTN)
        self.SubmitBTN.place(x=460, y=300, width=390, height=60)

    def TransferMoneyBTN(self):
        self.TranferCash = False
        try:
            amount = int(self.LABEL2ENTRY2Variable.get())
            accNo = self.LABEL3ENTRY3Variable.get()
            name = self.LABEL4ENTRY4Variable.get()
            if amount > 0:
                if amount <= self.cash:
                    with open(f'Customers\\{accNo}_{name}.txt', "r") as f:
                        details = f.read()
                        self.AccountHolderDetails = details.split("\n")
                        if str(f"Account Number: {accNo}") in self.AccountHolderDetails:
                            self.TranferCash = True
                    if self.TranferCash == True:
                        total_cash = int(self.AccountHolderDetails[6][9::]) + amount
                        left_cash = self.cash - amount
                        with open(f'Customers\\{accNo}_{name}.txt', "w") as f:
                            f.write(details.replace(str(self.AccountHolderDetails[6][9::]), str(total_cash)))

                        with open(f'Customers\\{accNo}_{name}.txt', "a") as f:
                            f.write(
                                f"\n{time.strftime('%d/%m/%y')}  {time.strftime('%H:%M:%S')}\t{amount} received from {self.name}")

                        with open(f'Customers\\{self.accNo}_{self.name}.txt', "r") as f:
                            details_2 = f.read()
                            self.AccountHolderDetails = details_2.split("\n")

                        with open(f'Customers\\{self.accNo}_{self.name}.txt', "w") as f:
                            f.write(details_2.replace(str(self.AccountHolderDetails[6][9::]), str(left_cash)))

                        with open(f'Customers\\{self.accNo}_{self.name}.txt', "a") as f:
                            f.write(
                                f"\n{time.strftime('%d/%m/%y')}  {time.strftime('%H:%M:%S')}\t{amount} transferred to {name}, Account No. {accNo}")

                        self.cash = left_cash
                        self.CashPresentTXT.config(text=f'  {self.cash}')
                        messagebox.showinfo("SUCCESS",
                                            f"Amount Transferred Successfully to {name},  Account no. {accNo}")

                        self.LABEL2ENTRY2Variable.set('')
                        self.LABEL3ENTRY3Variable.set('')
                        self.LABEL4ENTRY4Variable.set('')
                        self.f3.destroy()

                else:
                    messagebox.showerror('ERROR', 'Insufficient Balance')
            else:
                messagebox.showerror('ERROR', 'Enter Valid Amount')

        except:
            messagebox.showerror('ERROR', 'Enter Valid Details')

    def ShowTransactions(self):
        self.f3.destroy()
        with open(f"Customers\\{self.accNo}_{self.name}.txt", 'r') as f:
            f = f.read()
        with open("Customers\\PassBookShow.txt", 'w') as f2:
            f2.write(f)

        path = f"Customers\\PassBookShow.txt"
        os.startfile(path)

    def LogOut(self):
        try:
            self.f4.destroy()
            self.f3.destroy()
            self.f2.destroy()
            messagebox.showinfo('SUCCESS', 'Account Logout Success')
        except:
            self.f2.destroy()
            messagebox.showinfo('SUCCESS', 'Account Logout Success')

    def AccountCorrectionFRAME(self):
        self.f3.destroy()
        self.f3 = Frame(self.root, bd=5, relief=GROOVE)
        self.f3.place(x=321, y=300, width=880, height=390)

        self.LABEL1Variable.set('Account Correction')
        self.LABEL2Variable.set('Phone Number')
        self.LABEL3Variable.set("Password")
        self.LABEL4Variable.set("City")

        self.LABEL2ENTRY2Variable.set(self.phone)
        self.LABEL3ENTRY3Variable.set(self.password)
        self.LABEL4ENTRY4Variable.set(self.city)

        self.LABEL1 = Label(self.f3, text=self.LABEL1Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL1.place(x=20, y=20, width=700, height=50)

        self.LABEL2 = Label(self.f3, text=self.LABEL2Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL2.place(x=20, y=90, width=400, height=50)

        self.LABEL3 = Label(self.f3, text=self.LABEL3Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL3.place(x=20, y=160, width=400, height=50)

        self.LABEL4 = Label(self.f3, text=self.LABEL4Variable.get(), font=('Agency FB', 20, 'bold'), bd=5, relief=RIDGE)
        self.LABEL4.place(x=20, y=230, width=400, height=50)

        self.LABEL2ENTRY2 = Entry(self.f3, text=self.LABEL2ENTRY2Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL2ENTRY2.place(x=460, y=90, width=390, height=50)

        self.LABEL3ENTRY3 = Entry(self.f3, text=self.LABEL3ENTRY3Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL3ENTRY3.place(x=460, y=160, width=390, height=50)

        self.LABEL4ENTRY4 = Entry(self.f3, text=self.LABEL4ENTRY4Variable, font=('Agency FB', 20, 'bold'), bd=5,
                                  relief=RIDGE)
        self.LABEL4ENTRY4.place(x=460, y=230, width=390, height=50)

        self.SubmitBTN = Button(self.f3, text='Confirm Corrections', font=('Agency FB', 25, 'bold'), bd=5, relief=RIDGE,
                                command=self.AccountCorrectionBTN)
        self.SubmitBTN.place(x=460, y=300, width=390, height=60)

    def AccountCorrectionBTN(self):
        self.phone = self.LABEL2ENTRY2Variable.get()
        self.password = self.LABEL3ENTRY3Variable.get()
        self.city = self.LABEL4ENTRY4Variable.get()

        try:
            if self.LABEL2ENTRY2Variable.get() == "":
                messagebox.showerror('ERROR', 'Enter Phone No')
            elif len(self.LABEL2ENTRY2Variable.get()) != 10:
                messagebox.showerror('ERROR', 'Enter Valid Phone No')
            elif self.LABEL3ENTRY3Variable.get() =="":
                messagebox.showerror('ERROR', 'Enter password')
            elif len(self.LABEL3ENTRY3Variable.get()) <6:
                messagebox.showerror('ERROR', 'Enter password of at least 6 character')
            elif self.LABEL4ENTRY4Variable.get() =="":
                messagebox.showerror('ERROR', 'Enter City')
            else:
                with open(f'Customers\\{self.accNo}_{self.name}.txt', "r") as f:
                    details = f.read()
                    self.AccountHolderDetails = details.split("\n")
                with open(f'Customers\\{self.accNo}_{self.name}.txt', "w") as f:
                    f.write(details.replace(str(self.AccountHolderDetails[2][10::]), str(self.phone)))

                with open(f'Customers\\{self.accNo}_{self.name}.txt', "r") as f:
                    details = f.read()
                    self.AccountHolderDetails = details.split("\n")
                with open(f'Customers\\{self.accNo}_{self.name}.txt', "w") as f:
                    f.write(details.replace(str(self.AccountHolderDetails[3][10::]), str(self.password)))

                with open(f'Customers\\{self.accNo}_{self.name}.txt', "r") as f:
                    details = f.read()
                    self.AccountHolderDetails = details.split("\n")
                with open(f'Customers\\{self.accNo}_{self.name}.txt', "w") as f:
                    f.write(details.replace(str(self.AccountHolderDetails[4][6::]), str(self.city)))

                messagebox.showinfo('SUCCESS', 'Details Updated Successfully,\nChanges will appear in your account soon')
                self.LABEL2ENTRY2Variable.set('')
                self.LABEL3ENTRY3Variable.set('')
                self.LABEL4ENTRY4Variable.set('')
                self.f3.destroy()
        except:
            messagebox.showerror('ERROR', 'Enter Valid Details')


root = Tk()
obj = BankSoftware(root)
root.mainloop()
