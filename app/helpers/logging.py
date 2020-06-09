from flask import current_app, g

def dlog(input):
    if g.debug:
        print(input)
