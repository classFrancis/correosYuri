

class CargasFamiliares():
    def __init__(self,idCarga,rutCarga,nombreCarga,parentescoCarga,generoCarga):
        self.__idCarga = idCarga
        self.__rutCarga = rutCarga
        self.__nombreCarga = nombreCarga
        self.__parentescoCarga = parentescoCarga
        self.__generoCarga = generoCarga
    
    def __str__(self):
        return f'|D: {self.__idCarga} \n|RUT: {self.__rutCarga} \n|Nombre: {self.__nombreCarga} \n|Parentesco: {self.__parentescoCarga} \n|Género: {self.__generoCarga}'    

    def setIdCarga(self, idCarga):
        self.__idCarga = idCarga

    def getIdCarga(self):
        return self.__idCarga

    def setRutCarga(self, rutCarga):
        self.__rutCarga = rutCarga

    def getRutCarga(self):
        return self.__rutCarga

    def setNombreCarga(self, nombreCarga):
        self.__nombreCarga = nombreCarga

    def getNombreCarga(self):
        return self.__nombreCarga

    def setParentescoCarga(self, parentescoCarga):
        self.__parentescoCarga = parentescoCarga

    def getParentescoCarga(self):
        return self.__parentescoCarga

    def setGeneroCarga(self, generoCarga):
        self.__generoCarga = generoCarga

    def getGeneroCarga(self):
        return self.__generoCarga
 