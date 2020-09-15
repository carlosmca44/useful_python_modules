from math import fabs

def ammountComplete(n):
    if fabs(n) > 0.00009:
        return str(n)
    elif '.' in str(n):
        ent = str(n).split('.')
        ent2 = ent[1].split('e')
        part2 = str(ent[0]+ent2[0])
        ccero = ent[1].split('-')
        part1 = ''
        
        if int(ccero[1]) >= 10:
            part1 = str('0.'+'0'*(int(ccero[1])-1))
        else:
            x = []
            for i in ccero[1]:
                x.append(i)
            part1 = str('0.'+'0'*(int(ccero[1])-1))
    
        return part1+part2
    else:
        ent = str(n).split('e')
        part2 = ent[0]
        ccero = ent[1].replace('-','')
        part1 = ''

        if int(ccero) >= 10:
            part1 = str('0.'+'0'*(int(ccero)-1))
        else:
            x = []
            for i in ccero:
                x.append(i)
            part1 = str('0.'+'0'*(int(x[1])-1))

        return part1+part2 
