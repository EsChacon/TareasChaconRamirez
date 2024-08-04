def PWM():
    # Contador de 0 a 255
    sum = 0
    # Variable de conteo actual
    while True:
        sum = sum + 1
        if sum > 255:
            return None
            # Al superar 255 reinicia el conteo


PWM()
