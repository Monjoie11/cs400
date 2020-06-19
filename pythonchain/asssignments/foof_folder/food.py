class Food:

    clskind = 'this is what i am'
    clsname = 'this is who i am'

    def __init__(self, kind='a kind', name='a name'):
        self.kind = kind
        self.name = name

    def __repr__(self):
        print(self.kind, self.name)
        

    def describe(self):
        print("I'm a little {} and this is my {}".format(self.kind, self.name))

    
    @classmethod
    def clsdescribe(cls):
        print('this is what the class method says {}...{}'.format(cls.clskind, cls.clsname))



