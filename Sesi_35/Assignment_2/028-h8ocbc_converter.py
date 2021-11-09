def celsiusKelvinConvert(temp):
    '''1. Convert Celsius to and from Kelvin'''
    degree = float(temp[:-1])
    tempUnit = temp[-1]
    if tempUnit.lower() == 'c':
        convertUnit = 'Kelvin'
        kelvin = float(round(degree + 273, 15))
        print('Celsius to Kelvin : ', kelvin, convertUnit)
    else:
        convertUnit = 'Celsius'
        celsius = float(round(degree - 273, 15))
        print('Kelvin to Celsius : ', celsius, convertUnit)


def toFahrenheit(temp):
    '''2. Convert from Celsius/Kelvin to Fahrenheit'''
    degree = float(temp[:-1])
    tempUnit = temp[-1]
    convertUnit = 'Fahrenheit'
    if tempUnit == 'c':
        fromCelcius = float(round((degree * 9 / 5) + 32))
        print('Celsius to Fahrenheit', fromCelcius, convertUnit)
    else:
        fromKelvin = float(round((degree - 273.15) * 9 / 5 + 32))
        print('Kelvin to Fahrenheit', fromKelvin, convertUnit)


def fromFahrenheit(temp, convertTo):
    '''3. Convert from Fahrenheit to Celsius/Kelvin'''
    degree = float(temp[:-1])
    tempUnit = convertTo[-1]
    if tempUnit == 'c':
        convertUnit = 'Celsius'
        celsius = float(round((degree - 32) * 5 / 9))
        print('Fahrenheit to Celsius', celsius, convertUnit)
    else:
        convertUnit = 'Kelvin'
        kelvin = float(round((degree - 32) * 5 / 9 + 273.15))
        print('Fahrenheit to Kelvin', kelvin, convertUnit)


def convert(temp, tempUnit, convertTo):
    '''Main Function to convert all type of conversion'''
    if (tempUnit == 'c' or tempUnit == 'k') and convertTo != 'f':
        celsiusKelvinConvert(temp)
    elif convertTo == 'f':
        toFahrenheit(temp)
    elif tempUnit == 'f' and (convertTo == 'c' or convertTo == 'k'):
        fromFahrenheit(temp, convertTo)
    else:
        print ('Error')


loop = True
loop2 = True
while loop == True:
    temp = input(
        "Input the temperature you like to convert from [e.g., 45F, 102C, 99K]: "
    )
    degree = int(temp[:-1])
    tempUnit = temp[-1].lower()
    if tempUnit == 'f' or tempUnit == 'c' or tempUnit == 'k':
        while loop2 == True:
            convertTo = input(
                "Input the temperature unit you want to convert to [e.g., F, C, K]: "
            ).lower()
            if convertTo != tempUnit:
                convert(temp, tempUnit, convertTo)
                loop = False
                loop2 = False
            else:
                print('\n')
                print(
                    'The Temperature unit you want to convert from and to cannot be the same [e.g., C cannot be converted to C]'
                )
                print('\n')
                loop2 = True
    else:
        print('\n')
        print('The end of the input need to be either "k", "c", "f"!')
        print('\n')
        loop = True
