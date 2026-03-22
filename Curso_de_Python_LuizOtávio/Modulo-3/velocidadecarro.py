velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGER = 1

vel_carro_pass_ra = velocidade>RADAR_1
carro_passou_radar_1 =local_carro >= (LOCAL_1 - RADAR_RANGER) <= local_carro <= (LOCAL_1 + RADAR_RANGER)
carro_multador_radar_1 = carro_passou_radar_1 and vel_carro_pass_ra


if vel_carro_pass_ra:
    print('a velocidade do carro passou a do radar 1')

if carro_passou_radar_1:
    print('carro passou em radar 1')

if carro_multador_radar_1:
    print('carro multado em radar 1')