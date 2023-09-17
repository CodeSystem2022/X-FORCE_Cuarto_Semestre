from logger_base import log

class Usuario:
    def __init__ (self, idusuario, username, password):
        self._idusuario = idusuario
        self._username = username
        self._password = password
        
    def __str__ (self):
        return f"""
            Id usuario: {self._idusuario}, 
            Nombre: {self._username}, 
            Contraseña: {self._password}
            """
    @property
    def idusuario(self):
        return self._idusuario
    
    @idusuario.setter
    def idusuario(self, value):
        self._idusuario = value
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        self._username = value
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        self._password = value