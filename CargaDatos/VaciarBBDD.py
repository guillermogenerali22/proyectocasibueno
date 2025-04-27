import mysql.connector

class VaciarBBDD:
    def ejecutar(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bancolibros"
            )
            cursor = conexion.cursor()

            confirmacion = input("¿Estás seguro que deseas vaciar la base de datos? (S/N): ").strip().upper()
            if confirmacion == 'S':
                tablas = ["alumnoscrusoslibros", "alumnos", "libros", "materias", "cursos"]
                for tabla in tablas:
                    cursor.execute(f"DELETE FROM {tabla}")
                conexion.commit()
                print("✅ Base de datos vaciada correctamente.")
            else:
                print("⚠️ Operación cancelada.")
        except mysql.connector.Error as e:
            print(f"❌ Error al vaciar la base de datos: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
