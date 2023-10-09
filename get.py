#hollaaa
class Estado(object):
    def __init__(self, estaciones):
       #constructor de Estado. 
       #estaciones: una llista de objectos Estacion que representan las esatciones de Bicing
        self.estaciones = estaciones  # Lista de objetos Estacion

    def __eq__(self, other):
       #metodo para verificar si dos estados son iguales
        return self.estaciones == other.estaciones

    def __hash__(self):
        #método para generar un hash del estado
        return hash(tuple(self.estaciones))

    def __str__(self):
        #método para obtener una representación en cadena del estado
        return "\n".join([str(estacion) for estacion in self.estaciones])


class Furgoneta(object):
    def __init__(self, capacidad_maxima=30):
        self.capacidad_maxima = capacidad_maxima
        self.bicicletas = []  # Lista de bicicletas que transporta la furgoneta
        self.origen = None  # Estación de origen
        self.destinos = []  # Lista de estaciones de destino
        self.trayectos = []  # Lista de trayectos (pares de origen y destino)

    def cargar_bicicletas(self, bicicletas):
        """
        Carga bicicletas en la furgoneta, teniendo en cuenta su capacidad máxima.
        """
        if len(self.bicicletas) + len(bicicletas) <= self.capacidad_maxima:
            self.bicicletas.extend(bicicletas)
            return True
        else:
            return False  # No se pueden cargar más bicicletas

    def descargar_bicicletas(self):
        """
        Descarga las bicicletas en las estaciones de destino.
        """
        for destino, cantidad in self.destinos:
            # Realiza el traslado de bicicletas a la estación de destino
            # Aquí debes implementar la lógica para mover las bicicletas desde la furgoneta a la estación
            pass

    def realizar_trayecto(self):
        """
        Realiza un trayecto desde la estación de origen a las estaciones de destino.
        """
        if self.origen and self.destinos:
            self.trayectos.append((self.origen, self.destinos))
            self.descargar_bicicletas()  # Descarga las bicicletas en las estaciones de destino
            self.bicicletas = []  # La furgoneta queda vacía después del trayecto
        else:
            raise ValueError("La furgoneta no tiene origen o destinos asignados.")

    def asignar_origen(self, origen):
        """
        Asigna la estación de origen para la furgoneta.
        """
        self.origen = origen

    def asignar_destino(self, destino, cantidad):
        """
        Asigna una estación de destino y la cantidad de bicicletas a trasladar a esa estación.
        """
        self.destinos.append((destino, cantidad))

class Get(object):
    def get_station_count(self) -> int:
        """
        Obtiene el número total de estaciones de Bicing.
        """
        pass

    def get_station_info(self, station_id: int) -> dict:
        """
        Obtiene la información de una estación específica.

        Args:
            station_id (int): El identificador de la estación.

        Returns:
            dict: Un diccionario que contiene información sobre la estación.
                Ejemplo de estructura:
                {
                    "station_id": int,
                    "coordX": int,
                    "coordY": int,
                    "num_bicicletas_no_usadas": int,
                    "num_bicicletas_next": int,
                    "demanda": int
                }
        """
        pass

    def get_total_bicycles(self) -> int:
        """
        Obtiene el número total de bicicletas en todas las estaciones.
        """
        pass

    def get_total_demand(self) -> int:
        """
        Obtiene la demanda total prevista de bicicletas en todas las estaciones.
        """
        pass

    def get_available_bicycles(self) -> int:
        """
        Obtiene el número total de bicicletas disponibles para mover en todas las estaciones.
        """
        pass

    def get_needed_bicycles(self) -> int:
        """
        Obtiene el número total de bicicletas que se necesitan mover para cubrir la demanda en todas las estaciones.
        """
        pass

