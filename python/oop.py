# class person:
#     # attributes
#     # name:str
#     # age:int

#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def __del__(self):
#         print(f"{self.name} has been deleted.")
    
#     # Methods
#     def say_hi(self):
#         print(f"Hello, My name is {self.name}.")

# p1:person = person("Ram", 20)
# p2:person = person("Shyam", 20)

# print(p1.name)
# print(p1.age)

# p1.say_hi()
# p2.say_hi()


# class Animal:
#     def __init__(self, name, age, no_leg):
#         self.__name = name
#         self.age = age
#         self.no_leg = no_leg
#     def can_walk(self):
#         return f"{self.name} is my pet animal that have {self.no_leg} and they can walk."

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, newname):
#         self.__name = newname

# class Dog(Animal):
#     def __init__(self, name, age, no_leg, breed):
#         super().__init__(name, age, no_leg)

#         self.breed = breed  

# jack = Dog("Aman", 23, 4, "bhushya")
# jack.name = "Siroj"
# print(jack.can_walk())


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)

account.deposit(500)

account.withdraw(1000)

print(account.get_balance())