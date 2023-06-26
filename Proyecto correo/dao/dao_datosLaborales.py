from conex import conn 
import traceback

class daoDatoslaborales:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "correosyuri")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
    
    def addDatosLaborales(self,fechaCont,cargo,depto,rutTrab):
        sql = """INSERT INTO datosLaborales(fecha_contratacion, cargo, departamento, rut_trabajador)
                    VALUES(%s, %s, %s, %s);"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, ( fechaCont,cargo ,depto ,rutTrab))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje ="Datos agregados satisfactoriamente"
            else:
                mensaje="No se Agregaron datos"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje                  