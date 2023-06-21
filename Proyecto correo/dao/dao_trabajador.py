from conex import conn 
import traceback

class daoTrabajador:
    def __init__(self):
        try:
            self.conn = conn.Conex("localhost", "root", "", "correosyuri")
        except Exception as ex:
            print(ex)

    def getConex(self):
        return self.conn
    

    def validarLogin(self,nombreUsuario, claveUsuario):
        sql = "SELECT nombre_de_usuario, clave_accesos FROM usuario WHERE nombre_de_usuario = %s AND clave_accesos = %s;"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombreUsuario, claveUsuario))

            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def tipoDeUsuario(self,nombreUsuario,claveUsuario):
        sql ="SELECT dl.cargo, dl.departamento FROM usuario u JOIN datosLaborales dl ON u.rut_trabajador = dl.rut_trabajador JOIN trabajador t ON dl.rut_trabajador = t.rut WHERE u.nombre_de_usuario = %s AND u.clave_accesos = %s;"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombreUsuario, claveUsuario))

            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def mostrarDatosPorUseryPass(self,nombreUsuario, claveUsuario):
        sql ="""SELECT 
                    t.rut, 
                    t.nombre, 
                    t.genero, 
                    t.telefono, 
                    t.direccion, 
                    u.id as id_usuario,
                    u.nombre_de_usuario, 
                    u.clave_accesos, 
                    d.id as id_datosLaborales,
                    d.fecha_contratacion, 
                    d.cargo, 
                    d.departamento, 
                    c.id as id_cargasFamiliares,
                    c.rut_carga,
                    c.nombre_carga, 
                    c.parentesco, 
                    c.genero_carga, 
                    e.id as id_contactosEmergencia,
                    e.rut_contacto,
                    e.nombre_contacto, 
                    e.relacionTrabajador, 
                    e.telefono_contacto 
                FROM usuario u
                LEFT JOIN trabajador t ON u.rut_trabajador = t.rut
                LEFT JOIN datosLaborales d ON d.rut_trabajador = t.rut
                LEFT JOIN cargasFamiliares c ON c.rut_trabajador = t.rut
                LEFT JOIN contactosEmergencia e ON e.rut_trabajador = t.rut
                WHERE u.nombre_de_usuario = %s AND u.clave_accesos = %s;"""
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombreUsuario, claveUsuario))

            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    
      


    