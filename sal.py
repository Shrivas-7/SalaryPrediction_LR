#Libraries Imported
from tkinter import *
from   tkinter import messagebox as msg
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from   tkintertable import TableCanvas

#Function Build CSV Functionality
def csv1():
    class create_csv:
        def __init__(self, root):
            self.f = Frame(root, height=350, width=500)
            self.f.pack()    # Place the frame on root window
           
          # Creating label widgets
            self.message_label = Label(self.f,text='Display the Empsal CSV in TkinterTable',font=('Arial', 14))
          
          # Buttons
            self.confirm_button = Button(self.f,text='Display', font=('Arial', 14), bg='Orange',
                                 fg='Black', command=self.conv_to_csv)
            self.exit_button = Button(self.f,text='Exit', font=('Arial', 14), bg='Yellow',
                                 fg='Black', command=root.destroy)

          # Placing the widgets using grid manager
            self.message_label.grid(row=1, column=0)
            self.confirm_button.grid(row=2,column=0)
            self.exit_button.grid(row=2,column=2)
            
          

        def conv_to_csv(self):
            
            try:
                
                # Now display the CSV in 'tkintertable' widget
                self.f = Frame(root, height=200, width=300) 
                self.f.pack(fill=BOTH,expand=1)
                self.table = TableCanvas(self.f, read_only=True)
                self.table.importCSV('exp_sal.csv')
                self.table.show()
            except FileNotFoundError as e:
                msg.showerror('Error in opening file', e.msg)

    #--------------------------------------------------
    root=Tk()
    root.title('Build/Display CSV in Tkintertable')
    root.geometry('1000x620')
    conv_csv = create_csv(root)
    root.mainloop()
    

#Function for Predict Salary Functionality    
def predict():
    def cal():          
        x=yrs_entry.get()
        sal = regressor.predict(numpy.int64(x))
        output_label.config(text = 'The Expected Salary for '+str(x) +' years of Experience is : ' + str(sal[0]))
        #yrs_entry.delete(0,END)
    message_label = Label(root,text='Experience(years) : ',font=('Arial', 14))#widget
    message_label.grid(row=5, column=1)
    yrs_entry = Entry(root, font=('Arial', 14), width=6)
    yrs_entry.grid(row=5, column=2)
    yrs_entry.focus()
    predict_button = Button(root,text='Predict!!!', font=('Arial', 14), bg='Orange', fg='Black',command=cal)
    predict_button.grid(row=6, column=2)
    
    
#Function for Intercept & Coefficient Functionality
def inc():
    
    
    x=regressor.intercept_
    y=regressor.coef_
    output_label.config(text='Intercept : '+ str(x))
    output_label1.config(text='Co-efficient : '+ str(y[0]))
    
#Function for Scatter Plot Functionality
def plot():
    plt.scatter(X, Y, color = 'red')
    plt.plot(X, regressor.predict(X), color = 'blue')
    plt.title('Salary Vs Experience ')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.show()
    
#Function for Reset Functionality
def reset():
        
    output_label.configure(text = '')   # Erase the label text
    output_label1.configure(text = '')
    yrs_entry.focus()

#Function for Build DF Functionality
def df():
    print(expsal_df)

#----------------------------------------     
root = Tk()
root.title('Salary Prediction Model')
root.geometry('900x400')


# Importing the dataset
expsal_df = pd.read_csv('exp_sal.csv')

X = expsal_df.iloc[:, :-1].values
Y = expsal_df.iloc[:, 1].values # Dependent Variable/Target Values


# Splitting the Dataset into Training Set and Test Set
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test Set Results
y_pred = regressor.predict(X_test)



# Creating widgets 
title_label = Label(root,text='SALARY PREDICTION',font=('Arial', 14))
output_label = Label(root,text='', font=('Arial', 14))

output_label1 = Label(root,text='', font=('Arial', 14))
csv_button = Button(root,text='Build CSV', font=('Arial', 14), bg='Orange', fg='Black',command=csv1)
predict_button = Button(root,text='Predict Salary', font=('Arial', 14), bg='Khaki', fg='Black', command=predict)
exit_button = Button(root,text='Exit', font=('Arial', 14), bg='khaki', fg='Black', command=root.destroy)
intercept_button = Button(root,text='Intercept & Co-efficient', font=('Arial', 14), bg='Orange', fg='Black', command=inc)
plot_button = Button(root,text='Scatter Plot', font=('Arial', 14), bg='Yellow', fg='Black', command=plot)
reset_button = Button(root,text='Clear', font=('Arial', 14), bg='Khaki', fg='Black', command=reset)
df_button = Button(root,text='Build DF', font=('Arial', 14), bg='Orange', fg='Black',command=df)

# Placing widgets using grid manager
title_label.grid(row=0, column=3)
csv_button.grid(row=2, column=1)
output_label1.grid(row=8, column=1)
predict_button.grid(row=2, column=3)
intercept_button.grid(row=2, column=5)
df_button.grid(row=3, column=2)
plot_button.grid(row=3, column=4)
exit_button.grid(row=4, column=2)
reset_button.grid(row=4, column=4)
output_label.grid(row=7, column=1)
#output_label.grid(row=1, column=0, columnspan=3)

# mainloop
root.mainloop()
