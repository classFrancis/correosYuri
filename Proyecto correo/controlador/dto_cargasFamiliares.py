from dao.dao_cargasFamiliares import daoCargasFamiliares

class CargasFamiliaresDTO:
    
    def addCargasFamiliares(self,rutCarga,nombreCarga,parentesco,generoCarga,rutTrab):
        daocargasfamiliares = daoCargasFamiliares()
        resultado = daocargasfamiliares.addCargasFamiliares(rutCarga,nombreCarga,parentesco,generoCarga,rutTrab)
        return resultado