from w1thermsensor import W1ThermSensor

sensor1 = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "0000054f25aa")
temperature_in_fahrenheit = sensor1.get_temperature(W1ThermSensor.DEGREES_F)
print(temperature_in_fahrenheit)