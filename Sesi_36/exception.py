# # exception 
# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# #custom exception
# x = 10
# if x > 5:
#     raise Exception('your custom exception')


# import sys
# # assert ('linux' in sys.platform), "This code runs on Linux only."
# # assert ('windows' in sys.platform), "This code runs on Windows only."

# def os_interaction():
#     # assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win32' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except:
#     print('Windows function was not executed')

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

try:    
    with open('sample.txt') as file:        
        read_data = file.read()
        print('test')
except FileNotFoundError as error:    
    print(error)
    print('test2')
else:
    print('Executing the else clause.')
