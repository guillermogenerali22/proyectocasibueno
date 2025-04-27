import mysql.connector

class CargarBBDD:
    def ejecutar(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="bancolibros"
            )
            cursor = conexion.cursor()

            # Aquí puedes pedir al usuario datos para cargar registros, por ejemplo:
            tabla = input("¿Qué tabla deseas cargar? (alumnos / cursos / materias / libros): ").strip().lower()

            if tabla == "alumnos":
                nie = input("Introduce NIE: ")
                nombre = input("Introduce Nombre: ")
                apellidos = input("Introduce Apellidos: ")
                tramo = input("Introduce Tramo (0, 1 o 2): ")
                bilingue = input("¿Es bilingüe? (0 = Sí, 1 = No): ")

                sql = "INSERT INTO alumnos (nie, nombre, apellidos, tramo, bilingue) VALUES (%s, %s, %s, %s, %s)"
                valores = (nie, nombre, apellidos, tramo, bilingue)
                cursor.execute(sql, valores)

            elif tabla == "cursos":
                curso = input("Introduce nombre del curso: ")
                nivel = input("Introduce nivel: ")
                sql = "INSERT INTO cursos (curso, nivel) VALUES (%s, %s)"
                valores = (curso, nivel)
                cursor.execute(sql, valores)

            elif tabla == "materias":
                id_materia = int(input("Introduce ID de la materia: "))
                nombre = input("Introduce Nombre: ")
                departamento = input("Introduce Departamento: ")
                sql = "INSERT INTO materias (id, nombre, departamento) VALUES (%s, %s, %s)"
                valores = (id_materia, nombre, departamento)
                cursor.execute(sql, valores)

            elif tabla == "libros":
                isbn = input("Introduce ISBN: ")
                titulo = input("Introduce Título: ")
                autor = input("Introduce Autor: ")
                numero_ejemplares = int(input("Introduce Número de Ejemplares: "))
                id_materia = int(input("Introduce ID de Materia: "))
                id_curso = input("Introduce ID de Curso: ")
                sql = "INSERT INTO libros (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (isbn, titulo, autor, numero_ejemplares, id_materia, id_curso)
                cursor.execute(sql, valores)

            else:
                print("❌ Tabla no válida.")
                return

            conexion.commit()
            print(f"✅ Datos insertados en {tabla} correctamente.")
        except mysql.connector.Error as e:
            print(f"❌ Error al cargar la base de datos: {e}")
        finally:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
