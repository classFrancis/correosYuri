from dao.dao_contactosDeEmeregencia import daoContactosDeEmergencia

class ContactosDeEmergenciaDTO:
    
    def addContactosDeEmergencia(self,rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab):
        daocontactosdeemergencia = daoContactosDeEmergencia()
        resultado = daocontactosdeemergencia.addContactosDeEmergencia(rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab)
        return resultado
    
    def obtenerDatosDeContactos(self,rutTrab):
        daocontactosdeemergencia = daoContactosDeEmergencia()
        resultado = daocontactosdeemergencia.obtenerDatosDeContactos(rutTrab)
        return resultado
    
    def modificarContactosDeEmergencia(self,rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab,rutCont):
        daocontactosdeemergencia = daoContactosDeEmergencia()
        resultado = daocontactosdeemergencia.modificarContactosDeEmergencia(rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab,rutCont)
        return resultado