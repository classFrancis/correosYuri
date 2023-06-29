from conex import conn 
import traceback

class daoContactosDeEmergencia:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "correosyuri")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
    
    def addContactosDeEmergencia(self,rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab):
        sql = """INSERT INTO contactosEmergencia(rut_contacto, nombre_contacto, relacionTrabajador, telefono_contacto, rut_trabajador)
                    VALUES(%s, %s, %s, %s, %s);"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (rutContact, nombreContact,relacionTrab ,telefonoContact ,rutTrab))
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
    
    def obtenerDatosDeContactos(self,rutTrab):
        sql = """select rut_contacto,nombre_contacto,relacionTrabajador,telefono_contacto 
                    from contactosEmergencia 
                    where rut_trabajador = %s"""
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
    
    def modificarContactosDeEmergencia(self,rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab,rutCont):
        sql ="""UPDATE contactosEmergencia
        SET rut_contacto = %s,
            nombre_contacto = %s,
            relacionTrabajador = %s,
            telefono_contacto = %s
        WHERE rut_trabajador = %s and rut_contacto = %s;"""
        c = self.getConex()
        cursor = c.getConex().cursor()
        cursor.execute(sql, (rutContact,nombreContact,relacionTrab,telefonoContact,rutTrab,rutCont))
        c.getConex().commit()   
        if c.getConex().is_connected():
            c.closeConex()

    def deleteContactEmer(self, dato):
        sql = "DELETE FROM contactosemergencia WHERE rut_contacto = %s"
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