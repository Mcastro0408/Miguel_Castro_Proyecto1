import requests # Importacion de request
from Peliculas import Peliculas #Importacion de la clase peliculas
from Planetas import Planetas # Importacion de la clase Planetas
from Especies import Especies # Importacion de la clase Especies
from Personajes import Personajes # Importacion de la Clase Persona

# base de datos de las peliculas de la saga
def films_data_base():
    resp=requests.get("https://www.swapi.tech/api/films")
    return resp.json()

# base de datos de los personajes de la saga
def people_data_base():
    resp=requests.get("https://www.swapi.tech/api/people?page=2&limit=90")
    return resp.json()

# base de datos de las especies de la saga
def species_data_base():
    resp=requests.get("https://www.swapi.tech/api/species?page=2&limit=37")
    return resp.json()

# base de datos de las planetas de la saga
def planets_data_base():
    resp=requests.get("https://www.swapi.tech/api/planets?page=1&limit=60")
    return resp.json()

# creacion de objetos de personajes
def crear_peliculas():
    listasPersonajes=[] # Listas de Personajes objetos
    db=response
    for results in db:
        listasPersonajes.append(Personajes(results['name'], results['homeworld'], results['gender'], results['species'], results['starship'],results['vehicles']))
    
# creacion de objetos de peliculas
def crear_peliculas():
    listasPeliculas=[] # Listas de Peliculas objetos
    db=response
    for results in db:
        listasPeliculas.append(Peliculas(results['title'], results['episode_id'], results['director'], results['release_date'], results['openig_carwl'],))
    
# creacion de objetos de planetas
def crear_planetas():
    ListasPlanetas=[] # Listas de Planetas objetos
    db=response
    for results in db:
        ListasPlanetas.append(Planetas(results['name'], results['climate'], results['population'], results['orbital_period'], results['rotation_period']))

# creacion de objetos de especies
def crear_especies():
    ListasEspecies=[] # Listas de Especies objetos
    db=response
    for results in db:
            ListasEspecies.append(Especies(results['uid'], results['name'], results['language'], results['homeworld'], results['average_height'],))

# Sistema de busqueda por nombre
def search_people(db, name):
        find_number=0
        for people in db['results']: # Itera sobre cada personaje en la lista de resultados de la base de datos
            if name in people['name']: # Comprueba si el nombre buscado se encuentra en el nombre del personaje
                find_number+=1
                id=''
                for lu in people['url']:
                    if lu.isdigit():
                        id=id+lu
                        id=id[1:len(id)] # Construye el ID del personaje a partir del url
                        print(people["name"],"iD: ",id)
                        if find_number:
                            print(f"\nSe encontraron {find_number} resultados.")
                        else:
                            print("\nNo se encontraron resultados ")

print("Hola bienvenido a nuestra enciclopedia de Star Wars")
response=people_data_base()
# Sistema de opciones y respesta
while True:
    option=int(input("""
Introduzca una opcion:
    [0] Salir.
    [1] Buscar personajes.
    [2] Mostrar lista de peliculas.
    [3] Mostrar lista de planetas.
    [4] Mostrar lista de especies.
-------->"""))
    if option == 0:
        break
    elif option == 1:
        name=input("Introduzca el nombre: ")
        search_people(response,name)
    
    elif option == 2:
        for pelicula in listasPeliculas:
            pelicula.show_attr()
        
    elif option == 3:
        for planeta in ListasPlanetas:
            planeta.show_attr()

    elif option == 4:
        for especies in ListasEspecies:
            especies.show_attr()

    else:
        print("Opcion invalida. Intente nuevamente: ")

print("Hasta luego ")