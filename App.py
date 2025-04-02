import sys
from Generales.login import Login
from Generales.logout import Logout
from CargaDatos.VaciarBBDD import VaciarBBDD
from CargaDatos.GestionErrores import GestionErrores
from CargaDatos.CargarBBDD import CargarBBDD
from GestionAlumnos.FiltrarAlumnos import FiltrarAlumnos
from GestionAlumnos.Subcaso import Subcaso
from GestionPrestamos.GestionPrestamos import GestionPrestamos
from GestionListados.GestionListados import GestionListados


def main():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar sesión")
        print("2. Vaciar Base de Datos")
        print("3. Gestionar Errores")
        print("4. Cargar Base de Datos")
        print("5. Filtrar Alumnos")
        print("6. Modificar Datos de Alumnos")
        print("7. Gestionar Préstamos")
        print("8. Generar Listados")
        print("9. Cerrar Sesión")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            login = Login()
            if login.autenticar():
                print("Acceso concedido")
            else:
                print("Acceso denegado")
        elif opcion == "2":
            VaciarBBDD().ejecutar()
        elif opcion == "3":
            GestionErrores().ejecutar()
        elif opcion == "4":
            CargarBBDD().ejecutar()
        elif opcion == "5":
            FiltrarAlumnos().ejecutar()
        elif opcion == "6":
            Subcaso().ejecutar()
        elif opcion == "7":
            GestionPrestamos().ejecutar()
        elif opcion == "8":
            GestionListados().ejecutar()
        elif opcion == "9":
            Logout().ejecutar()
        elif opcion == "0":
            print("Saliendo del programa...")
            sys.exit()
        else:
            print("Opción no válida, por favor seleccione nuevamente.")


if __name__ == "__main__":
    main()
