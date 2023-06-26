from utils.encoder import Encoder
from dao.dao_usuario import daoUsuario

class UsuarioDTO:
    
    def addUsuario(self,nombUsuario,password,rutTrab):
        daousuario = daoUsuario()
        resultado = daousuario.addUsuario(nombUsuario,Encoder().encode(password),rutTrab)
        return resultado
    
    def validarNombreUsuario(self,nombUsuario):
        daousuario = daoUsuario()
        resultado = daousuario.validarNombreUsuario(nombUsuario)
        return resultado
        