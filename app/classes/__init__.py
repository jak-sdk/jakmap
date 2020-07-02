from importlib import import_module

## there must be a better way of separating spec level code
## and backend level implementation than this

# use pythons ability to create classes on the fly to 
# munge together classes/SomeClass with classes/backends/someBackend/SomeClass
# and redefine it here

# this essentially layers the backend class over the top of the one in this dir,
# filling in the gaps left by @JMAP.abstract 
#  (and possibly clobbering everything else, this is a Wild-West style of 
#       implementing a configurable implementation)

# todo:
#  1. come up with a sensible way of configuring this, backends should be configurable
#     without diving into code (especially __init__.py, this is cruel)
#  2. delete all of this and use a better way, possibly at application construction
#
def load(classes, overload_dir=None):
    for filename,classname in classes.items():
        mod  = import_module("classes."+filename)
        cls = getattr(mod, classname)
    
        if overload_dir:
            ovmod = import_module("classes.backends."+overload_dir+"."+filename)
            ovcls = getattr(ovmod, classname)
            globals()[classname] = type(classname, (ovcls, cls), {})
        else:
            globals()[classname] = cls
    


#        <filename>        <classname>
cs = {'session_resource':'SessionResource',
      'jmap':'JMAP',
      'core':'Core',
      'result_reference':'ResultReference'
     }

cso = {
      'user':'User',
      'mailbox':'Mailbox'
    }

load(cs)

load(cso, "mysql")
