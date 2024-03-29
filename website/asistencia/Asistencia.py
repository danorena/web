# Instalar pandas
# instalar openpyx
from distutils.text_file import TextFile

from asistencia.ruta import rutaDescarga


class Asistencia:
    # Constructor 
    def __init__(self,ficha,fecha):
        self.ficha = ficha
        self.fecha = fecha
        from .ruta import ruta, rutaDescarga
        # from ruta import ruta, rutaDescarga
        self.ruta = ruta()
        self.rutaDescarga = rutaDescarga()

    # Funcion para obtener el nombre del aprendiz, la asistencia y el dia
    def dataFrameAsistencia(self,ficha):
        # Importamos la libreria de pandas
        import pandas as pd
        
        # Leemos el archivo .Json
        # libreria pygithub
        import json
        from github import Github

        g = Github("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")
        repo = g.get_repo("danorena/attendance")
        contents = repo.get_contents(f"attendance/model/datasets/attendance_system_dataset/{ficha}/database/attendance.json")
        fileJson = contents.decoded_content.decode()
        fileJson = json.loads(fileJson)
        fileJson = pd.DataFrame(fileJson)
        fileJson = pd.DataFrame.to_json(fileJson)
        fileJson = pd.read_json(fileJson)
        
        # Inicializamos una variable en 0 para el contador y una lista vacia
        a = 0
        aprendiz = []
        idAprendiz = []
        # Recorremos todos los estudiantes
        for sKey, sValue in fileJson['student'].items():
            # Contador para buscar el valor
            a +=1
            count = str(a)
            # Obtenemos el id
            idAprendiz.append(sKey)
            # Obtenemos el valor/Nombre del aprendiz
            aprendiz.append(sValue[count][0])
            
        # Creamos una lista vacia
        asistencia = []
        # Recorremos todos las asistencias
        for aList in fileJson['attendance'].values:
            # Evaluamos si la fecha obtenida es igual que buscaremos
            try:
                # [K] corresponde a fecha y [V] al id del aprendiz
                for k,value in aList.items():
                    if self.fecha == k:
                        for v in value.keys():
                            asistencia.append(int(v))
            except:
                pass
        
        # Creamos una lista para guardar la asistencia
        asistenciaAprendiz = []
        for id in idAprendiz:
            # Evaluamos si el id esta en la asistencia
            if id in asistencia:
                asistenciaAprendiz.append("Presente")
            else:
                asistenciaAprendiz.append('No vino')
        
        
        data = {
            '   Nombre Aprendiz' : aprendiz,
            'Asistencia' : asistenciaAprendiz
        }
        
        
        # Columnas a mostrar en el excel
        # Convertimos el diccionario a un DataFrame
        excelAsistencia = pd.DataFrame.from_dict(data)
        return excelAsistencia

    # Funcion para mostrar la asistencia
    def mostrarAsistencia(self,dataFrame):
        print(f'Fecha: {self.fecha}')
        return dataFrame

    def toExcel(self,dataFrame):
        try:
            dataFrame.to_excel(f'{self.rutaDescarga}/website/static/asistencia/excel/asistenciaFicha.xlsx')
            print('Excel exportado correctamente')
        except:
            print('Hubo un error exportado el archivo Excel')
   
    # Funcion para convertir el dataFrame a Html
    def toHtml(self,dataFrame):
        try:
            # Creamos el string para hacer el documento de HMTL
            html_string = """
            {{% load static %}}
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Asistencia</title>
                    <link rel="stylesheet" type="text/css" href="{{% static 'asistencia/css/tables.css'%}}"/>
                    <link rel="stylesheet" href="{{% static 'assets/font-awesome/css/font-awesome.css' %}}"/>
                </head>
                <body>
                    <header>
			            <div class="navigation-menu" id="navigation-menu">
                        <div class="row1" id="row1">
                        <a href="/asistencia" id="button"><i class="fa-solid icon-arrow-left"></i> Buscar otra ficha</a>
                        </div>
                        <div class="row2" id="row2">
                        <a href="{{% static 'asistencia/excel/asistenciaFicha.xlsx'%}}" download="asistencia.xlsx" id="button"><i class="fa-solid icon-download"></i> Descargar Asistencia</a>
                        </div>
			            </div>
		            </header>
                    {table}
                </body>
            </html>
            """
            # Creamos el archivo 
            text_file = open("template/asistenciaFicha.html", "w")
            # Exportamos el archivo html
            html = html_string.format(table=dataFrame.to_html())
            text_file.write(html)
            text_file.close()

            # Hacemos que se conviertan todos los caracteres a utf-8
            with open("template/asistenciaFicha.html", "w", encoding="utf-8") as file:
                file.write(html)
            
            print('HTML exportado correctamente')
            # Creamos el archivo de Excel para que sea posible descargarlo
            self.toExcel(dataFrame)
        except:
            print('Hubo un error exportado el archivo html')


# ficha = '2256256'
# fecha = '2022-07-08'

# asistencia = Asistencia(ficha,fecha)

# asistencia.toExcel(asistencia.dataFrameAsistencia(ficha))
# print(asistencia.mostrarAsistencia(asistencia.dataFrameAsistencia(ficha)))
# asistencia.toHtml(asistencia.dataFrameAsistencia(ficha))