horasvendidas = 3000


horasconsumidas = 0

horasdisponiveismes = 800

mesatual = 6

horasdisponiveis = 4800  # horasdisponiveismes * mesatual

tabela = {}

while horasvendidas >= 0:
    horasdisponiveis -= horasvendidas
    horasconsumidas = horasdisponiveismes
    horasvendidas -= horasconsumidas
    
    if horasvendidas < 0:
        horasconsumidas += horasvendidas
        sobra = horasconsumidas
        horasvendidas = 0
        while horasdisponiveis > 0:
            print()
        print(horasconsumidas)
        break
    print(horasconsumidas)

print(horasvendidas)
