"""
Problema de Selección de Actividades (Activity Selection Problem)
Algoritmo Voraz para seleccionar el máximo número de actividades sin traslape.

Dado un conjunto de actividades con tiempo de inicio y fin,
selecciona el máximo número de actividades posibles de manera que no se traslapen.
"""

from typing import List, Tuple
import random


class Actividad:
    """Representa una actividad con tiempo de inicio y fin."""
    
    def __init__(self, inicio: int, fin: int, nombre: str = ""):
        if inicio >= fin:
            raise ValueError("El tiempo de inicio debe ser menor que el tiempo de fin")
        self.inicio = inicio
        self.fin = fin
        self.nombre = nombre
        self.duracion = fin - inicio
    
    def __repr__(self):
        return f"Actividad({self.inicio}-{self.fin}, '{self.nombre}')"
    
    def traslapa_con(self, otra: 'Actividad') -> bool:
        """
        Verifica si esta actividad se traslapa con otra.
        
        Args:
            otra: Otra actividad a comparar
        
        Returns:
            True si hay traslape, False en caso contrario
        """
        return not (self.fin <= otra.inicio or otra.fin <= self.inicio)


def seleccion_actividades_voraz(actividades: List[Actividad]) -> List[Actividad]:
    """
    Resuelve el problema de selección de actividades usando algoritmo voraz.
    
    Estrategia: Ordenar por tiempo de fin (menor a mayor) y seleccionar actividades
    que no se traslapen, siempre eligiendo la que termina más temprano.
    
    Args:
        actividades: Lista de actividades disponibles
    
    Returns:
        Lista de actividades seleccionadas (máximo número sin traslape)
    """
    if not actividades:
        return []
    
    # Ordenar actividades por tiempo de fin (menor a mayor)
    actividades_ordenadas = sorted(actividades, key=lambda x: x.fin)
    
    seleccionadas = []
    ultimo_fin = -1  # Tiempo de fin de la última actividad seleccionada
    
    for actividad in actividades_ordenadas:
        # Si la actividad comienza después o al mismo tiempo que termina la última seleccionada
        if actividad.inicio >= ultimo_fin:
            seleccionadas.append(actividad)
            ultimo_fin = actividad.fin
    
    return seleccionadas


def generar_actividades_aleatorias(n: int, tiempo_max: int = 100) -> List[Actividad]:
    """
    Genera una lista de actividades aleatorias para pruebas.
    
    Args:
        n: Número de actividades a generar
        tiempo_max: Tiempo máximo para el fin de las actividades
    
    Returns:
        Lista de actividades generadas
    """
    random.seed(42)  # Para reproducibilidad
    actividades = []
    
    for i in range(n):
        inicio = random.randint(0, tiempo_max - 1)
        fin = random.randint(inicio + 1, tiempo_max)
        nombre = f"Actividad {i+1}"
        actividades.append(Actividad(inicio, fin, nombre))
    
    return actividades


def verificar_sin_traslape(actividades: List[Actividad]) -> bool:
    """
    Verifica que las actividades seleccionadas no se traslapen.
    
    Args:
        actividades: Lista de actividades a verificar
    
    Returns:
        True si no hay traslapes, False en caso contrario
    """
    for i in range(len(actividades)):
        for j in range(i + 1, len(actividades)):
            if actividades[i].traslapa_con(actividades[j]):
                return False
    return True


def mostrar_resultado_actividades(
    actividades_disponibles: List[Actividad],
    actividades_seleccionadas: List[Actividad]
) -> None:
    """
    Muestra el resultado de la selección de actividades de forma legible.
    
    Args:
        actividades_disponibles: Todas las actividades disponibles
        actividades_seleccionadas: Actividades seleccionadas por el algoritmo
    """
    print(f"\n{'='*80}")
    print(f"SELECCIÓN DE ACTIVIDADES")
    print(f"{'='*80}")
    
    print(f"\nActividades disponibles: {len(actividades_disponibles)}")
    print(f"Actividades seleccionadas: {len(actividades_seleccionadas)}")
    
    # Mostrar todas las actividades ordenadas por inicio
    print(f"\nTodas las actividades (ordenadas por inicio):")
    print(f"{'Nombre':<15} {'Inicio':>8} {'Fin':>8} {'Duración':>10}")
    print("-" * 50)
    
    actividades_ordenadas = sorted(actividades_disponibles, key=lambda x: x.inicio)
    for actividad in actividades_ordenadas:
        marcador = "✓" if actividad in actividades_seleccionadas else " "
        print(f"{marcador} {actividad.nombre:<13} "
              f"{actividad.inicio:>8} "
              f"{actividad.fin:>8} "
              f"{actividad.duracion:>10}")
    
    # Mostrar línea de tiempo
    print(f"\nLínea de tiempo (actividades seleccionadas marcadas con ✓):")
    tiempo_max = max(act.fin for act in actividades_disponibles)
    
    # Crear representación visual simple
    linea = [' '] * (tiempo_max + 1)
    for actividad in actividades_seleccionadas:
        for i in range(actividad.inicio, actividad.fin):
            if i < len(linea):
                linea[i] = '█'
    
    print("Tiempo: ", end="")
    for i in range(0, tiempo_max + 1, max(1, tiempo_max // 20)):
        print(f"{i:3d}", end="")
    print()
    
    print("Actividades: ", end="")
    for i in range(0, tiempo_max + 1, max(1, tiempo_max // 20)):
        print(f" {linea[i]} ", end="")
    print()
    
    # Verificar que no hay traslapes
    if verificar_sin_traslape(actividades_seleccionadas):
        print("\n✓ Verificación: Las actividades seleccionadas NO se traslapan")
    else:
        print("\n✗ ERROR: Las actividades seleccionadas SÍ se traslapan")
    
    # Calcular tiempo total cubierto
    tiempo_total = sum(act.duracion for act in actividades_seleccionadas)
    print(f"Tiempo total cubierto: {tiempo_total} unidades")


def probar_seleccion_actividades():
    """
    Prueba el algoritmo con diferentes casos.
    """
    print("=" * 80)
    print("PROBLEMA DE SELECCIÓN DE ACTIVIDADES - ALGORITMO VORAZ")
    print("=" * 80)
    
    # Caso 1: Ejemplo simple
    print(f"\n{'#'*80}")
    print("CASO 1: Ejemplo Simple")
    print(f"{'#'*80}")
    
    actividades1 = [
        Actividad(1, 4, "A"),
        Actividad(3, 5, "B"),
        Actividad(0, 6, "C"),
        Actividad(5, 7, "D"),
        Actividad(3, 8, "E"),
        Actividad(5, 9, "F"),
        Actividad(6, 10, "G"),
        Actividad(8, 11, "H"),
        Actividad(8, 12, "I"),
        Actividad(2, 13, "J"),
        Actividad(12, 14, "K"),
    ]
    
    seleccionadas1 = seleccion_actividades_voraz(actividades1)
    mostrar_resultado_actividades(actividades1, seleccionadas1)
    
    # Caso 2: Actividades aleatorias
    print(f"\n{'#'*80}")
    print("CASO 2: 20 Actividades Aleatorias")
    print(f"{'#'*80}")
    
    actividades2 = generar_actividades_aleatorias(20, tiempo_max=50)
    seleccionadas2 = seleccion_actividades_voraz(actividades2)
    mostrar_resultado_actividades(actividades2, seleccionadas2)
    
    # Caso 3: Muchas actividades
    print(f"\n{'#'*80}")
    print("CASO 3: 50 Actividades Aleatorias")
    print(f"{'#'*80}")
    
    actividades3 = generar_actividades_aleatorias(50, tiempo_max=100)
    seleccionadas3 = seleccion_actividades_voraz(actividades3)
    mostrar_resultado_actividades(actividades3, seleccionadas3)
    
    print("\n" + "=" * 80)
    print("Análisis del Algoritmo:")
    print("=" * 80)
    print("Complejidad temporal: O(n log n) - dominada por la ordenación")
    print("Complejidad espacial: O(n) - para almacenar las actividades ordenadas")
    print("\nOptimalidad: Este algoritmo voraz SIEMPRE encuentra la solución óptima")
    print("             (máximo número de actividades sin traslape)")
    print("\nEstrategia: Seleccionar siempre la actividad que termina más temprano")
    print("            entre las que no se traslapan con las ya seleccionadas.")


if __name__ == "__main__":
    probar_seleccion_actividades()

