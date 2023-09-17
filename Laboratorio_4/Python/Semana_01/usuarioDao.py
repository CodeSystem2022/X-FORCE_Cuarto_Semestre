from conexion import Conexion
from usuario import Usuario
from logger_base import log

class UsuarioDAO:
    

#    DAO = Data Access Object
#    
#    CRUD = Create -> crear
#           Read -> leer
#           Update -> actualizar
#           Delete -> eliminar
    
    _SELECCIONAR = "SELECT idusuario, username, password FROM usuario ORDER BY idusuario"
    _INSERTAR = "INSERT INTO Usuario (username, password) VALUES (%s, %s)"
    _ACTUALIZAR = "UPDATE Usuario SET username=%s, password=%s WHERE idusuario=%s"
    _ELIMINAR = "DELETE FROM Usuario WHERE idusuario=%s"
    
    @classmethod
    def seleccionar(cls):
        #with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                usuarios = []
                for registro in registros:
                    usuario = Usuario(registro[0], registro[1], registro[2])
                    usuarios.append(usuario)
                return usuarios

    @classmethod
    def insertar(cls, usuario):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._INSERTAR, valores)
                log.debug (f"Usuario insertado: {usuario}")
                return cursor
            
    @classmethod
    def actualizar(cls, usuario):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (usuario.username, usuario.password, usuario.idusuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug (f"Usuario actualizado: {usuario}")
                return cursor.rowcount
    @classmethod
    def eliminar (cls, usuario):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (usuario.idusuario,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f"Usuario/s eliminado/s: {usuario}")

if __name__ == "__main__":
    
    usuario1 = Usuario (idusuario="7", username="genkhisKn", password="temuyin365")
    usuariosEliminados = UsuarioDAO.eliminar(usuario1)
    log.debug (f"Usuarios actualizados: {usuariosEliminados}")
    
    #usuarios = UsuarioDAO.seleccionar()
    #for usuario in usuarios:
    #    log.debug(usuario)