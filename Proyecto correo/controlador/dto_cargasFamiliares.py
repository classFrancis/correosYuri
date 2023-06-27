from modelo.cargasFamiliares import CargasFamiliares
from dao.dao_cargasFamiliares import daoCargasFamiliares

class CargasFamiliaresDTO:
    
    def addCargasFamiliares(self,rutCarga,nombreCarga,parentesco,generoCarga,rutTrab):
        daocargasfamiliares = daoCargasFamiliares()
        resultado = daocargasfamiliares.addCargasFamiliares(rutCarga,nombreCarga,parentesco,generoCarga,rutTrab)
        return resultado
    
    def obtenerDatosDeCargas(self,rutTrab):
        daocargasfamiliares = daoCargasFamiliares()
        resultado = daocargasfamiliares.obtenerDatosDeCargas(rutTrab)
        return resultado
    
    def modificarCargasFamiliares(self,rutCarga,nombreCarga,parentesco,generoCarga,rutTrab,rutCar):
        daocargasfamiliares = daoCargasFamiliares()
        resultado = daocargasfamiliares.modificarCargasFamiliares(rutCarga,nombreCarga,parentesco,generoCarga,rutTrab,rutCar)
        return resultado