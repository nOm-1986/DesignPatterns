""" 
El GIL (Global Interpreter Lock) en Python es un mecanismo que asegura que solo un hilo puede ejecutar código Python a la vez en una instancia del intérprete CPython
El GIL fue implementado como una forma fácil de administrar la memoria y para simplificar tareas como la recolección de basura.
También es útil para evitar situaciones como los race conditions. Sin embargo trae otros problemas importantes, como limitar el paralelismo real.
"""

import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        
        return cls._instance