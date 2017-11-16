class node(object):
    def __int__(self,data):
        self.data=data
        self.next=None
class linkedlist(object):
    def __int__(self):
        self.head=None
    def IDAnsert(self,data):
        nextnode=node(data)

l=linkedlist()
l.insert(1)
