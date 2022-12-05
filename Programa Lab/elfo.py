from personaje import Personaje
class Elfo(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida=0, daño=0, bonificacion=0, reino="",tipo=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion,tipo)
        self.__reino = reino
 

    def GetReino(self):
        return self.__reino

    def SetReino(self,reino):
        self.reino = reino    

    def QuitaVida():
        vidainicio= (Elfo.GetVida -(Elfo.GetVida * 0.1))
        return vidainicio

    def Historia():
        print("Elfo habiles con magia y agiles")       

    def Derrota():
        print("he sido derrotado")
    def Victoria():
        print("Siempre confia en el poder divino")        