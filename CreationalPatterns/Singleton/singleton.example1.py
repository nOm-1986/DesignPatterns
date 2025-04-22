"""
    Singleton - Creational Pattern

    - Only one instance of the class
    - Global access to that instance
    As a global variable, singleton patter allows us to access the object anywhere in our system program. And prevents the developer to write the funtionality in other part of the program.
"""

class MySingleton:
    _instance = None

    # This method is call when we create a instance of objet. It is called before __init__.
    def __new__(cls):
        if cls._instance is None: # if instance doesn't exits just create new one
            print("Creating the new Singleton's instance")
            cls._instance = super(MySingleton, cls).__new__(cls)
        return cls._instance
    

singleton = MySingleton()