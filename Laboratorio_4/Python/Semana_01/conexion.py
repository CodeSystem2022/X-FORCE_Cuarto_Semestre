#import psycopg2 as bd
from logger_base import log
from psycopg2 import pool
import sys


class Conexion:
    _DATABASE = "CuartoSemestreBase1"
    _USERNAME = "postgres"
    _PASSWORD = "1234"
    _DB_PORT = "5432"
    _HOST = "127.0.0.1"  # localhost
    #_conexion = None
    #_cursor = None
    _min_con = 1
    _max_con = 5
    _pool = None

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f"Conexion obtenida del pool: {conexion}")
        return conexion
        

    @classmethod
    def obtenerCursor(cls):
        #if cls._cursor is None:
        #    try:
        #        cls._cursor = cls.obtenerConexion().cursor()
        #        log.debug(f"Se abrió correctamente el cursor: {cls._cursor}")
        #        return cls._cursor
        #    except Exception as e:
        #        log.error(f"Ocurrió un error: {e}")
        #        sys.exit()
        #else:
        #    return cls._cursor
        pass

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._min_con,
                                                      cls._max_con,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f"Creación del pool exitosa: {cls._pool}")
                return cls._pool
            except Exception as e:
                log.error(f"Ocurrio un error al obtener el pool: {e}")
                sys.exit
        else:
            return cls._pool
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f"regresamos la conexion del pool {conexion}")
        
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        
                

if __name__ == "__main__":
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()


