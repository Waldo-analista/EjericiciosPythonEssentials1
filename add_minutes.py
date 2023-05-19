hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

minutos_totales=hour*60+mins+dura
horas=minutos_totales//60
minutos=minutos_totales%60
if horas>24:
    horas=horas%24

print(f'Las hora es: {horas}:{minutos}')

