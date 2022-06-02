class dog:
    def __init__(self,no_of_eyes,color):
        self.no_of_eyes=no_of_eyes
        self.color=color
    def barking(self):
        print("woof woof!")
german_shepherd=dog(no_of_eyes=2,color='grey')
dodger=dog(color='white',no_of_eyes=1)
dobberman=dog(2,'black')
print(german_shepherd.color)
print(dodger.no_of_eyes,dodger.color)
print(dobberman.color)

dobberman.color='dark-brown'
print(dobberman.color)
print(dobberman.no_of_eyes)
dobberman.barking()


