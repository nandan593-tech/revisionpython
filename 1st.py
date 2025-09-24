class Dog:
    legs=4
    def eat(self):
        print("Dog is eating")
    def speak(self):
        print("Dog barks")
d=Dog();#Dog is a constructor and d is an object
d.eat();
d.speak();
print('Dog has',d.legs,'legs')
Dog.eat(d);#d as object