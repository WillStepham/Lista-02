def questao1():
    return 5**2,9*5,15/12,12/15,15//12,12//15,5%2,9%5,15%12,12%15,6%6,0%7

def questao2():
    return '5 da tarde'

def questao3():
    a=int(input('Digite a hora atual: '))
    b=int(input('Digite daqui a quantas horas o alarme deverá tocar: '))
    desp=(a+b)%24
    if desp>24:
        desp=desp%24
    return print('O alarme tocará às {}h'.format(desp))

def questao4():
    a=int(input('Digite o dia inicial: '))
    b=input('Digite o dia da semana: ')
    c=int(input('Digite quantos dias ficará de férias: '))
    dias = ('Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo')
    ds=dias.index(b)
    #dr=(a+c)%30
    dsr=c%7
    dsf=ds+dsr
    while dsf>=7:
        dsf=dsf%7
    return print('o retorno das férias será:',dias[dsf])

def questao5():
    a='Só'
    b='trabalho'
    c='sem'
    d='diversão'
    e='faz'
    f='de'
    g='João'
    h='em'
    i='chato'
    return print(a,b,c,d,f,g,h,i)

def questao6():
    x=6 * (1 - 2)
    return print('6*(1-2) =',x)

def questao7():
    t=float(input('Digite a quantidade de anos: '))
    A=10000*((1+(0.08/12))**(12*t))
    return print('O valor final é: {:.2f}'.format(A))

def questao8():
    r=float(input('Digite o raio do círculo: '))
    a=3.14*(r**2)
    return print('A área do círculo de raio',r,'é:',a)

def questao9():
    a=float(input('Digite altura do retângulo: '))
    b=float(input('Digite largura do retângulo: '))
    return print('A área do retangulo é:',a*b)
    
def questao10():
    km=float(input('Digite a quilometragem percorrida: '))
    l=float(input('Digite a quantidade de litros consumido: '))
    c=km/l
    return print('O consumo de gasolina é de: {:.2f}Km/l'.format(c))

def questao11():
    c=float(input('Digite a temperatura em ºC: '))
    f=(1.8*c)+32
    return print('{}ºC em Fahrenheit é: {:.2f}ºF'.format(c,f))

def questao12():
    f=float(input('Digite a temperatura em ºF: '))
    c=(f-32)/1.8
    return print('{}ºF em Celsius é: {:.2f}ºC'.format(f,c))
