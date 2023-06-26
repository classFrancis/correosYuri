from conex import conn 
import traceback

class daoCargasFamiliares:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "correosyuri")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
    
    def addCargasFamiliares(self,rutCarga,nombreCarga,parentesco,generoCarga,rutTrab):
        sql = """INSERT INTO cargasFamiliares(rut_carga, nombre_carga, parentesco, genero_carga, rut_trabajador)
                    VALUES(%s, %s, %s, %s, %s);"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (rutCarga, nombreCarga,parentesco ,generoCarga ,rutTrab))
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