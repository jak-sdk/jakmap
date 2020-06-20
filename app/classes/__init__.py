from importlib import import_module

cs = {'session_resource':'SessionResource',
      'user':'User',
      'jmap':'JMAP',
      'mailbox':'Mailbox',
      'core':'Core',
      'result_reference':'ResultReference'
     }

for k,v in cs.items():
    b  = import_module("classes."+k)
    ba = getattr(b, v)

    vars()[v] = ba

    #ov = import_module("objs.override."+k)
    #ova = getattr(ov, v)
    #vars()[v] = type(k, (ova, ba), {})

