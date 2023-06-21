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
    
        