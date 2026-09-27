'''OOPS CONCEPTS
1. Class
2. Object 
3. Inheritance
4. Polymorphism
5. Encapsulation
6. Abstraction'''
class Animal:
    name="sandeep reddy vanga"
    def __init__(self):
        print(f"the director is {self.name}")
e=Animal()
print(e.name)
class Tiger(Animal):
    def run(self):
        print("tiger is nothing but sandeep reddy vanga")
t=Tiger()
t.run()