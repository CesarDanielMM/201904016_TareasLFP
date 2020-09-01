import os
import webbrowser

class Usuario():
    def __init__(self, nombre, edad, activo, saldo):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        self.saldo = saldo

    def __repr__(self):
        return "{0},{1},{2},{3}".format(self.nombre, self.edad, self.activo, self.saldo)

def GenerarReporte(Usuarios):
    datos = ""
    contador = 1
    for Usuarios in Usuarios:
        datos += "<tr>\n"
        datos += "<th scope=\"row\">" + str(contador) + "</th>\n"
        datos += "<td>" + str(Usuarios.nombre) + "</td>\n"
        datos += "<td>" + str(Usuarios.edad) + "</td>\n"
        datos += "<td>" + str(Usuarios.activo) + "</td>\n"
        datos += "<td>" + str(Usuarios.saldo) + "</td>\n"
        datos += "</tr>\n"
        contador = contador + 1

    html_str = """
            <!DOCTYPE html>
            <html>
            <head>
              <title>Reporte</title>
               <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
            </head>
            <body>
            <table class="table table-striped">
              <thead>
                <tr>
                  <th scope="col">Numero</th>
                  <th scope="col">Nombre</th>
                  <th scope="col">Edad</th>
                  <th scope="col">Activo</th>
                  <th scope="col">Saldo</th>
                </tr>
              </thead>
              <tbody>
              """ + datos + """    
              </tbody>
            </table>
            </body>
            </html>

            """
    Html_file = open("ReporteUsuarios.html", "w")
    Html_file.write(html_str)
    Html_file.close()


Usuarios = [Usuario('Jose', 19, True, 4500.10),Usuario('Edgar', 40, False, 4800.30),Usuario('Ana', 50, True, 3400.95),
            Usuario('Roberto', 50, True, 3220.32),Usuario('Melany', 17, False, 4432.87),Usuario('Pedro', 20, True, 4214.54),
            Usuario('David', 19, True, 4023.22),Usuario('Luis', 21, False, 3344.50),Usuario('Javier', 25, True, 2344.20),
            Usuario('Alejandro', 15, False, 5102.70)]

GenerarReporte(Usuarios)

url = 'file://' + os.path.realpath('ReporteUsuarios.html')

webbrowser.open(url, new=2)

