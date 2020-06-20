#import _jakmap
from flask import Flask,request,render_template,send_from_directory,g,abort
from classes import *
from _db import init_db
from helpers import *
import json
from definitions import *

# yuck
GLOBAL = {}

app = Flask(__name__)

#app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config.from_pyfile('config')

GLOBAL['app'] = app

@app.before_request
def before_request():
    init_db()
    #check or setup auth here?
    g.user = User()

#@app.route('/css/<path:path>')
#def send_css(path):
#    return send_from_directory('static/css', path)
#@app.route('/js/<path:path>')
#def send_js(path):
#    return send_from_directory('static/js', path)
#@app.route('/icons/<path:path>')
#def send_icons(path):
#    return send_from_directory('static/icons', path)
#@app.route('/img/<path:path>')
#def send_img(path):
#    return send_from_directory('static/img', path)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/.well-known/jmap', methods=['GET', 'POST'])
def get_session_resource():
    # are they authenticated?
    if request.method == "GET":
        return jdump(JMAP.sessionResource())
    else:
        jmap_request = request.get_json(silent=True)
        if jmap_request is None:
            dprint("aborting 400 - invalid JSON")
            raise InvalidJSON() 
        return jdump(JMAP.process(jmap_request))

#@app.route('/foo')
#def foo():
#    return str(app.config)

# invalidjson, unknowncapability etc
@app.errorhandler(JakmapException)
def errorhandler(e):
    return e.message, e.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
