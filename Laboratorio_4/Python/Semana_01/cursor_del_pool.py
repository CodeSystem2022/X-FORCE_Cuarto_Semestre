from logger_base import log
from conexion import Conexion

class CursorDelPool:
    def __init__(self):
        self.conexion = None
        self._cursor = None
        
        
    def __enter__ (self):
        log.debug("Inicio del método with y __enter__")
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):  #tipo de escepcion, valor de escepcion t detalles de escepcion.
        log.debug("Se ejecuta el metodo exit")
        if exc_val:
            self._conexion.rollback()
            log.debug(f"Ocurrió una excepcion: {exc_val}")
        else:
            self.conexion._commit()
            log.debug("Commit de la transaccion")
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug (f"Estamos dentro del bloque with.")
        cursor.execute("SELECT  * FROM usuario")
        log.debug(cursor.fetchall())