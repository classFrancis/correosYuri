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
            
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    
    def obtenerDatosDeCargas(self,rutTrab):
        sql = "select rut_carga,nombre_carga,parentesco,genero_carga from cargasFamiliares where rut_trabajador = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (rutTrab,))

            resultado = cursor.fetchall()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def modificarCargasFamiliares(self,rutCarga,nombreCarga,parentesco,generoCarga,rut,rutCar):
        sql ="""UPDATE cargasFamiliares
                SET rut_carga = %s,
                    nombre_carga = %s,
                    parentesco = %s,
                    genero_carga = %s
                WHERE rut_trabajador = %s and rut_carga = %s;"""
        c = self.getConex()
        cursor = c.getConex().cursor()
        cursor.execute(sql, (rutCarga, nombreCarga,parentesco ,generoCarga ,rut,rutCar))
        c.getConex().commit()   
        if c.getConex().is_connected():
            c.closeConex()

    def deleteCargaFam(self, dato):
        sql = "DELETE FROM cargasfamiliares WHERE rut_carga = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (dato,))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Datos modificados satisfactoriamente"
            else:
                mensaje = "No se realizaron cambios"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos..vuelva a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje