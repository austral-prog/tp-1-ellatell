def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
horas_completas = total_segundos // 3600  
    print("Horas completas: ", horas_completas)
    minutos_completos: (total_segundos % 3600) // 60 
    print("minutos completos resultantes:  ", minutos_completos)
    segundos_restantes = total_segundos % 60 
    print("segundos restantes: ", segundos_restantes)
