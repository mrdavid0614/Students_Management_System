from pysondb import db
from estudiante import Estudiante

tabla_estudiante = db.getDb("estudiante.json")

def obtenerEstudiantes():
  return tabla_estudiante.getAll()

def obtenerEstudiante(matricula):
  return tabla_estudiante.getBy({ "Matricula": matricula })

def crearEstudiante(matricula, nombre, apellido, n1, n2, promedio, valor_literal):
  estudiante1 = Estudiante(matricula, nombre, apellido, n1, n2, promedio, valor_literal)
  tabla_estudiante.add(estudiante1.__dict__)

def actualizarEstudiante(id, data):
  tabla_estudiante.updateById(id, data)

def eliminarEstudiante(id):
  tabla_estudiante.deleteById(id)