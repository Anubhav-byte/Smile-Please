from win10toast import ToastNotifier
from random import choice
import jokes

n=ToastNotifier()



for i in range(10):

    joke= jokes.geek()
    n.show_toast("A joke for you", joke , duration=5)
