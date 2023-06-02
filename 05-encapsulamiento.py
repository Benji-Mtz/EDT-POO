class Usuario:
    def __init__(self, nombre, apellido, contrasenia, correo, telefono) -> None:
        # public attribute
        self.nombre = nombre
        self.apellido = apellido
        self.contrasenia = self.encriptar_contrasenia(contrasenia)
        self.correo = correo
        
        # private attribute
        self.__telefono = telefono
        
    def encriptar_contrasenia(self, contrasenia):
        pass
    
    def verificar_contrasenia(self, contrasenia):
        pass
    
    def obtener_telefono(self):
        return self.__telefono
    
    def actualizar_telefono(self, telefono):
        self.__telefono = telefono
        
usuario = Usuario(nombre="Benji", apellido="Mtz", correo="hola", contrasenia="132", telefono="1234567890")

print(usuario.obtener_telefono())
usuario.actualizar_telefono("1122334455")
print(usuario.obtener_telefono())