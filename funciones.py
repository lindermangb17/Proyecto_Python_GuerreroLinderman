import json

ruta_base_datos="/home/camper/Documentos/Linderman Ejercicios/Proyecto_Python_GuerreroLinderman/base_datos.json"


def cargar_base_datos():
    with open(ruta_base_datos,"r",encoding="utf-8") as archivo:
        base_datos = json.load(archivo)
    return base_datos

def guardar_datos(base_datos):
    with open(ruta_base_datos, "w", encoding="utf-8") as archivo:
        json.dump(base_datos, archivo, indent=4)


def login():
    print("\n ==== CLÍNICA ACME ====")

    while True:
        Correo=input("Correo: ").strip().lower()
        Contraseña=input("Contraseña: ")

        cedula_usuario = verificar_login(Correo, Contraseña)

        if cedula_usuario != None:
            print("Inicio de sesión exitoso")
            break       
        else:
            print("Correo o contraseña incorrectos")
    return cedula_usuario 


def verificar_login(corr,contra):
    base_datos = cargar_base_datos()
    for u in base_datos["usuarios"]:

        if base_datos["usuarios"][u]["email"].lower() == corr and base_datos["usuarios"][u]["contrasena"] == contra:
            return u
        
    return None


import random

def registrar_usuario():
    base_datos = cargar_base_datos()

    # 1. Validar cedula
    cedula = input("Ingrese la cédula: ").strip()

    while cedula == "" or not cedula.isdigit() or cedula in base_datos["usuarios"]:

        if cedula == "" or not cedula.isdigit():
            print("Cédula inválida. Solo se permiten números y no puede estar vacía")

        elif cedula in base_datos["usuarios"]:
            print("Usuario ya existe")

        input("Presione Enter para volver al menú ")
        return

    # 2. datos personales
    nombres = input("Nombres: ").strip()

    while nombres == "":
        print("Este campo es obligatorio")
        nombres = input("Nombres: ").strip()

    
    apellidos = input("Apellidos: ").strip()

    while apellidos == "":
            print("Este campo es obligatorio")
            apellidos = input("apellidos: ").strip()

    telefono = input("Teléfono: ")

    while telefono.isdigit()==False:
        print("El teléfono solo debe contener números")
        telefono = input("Ingrese otro teléfono: ")

    email = input("Email: ").strip()
    
    while email == "":
            print("El email es obligatoria")
            email = input("Ingrese un email: ").strip()


    direccion = input("Dirección: ").strip()
    
    while direccion == "":
        print("La dirección es obligatoria")
        direccion = input("Ingrese la dirección: ").strip()

    # 3. rol
    print("Seleccione el rol:")
    print("1. Médico")
    print("2. Administrativo")

    rol = input("Opción: ")

    while rol != "1" and rol != "2":
        print("Opción inválida")
        rol = input("Seleccione 1 o 2: ")

    if rol == "1":
        rol = "medico"
    else:
        rol = "administrativo"

    # 4. Validar correo 
    while True:
        existe = False

        for u in base_datos["usuarios"]:
            if email.lower() == base_datos["usuarios"][u]["email"].lower():
                existe = True
                break

        if existe == True:
            print("Email ya registrado!!")
            email = input("Ingrese otro email: ").strip()

            while email == "":
                print("El email es obligatorio")
                email = input("Ingrese otro email: ").strip()
        else:
            break

    # 5. Generar contraseña aleatoria de 8 dígitos
    while True:
        contrasena = ""
        for i in range(8):
            digito = random.randint(0, 9)
            contrasena += str(digito)

        existe = False

        for u in base_datos["usuarios"]:
            if contrasena == base_datos["usuarios"][u]["contrasena"]:
                existe = True
                break

        if existe == False:
            break

    # 6. Agregar usuario al diccionario
    base_datos["usuarios"][cedula] = {
        "nombre": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "rol": rol,
        "contrasena": contrasena
    }

    # 7. Guardar en JSON
    guardar_datos(base_datos)

    # 8. Mostrar credenciales
    print("\nUsuario registrado exitosamente")
    print("Usuario:", email)
    print("Contraseña:", contrasena)
    print("Por favor anote y guarde su contraseña!!!")
    input("\nPresione enter para volver al menu ")


def registro_pacientes():
    base_datos = cargar_base_datos()
        
        # 1.  cedula
    cedula = input("Ingrese la cédula: ").strip()
    
    while cedula == "" or not cedula.isdigit() or cedula in base_datos["pacientes"]:

        if cedula == "" or not cedula.isdigit():
            print("Cédula inválida. Solo se permiten números")

        elif cedula in base_datos["pacientes"]:
            print("El paciente ya está registrado")

        input("Presione Enter para volver al menú ")
        return

        # 2. datos personales

    nombres = input("Nombres: ").strip()
    while nombres == "":
        print("Este campo es obligatorio")
        nombres = input("Nombres: ").strip()

    apellidos = input("Apellidos: ").strip()

    while apellidos == "":
        print("Este campo es obligatorio")
        apellidos = input("apellidos: ").strip()

    telefono = input("Teléfono: ")
    
    while telefono.isdigit()==False:
        print("El teléfono solo debe contener números")
        telefono = input("Ingrese otro teléfono: ")
    
    email = input("Correo electronico: ").strip()

    while email == "":
            print("El email es obligatoria")
            email = input("Ingrese un email: ").strip()


    direccion = input("Dirección: ").strip()

    while direccion == "":
        print("La dirección es obligatoria")
        direccion = input("Ingrese la dirección: ").strip()

    print("Seleccione el genero:")
    print("1. Masculino")
    print("2. Femenino")

    genero = input("Opción: ")
    
    while genero != "1" and genero != "2":
        print("Opción inválida")
        genero = input("Seleccione 1 o 2: ")
    
    if genero == "1":
        genero = "Masculino"
    else:
        genero = "Femenino"

    print("Seleccione el estado civil:")
    print("1. Soltero/a")
    print("2. Casado/a")

    estadocivil= input("Opción: ")

    while estadocivil != "1" and estadocivil != "2":
            print("Opción inválida")
            estadocivil = input("Seleccione 1 o 2: ")
        
    if estadocivil == "1":
        estadocivil = "Soltero/a"
    else:
        estadocivil = "Casado/a"

    base_datos["pacientes"][cedula] = {
            "nombre": nombres,
            "apellidos": apellidos,
            "telefono": telefono,
            "email": email,
            "direccion": direccion,
            "genero": genero,
            "estado civil": estadocivil
        }

    guardar_datos(base_datos)

    print("\nPaciente registrado exitosamente")


def diagnosticar_pacientes(cedula_medico):
    base_datos = cargar_base_datos()

    cedula_paciente = input("Ingrese la cédula del paciente: ")

    if cedula_paciente not in base_datos["pacientes"]:
        print("Paciente no registrado")
        input("Presione Enter para volver al menú...")
        return

    nombre_paciente = base_datos["pacientes"][cedula_paciente]["nombre"]
    apellido_paciente = base_datos["pacientes"][cedula_paciente]["apellidos"]

    print("Paciente encontrado:", nombre_paciente, apellido_paciente)

    while True:
        fecha = input("Ingrese la fecha de consulta (AAAA-MM-DD): ")
        partes = fecha.split("-")

        if len(partes) != 3:
            print("Formato incorrecto")
            continue

        if len(partes[0]) != 4 or len(partes[1]) != 2 or len(partes[2]) != 2:
                print("Use el formato AAAA-MM-DD")
                continue
        
        if not partes[0].isdigit() or not partes[1].isdigit() or not partes[2].isdigit():
                print("La fecha debe contener números")
                continue

        anio = int(partes[0])
        mes = int(partes[1])
        dia = int(partes[2])

        if anio < 1 or mes < 1 or mes > 12:
            print("Año o mes inválido")
            continue

        if mes == 2:
            if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
                max_dias = 29
            else:
                max_dias = 28

        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            max_dias = 30

        else:
            max_dias = 31

        if dia < 1 or dia > max_dias:
            print("Día inválido para ese mes")
            continue
        break

    print("fecha registrada correctamente")

    sintomas = []

    while True:
        print("Ingrese los síntomas (digite 999 para terminar):")
        sintoma = input(f"Síntoma {len(sintomas) + 1}: ")
        if sintoma.strip() == "":
            print("Ingrese un sIntoma válido")
            continue

        if sintoma=="999":
            if len(sintomas)==0:
                print("Ingrese al menso un sintoma")
                continue
            else:
                break

        sintomas.append(sintoma)

    diagnostico = input("Ingrese el diagnóstico del paciente: ")

    while diagnostico.strip() == "":
        print("¡Es obligatorio llenar este espacio!")
        diagnostico = input("Ingrese el diagnóstico nuevamente: ")
    print("Diagnóstico registrado correctamente")

    medicamentos = []

    while True:
            medicamento = input(f"medicamento {len(medicamentos) + 1} (digite 999 para terminar):")

            if medicamento.strip() == "":
                print("El nombre del medicamento es obligatorio")
                continue
            
            if medicamento=="999":
                if len(medicamentos)==0:
                    print("Ingrese al menos un medicamento")
                    continue
                else:
                     break
                
            cantidad=input(f"cantidad de medicamento {len(medicamentos) + 1}:")

            while not cantidad.isdigit() or int(cantidad) <=0:

                print("Ingrese una cantidad válida mayor que cero")

                cantidad = input("Cantidad del medicamento ")

            cantidad = int(cantidad)

            dosis=input(f"dosis de medicamento {len(medicamentos) + 1}:")

            while dosis.strip() =="":
                 print("La dosis es obligatoria")
                 dosis = input("Ingrese nuevamente la dosis: ")

            tiempo=input(f"duracion del tratamiento den días:")

            while not tiempo.isdigit() or int(tiempo) <=0:

                print("Ingrese un tiempo valido mayor que cero")
                tiempo = input("Duración del tratamiento en días: ")
            tiempo = int(tiempo)

            datos_medicamento = {
                    "medicamento": medicamento,
                    "cantidad": cantidad,
                    "dosis": dosis,
                    "tiempo": tiempo
                }
            medicamentos.append(datos_medicamento)

    if len(base_datos["diagnosticos"]) == 0:
        numero = 1
    
    else:
        numero_mayor = 0

        for codigo in base_datos["diagnosticos"]:
                numero = int(codigo.split("S")[1])

                if numero > numero_mayor:
                    numero_mayor=numero

        numero = numero_mayor + 1

    codigo_consulta = "CONS" + str(numero).zfill(5)    

    print("Código de consulta:", codigo_consulta)

        

    base_datos["diagnosticos"][codigo_consulta]={
        "cedula_paciente": cedula_paciente,
        "cedula_medico": cedula_medico,
        "fecha": fecha,
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "medicamentos": medicamentos
    }

    guardar_datos(base_datos)

    nombre_medico = base_datos["usuarios"][cedula_medico]["nombre"]
    apellido_medico = base_datos["usuarios"][cedula_medico]["apellidos"]
    nombre_paciente = base_datos["pacientes"][cedula_paciente]["nombre"]
    apellido_paciente = base_datos["pacientes"][cedula_paciente]["apellidos"]
    
   
    ruta_prescripcion = "/home/camper/Documentos/Linderman Ejercicios/Proyecto_Python_GuerreroLinderman/prescripciones/" + codigo_consulta + ".json"

    prescripcion = {
        "consulta": codigo_consulta,
        "cedula paciente": cedula_paciente,
        "nombre paciente":nombre_paciente + " " + apellido_paciente,
        "medico": nombre_medico + " " +apellido_medico,
        "cedula medico": cedula_medico,
        "fecha": fecha,
        "medicamentos": medicamentos
         }

    
    with open(ruta_prescripcion, "w", encoding="utf-8") as archivo:
        json.dump(prescripcion, archivo, indent=4)

    print("Prescripcion generada exitosamente")
    print("Archivo:", ruta_prescripcion)


def consultar_historia():
    base_datos=cargar_base_datos()

    cedula = input("Ingrese la cédula del paciente: ")

    if cedula not in base_datos["pacientes"]:
        print("Paciente no registrado")
        input("Presione Enter para volver al menú ")
        return

    paciente = base_datos["pacientes"][cedula]

    print("\n========== HISTORIA CLÍNICA ==========\n")
    print("Cédula:", cedula)
    print("Nombre:", paciente["nombre"])
    print("Apellidos:", paciente["apellidos"])
    print("Teléfono:", paciente["telefono"])
    print("Email:", paciente["email"])
    print("Direccion:", paciente["direccion"])
    print("Genero:", paciente["genero"])
    print("Estado civil:", paciente["estado civil"])

    encontrado = False

    for codigo in base_datos["diagnosticos"]:
        consulta = base_datos["diagnosticos"][codigo]

        if consulta["cedula_paciente"] == cedula:
                encontrado = True

                print("-------------------------")
                print("Consulta encontrada:", codigo)
                print("Fecha:", consulta["fecha"])
                print("Diagnóstico:", consulta["diagnostico"])

                cedula_medico = consulta["cedula_medico"]

                medico = base_datos["usuarios"][cedula_medico]

                print("Medico:", medico["nombre"], medico["apellidos"])

                print("\nSintomas:")

                for sintoma in consulta["sintomas"]:
                    print(f"- {sintoma}")

                print("\nMedicamentos prescritos:")
                
                for medicamento in consulta["medicamentos"]:
                    print("Medicamento:", medicamento["medicamento"])
                    print("Cantidad:", medicamento["cantidad"])
                    print("Dosis:", medicamento["dosis"])
                    print("Duración:", medicamento["tiempo"], "Días")
                    
    input("\nPresione enter para volver al menu ")

    if encontrado == False:
        print("El paciente no tiene consultas registradas")
    input("Presione enter para volver al menu ")

def menu(cedula_usuario,rol_usuario):
    while True:
        print("""
 ========= MENÚ CLÍNICA ACME =========

 1. Registrar usuario
 2. Registrar paciente
 3. Diagnosticar paciente
 4. Consultar historia clínica
 5. Cerrar sesión
 6. Generar reporte carga medicos\n
 """)
        opcion=input("eleccione una opción: ")

        match opcion:
            case "1":
                if rol_usuario=="administrativo":
                    registrar_usuario()
                else:
                    print("No tiene permisos para registrar usuarios")
                    input("Presione enter para volver al menú ")
            case "2":
                    registro_pacientes()
            case "3":
                if rol_usuario=="medico":
                    diagnosticar_pacientes(cedula_usuario)
                else:
                    print("No tiene permisos para diagnosticar pacientes")
                    input("Presione enter para volver al menú ")
            case "4":
                consultar_historia()
            case "5":
                print("Sesión cerrada correctamente")
                break
            case "6":
                carga_medicos()
            case _:
                print("Opcion invalida")

def iniciar_sistema():
    while True:
        cedula_usuario = login()

        base_datos = cargar_base_datos()
        rol_usuario = base_datos["usuarios"][cedula_usuario]["rol"]

        menu(cedula_usuario, rol_usuario)


def carga_medicos():
    base_datos = cargar_base_datos()

    ruta_reporte_carga_medicos = "/home/camper/Documentos/Linderman Ejercicios/Proyecto_Python_GuerreroLinderman/reporte_carga_medicos.json"


    for cedula in base_datos["usuarios"]:
            
        if base_datos["usuarios"][cedula]["rol"]== "medico":

            total_diagnosticos=0

        for consulta in base_datos["diagnosticos"]:    
            if base_datos["diagnosticos"][consulta]["cedula_medico"]== cedula:
                total_diagnosticos+=1

            pacientes_distintos=[]

            if base_datos["diagnosticos"][consulta]["cedula_paciente"] not in pacientes_distintos:
                pacientes_distintos.append(base_datos["diagnosticos"][consulta]["cedula_paciente"])

            sintomas_totales=[]

            sintomas_totales.append(base_datos["diagnosticos"][consulta]["cedula_paciente"][len("sintomas")])

            sintomas_promedio=len(sintomas_totales)/total_diagnosticos

            medicamentos_totales=[]
            
            medicamentos_totales.append(base_datos["diagnosticos"]["cedula_paciente"]["medicamentos"])

            medicamentos_promedio=len(medicamentos_totales)/total_diagnosticos

            reporte_carga_medicos= {
                "id_medico": cedula,
                "nombre_completo":base_datos["usuarios"]["nombre"] +" "+base_datos["usuarios"]["apellidos"] ,
                "total_diagnosticos": total_diagnosticos,
                "pacientes_distintos": len(pacientes_distintos),
                "promedio_sintomas_por_consulta": sintomas_promedio,
                "promedio_medicamentos_por_consulta": medicamentos_promedio
             }

    with open(ruta_reporte_carga_medicos, "w", encoding="utf-8") as reporte:
            json.dump(reporte_carga_medicos, reporte, indent=4)

    guardar_datos(reporte_carga_medicos.json )
