def calculo_promedio(lista_valores):
    # Codigos de retorno esperados
    # Caso de éxito => 0
    # Errores esperados funcion calculo_promedio
    # Error Lista ingresada no contiene únicamente números => -80
    # Error Lista ingresada tiene más de 10 elementos       => -90

    res = 0  # Resultado suma de valores de la lista

    try:
        for i in lista_valores:
            # Recorrer lista evaluando si valores son números y sumarlos
            if isinstance(i, bool):
                return -80, None
            res = res + i

    except TypeError:
        return -80, None

    if len(lista_valores) > 10:
        return -90, None
    try:
        # Calcular el promedio del resultado res y mostrar en pantalla
        return 0, res / len(lista_valores)
    except ZeroDivisionError:
        return 0, None


def operation_selector(num1, num2, op):
    '''
    Codigos de retorno esperados

    Caso de éxito => 0

    Errores esperados funcion operation_selector

    Error Parámetro ingresado no es de tipo Entero => -50
    Error Parámetro ingresado no es String => -60
    Error Parámetro ingresado no cumple con las
    especificaciones del programa (+, -, *, &) => -70
    '''
    # Sección de ejecución de la operación solicitada
    try:
        operacion = {
            "+": num1 + num2,
            "-": num1 - num2,
            "*": num1 * num2,
            "&": num1 & num2
        }
    except TypeError:
        return -50, None

    # Sección de pruebas de validación datos ingresados

    if not (isinstance(num1, int) | isinstance(num2, int)):
        return -50, None
    if isinstance(num1, bool) | isinstance(num2, bool):
        return -50, None
    if not isinstance(op, str):
        return -60, None
    if operacion.get(op) is None:
        return -70, None

    return 0, operacion.get(op)
