from modelo.trabajador import Trabajador
from modelo.usuario import Usuario
from modelo.datosLaborales import DatosLaborales
from modelo.cargasFamiliares import CargasFamiliares
from modelo.contactosDeEmergencia import ContactosDeEmergencia
from utils.encoder import Encoder
from dao.dao_trabajador import daoTrabajador
import datetime

class TrabajadorDTO:
    
    def validarLogin(self, nombreUsuario, claveUsuario):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.validarLogin(nombreUsuario, Encoder().encode(claveUsuario))
        return resultado
    
    def validarRut(self,rut):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.validarRut(rut)
        return resultado   
    
    def tipoDeUsuario(self,nombreUsuario, claveUsuario):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.tipoDeUsuario(nombreUsuario, claveUsuario)
        return resultado
    
    def mostrarDatosPorUseryPass(self,nombreUsuario, claveUsuario):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.mostrarDatosPorUseryPass(nombreUsuario, claveUsuario)
        date = resultado[9]
        fecha = date.strftime('%d-%m-%Y')
        trabajador = Trabajador(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],Usuario(resultado[5],resultado[6],resultado[7]),DatosLaborales(resultado[8],fecha,resultado[10],resultado[11]),CargasFamiliares(resultado[12],resultado[13],resultado[14],resultado[15],resultado[16]),ContactosDeEmergencia(resultado[17],resultado[18],resultado[19],resultado[20],resultado[21]))
        return trabajador
    
    def addTrabajador(self,rutTrab,nombTrab,generoTrab,telefonoTrab,direccionTrab):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.addTrabajador(rutTrab,nombTrab,generoTrab,telefonoTrab,direccionTrab)
        return resultado
    
    def modificarDatosPersonales(self,nombre,genero,telefono,direccion,rut):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.modificarDatosPersonales(nombre,genero,telefono,direccion,rut)
        return resultado

    def showDataGender(self, gender):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.showDataGender(gender)
        lista = []
        if resultado is not None:
            for u in resultado:
                worker = Trabajador(u[0],u[1],u[2],u[3],u[4],Usuario(u[5],u[6],u[7]),DatosLaborales(u[8],u[9],u[10],u[11]),CargasFamiliares(u[12],u[13],u[14],u[15],u[16]),ContactosDeEmergencia(u[17],u[18],u[19],u[20],u[21]))
                lista.append(worker)
        return lista

    def showDataCargo(self, cargo):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.showDataCargo(cargo)
        lista = []
        if resultado is not None:
            for u in resultado:
                worker = Trabajador(u[0],u[1],u[2],u[3],u[4],Usuario(u[5],u[6],u[7]),DatosLaborales(u[8],u[9],u[10],u[11]),CargasFamiliares(u[12],u[13],u[14],u[15],u[16]),ContactosDeEmergencia(u[17],u[18],u[19],u[20],u[21]))
                lista.append(worker)
        return lista

    def showDataAreaDep(self, area, dep):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.showDataAreaDep(area, dep)
        lista = []
        if resultado is not None:
            for u in resultado:
                worker = Trabajador(u[0],u[1],u[2],u[3],u[4],Usuario(u[5],u[6],u[7]),DatosLaborales(u[8],u[9],u[10],u[11]),CargasFamiliares(u[12],u[13],u[14],u[15],u[16]),ContactosDeEmergencia(u[17],u[18],u[19],u[20],u[21]))
                lista.append(worker)
        return lista

    def showAll(self):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.showAll()
        lista = []
        if resultado is not None:
            for u in resultado:
                worker = Trabajador(u[0],u[1],u[2],u[3],u[4],Usuario(u[5],u[6],u[7]),DatosLaborales(u[8],u[9],u[10],u[11]),CargasFamiliares(u[12],u[13],u[14],u[15],u[16]),ContactosDeEmergencia(u[17],u[18],u[19],u[20],u[21]))
                lista.append(worker)
        return lista

    def deleteDatoTrabajador(self, dato,rut):
        daotrabajador = daoTrabajador()
        resultado = daotrabajador.deleteDatoTrabajador(dato, rut)
        return resultado