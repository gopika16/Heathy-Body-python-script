from time import time,sleep
from plyer import notification
# from datetime import datetime
from random import choice
 

# sends the notification
def sendNotification(heading,msg,waiting):
    notification.notify(
            title = heading,
            message=msg ,
            timeout=waiting
    )
#     log_now(time())

# this function can be used to keep a track of all the tasks
# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {datetime.now()}\n")

if __name__=='__main__':
    # initalizing time
    initial_hydrate=time()
    initial_eyes=time()
    initial_break=time()

    # passes a random message form a list of messages
    msgs=["Water is your new best friend","Do your squats, drink your water.","Water is the best of all things.","Drink water and mind your business" ,"Drink your way to better health. Drink water!"]

    # messages for the notification
    hydra_head="Hydrate Yourself"
    hydra_msg=choice(msgs)

    eyes_head="ROLL YOUR EYES"
    eyes_msg="OH NAH! not actually jus give them a break"

    break_head="Take a Break "
    break_msg="Sit back & Relaxxx "

    # set the duration for each task
    rep_water=35*60
    rep_eyes=10*60
    rep_break=60*60

    while True:
        sleep(10*60)
        if time() - initial_hydrate > rep_water:
            sendNotification(hydra_head,hydra_msg,60)
            initial_hydrate=time()
            sleep(10*60)
            
        if time() - initial_eyes > rep_eyes:
            sendNotification(eyes_head,eyes_msg,60)
            initial_eyes=time()
            
        if time() - initial_break > rep_break:
            sendNotification(break_head,break_msg,180)
            initial_break=time()
            sleep(10*60)
            