from dao.dao_contactosDeEmeregencia import daoContactosDeEmergencia

class ContactosDeEmergenciaDTO:
    
    def addContactosDeEmergencia(self,rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab):
        daocontactosdeemergencia = daoContactosDeEmergencia()
        resultado = daocontactosdeemergencia.addContactosDeEmergencia(rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab)
        return resultado