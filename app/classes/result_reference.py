class ResultReference:
    #resultOf = None 
    #name = None
    #path = None
    
    def __init__(self, method_call_id, name, path):
        self.resultOf = method_call_id
        self.name = name
        self.path = path
    
    def getPreviousResults(self):
        # look for resultOf + name combo in JMAP previous method calls
        # resolve path to a subset of the results object
        return "foo"

