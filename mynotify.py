from time import time
from plyer import notification
from random import choice

def sendNotification(heading,msg,waiting):
    notification.notify(
            title = heading,
            message=msg ,
            app_name="Health YOu",
            timeout=waiting
)

if __name__=='__main__':
    initial_hydrate=time()
    initial_eyes=time()
    initial_break=time()

    hydra_head="Hydrate Yourself"
    msgs=["Water is your new best friend","Do your squats, drink your water.","Water is the best of all things.","Drink water and mind your business" ,"Drink your way to better health. Drink water!"]
    hydra_msg=choice(msgs)

    eyes_head="ROLL YOUR EYES"
    eyes_msg="OH NAH! not actually jus give them a break"

    break_head="Take a Break "
    break_msg="Sit back & Relaxxx "

    rep_water=5*60
    rep_eyes=1*60
    rep_break=3*60

    while True:
        if time() - initial_hydrate > rep_water:
            sendNotification(hydra_head,hydra_msg,15)
            initial_hydrate=time()
            
        if time() - initial_eyes > rep_eyes:
            sendNotification(eyes_head,eyes_msg,45)
            initial_eyes=time()
            
        if time() - initial_break > rep_break:
            sendNotification(break_head,break_msg,10)
            initial_break=time()
            