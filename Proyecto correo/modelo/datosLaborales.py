

class DatosLaborales():
    def __init__(self,idDatosLaborales,fechaContratacion,cargo,depto):
        self.__idDatosLaborales = idDatosLaborales
        self.__fechaContratacion = fechaContratacion
        self.__cargo = cargo
        self.__depto = depto
        
    def __str__(self):
        return f'|ID: {self.__idDatosLaborales} \n|Fecha de Contratación: {self.__fechaContratacion} \n|Cargo: {self.__cargo}\n|Departamento: {self.__depto}'

    def setIdDatosLaborales(self, idDatosLaborales):
        self.__idDatosLaborales = idDatosLaborales

    def getIdDatosLaborales(self):
        return self.__idDatosLaborales

    def setFechaContratacion(self, fechaContratacion):
        self.__fechaContratacion = fechaContratacion

    def getFechaContratacion(self):
        return self.__fechaContratacion
    
    def setDepto(self, cargo):
        self.__cargo = cargo

    def getDepto(self):
        return self.__cargo

    def setDepto(self, depto):
        self.__depto = depto

    def getDepto(self):
        return self.__depto
            
        