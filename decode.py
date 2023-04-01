from numpy import array
import base64

def bloq(OUTPUT, HEXA_BACK):
    
    def hunting(i_secondary):
        SUPER = 0;PRO = 1
        i_secondary = int(i_secondary)
        for i in range(len(str(i_secondary))-1,-1,-1):
            SUPER+=int(str(i_secondary)[i])*PRO
            PRO*=2
        return str(SUPER)
    
    F=0
    for i in range(0, len(OUTPUT), 7):
        HEXA_BACK[F]=OUTPUT[i:i+7]
        F+=1

    for i_primary, i_secondary in enumerate(HEXA_BACK):
        if i_primary < F:
            if'2' in i_secondary:
                SUPER = hunting(i_secondary.replace("2", "0"))+','
            else:
                SUPER = hunting(i_secondary)
        HEXA_BACK[i_primary]=SUPER
        


def bloq_bloq(lst):
    final = ''
    for i in lst:
        if not(str(i)[-1].isdigit()):
            final += chr(int(i[:len(i)-1])+63)
        else:
            final += chr(int(i))
    return base64.b64decode(final.encode('utf-8'))

def MASTER(PIXA):
    HEXA_BACK=array([str]*(len(PIXA)//7))                                     ###  LIST OF BINARY CODES 7 DIGISTS
    bloq(PIXA, HEXA_BACK)
    final = bloq_bloq(HEXA_BACK)

    return final.decode('utf-8')

