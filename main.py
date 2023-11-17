from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play(-1)

def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    ProgressbarLabelA.place_forget()
    ProgressbarLabelB.place_forget()
    ProgressbarLabelC.place_forget()
    ProgressbarLabelD.place_forget()

    b = event.widget
    value = b['text']

    for i in range(15):

        if value == correct_answers[i]:
            if value == correct_answers[14]:
                def close():
                    new_window1.destroy()
                    root.destroy()

                def playAgain():
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                    new_window1.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])

                    optionButtonA.config(text=a_option[0])
                    optionButtonB.config(text=b_option[0])
                    optionButtonC.config(text=c_option[0])
                    optionButtonD.config(text=d_option[0])

                    amountLable.config(image=amountImage)

                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()

                new_window1 = Toplevel()
                new_window1.overrideredirect(True)
                new_window1.config(bg='black')
                new_window1.geometry('500x400+140+30')
                new_window1.title('You Won 0 Pounds')
                imgLabel = Label(new_window1, image=centerImage, bd=0)
                imgLabel.pack(pady=30)

                winLabel = Label(new_window1, text="Congratulations, You Won Buddy!", font=('arial', 20, 'bold'),
                                 bg='black', fg='white')
                winLabel.pack()

                playAgainButton = Button(new_window1, text='Play Again', font=('arial', 15, 'bold'), bg='black',
                                         fg='white',
                                         activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                         command=playAgain)
                playAgainButton.pack()

                closeButton = Button(new_window1, text='Close', font=('arial', 15, 'bold'), bg='black', fg='white',
                                     activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                     command=close)
                closeButton.pack()

                maholImage = PhotoImage(file='moai.png')
                maholLable = Label(new_window1, image=maholImage, bg='black')
                maholLable.place(x=45, y=280)

                maholLable1 = Label(new_window1, image=maholImage, bg='black')
                maholLable1.place(x=350, y=280)

                new_window1.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButtonA.config(text=a_option[i + 1])
            optionButtonB.config(text=b_option[i + 1])
            optionButtonC.config(text=c_option[i + 1])
            optionButtonD.config(text=d_option[i + 1])
            amountLable.config(image=amountImages[i])
        if value not in correct_answers:
            def close():
                new_window.destroy()
                root.destroy()

            def tryagain():
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)

                new_window.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])

                optionButtonA.config(text=a_option[0])
                optionButtonB.config(text=b_option[0])
                optionButtonC.config(text=c_option[0])
                optionButtonD.config(text=d_option[0])

                amountLable.config(image=amountImage)

            new_window = Toplevel()
            new_window.overrideredirect(True)
            new_window.config(bg='black')
            new_window.geometry('500x400+140+30')
            new_window.title('You Won 0 Pounds')
            imgLabel = Label(new_window, image=centerImage, bd=0)
            imgLabel.pack(pady=30)

            loseLabel = Label(new_window, text="oops You lost !", font=('arial', 20, 'bold'), bg='black',
                              fg='white')
            loseLabel.pack()

            tryagainButton = Button(new_window, text='Try again', font=('arial', 15, 'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(new_window, text='Close', font=('arial', 15, 'bold'), bg='black', fg='white',
                                 activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                 command=close)
            closeButton.pack()

            alealeImage = PhotoImage(file='frustrated.png')
            alealeLable = Label(new_window, image=alealeImage, bg='black')
            alealeLable.place(x=45, y=280)

            alealeLable1 = Label(new_window, image=alealeImage, bg='black')
            alealeLable1.place(x=350, y=280)

            new_window.mainloop()
            break

def lifeline50():
    lifeline50Button.config(image=image50x, state=DISABLED)
    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButtonA.config(text='')
        optionButtonC.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButtonB.config(text='')
        optionButtonD.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButtonC.config(text='')
        optionButtonD.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButtonA.config(text='')
        optionButtonD.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButtonA.config(text='')
        optionButtonB.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButtonA.config(text='')
        optionButtonB.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButtonA.config(text='')
        optionButtonC.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButtonB.config(text='')
        optionButtonC.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButtonA.config(text='')
        optionButtonD.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButtonC.config(text='')
        optionButtonD.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButtonB.config(text='')
        optionButtonC.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButtonB.config(text='')
        optionButtonC.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButtonB.config(text='')
        optionButtonD.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButtonA.config(text='')
        optionButtonD.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButtonA.config(text='')
        optionButtonB.config(text='')


def audiencePolelifeline():
    audiencePoleButton.config(image=audiencePolex, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    ProgressbarLabelA.place(x=580, y=320)
    ProgressbarLabelB.place(x=620, y=320)
    ProgressbarLabelC.place(x=660, y=320)
    ProgressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=20)
        progressbarB.config(value=90)
        progressbarC.config(value=35)
        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=64)
        progressbarB.config(value=40)
        progressbarC.config(value=85)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)
        progressbarB.config(value=25)
        progressbarC.config(value=32)
        progressbarD.config(value=22)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=33)
        progressbarB.config(value=70)
        progressbarC.config(value=21)
        progressbarD.config(value=45)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=52)
        progressbarB.config(value=30)
        progressbarC.config(value=88)
        progressbarD.config(value=47)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=52)
        progressbarB.config(value=47)
        progressbarC.config(value=41)
        progressbarD.config(value=93)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=52)
        progressbarB.config(value=39)
        progressbarC.config(value=47)
        progressbarD.config(value=86)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=52)
        progressbarB.config(value=40)
        progressbarC.config(value=46)
        progressbarD.config(value=77)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=76)
        progressbarB.config(value=96)
        progressbarC.config(value=75)
        progressbarD.config(value=72)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=20)
        progressbarB.config(value=90)
        progressbarC.config(value=35)
        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=93)
        progressbarB.config(value=33)
        progressbarC.config(value=36)
        progressbarD.config(value=69)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=96)
        progressbarB.config(value=44)
        progressbarC.config(value=39)
        progressbarD.config(value=66)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=82)
        progressbarB.config(value=40)
        progressbarC.config(value=88)
        progressbarD.config(value=34)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=67)
        progressbarB.config(value=80)
        progressbarC.config(value=98)
        progressbarD.config(value=56)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=49)
        progressbarB.config(value=30)
        progressbarC.config(value=76)
        progressbarD.config(value=100)

def phoneLifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    phoneLifelineButton.config(image=phoneImagex, state=DISABLED)
def phoneclick():
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'Jay shri Raam, sahi jawaab hai  {correct_answers[i]}')
            engine.runAndWait()


correct_answers = ["28", "J. Nehru", "Jupitar", "Hydrogen", "Japan", "Pacific",
                   "Alan Turing", "Vatican City", "In 16th century", "195", "Euro", "Blue Whale",
                   "1992", "Avocado", "700"]

questions = ["How many States in India?",
             "Who is the first Prime Minister of India?",
             "What is the largest planet in our solar system?",
             "Which element has the chemical symbol 'H'?",
             "Which country is known as the Land of the Rising Sun?",
             "Which ocean is the largest?",
             "Who is known as the 'Father of Computer Science'?",
             "what is the smallest country?",
             "When the Cricket Invented?",
             "How many countries in the world?",
             "What is the currency of Italy?",
             "What is the largest mammal in the world?",
             "When babri masjid destroyed?",
             "What is the main ingredient in guacamole?",
             "How many Shlokas in Shrimad Bhagavad Gita?"
             ]
a_option = ["26", "V. patel", "Jupitar", "oxygen", "Indonesia", "Antarctic ",
            "Charles Darwin", "Nauru", "In 17th century", "190", "Euro", "Blue Whale",
            "1993", "Tomatoes", "743"]
b_option = ["28", "I. Gandhi", "Mars", "Hydrogen", "Nepal", "Indian",
            "Nikola Tesla", "Tuvalu", "In 16th century", "195", "Cedi", "Giraffe",
            "1994", "Onions", "806"]
c_option = ["32", "J. Nehru", "Earth", "Helium", "Japan", "Arctic",
            "C. Babbage", "Monaco", "In 19th century", "200", "Lek", "Elephant",
            "1992", "Avocado", "650"]
d_option = ["34", "M. Singh", "Venus", "Lithium", "Africa", "Pacific",
            "Alan Turing", "Vatican City", "In 20th century", "205", "Rupee", "Hippopotamus",
            "1991", "Peppers", "700"]

root = Tk()

root.geometry('1270x652+0+0')
root.title('Be a Mr.MEMER by Mr.Akash')

root.config(bg='black')

leftframe = Frame(root, bg='black', padx=90)
leftframe.grid(row=0, column=0)

topFrame = Frame(leftframe, bg='black', pady=15)
topFrame.grid()

centerFrame = Frame(leftframe, bg='black', pady=15)
centerFrame.grid(row=1, column=0)

bottomFrame = Frame(leftframe)
bottomFrame.grid(row=2, column=0)

rightframe = Frame(root, pady=25, padx=50, bg='black')
rightframe.grid(row=0, column=1)

image50 = PhotoImage(file='50-50.png')
image50x = PhotoImage(file='50-50-X.png')
lifeline50Button = Button(topFrame, image=image50, bg='black', border=0, activebackground='black', width=180, height=80,
                          command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='audiencePole.png')
audiencePolex = PhotoImage(file='audiencePoleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bg='black', border=0, activebackground='black', width=180,
                            height=80, command=audiencePolelifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='phoneAFriend.png')
phoneImagex = PhotoImage(file='phoneAFriendX.png')
phoneLifelineButton = Button(topFrame, image=phoneImage, bg='black', border=0, activebackground='black', width=180,
                             height=80, command=phoneLifeline)
phoneLifelineButton.grid(row=0, column=2)

callimage = PhotoImage(file='phone.png')
callButton = Button(root, image=callimage, bd=0, bg='black', activebackground='black', cursor='hand2',
                    command=phoneclick)

centerImage = PhotoImage(file='center.png')
logoLabel = Label(centerFrame, image=centerImage, bg='black', width=300, height=200)
logoLabel.grid(row=0, column=0)

amountImage = PhotoImage(file='picture0.png')
amountImage1 = PhotoImage(file='picture1.png')
amountImage2 = PhotoImage(file='picture2.png')
amountImage3 = PhotoImage(file='picture3.png')
amountImage4 = PhotoImage(file='picture4.png')
amountImage5 = PhotoImage(file='picture5.png')
amountImage6 = PhotoImage(file='picture6.png')
amountImage7 = PhotoImage(file='picture7.png')
amountImage8 = PhotoImage(file='picture8.png')
amountImage9 = PhotoImage(file='picture9.png')
amountImage10 = PhotoImage(file='picture10.png')
amountImage11 = PhotoImage(file='picture11.png')
amountImage12 = PhotoImage(file='picture12.png')
amountImage13 = PhotoImage(file='picture13.png')
amountImage14 = PhotoImage(file='picture14.png')
amountImage15 = PhotoImage(file='picture15.png')

amountImages = [amountImage1, amountImage2, amountImage3, amountImage4, amountImage5, amountImage6, amountImage7,
                amountImage8, amountImage9, amountImage10, amountImage11, amountImage12, amountImage13, amountImage14,
                amountImage15]

amountLable = Label(rightframe, image=amountImage, bg='black')
amountLable.grid(row=0, column=0)

layImage = PhotoImage(file='lay.png')
layLable = Label(bottomFrame, image=layImage, bg='black')
layLable.grid(row=0, column=0)

questionArea = Text(bottomFrame, font=('arial', 18, 'bold'), width=26, height=2, wrap='word', bg='black', fg='white',
                    bd=0)
questionArea.place(x=70, y=14)
questionArea.insert(END, questions[0])

labelA = Label(bottomFrame, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelA.place(x=60, y=110)

optionButtonA = Button(bottomFrame, text=a_option[0], font=('arial', 16, 'bold'), bg='black', fg='white',
                       bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButtonA.place(x=90, y=106)

labelB = Label(bottomFrame, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelB.place(x=330, y=110)

optionButtonB = Button(bottomFrame, text=b_option[0], font=('arial', 16, 'bold'), bg='black', fg='white',
                       bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButtonB.place(x=360, y=106)

labelC = Label(bottomFrame, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelC.place(x=60, y=190)

optionButtonC = Button(bottomFrame, text=c_option[0], font=('arial', 16, 'bold'), bg='black', fg='white',
                       bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButtonC.place(x=90, y=185)

labelD = Label(bottomFrame, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelD.place(x=330, y=190)

optionButtonD = Button(bottomFrame, text=d_option[0], font=('arial', 16, 'bold'), bg='black', fg='white',
                       bd=0, activebackground='black', activeforeground='white', cursor='hand2')
optionButtonD.place(x=360, y=187)

optionButtonA.bind('<Button-1>', select)
optionButtonB.bind('<Button-1>', select)
optionButtonC.bind('<Button-1>', select)
optionButtonD.bind('<Button-1>', select)

progressbarA = Progressbar(root, orient=VERTICAL, length=120)
progressbarB = Progressbar(root, orient=VERTICAL, length=120)
progressbarC = Progressbar(root, orient=VERTICAL, length=120)
progressbarD = Progressbar(root, orient=VERTICAL, length=120)

ProgressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')
ProgressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')
ProgressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')
ProgressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

root.mainloop()
