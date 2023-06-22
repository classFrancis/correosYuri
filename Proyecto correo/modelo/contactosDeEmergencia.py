

class ContactosDeEmergencia():
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
        
        
        