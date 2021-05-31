# Flask test server
import datetime
from termcolor import colored
from flask import Flask

app = Flask(__name__)
#This need to stay on top of the code after the imports
print(colored('----STARTING SERVER----', 'green'))
startup_time = datetime.datetime.now()
print(startup_time.strftime("Time: %H:%M:%S"))
print()
#-----------------------------------------

@app.route('/')
def hello_world():
    return 'Hello, World!'

print(colored('----SERVER HAS STARTED----', 'green'))
bot_ready_time = datetime.datetime.now()
print(bot_ready_time.strftime("Time: %H:%M:%S"))
time = bot_ready_time - startup_time
if time > datetime.timedelta(seconds=10):
    color = "red"
else:
    color = "green"

print(colored("Start up time:", "green"), colored(time, color))
