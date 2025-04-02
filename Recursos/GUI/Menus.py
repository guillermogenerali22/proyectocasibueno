# Generales/login.py
from Recursos.GUI import formulario_login
from Recursos.Clases import Alumno  # Ejemplo de importación, puedes ajustarlo según necesidades

class Login:
    def __init__(self):
        pass

    def mostrar_formulario(self):
        print("Mostrando formulario de login")
        formulario_login.mostrar()

    def validar_usuario(self, username, password):
        # Ejemplo básico de validación (lógica a reemplazar por la real)
        if username == "admin" and password == "admin":
            print("Acceso concedido. Mostrando menú de administrador.")
            return True
        else:
            print("Error de autenticación. Usuario o contraseña incorrectos.")
            return False

if __name__ == "__main__":
    login = Login()
    login.mostrar_formulario()
    # Simulación de validación:
    login.validar_usuario("admin", "admin")
