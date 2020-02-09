# Polymorphism
def polyexample1():
    print('=========== POLYMORMIS USING LEN FUNCTION ===================')
    numbers = [1,5,56,6,7]
    name = 'John Doe'
    dict = {'name': 'John', 'last name': 'Doe'}

    print(len(numbers))
    print(len(name))
    print(len(dict))

print('============= POLYMORPHISM USING CLASS FUNCTIONS ==================')
class Car:
    def drive(self):
        print('drive slowly and carefully')

class Motocycle:
    def drive(self):
        print('enjoy the fast drive and no traffic')
    
class ElectricCar(Car):
    pass
    # overriding the function from parent class
    def drive(self, name=''):
        if name=='':
            print('thank you for caring about environment, safe drive!')
        else: 
            print(f"Happy drive with your {name}!!!")


corola = Car()
hdavidson = Motocycle()
tesla = ElectricCar()

corola.drive()
hdavidson.drive()
tesla.drive()
tesla.drive('Model Y')
