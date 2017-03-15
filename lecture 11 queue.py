class Queue(object):
    
    def __init__(self):
        self.qList = []
        
    def insert(self, e):
        self.qList.append(e)
        
    def remove(self):
        try:
            return self.qList.pop(0)
        except:
            raise ValueError()
            
    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.qlist]) + '}'  