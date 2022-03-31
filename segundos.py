
segundos_str = input("Por favor, entre com o número de Segundos que deseja converter:")
total_segs = int(segundos_str)

dias = total_segs // 86400
horas = total_segs % 86400
horas_rest = horas // 3600
segs_rest = total_segs % 3600
minutos = segs_rest // 60
seg_rest_final = segs_rest % 60

print(dias, "dias,", horas_rest, "horas,", minutos, "minutos e", seg_rest_final, "segundos")