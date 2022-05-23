# def decorador(func):

#   def decorar():
#     print('Inicia la ejecucion de la funcion: ', func.__name__)
#     func()
#     print('Termina la ejecucion de la funcion: ', func.__name__)

#   return decorar

def decorador(func):

  def decorar(*args):
    print('Inicia la ejecucion de la funcion: ', func.__name__)
    func(*args)
    print('Termina la ejecucion de la funcion: ', func.__name__)

  return decorar

@decorador
def hola(nombre):
  print('Hola Mundo', nombre)

@decorador
def sumar (a, b):
  suma = a + b
  print('La suma es:', suma)

hola('Alex')

sumar(10, 20)