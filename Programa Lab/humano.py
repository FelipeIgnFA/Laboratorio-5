from personaje import Personaje
class Humano(Personaje):
    def __init__(self, nombre="", raza="", arma="", vida=0, daño=0, bonificacion=0, familia="",tipo=""):
        super().__init__(nombre, raza, arma, vida, daño, bonificacion,tipo)
        self.__familia = familia

    def GetFamilia(self):
        return self.__familia
    def SetFamilia(self, familia):
        self.__familia=familia    

    def SuperBono():
        bono= ((Humano.GetDaño) + ((Humano.GetDaño * 0.1)))
        return bono         

    def Historia():
        print("Humanos se creen dueños del mundo, que demuestren su valor en batalla")

    def Derrota():
        print("como he podido perder")
    def Victoria():
        print("Como de costumbre he ganado ")                 