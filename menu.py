# coding=utf-8
import os
import time
import webbrowser
from os import system
from estudiante import Estudiante
from db import crearEstudiante, actualizarEstudiante, eliminarEstudiante, obtenerEstudiante, obtenerEstudiantes
import msvcrt
from playsound import playsound

carpeta_actual = os.path.dirname(__file__)
audios = f"{ carpeta_actual }/audios"
audio_bienvenida = f"{ audios }/bienvenida.mp3"
audio_est_aniadido = f"{ audios }/estudiante_aniadido.mp3"
audio_est_modificado = f"{ audios }/estudiante_modificado.mp3"
audio_est_eliminado = f"{ audios }/estudiante_eliminado.mp3"
audio_exportacion = f"{ audios }/exportacion.mp3"
audio_modificacion_invalida = f"{ audios }/modificacion_invalida.mp3"
audio_eliminacion_invalida = f"{ audios }/eliminacion_invalida.mp3"
audio_creditos = f"{ audios }/creditos.mp3"
audio_volver_al_menu = f"{ audios }/volver_al_menu.mp3"
audio_despedida = f"{ audios }/despedida.mp3"

def obtenerValorLiteral(promedio):
    if promedio >= 90 and promedio <= 100:
        ValorLiteral = "A"
        return ValorLiteral

    elif promedio >= 80 and promedio < 90:
        ValorLiteral = "B"
        return ValorLiteral

    elif promedio >= 70 and promedio < 80:
        ValorLiteral = "C"
        return ValorLiteral

    elif promedio < 70:
        ValorLiteral = "F"
        return ValorLiteral

    else:
        ValorLiteral = "NULL"
        return ValorLiteral

def MenuPrincipal():
    playsound(audio_bienvenida, False)
    while True:
      system("clear")
      print("""
  ----------Menu Principal--------
  1-Agregar estudiante
  2-Modificar estudiante
  3-Eliminar estudiante
  4-Exportar estudiantes
  5-Acerca de
  6-Salir
      """)
      
      opcion = input("Elija una opcion: ")
      system("clear")
      if opcion == "1":
          print("""
  Para agregar el estudiante, ingrese las siguientes informaciones:""")
          matricula = input("Ingrese su matricula: ")

          if len(obtenerEstudiante(matricula)) != 0:
              print("Este estudiante ya existe.")
              time.sleep(1.5)
          else:
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            nota1 = int(input("Ingrese su primera nota: "))
            nota2 = int(input("Ingrese su segunda nota: "))
            promedio = (nota1 + nota2) / 2
            valorLiteral = obtenerValorLiteral(promedio)
            crearEstudiante(matricula, nombre, apellido, nota1, nota2, promedio,
                            valorLiteral)
            print("Estudiante añadido exitosamente...")
            playsound(audio_est_aniadido)
  
      elif opcion == "2":
          matricula = input(
              "Ingrese la matricula del estudiante que desea modificar: ")
          if len(obtenerEstudiante(matricula)) == 0:
              print("El estudiante no existe")
              playsound(audio_modificacion_invalida)
          else:
              estudiante = obtenerEstudiante(matricula)[0]
              nombre = input("Ingrese su nombre: ")
              apellido = input("Ingrese su apellido: ")
              nota1 = int(input("Ingrese su primera nota: "))
              nota2 = int(input("Ingrese su segunda nota: "))
              promedio = (nota1 + nota2) / 2
              valorLiteral = obtenerValorLiteral(promedio)
              estudiante_actualizado = Estudiante(matricula, nombre, apellido,
                                                  nota1, nota2, promedio,
                                                  valorLiteral)
              actualizarEstudiante(estudiante["id"],
                                   estudiante_actualizado.__dict__)
              print("¡El registro ha sido modificado de manera satisfactoria!")
              playsound(audio_est_modificado)
  
      elif opcion == "3":
          matricula = input(
              "Ingrese la matricula del estudiante que desea eliminar: ")
          if len(obtenerEstudiante(matricula)) == 0:
              print("El estudiante no existe")
              playsound(audio_eliminacion_invalida)
          else:
              estudiante = obtenerEstudiante(matricula)[0]
              eliminarEstudiante(estudiante["id"])
              print("¡El estudiante ha sido eliminado correctamente!")
              playsound(audio_est_eliminado)
  
      elif opcion == "4":
  
          pagina = open("ListadoEstudiantes.html", "w", encoding="utf-8")

          cuerpo_html = """<!DOCTYPE html>
  <html lang="en">
  <head>
  <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Listado de estudiantes</title>
      <style>
        table {
            width: 50%;
            border: 1px solid black;
        }

        th {
            font-size: 1.1rem;
        }

        th, td {
            padding: 10px
        }

        td {
            text-align: center;
        }

      </style>
  </head>
  <body>
   <table>
     <tr>
      <th>Matricula</th>
      <th>Nombre</th>
      <th>Apellidos</th>  
      <th>Nota1</th>
      <th>Nota2</th>
      <th>Promedio</th>
      <th>EQ</th>  
    </tr>"""

          estudiantes = obtenerEstudiantes()

          for i in range(len(estudiantes)):
            cuerpo_html += f"""
              <tr>
                <td>{estudiantes[i]["Matricula"]}</td>
                <td>{estudiantes[i]["Nombre"]}</td>
                <td>{estudiantes[i]["Apellido"]}</td>
                <td>{estudiantes[i]["Nota1"]}</td>
                <td>{estudiantes[i]["Nota2"]}</td>
                <td>{estudiantes[i]["Promedio"]}</td>
                <td>{estudiantes[i]["ValorLiteral"]}</td>  
              </tr>
            """
          cuerpo_html +="""
            </table>
            </body>
            </html>
        """

          pagina.write(cuerpo_html)
          pagina.close()
          ruta_archivo = (f"file://{ carpeta_actual }/ListadoEstudiantes.html").replace("mnt/c", "C:")
          playsound(audio_exportacion)
          webbrowser.open(ruta_archivo)
  
      elif opcion == "5":
          print("""
  ---------Derechos reservados para----------
  Raymond David Mora Montero / 2021-1897
  Leonel Antonio Holguin Pujols / 2021-1972
                """)
          playsound(audio_creditos)
          playsound(audio_volver_al_menu, False)
          msvcrt.getch()
        
      elif opcion == "6":
        print("¡Hasta la próxima!")
        playsound(audio_despedida)
        break
     