def getTemperature():
    f_temperature = int(input('What is the temperature?'))


def convertTemperature(tempetureF):
    C = ((tempetureF-32)*5/9)
    return tempetureC

def displaysTemperature(c_temperature):
    print(f"The temperature is {c_temperature}")
    
    


if __name__ == "__main__":
  temperature = getTemperature()
  temperatureC = convertTemperature(temperature)
  displaysTemperature()