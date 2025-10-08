from numeros import invierte_numero, convierte_binario, busca_perfecto, busca_perfecto_rapido
import time

def test_invierte_numero():
    print("Probando invierte_numero...")
    assert invierte_numero(0) == 0
    assert invierte_numero(12345) == 54321
    assert invierte_numero(1000) == 1
    assert invierte_numero(987654321) == 123456789

def test_convierte_binario():
    print("Probando convierte_binario...")
    assert convierte_binario(0) == "0"
    assert convierte_binario(5) == "101"
    assert convierte_binario(10) == "1010"
    assert convierte_binario(255) == "11111111"

def test_busca_perfecto():
    print("Probando busca_perfecto...")
    def cronometra_llamada(func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        return end - start, result

    tiempo, resultado = cronometra_llamada(busca_perfecto, 1)
    print(f"Tiempo ejecución de busca_perfecto(1): {tiempo:.6f} segundos")
    assert resultado == 6

    tiempo, resultado = cronometra_llamada(busca_perfecto, 2)
    print(f"Tiempo ejecución de busca_perfecto(2): {tiempo:.6f} segundos")
    assert resultado == 28

    tiempo, resultado = cronometra_llamada(busca_perfecto, 3)
    print(f"Tiempo ejecución de busca_perfecto(3): {tiempo:.6f} segundos")
    assert resultado == 496

    tiempo, resultado = cronometra_llamada(busca_perfecto, 4)
    print(f"Tiempo ejecución de busca_perfecto(4): {tiempo:.6f} segundos")
    assert resultado == 8128

    # Descomenta estas líneas si quieres probar con un número mayor (ten en cuenta que puede tardar...)
    #tiempo, resultado = cronometra_llamada(busca_perfecto, 5)
    #print(f"Tiempo ejecución de busca_perfecto(5): {tiempo:.6f} segundos")
    #assert resultado == 33550336

test_invierte_numero()
test_convierte_binario()
test_busca_perfecto()
print("Todas las pruebas pasaron correctamente.")