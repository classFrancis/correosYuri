from dao.dao_datosLaborales import daoDatoslaborales

class DatosLaboralesDTO:
    
    def addDatosLaborales(self,fechaCont,cargo,depto,rutTrab):
        daodatoslaborales = daoDatoslaborales()
        resultado = daodatoslaborales.addDatosLaborales(fechaCont,cargo,depto,rutTrab)
        return resultado