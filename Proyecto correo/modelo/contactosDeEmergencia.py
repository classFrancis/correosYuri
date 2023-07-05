

class ContactosDeEmergencia():
    """
    La clase ContactosDeEmergencia representa un contacto de emergencia para un empleado en el sistema. 
    Almacena el ID del contacto, RUT del contacto, nombre del contacto, 
    la relación con el trabajador, y el número de teléfono del contacto.
    
    Atributos:
        idContacto (str): La identificación del contacto de emergencia.
        rutContacto (str): El RUT del contacto de emergencia.
        nombreContacto (str): El nombre del contacto de emergencia.
        relacionConTrabajador (str): La relación del contacto de emergencia con el empleado.
        telefonoContacto (str): El número de teléfono del contacto de emergencia.
        
    Métodos:
        getIdContacto: Retorna la identificación del contacto de emergencia.
        setIdContacto: Establece la identificación del contacto de emergencia.
        
        getRutContacto: Retorna el RUT del contacto de emergencia.
        setRutContacto: Establece el RUT del contacto de emergencia.
        
        getNombreContacto: Retorna el nombre del contacto de emergencia.
        setNombreContacto: Establece el nombre del contacto de emergencia.
        
        getRelacionConTrabajador: Retorna la relación del contacto de emergencia con el empleado.
        setRelacionConTrabajador: Establece la relación del contacto de emergencia con el empleado.
        
        getTelefonoContacto: Retorna el número de teléfono del contacto de emergencia.
        setTelefonoContacto: Establece el número de teléfono del contacto de emergencia.
        
        __str__: Retorna una representación en cadena de caracteres del contacto de emergencia.
    """
    def __init__(self,idContacto,rutContacto,nombreContacto,relacionConTrabajador,telefonoContacto):
        self.__idContacto = idContacto
        self.__rutContacto = rutContacto
        self.__nombreContacto = nombreContacto
        self.__relacionConTrabajador = relacionConTrabajador
        self.__telefonoContacto = telefonoContacto
    
    def __str__(self):
        return f'|ID: {self.__idContacto} \n|RUT: {self.__rutContacto} \n|Nombre: {self.__nombreContacto} \n|Relación con Trabajador: {self.__relacionConTrabajador} \n|Teléfono Contacto: {self.__telefonoContacto}'

    def setIdContacto(self, idContacto):
        self.__idContacto = idContacto

    def getIdContacto(self):
        return self.__idContacto

    def setRutContacto(self, rutContacto):
        self.__rutContacto = rutContacto

    def getRutContacto(self):
        return self.__rutContacto

    def setNombreContacto(self, nombreContacto):
        self.__nombreContacto = nombreContacto

    def getNombreContacto(self):
        return self.__nombreContacto

    def setRelacionConTrabajador(self, relacionConTrabajador):
        self.__relacionConTrabajador = relacionConTrabajador

    def getRelacionConTrabajador(self):
        return self.__relacionConTrabajador

    def setTelefonoContacto(self, telefonoContacto):
        self.__telefonoContacto = telefonoContacto

    def getTelefonoContacto(self):
        return self.__telefonoContacto   
        
        
        