import mysql.connector


class GestionAlumnos:
    def __init__(self, host="localhost", user="root", password="", database="bancolibros"):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def filtrar_alumnos(self, filtro=None):
        query = "SELECT * FROM alumnos"
        if filtro:
            query += " WHERE nombre LIKE %s OR apellidos LIKE %s"
            self.cursor.execute(query, (f"%{filtro}%", f"%{filtro}%"))
        else:
            self.cursor.execute(query)
        return self.cursor.fetchall()

    def modificar_alumno(self, nie, nombre=None, apellidos=None, tramo=None, bilingue=None):
        query = "UPDATE alumnos SET "
        updates = []
        values = []
        if nombre:
            updates.append("nombre = %s")
            values.append(nombre)
        if apellidos:
            updates.append("apellidos = %s")
            values.append(apellidos)
        if tramo:
            updates.append("tramo = %s")
            values.append(tramo)
        if bilingue is not None:
            updates.append("bilingue = %s")
            values.append(bilingue)

        if updates:
            query += ", ".join(updates) + " WHERE nie = %s"
            values.append(nie)
            self.cursor.execute(query, tuple(values))
            self.conn.commit()
            return self.cursor.rowcount
        return 0

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()


if __name__ == "__main__":
    gestion = GestionAlumnos()
    alumnos = gestion.filtrar_alumnos()
    for alumno in alumnos:
        print(alumno)

    nie_modificar = input("Ingrese el NIE del alumno a modificar: ")
    nuevo_nombre = input("Nuevo nombre (dejar vacío para no cambiar): ") or None
    nuevo_apellido = input("Nuevos apellidos (dejar vacío para no cambiar): ") or None
    nuevo_tramo = input("Nuevo tramo (dejar vacío para no cambiar): ") or None
    nuevo_bilingue = input("Bilingüe (0 para Sí, 1 para No, dejar vacío para no cambiar): ")
    nuevo_bilingue = int(nuevo_bilingue) if nuevo_bilingue else None

    filas_afectadas = gestion.modificar_alumno(nie_modificar, nuevo_nombre, nuevo_apellido, nuevo_tramo, nuevo_bilingue)
    print(f"{filas_afectadas} registro(s) actualizado(s).")
    gestion.cerrar_conexion()
