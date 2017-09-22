import numpy as np
import matplotlib.pyplot as plt

def add_participantes(year, inicial, avanzado, escuelas):
  participantes[year] = {'inicial': inicial,
                         'avanzado':avanzado,
                         'total': inicial+avanzado,
                         'escuelas': escuelas
  }

participantes = {}
#add_participantes(2017, 80, 50, 22)
add_participantes(2016, 90, 40, 18)
add_participantes(2015, 108, 38, 25)
add_participantes(2014, 60, 20, 19)
add_participantes(2013, 48, 20, 15)
add_participantes(2012, 50, 30, 15)
add_participantes(2011, 45, 25, 14)
add_participantes(2010, 48, 32, 15)
add_participantes(2009, 39, 21, 12)
add_participantes(2008, 39, 26, 11)
add_participantes(2007, 35, 21, 12)

years = []
inicial_per_year = []
avanzado_per_year = []
total_per_year = []
escuelas_per_year = []
for i in range(min(y for y in participantes.keys()), max(y for y in participantes.keys())+1):
  years.append(i)
  inicial_per_year.append(participantes[i]['inicial'])
  avanzado_per_year.append(participantes[i]['avanzado'])
  total_per_year.append(participantes[i]['total'])
  escuelas_per_year.append(participantes[i]['escuelas'])

plt.figure()
plt.plot(years, total_per_year, '*-b', label='Total de participantes')
plt.plot(years, inicial_per_year, '*r', label='Participantes de nivel inicial')
plt.plot(years, avanzado_per_year, '*g', label='Participantes de nivel avanzado')
plt.ylim([0,150])
plt.title('Participantes por año')
plt.legend()
plt.grid()
plt.savefig('participantes_per_year.eps')
#plt.show()


plt.figure()
plt.plot(years, escuelas_per_year, '*-r', label='Escuelas participantes')
plt.ylim([0,30])
plt.title('Escuelas participantes por año')
plt.legend()
plt.grid()
plt.savefig('escuelas_per_year.eps')
#plt.show()
