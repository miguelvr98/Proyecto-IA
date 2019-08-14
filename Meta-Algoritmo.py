import pandas
import numpy

adults_train = pandas.read_csv('adult_train.csv', header=None,
                       names=['age', 'capital-gain', 'capital-loss', 'hours-per-week',
                              'workClass', 'education', 'marital-status','occupation',
                              'relationship','race','sex','native-country','inconme'])
<<<<<<< HEAD
                              
print(adults_train.shape)  # Número de filas y columnas
adults_train.head(10)
=======

print(adults_train.shape)  # El metodo shape muestra el numero de filas y columnas del .csv
>>>>>>> sergi
