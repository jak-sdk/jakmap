class Filter(object):
    def __init__(self, args, filterableConditions):
        self.__valid = True
        self.filterableConditions = filterableConditions

        if args == '': # or None? null? what's the correct empty filter?
            pass

        # dict matching FilterOperator
        elif args.keys() == ['operator', 'conditions']:
            self.operator = args['operator']
            self.conditions = []
            for thing in args['conditions']:
                self.conditions.append(Filter(thing, self.filterableConditions))
        else: # FilterCondition
            self.filterCondition = {}
            for prop, value in args.items():
                if prop not in self.filterableConditions:
                    self.__valid = False
                self.filterCondition[prop] = value

    def matches(self, obj):
        if not self.valid:
            return None

        # note if the object doesn't have all the prop fields then you'll get weird behaviour, presumably it always will, that's why we pass in what fields are filterable on
        try:
            if self.filterCondition:
                return all([obj[prop] == value for prop, value in self.filterCondition.items()])
        except AttributeError:
            pass

        if self.operator == 'AND':
            return all([cond.matches(obj) for cond in self.conditions])

        elif self.operator == 'OR':
            return any([cond.matches(obj) for cond in self.conditions])

        elif self.operator == 'NOT':
            return not(any([cond.matches(obj) for cond in self.conditions]))

        # raise error


    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator):
        if operator in ['AND', 'OR', 'NOT']:
            self.__operator = operator
        else:
            self.__valid = False

    @property
    def valid(self):
        # if we're ok, then defer to children
        try:
            return all([cond.valid for cond in self.conditions])
        except AttributeError:
            return self.__valid
            


if __name__ == "__main__":
    q = {'operator': 'OR', 'conditions':[
        {'operator':'AND', 'conditions':[{'hat':'red'},{'jacket':'yellow'}]},
        {'jacket':'red'}
    ]}
    p1 = {'hat':'red', 'jacket':'yellow'}
    p2 = {'hat':'none','jacket':'yellow'}
    p3 = {'hat':'none','jacket':'red'}
    keys = p1.keys()
    f = Filter(q, keys)
    for p in [p1,p2,p3]:
        print(f.matches(p))
