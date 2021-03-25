import db
from model import Tarea, Estado, Usuario


salir = True 

def ListaDeTareas():
    print('Estas son tus tareas')

    tareas = db.session.query(Tarea).all()
    for tarea in tareas:
        print(tarea.id, tarea.titulo, tarea.descripcion, tarea.estado, tarea.responsable, tarea.fecha)

    

def CrearUnaNuevaTarea():
    print('Crear una tarea nueva.')
    titulo = input("Escribe un titulo: ")
    descripcion = input("Escribe una descripcion: ")
    estado = input("Escribe un estado, en desarrollo, en correccion o terminado : ")
    responsable = input("Escribe responsable: ")
    fecha = input("Escribe fecha de creacion: ")

    tarea = Tarea(titulo, descripcion, estado, responsable, fecha)

    db.session.add(tarea)
    db.session.commit()


    print('Tarea creada')

def CambiarEstadoDeUnaTarea():
    print ('Cambiar estado de la tarea')
    
    estadoReferencia = input("Escribe titulo de la tarea a editar:  ")

    estadoActual = db.session.query(Tarea).filter_by(titulo=estadoReferencia).first()
    NombreEstado = input('Elegir nuevo estado entre "en desarrollo", "en corrección", "terminado": ')

    if(NombreEstado.lower() == "en desarrollo"):
        estadoNuevo = "en desarrollo"
        estadoActual.estado = estadoNuevo
        db.session.commit()
    
    
    elif(NombreEstado.lower() == "en corrección"):
        estadoNuevo = "en corrección"
        estadoActual.estado = estadoNuevo
        db.session.commit()
    
    elif(NombreEstado.lower() == "terminado"):
        estadoNuevo = "terminado"
        estadoActual.estado = estadoNuevo
        db.session.commit()
    
    else:
        print("Estado no encontrado, introduzca uno de las tres opciones. ")


    print('Estado actualizado')


def EditarUnaTarea():

    tituloReferencia = input("Escribe un titulo antiguo :  ")
    titulo = input("Escribe un nuevo titulo: ")
    descripcion = input("Escribe una nueva descripcion: ")
    responsable = input("Escibe nuevo responsable: ")
    fecha = input("Escribe nueva fecha: ")

    tarea = db.session.query(Tarea).filter_by(titulo=tituloReferencia).first()
    tarea.titulo = titulo 
    tarea.descripcion = descripcion
    tarea.responsable = responsable
    tarea.fecha = fecha 
    
    db.session.commit()

    print('Tarea Editada')


def BorrarUnaTarea ():
    
    tituloReferencia = input("Escribe el titulo de la tarea a eliminar : ")
    tarea = db.session.query(Tarea).filter_by(titulo=tituloReferencia).first()


    db.session.delete(tarea)
    db.session.commit()
    print('Tarea borrada')


def BusquedaPorEmail():
    email = input("Escribe el email : ")
    usuario = db.session.query(Usuario).filter_by(email=email).first()

    print(usuario)

def BusquedaPorResponsable():
    
    responsable = input("Escribe un nombre : ")
    tarea = db.session.query(Tarea).filter_by(responsable=responsable).first()
    print(tarea)


def ListaDeUsuarios():

    print("Estos son los usuarios")
    usuarios = db.session.query(Usuario).all()
    for usuario in usuarios:
        print(usuario.id, usuario.nombre, usuario.apellido, usuario.email)

    
def CrearUsuario():
    print("Crea un usuario")
    nombre = input("Nombre  de la persona que realice la tarea: ")
    apellido = input("Apellido de la persona que realice la tarea: ")
    email = input("Email del usuario: ")

    usuario = Usuario(nombre, apellido, email)

    db.session.add(usuario)
    db.session.commit()
    print("usuario creado")



def EditarUsuario():
    
    nombreReferencia = input("Escribe el nombre del usuario a madificar :  ")
    nombre = input("Escribe un nuevo nombre: ")
    apellido = input("Escribe un nuevo apellido: ")
    email = input("Escibe nuevo email: ")
    
    usuario = db.session.query(Usuario).filter_by(nombre=nombreReferencia).first()
    usuario.nombre = nombre 
    usuario.apellido = apellido
    usuario.email = email
    db.session.commit()

    print('Tarea Editada')

def EliminarUsuario():
    
    nombreReferencia = input("Escribe el usuario a eliminar : ")
    usuario = db.session.query(Usuario).filter_by(nombre=nombreReferencia).first()


    db.session.delete(usuario)
    db.session.commit()
    print('Usuario eliminado')




while salir:


    print("Bienvenido a las tareas")
    print("[1]Lista de tareas")
    print("[2]Crear una nueva tarea")
    print("[3]Cambiar estado de una tarea")
    print("[4]Editar una tarea")
    print("[5]Borrar una tarea")
    print("[6]Busqueda por email o responsable")
    print("[7]Lista de usuarios")
    print("[8]Crar usuario")
    print("[9]Editar usuario")
    print("[10]Eliminar usuario")
    print("[11]Salir")
    opciones = input("Introduce un numero: ")

    if(opciones == '1'):
        ListaDeTareas()

    elif (opciones == '2'):
        CrearUnaNuevaTarea()

    elif(opciones =='3'):
        CambiarEstadoDeUnaTarea()

    elif(opciones =='4'):
        EditarUnaTarea()

    elif(opciones =='5'):
        BorrarUnaTarea()

    elif(opciones =='6'):
        
        print("Busqueda por email o responsable")

        print("[1]Busqueda por email")
        print("[2]Busqueda por responsable")
        opcion = input("Introduce un numero : ")


        if (opcion =="1"):
            BusquedaPorEmail()
        elif (opcion =="2"):
            BusquedaPorResponsable()

    elif(opciones =='7'):  
        ListaDeUsuarios()

    elif(opciones =='8'):
        CrearUsuario()

    elif(opciones =='9'): 
        EditarUsuario()
    
    elif(opciones =='10'):
        EliminarUsuario()
    
    elif(opciones =='11'):
        salir = False
        print('Cerrando Agenda')
    else:
        print('Opcion incorrecta')

