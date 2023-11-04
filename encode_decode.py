##importing mmodules
from tkinter import *
# from tkinter import *
import base64
from tkinter import filedialog

#initialize window
root = Tk()
root.geometry('800x500')
root.resizable(0,0)

#title of the window
root.title("TextImg - Message Encode and Decode")



#label

Label(root, text ='ENCODE DECODE', font = 'arial 20 bold').pack()
# Label(root, text ='Pumbas', font = 'arial 20 bold').pack(side =BOTTOM)


#define variables

Text1 = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()



#######define function#####

#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text1.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text1.get()))
    else:
        Result.set('Invalid Mode')



#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text1.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
   #entry1.delete(0,-1)

def encrypt_image():
    file1=filedialog.askopenfile(mode='r',filetype=[('jpg file','*.jpg')])
    if file1 is not None:
        # print(file1)
        file_name=file1.name
        print(file_name)
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()


#################### Label and Button #############

#Message
Label(root, font= 'arial 12 bold', text='MESSAGE').place(x= 60,y=60)
Entry(root, font = 'arial 10', textvariable = Text1, bg = 'ghost white').place(x=290, y = 60)

#key
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)


#mode
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)



#result
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)

######result button
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)


#reset button
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)


Label(root, font = 'arial 12 bold', text ='IMAGE ENCRYPTION AND DECRYPTION').place(x=150, y = 250)
b1=Button(root,text="Image Encrypt",command=encrypt_image)
b1.place(x=290,y=300)
entry1=Text(root,height=1,width=20)
Label(root, font = 'arial 12 bold', text ='KEY').place(x=50, y = 350)
entry1.place(x=290,y=350)
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 400)

#exit button
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 400)

root.mainloop()