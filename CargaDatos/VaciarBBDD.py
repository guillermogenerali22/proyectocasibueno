# CargaDatos/VaciarBBDD.py
class VaciarBBDD:
    def __init__(self):
        pass

    def mostrar_menu(self):
        print("¿Desea vaciar la base de datos? (S/N)")

    def vaciar(self, confirmacion):
        if confirmacion.upper() == 'S':
            print("Base de datos vaciada.")
            # Aquí se implementaría la lógica para vaciar la BBDD
        else:
            print("Proceso cancelado.")

if __name__ == "__main__":
    vaciar_bbdd = VaciarBBDD()
    vaciar_bbdd.mostrar_menu()
    # Simulación de confirmación:
    vaciar_bbdd.vaciar("S")
