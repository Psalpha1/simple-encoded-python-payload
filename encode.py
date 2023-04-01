import base64

rest = []

def step_1(txt):
    for i in range(len(txt)):
        if ((ord(txt[i])+64) > 128) :
            rest.append(str(abs(ord(txt[i])-63))+ ',') 
        else:
            rest.append(str(ord(txt[i])))

def convertir(n):
    ch = ''
    while n != 0:
        r = n % 2
        n = n //2
        ch = str(r) + ch
    return ch

def step_2(lst):
    length = len(lst)

    for index in range(length):
        if lst[index].isdecimal():
            lst[index] = convertir(int(lst[index]))
        else:
            lst[index] = '2'+convertir(int(lst[index][:len(lst[index])-1]))

    for index, value in enumerate(lst):
        lst[index] = ('0'*7)[:7-len(value)]+value

def step_3(lst):
    string = ''
    for i in lst:
        string += i
    return string

def MASTER(string):
    txt = base64.b64encode(string.encode('utf-8')).decode('utf-8')
    step_1(txt)
    step_2(rest)
    return step_3(rest)


### You can just remove it and replace it with print(MASTER('Your payload here'))

with open('payload.txt', 'r') as file:
    text = file.read()
    file.close()

with open('encoded_payload.txt', 'w') as file:
    file.write(MASTER(text))
    file.close()