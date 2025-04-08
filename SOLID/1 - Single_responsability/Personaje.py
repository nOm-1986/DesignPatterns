from abc import ABC, abstractmethod

class Personaje(ABC):

    def __init__(yomismo, nombre, nivel=1, experiencia=0, max_exp=50, exp_por_ataque=1):
        yomismo._nombre = nombre
        yomismo._nivel = nivel
        yomismo._experiencia = experiencia
        yomismo._maxima_experiencia = max_exp
        yomismo._exp_por_ataque = exp_por_ataque

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def _mejorar_habilidades(self):
        pass