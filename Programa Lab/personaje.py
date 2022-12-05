class Personaje():
    def __init__(self,nombre="",raza="",arma="",vida=0,daño=0,bonificacion=0, tipo=""):
        self.__nombre = nombre
        self.__raza = raza
        self.__arma = arma
        self.__vida = vida
        self.__daño = daño
        self.__bonificacion = bonificacion
        self.__tipo = tipo
    
    def __str__(self):
        pass
    def GetTipo(self):
        return self.__tipo
    def SetTipo(self, tipo):
        self.__tipo=tipo    
    
    def GetNombre(self):
        return self.__nombre
    def SetNombre(self, nombre):
        self.__nombre = nombre    
    
    def GetRaza(self):
        return self.__raza
    def SetRaza(self, raza):
        self.__raza = raza       
    
    def GetArma(self):
        return self.__arma
    def SetArma(self, arma):
        self.__arma = arma     
   
    def GetVida(self):
        return self.__vida
    def SetVida(self, vida):
        self.__vida = vida  
    
    def GetDaño(self):
        return self.__daño
    def SetDaño(self, daño):
        self.__daño = daño          
    
    def GetBonificacion(self):
        return self.__bonificacion
    def SetBonificacion(self, bonificacion):
        self.__bonificacion = bonificacion     


    def Historia():
        pass

    def Victoria():
        pass
    def Derrota():
        pass    

    def MensajeInicial():
        pass