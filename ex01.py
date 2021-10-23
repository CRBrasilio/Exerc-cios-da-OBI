d = int(input('Digite a distância do arremesso em cm:'))
if(d<=800):
    print('1 ponto')
elif(d>800 and d<=1400):
    print('2 pontos')
elif(d>1400 and d<=2000):
    print('3 pontos')
else:
    print('-1')


