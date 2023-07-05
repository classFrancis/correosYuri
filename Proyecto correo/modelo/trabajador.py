from modelo.usuario import Usuario
from modelo.datosLaborales import DatosLaborales
from modelo.cargasFamiliares import CargasFamiliares
from modelo.contactosDeEmergencia import ContactosDeEmergencia



class Trabajador:
    """
    La clase Trabajador representa a un empleado en el sistema. 
    Almacena datos personales, laborales, 
    información sobre la familia del trabajador (cargas familiares), y contactos de emergencia.
    
    Atributos:
        rutTrabajador (str): El RUT del trabajador.
        nombreTrabajador (str): El nombre del trabajador.
        generoTrabajador (str): El género del trabajador.
        telefonoTrabajador (str): El teléfono del trabajador.
        direccionTrabajador (str): La dirección del trabajador.
        usuario (obj): El objeto Usuario asociado al trabajador.
        datosLaborales (obj): El objeto DatosLaborales que contiene la información laboral del trabajador.
        cargasFamiliares (obj): El objeto CargasFamiliares que contiene la información sobre la familia del trabajador.
        contactosDeEmergencia (obj): El objeto ContactosDeEmergencia que contiene la información de contactos de emergencia del trabajador.
        
    Métodos:
        getRutTrabajador: Retorna el RUT del trabajador.
        setRutTrabajador: Establece el RUT del trabajador.
        
        getNombreTrabajador: Retorna el nombre del trabajador.
        setNombreTrabajador: Establece el nombre del trabajador.
        
        getGeneroTrabajador: Retorna el género del trabajador.
        setGeneroTrabajador: Establece el género del trabajador.
        
        getTelefonoTrabajador: Retorna el teléfono del trabajador.
        setTelefonoTrabajador: Establece el teléfono del trabajador.
        
        getDireccionTrabajador: Retorna la dirección del trabajador.
        setDireccionTrabajador: Establece la dirección del trabajador.
        
        getUsuario: Retorna el objeto Usuario del trabajador.
        setUsuario: Establece el objeto Usuario del trabajador.
        
        getDatosLaborales: Retorna el objeto DatosLaborales del trabajador.
        setDatosLaborales: Establece el objeto DatosLaborales del trabajador.
        
        getCargasFamiliares: Retorna el objeto CargasFamiliares del trabajador.
        setCargasFamiliares: Establece el objeto CargasFamiliares del trabajador.
        
        getContactosDeEmergencia: Retorna el objeto ContactosDeEmergencia del trabajador.
        setContactosDeEmergencia: Establece el objeto ContactosDeEmergencia del trabajador.
        
        __str__: Retorna una representación en cadena de caracteres de los datos del trabajador.
    """   
    def __init__(self,rutTrabajador,nombreTrabajador,generoTrabajador,telefonoTrabajador,direccionTrabajador,usuario,datosLaborales,cargasFamiliares,contactosDeEmergencia):
        self.__rutTrabajador = rutTrabajador
        self.__nombreTrabajador= nombreTrabajador
        self.__generoTrabajador = generoTrabajador
        self.__telefonoTrabajador = telefonoTrabajador
        self.__direccionTrabajador = direccionTrabajador
        self.__usuario = usuario
        self.__datosLaborales = datosLaborales
        self.__cargasFamiliares = cargasFamiliares
        self.__contactosDeEmergencia = contactosDeEmergencia
        
    def __str__(self):
        return f'|Rut: {self.__rutTrabajador} \n|Nombre: {self.__nombreTrabajador} \n|Género: {self.__generoTrabajador} \n|Teléfono: {self.__telefonoTrabajador} \n|Dirección: {self.__direccionTrabajador} \n------------------\n|Usuario\n------------------\n{self.__usuario} \n------------------\n|Datos Laborales\n------------------\n{self.__datosLaborales} \n------------------\n|Cargas Familiares\n------------------\n{self.__cargasFamiliares} \n------------------\n|Contactos de Emergencia\n------------------\n{self.__contactosDeEmergencia}'    

    def setRutTrabajador(self, rutTrabajador):
        self.__rutTrabajador = rutTrabajador

    def getRutTrabajador(self):
        return self.__rutTrabajador

    def setNombreTrabajador(self, nombreTrabajador):
        self.__nombreTrabajador = nombreTrabajador

    def getNombreTrabajador(self):
        return self.__nombreTrabajador

    def setGeneroTrabajador(self, generoTrabajador):
        self.__generoTrabajador = generoTrabajador

    def getGeneroTrabajador(self):
        return self.__generoTrabajador

    def setTelefonoTrabajador(self, telefonoTrabajador):
        self.__telefonoTrabajador = telefonoTrabajador

    def getTelefonoTrabajador(self):
        return self.__telefonoTrabajador

    def setDireccionTrabajador(self, direccionTrabajador):
        self.__direccionTrabajador = direccionTrabajador

    def getDireccionTrabajador(self):
        return self.__direccionTrabajador

    def setUsuario(self, usuario):
        self.__usuario = usuario

    def getUsuario(self):
        return self.__usuario

    def setDatosLaborales(self, datosLaborales):
        self.__datosLaborales = datosLaborales

    def getDatosLaborales(self):
        return self.__datosLaborales  
    
    def setCargasFamiliares(self, cargasFamiliares):
        self.__cargasFamiliares = cargasFamiliares

    def getCargasFamiliares(self):
        return self.__cargasFamiliares
    def setContactosDeEmergencia(self, contactosDeEmergencia):
        self.__contactosDeEmergencia = contactosDeEmergencia

    def getContactosDeEmergencia(self):
        return self.__contactosDeEmergencia    


        