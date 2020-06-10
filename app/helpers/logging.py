from flask import current_app, g
#from main import GLOBAL

def dprint(input):
    #if GLOBAL['app'].config['DEBUG']:
        print("DEBUG:" + str(input))
