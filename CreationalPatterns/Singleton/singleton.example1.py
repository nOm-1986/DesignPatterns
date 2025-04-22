"""
    Singleton - Creational Pattern

    - Only one instance of the class
    - Global access to that instance
    As a global variable, singleton patter allows us to access the object anywhere in our system program. And prevents the developer to write the funtionality in other part of the program.
"""
import uuid

class MySingleton:
    _instance = None
    id = None

    # This method is call when we create a instance of objet. It is called before __init__.
    def __new__(cls):
        if cls._instance is None: # if instance doesn't exits just create new one
            print("Creating the new Singleton's instance")
            cls._instance = super(MySingleton, cls).__new__(cls)
            cls.id = uuid.uuid4()
        return cls._instance
    

singleton1 = MySingleton()
print(f"Intance 1 ID: {singleton1.id}")

singleton2 = MySingleton()
print(f"Intance 2 ID: {singleton2.id}")

singleton3 = MySingleton()
print(f"Intance 3 ID: {singleton3.id}")