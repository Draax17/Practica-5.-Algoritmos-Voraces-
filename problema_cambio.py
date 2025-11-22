"""
Problema del Cambio (Change-Making Problem)
Algoritmo Voraz para dar cambio con la menor cantidad de monedas.

Monedas disponibles: {1, 5, 10, 25}
"""


def dar_cambio_voraz(cantidad: int, monedas: list[int] = [25, 10, 5, 1]) -> dict[int, int]:
    """
    Resuelve el problema del cambio usando un algoritmo voraz.
    
    Estrategia: Siempre elegir la moneda de mayor denominación posible.
    
    Args:
        cantidad: La cantidad total a cambiar
        monedas: Lista de monedas disponibles (ordenadas de mayor a menor)
    
    Returns:
        Diccionario con la cantidad de cada moneda utilizada
    """
    # Ordenar monedas de mayor a menor (asegurar orden correcto)
    monedas_ordenadas = sorted(monedas, reverse=True)
    
    resultado = {}
    cantidad_restante = cantidad
    
    for moneda in monedas_ordenadas:
        if cantidad_restante >= moneda:
            cantidad_monedas = cantidad_restante // moneda
            resultado[moneda] = cantidad_monedas
            cantidad_restante = cantidad_restante % moneda
    
    return resultado


def mostrar_cambio(cantidad: int, resultado: dict[int, int]) -> None:
    """
    Muestra el resultado del cambio de forma legible.
    
    Args:
        cantidad: La cantidad original
        resultado: Diccionario con las monedas utilizadas
    """
    print(f"\nCambio para ${cantidad}:")
    print("-" * 40)
    
    total_monedas = 0
    for moneda in sorted(resultado.keys(), reverse=True):
        cantidad_monedas = resultado[moneda]
        if cantidad_monedas > 0:
            print(f"  ${moneda:2d}: {cantidad_monedas:3d} moneda(s)")
            total_monedas += cantidad_monedas
    
    print("-" * 40)
    print(f"Total de monedas utilizadas: {total_monedas}")
    
    # Verificar que la suma es correcta
    suma_verificacion = sum(moneda * cantidad for moneda, cantidad in resultado.items())
    print(f"Verificación: ${suma_verificacion} (esperado: ${cantidad})")
    if suma_verificacion == cantidad:
        print("✓ Verificación correcta")
    else:
        print("✗ Error en la verificación")


def probar_casos():
    """
    Prueba el algoritmo con diversos casos de N.
    """
    print("=" * 60)
    print("PROBLEMA DEL CAMBIO - ALGORITMO VORAZ")
    print("=" * 60)
    
    casos_prueba = [
        1,      # Caso mínimo
        4,      # Solo monedas de 1
        5,      # Una moneda de 5
        10,     # Una moneda de 10
        25,     # Una moneda de 25
        26,     # 25 + 1
        30,     # 25 + 5
        37,     # 25 + 10 + 1 + 1
        49,     # 25 + 10 + 10 + 1 + 1 + 1 + 1
        50,     # 25 + 25
        67,     # 25 + 25 + 10 + 5 + 1 + 1
        99,     # 25 + 25 + 25 + 10 + 10 + 1 + 1 + 1 + 1
        100,    # 25 + 25 + 25 + 25
        123,    # Caso más complejo
        250,    # Caso grande
    ]
    
    for cantidad in casos_prueba:
        resultado = dar_cambio_voraz(cantidad)
        mostrar_cambio(cantidad, resultado)
    
    print("\n" + "=" * 60)
    print("Análisis del Algoritmo:")
    print("=" * 60)
    print("Complejidad temporal: O(n) donde n es el número de tipos de monedas")
    print("Complejidad espacial: O(n) para almacenar el resultado")
    print("\nNota: Este algoritmo es óptimo para el sistema de monedas {1, 5, 10, 25}")
    print("      porque es un sistema de monedas canónico (greedy siempre da la solución óptima)")


if __name__ == "__main__":
    probar_casos()

