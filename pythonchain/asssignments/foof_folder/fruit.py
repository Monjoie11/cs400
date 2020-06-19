from food import Food

class Fruit(Food):

    def __init__(self, kind, name):
        super(kind, name)
        self.kind = kind
        self.name = name

        


    def clean(self):
        print('I am clean {}...{}'.format(self.kind, self.name))


avacado = Fruit('a fruit', 'an avacado')
avacado.clean()





