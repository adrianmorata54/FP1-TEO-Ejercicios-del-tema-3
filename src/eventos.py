from datetime import date, timedelta
 
def es_dia_festivo(fecha: date) -> bool:    
    """
    Función auxiliar que simula la verificación de días festivos.
    Parámetros:
        fecha: date: La fecha a verificar.
    Devuelve:
        bool: True si la fecha es un día festivo, False en caso contrario.
    """
    dias_festivos = {
        date(2026, 1, 1),   # Año Nuevo
        date(2026, 1, 6),   # Día de Reyes
        date(2026, 3, 19),  # San José
        date(2026, 5, 1),   # Día del Trabajo
        date(2026, 8, 15),  # Asunción de la Virgen
        date(2026, 10, 12), # Fiesta Nacional de España
        date(2026, 11, 1),  # Todos los Santos
        date(2026, 12, 6),  # Día de la Constitución
        date(2026, 12, 8),  # Inmaculada Concepción
        date(2026, 12, 25)  # Navidad
    }
    return fecha in dias_festivos

def es_dia_no_laborable(fecha: date) -> bool:
    dia_semana = fecha.weekday()
    return dia_semana>=5 or es_dia_festivo(fecha)

def calcular_siguiente_valida(fecha_anterior: date, intervalo_dias: int) -> date:
    while es_dia_no_laborable(fecha):
        fecha = fecha + timedelta(days=intervalo_dias)
    return fecha

def planificar_evento(fecha_inicio: date, intervalo_dias: int, num_eventos: int) -> None:
    pass