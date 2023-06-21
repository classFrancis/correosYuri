from modelo.usuario import Usuario
from modelo.datosLaborales import DatosLaborales
from modelo.cargasFamiliares import CargasFamiliares
from modelo.contactosDeEmergencia import ContactosDeEmergencia



class Trabajador:
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
        return f'Rut: {self.__rutTrabajador} \nNombre: {self.__nombreTrabajador} \nGénero: {self.__generoTrabajador} \nTeléfono: {self.__telefonoTrabajador} \nDirección: {self.__direccionTrabajador} \n------------------\nUsuario: \n{self.__usuario} \n------------------\nDatos Laborales: \n{self.__datosLaborales} \n------------------\nCargas Familiares: \n{self.__cargasFamiliares} \n------------------\nContactos de Emergencia: \n{self.__contactosDeEmergencia}'    

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


        