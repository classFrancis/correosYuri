

class Usuario():
    def __init__(self,idUsuario,nombre,claveAcceso):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__claveAcceso = claveAcceso
        
    def __str__(self):
        return f'|ID: {self.__idUsuario} \n|Nombre: {self.__nombre}'

    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    def getIdUsuario(self):
        return self.__idUsuario

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setClaveAcceso(self, claveAcceso):
        self.__claveAcceso = claveAcceso

    def getClaveAcceso(self):
        return self.__claveAcceso
        
        
        