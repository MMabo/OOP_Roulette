class Outcome:
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def winamount(self, amount):
        return self.odds*amount

    def __eq__(self, other):
        if self.name == other.name:
            return True
        
    def __ne__(self,other):
        if self.name != other.name:
            return True

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return "{0} ({1}:11)".format(self.name,self.odds) # name (odds:1)

    def __repr__(self):
        return "{class_:s}({name!r}, {odds!r})".format(class_=type(self).__name__, **vars(self) )

class Bin(frozenset):
    pass
    
class Wheel():
