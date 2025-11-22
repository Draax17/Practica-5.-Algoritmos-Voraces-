"""
Problema de la Mochila Fraccionaria (Fractional Knapsack Problem)
Algoritmo Voraz para maximizar el valor en una mochila con capacidad limitada.

Estrategia: Ordenar por ratio valor/peso (densidad de valor) y tomar fracciones si es necesario.
"""

import random
from typing import List, Tuple


class Articulo:
    """Representa un artículo con peso y valor."""
    
    def __init__(self, peso: float, valor: float, nombre: str = ""):
        self.peso = peso
        self.valor = valor
        self.nombre = nombre
        self.ratio = valor / peso if peso > 0 else 0
    
    def __repr__(self):
        return f"Articulo(peso={self.peso}, valor={self.valor}, ratio={self.ratio:.2f})"


def mochila_fraccionaria_voraz(
    articulos: List[Articulo], 
    capacidad: float
) -> Tuple[List[Tuple[Articulo, float]], float]:
    """
    Resuelve el problema de la mochila fraccionaria usando algoritmo voraz.
    
    Estrategia: Ordenar por ratio valor/peso (mayor a menor) y tomar artículos completos
    o fracciones hasta llenar la mochila.
    
    Args:
        articulos: Lista de artículos disponibles
        capacidad: Capacidad máxima de la mochila
    
    Returns:
        Tupla con:
        - Lista de tuplas (artículo, fracción_tomada)
        - Valor total obtenido
    """
    # Ordenar artículos por ratio valor/peso (mayor a menor)
    articulos_ordenados = sorted(articulos, key=lambda x: x.ratio, reverse=True)
    
    mochila = []
    capacidad_restante = capacidad
    valor_total = 0.0
    
    for articulo in articulos_ordenados:
        if capacidad_restante <= 0:
            break
        
        if articulo.peso <= capacidad_restante:
            # Tomar el artículo completo
            mochila.append((articulo, 1.0))
            valor_total += articulo.valor
            capacidad_restante -= articulo.peso
        else:
            # Tomar una fracción del artículo
            fraccion = capacidad_restante / articulo.peso
            mochila.append((articulo, fraccion))
            valor_total += articulo.valor * fraccion
            capacidad_restante = 0
    
    return mochila, valor_total


def generar_articulos_aleatorios(n: int, peso_max: float = 100.0, valor_max: float = 1000.0) -> List[Articulo]:
    """
    Genera una lista de artículos aleatorios para pruebas.
    
    Args:
        n: Número de artículos a generar
        peso_max: Peso máximo de un artículo
        valor_max: Valor máximo de un artículo
    
    Returns:
        Lista de artículos generados
    """
    random.seed(42)  # Para reproducibilidad
    articulos = []
    
    for i in range(n):
        peso = round(random.uniform(1.0, peso_max), 2)
        valor = round(random.uniform(10.0, valor_max), 2)
        nombre = f"Artículo {i+1}"
        articulos.append(Articulo(peso, valor, nombre))
    
    return articulos


def mostrar_resultado_mochila(
    mochila: List[Tuple[Articulo, float]], 
    valor_total: float, 
    capacidad: float,
    num_articulos: int
) -> None:
    """
    Muestra el resultado de la mochila de forma legible.
    
    Args:
        mochila: Lista de artículos en la mochila con sus fracciones
        valor_total: Valor total obtenido
        capacidad: Capacidad de la mochila
        num_articulos: Número total de artículos disponibles
    """
    print(f"\n{'='*70}")
    print(f"RESULTADO MOCHILA FRACCIONARIA ({num_articulos} artículos, capacidad: {capacidad})")
    print(f"{'='*70}")
    
    peso_total = 0.0
    print(f"\nArtículos seleccionados:")
    print(f"{'Nombre':<15} {'Peso':>10} {'Valor':>10} {'Ratio':>10} {'Fracción':>10} {'Valor Obtenido':>15}")
    print("-" * 70)
    
    for articulo, fraccion in mochila:
        peso_usado = articulo.peso * fraccion
        valor_obtenido = articulo.valor * fraccion
        peso_total += peso_usado
        
        print(f"{articulo.nombre:<15} "
              f"{articulo.peso:>10.2f} "
              f"{articulo.valor:>10.2f} "
              f"{articulo.ratio:>10.2f} "
              f"{fraccion:>10.2%} "
              f"{valor_obtenido:>15.2f}")
    
    print("-" * 70)
    print(f"Peso total utilizado: {peso_total:.2f} / {capacidad:.2f}")
    print(f"Valor total obtenido: {valor_total:.2f}")
    print(f"Eficiencia (valor/peso): {valor_total/peso_total:.2f}" if peso_total > 0 else "")


def probar_mochila_fraccionaria():
    """
    Prueba el algoritmo con 10, 100 y 1000 artículos.
    """
    print("=" * 70)
    print("PROBLEMA DE LA MOCHILA FRACCIONARIA - ALGORITMO VORAZ")
    print("=" * 70)
    
    casos_prueba = [10, 100, 1000]
    capacidad_base = 500.0
    
    for num_articulos in casos_prueba:
        print(f"\n{'#'*70}")
        print(f"PRUEBA CON {num_articulos} ARTÍCULOS")
        print(f"{'#'*70}")
        
        # Generar artículos aleatorios
        articulos = generar_articulos_aleatorios(num_articulos)
        
        # Calcular capacidad basada en el número de artículos
        capacidad = capacidad_base * (num_articulos / 10)
        
        # Resolver el problema
        mochila, valor_total = mochila_fraccionaria_voraz(articulos, capacidad)
        
        # Mostrar resultados
        mostrar_resultado_mochila(mochila, valor_total, capacidad, num_articulos)
        
        # Estadísticas adicionales
        print(f"\nEstadísticas:")
        print(f"  - Artículos disponibles: {num_articulos}")
        print(f"  - Artículos seleccionados: {len(mochila)}")
        print(f"  - Tiempo estimado: O(n log n) para ordenar + O(n) para seleccionar")
    
    print("\n" + "=" * 70)
    print("Análisis del Algoritmo:")
    print("=" * 70)
    print("Complejidad temporal: O(n log n) - dominada por la ordenación")
    print("Complejidad espacial: O(n) - para almacenar los artículos ordenados")
    print("\nOptimalidad: Este algoritmo voraz SIEMPRE encuentra la solución óptima")
    print("             para el problema de la mochila fraccionaria.")


if __name__ == "__main__":
    probar_mochila_fraccionaria()

