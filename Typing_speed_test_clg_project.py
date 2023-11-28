words = ["The quick brown fox jumps over the lazy dog",
         "Jackdaws love my big sphinx of quartz",
         "Mr. Jock, TV quiz PhD, bags few lynx",
         "How vexingly quick daft zebras jump!",
         "Sphinx of black quartz, judge my vow",
         "Waltz, nymph, for quick jigs vex Bud",
         "The five boxing wizards jump quickly",
         "Crazy Fredrick bought many very exquisite opal jewels",
         "The jay, pig, fox, zebra, and my wolves quack",
         "How quickly daft jumping zebras vex!",
         "The sleek black panther quickly caught the zebra and jumped over it with grace",
         "Breezily jangling on my xylophone, I quickly whizzed down the fjord",
         "The quick sly fox jumps over the brown lazy dog and misses him",
         "Glib jocks quiz nymph to vex dwarf",
         "A mad boxer shot a quick, gloved jab to the jaw of his dizzy opponent",
         "The vixen twirls the black robe of a judge with zeal"]

def time():

    global timeleft,score,miss
    
    if(timeleft>0):
        timeleft-=1
        timerLabelCount.configure(text=timeleft)
        timerLabelCount.after(1000,time)

    else:
        gamePlayDetailLabel.configure(text=' hit= {} | miss= {} | total score= {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Attention','To play again hit retry button')
        
        if(rr == True):
            score =0
            timeleft = 60
            miss =0
            timerLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)

def startGame(event):
    
    global score,miss

    if(timeleft ==60):
        time()
    gamePlayDetailLabel.configure(text='')

    if(wordEntry.get() == wordLabel['text']):
         score = score + 1
         scoreLabelCount.configure(text=score)

    else:
        miss+=1

    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)


from logging import root
from tkinter import *
from tkinter import font
import random
from tkinter import messagebox


####################################### Root method
root= Tk()
root.geometry('800x600+400+100')
root.config(bg='powder blue')
root.title('Typing speed test')

####################################### Variables

score = 0
miss= 0
timeleft = 60

####################################### Label method

font.Label = Label(root,text ='Welcome to the typing speed test app',font = ('airal',25,font.BOLD),
                   bg ='powder blue')

font.Label.place(x=100,y=10)

random.shuffle(words)

wordLabel = Label(root,text = words[0],font = ('airal',20,font.BOLD),wraplength=600,bg = 'powder blue')
wordLabel.place(x=130,y=200)

scoreLabel = Label(root,text ='Score',font=('airal',25,font.BOLD),bg = 'powder blue')
scoreLabel.place(x=50,y=100)

scoreLabelCount = Label(root,text = score ,font=('airal',25,font.BOLD),bg = 'powder blue',fg ='green')
scoreLabelCount.place(x=80,y=150)

timerLabel = Label(root,text='Time left',font=('airal',25,font.BOLD),bg = 'powder blue')
timerLabel.place(x=620,y=100)

timerLabelCount = Label(root,text = timeleft ,font=('airal',25,font.BOLD),bg = 'powder blue',fg ='red')
timerLabelCount.place(x=670,y=150)

gamePlayDetailLabel = Label(root,text='Start typing and hit enter',font=('airal',25),bg='powder blue')
gamePlayDetailLabel.place(x=220,y=450)

###################################### Entry method

wordEntry = Entry(root,font=('airal',20),width=50,justify='center')
wordEntry.place(x=20,y=300)
wordEntry.focus_set()


root.bind('<Return>',startGame)
root.mainloop()
