from typing import Protocol

# Protocol
# Es una opción nueva que viene con el PEP544 para python 3.8
# Es algo implicito para declarar interfaces
# Solo es de ayuda si hacemos uso de type hints y verificación estática de tipos

class IAnimal(Protocol):
    """ Esta clase define la interfaz IAnimal - se utiliza la I para denotar que es interfaz """

    def colocaDatos(self, nombre: str, peso:float)-> bool:
        """
        Parameteres
        ------------
        nombre : str
            Nombre del animal
        peso : float
            Peso del animal
        
        Returns
        -------
        IAnimal
        Indica si el animal tiene sobrepeso
        """

    def caminar(self, metros: int) -> None:
        """"
        Parameters
        --------------
        metros : int
            Cantidad de metros que camina
        Returns
        --------------
        None
        """

class Gato(IAnimal):
    def colocaDatos(self, nombre: str, peso: int)-> bool:
        self.nombre = nombre
        self.peso = peso

        if self.peso > 7: return True
        else: return False
    
    def caminar2(self, metros: int) -> None:
        if metros > 70 and metros < 850:
            print("Pinche gato callejero")

    def __repr__(self):
        return f"Coño {self.nombre}"


if __name__ == "__main__":
    miGato = Gato()
    miGato.colocaDatos('guau', 10)
    miGato.caminar(450)
    print(miGato)