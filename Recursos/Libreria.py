# Recursos/Clases.py
class Alumno:
    def __init__(self, nombre: str, apellidos: str, tramoconcedido: str, seccion: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramoconcedido = tramoconcedido
        self.seccion = seccion  # 'S' o 'N'

class Curso:
    def __init__(self, anio: str, nivel: str):
        self.anio = anio
        self.nivel = nivel

class ACL:
    def __init__(self, fechaprestamo, fechadevolucion, estado: str):
        self.fechaprestamo = fechaprestamo
        self.fechadevolucion = fechadevolucion
        self.estado = estado  # 'Entregado' o 'A devolver'

class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, numero: int, ejemplares: int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.numero = numero
        self.ejemplares = ejemplares

class Materia:
    def __init__(self, nombre: str, departamento: str):
        self.nombre = nombre
        self.departamento = departamento
