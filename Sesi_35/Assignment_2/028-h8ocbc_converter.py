# Fungsi untuk soal nomor 1
def celsiusKelvinConvert(temp):
    '''
    1. Convert Celsius to and from Kelvin
    :param temp: Input temperature as temp | string
  
    :return: print : Print the result of conversion | float, string
    '''
    degree = float(temp[:-1])
    tempUnit = temp[-1]
    if tempUnit.lower() == 'c':
        convertUnit = 'Kelvin'
        kelvin = float(round(degree + 273, 15))# Formula to convert from Celsius to Kelvin and then round it to the nearest integer
        print('Celsius to Kelvin : ', kelvin, convertUnit)
    else:
        convertUnit = 'Celsius'
        celsius = float(round(degree - 273, 15))# Formula to convert from Kelvin to Celsius and then round it to the nearest integer
        print('Kelvin to Celsius : ', celsius, convertUnit)

# Fungsi untuk soal nomor 2
def toFahrenheit(temp):
    '''
    2. Convert from Celsius/Kelvin to Fahrenheit
    :param temp: Input temperature as temp | string
  
    :return: print : Print the result of conversion | float, string
    '''
    degree = float(temp[:-1])
    tempUnit = temp[-1]
    convertUnit = 'Fahrenheit'
    if tempUnit == 'c':
        fromCelcius = float(round((degree * 9 / 5) + 32))# Formula to convert from Celsius to Fahrenheit and then round it to the nearest integer
        print('Celsius to Fahrenheit : ', fromCelcius, convertUnit)
    else:
        fromKelvin = float(round((degree - 273.15) * 9 / 5 + 32))# Formula to convert from Kelvin to Fahrenheit and then round it to the nearest integer
        print('Kelvin to Fahrenheit : ', fromKelvin, convertUnit)

# Fungsi untuk soal nomor 3 
def fromFahrenheit(temp, convertTo):
    '''
    3. Convert from Fahrenheit to Celsius/Kelvin
    :param temp: Input temperature as temp | string
    :param convertTo: Input the temperature unit that user want to convert to as convertTo | string

    :return: print : Print the result of conversion | float, string
    '''
    degree = float(temp[:-1])
    tempUnit = convertTo[-1]
    if tempUnit == 'c':
        convertUnit = 'Celsius'
        celsius = float(round((degree - 32) * 5 / 9))# Formula to convert from Fahrenheit to Celsius and then round it to the nearest integer
        print('Fahrenheit to Celsius : ', celsius, convertUnit)
    else:
        convertUnit = 'Kelvin'
        kelvin = float(round((degree - 32) * 5 / 9 + 273.15))# Formula to convert from Fahrenheit to Kelvin and then round it to the nearest integer
        print('Fahrenheit to Kelvin : ', kelvin, convertUnit)

# Fungsi Tambahan untuk melakukan segala macam konversi suhu / temperatur
def convert(temp, tempUnit, convertTo):
    '''
    Main Function to convert all type of conversion
    :param temp: Input temperature as temp | string
    :param tempUnit: Input the temperature unit of the temperature as tempUnit | string
    :param convertTo: Input the temperature unit that user want to convert to as convertTo | string

    :return: run function : run function according to parameter | function() and output
    '''
    if (tempUnit == 'c' or tempUnit == 'k') and convertTo != 'f':
        celsiusKelvinConvert(temp)
    elif convertTo == 'f':
        toFahrenheit(temp)
    elif tempUnit == 'f' and (convertTo == 'c' or convertTo == 'k'):
        fromFahrenheit(temp, convertTo)
    else:
        print ('Error')

# melakukan proses input dari user yang juga disertai beberapa validasi
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
                print('\n')
                convert(temp, tempUnit, convertTo)
                print('\n')
                loop = False
                loop2 = False
            else:
                print(
                    'The Temperature unit you want to convert from and to cannot be the same [e.g., C cannot be converted to C]'
                )
                print('\n')
                loop2 = True
    else:
        print('The end of the input need to be either "k", "c", "f"!')
        print('\n')
        loop = True
