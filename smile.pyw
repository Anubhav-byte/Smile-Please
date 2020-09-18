from win10toast import ToastNotifier
import random
import jokes
import time

n=ToastNotifier()

count=1

for i in range(10):
    interval=60 * 45

    rn= random.randint(1,4)
    if(rn==1):

        joke= jokes.geek()
        n.show_toast("A joke for you", joke , duration=30)
        count +=1
    elif rn==2:

        joke=jokes.icanhazdad()
        n.show_toast("Hear a joke", joke , duration=30 )
        count +=1

    elif rn==3:

        joke=jokes.chucknorris()
        n.show_toast("Have you heard this joke?", joke , duration=30 )
        count +=1

    else:
        joke=jokes.icndb()
        n.show_toast("Smiling helps" , joke , duration=30)
        count +=1

    if count%2 == 0:
        message='You should drink water'
        n.show_toast('Hey! Listen' , message , duration=15)

    if count%5 == 0:
        message = "You are making the monitor shy with your long stare, see something else"
        n.show_toast("Alert", message, duration=15)
    time.sleep(interval)
