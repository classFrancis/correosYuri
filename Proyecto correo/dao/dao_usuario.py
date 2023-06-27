from conex import conn 
import traceback

class daoUsuario:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "correosyuri")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
    
    def addUsuario(self,nombUsuario,password,rutTrab):
        sql = """INSERT INTO usuario(nombre_de_usuario, clave_accesos, rut_trabajador)
                VALUES(%s, %s, %s);"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombUsuario,password ,rutTrab))
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
    
    def validarNombreUsuario(self,nombUsuario):
        sql = 'select * from usuario where nombre_de_usuario = %s;' 
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombUsuario,))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado