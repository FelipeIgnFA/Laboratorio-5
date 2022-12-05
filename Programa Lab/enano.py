import random
from personaje import Personaje
class Enano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida=0, daño=0, bonificacion=0,clan="",tipo=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion,tipo)
        self.__clan=clan
    def GetClan(self):
        return self.__clan

    def SetClan(self,clan):
        self.__clan = clan 

    def AumentoVida():
        vidainicial = float(Enano.GetVida() + random.randint(50,100))
        return vidainicial

    def Historia():
        print("Los enanos son debiles pero valerosos ")    
    def Derrota():
        print("Maldita sea he perdido")
    def Victoria():
        print("UF apestas, te he vencido")    
