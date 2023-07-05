

class CargasFamiliares():
    """
    La clase CargasFamiliares representa una carga familiar de un empleado en el sistema. 
    Almacena el ID de la carga, RUT de la carga, nombre de la carga, 
    parentesco de la carga, y el género de la carga.
    
    Atributos:
        idCarga (str): La identificación de la carga familiar.
        rutCarga (str): El RUT de la carga familiar.
        nombreCarga (str): El nombre de la carga familiar.
        parentescoCarga (str): El parentesco de la carga familiar con el empleado.
        generoCarga (str): El género de la carga familiar.
        
    Métodos:
        getIdCarga: Retorna la identificación de la carga familiar.
        setIdCarga: Establece la identificación de la carga familiar.
        
        getRutCarga: Retorna el RUT de la carga familiar.
        setRutCarga: Establece el RUT de la carga familiar.
        
        getNombreCarga: Retorna el nombre de la carga familiar.
        setNombreCarga: Establece el nombre de la carga familiar.
        
        getParentescoCarga: Retorna el parentesco de la carga familiar con el empleado.
        setParentescoCarga: Establece el parentesco de la carga familiar con el empleado.
        
        getGeneroCarga: Retorna el género de la carga familiar.
        setGeneroCarga: Establece el género de la carga familiar.
        
        __str__: Retorna una representación en cadena de caracteres de la carga familiar.
    """
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
 