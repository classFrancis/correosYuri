

class DatosLaborales():
    """
    La clase DatosLaborales representa la información laboral de un empleado en el sistema. 
    Almacena el ID de los datos laborales, la fecha de contratación, el cargo y el departamento del empleado.
    
    Atributos:
        idDatosLaborales (str): La identificación de los datos laborales.
        fechaContratacion (datetime): La fecha de contratación del empleado.
        cargo (str): El cargo del empleado.
        depto (str): El departamento en el que trabaja el empleado.
        
    Métodos:
        getIdDatosLaborales: Retorna la identificación de los datos laborales.
        setIdDatosLaborales: Establece la identificación de los datos laborales.
        
        getFechaContratacion: Retorna la fecha de contratación del empleado.
        setFechaContratacion: Establece la fecha de contratación del empleado.
        
        getCargo: Retorna el cargo del empleado.
        setCargo: Establece el cargo del empleado.
        
        getDepto: Retorna el departamento en el que trabaja el empleado.
        setDepto: Establece el departamento en el que trabaja el empleado.
        
        __str__: Retorna una representación en cadena de caracteres de los datos laborales del empleado.
    """
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
    
    def setCargo(self, cargo):
        self.__cargo = cargo

    def getCargo(self):
        return self.__cargo

    def setDepto(self, depto):
        self.__depto = depto

    def getDepto(self):
        return self.__depto
            
        