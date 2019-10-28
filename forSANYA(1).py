import textwrap
alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = "влцдутжбюцхъяррмшбрхцэооэцгбрьцмйфктъъюьмшэсяцпунуящэйтаьэдкцибрьцгбрпачкъуцпъбьсэгкцъгуущарцёэвърюуоюэкааэбрняфукабъарпяъафкъиьжяффнйояфывбнэнфуюгбрьсшьжэтбэёчюъюръегофкбьчябашвёэуъъюаднчжчужцёэвлрнчулбюпцуруньъшсэюъзкцхъяррнрювяспэмасчкпэужьжыатуфуярюравртубурьпэщлафоуфбюацмнубсюкйтаьэдйюнооэгюожбгкбрънцэпотчмёодзцвбцшщвщепчдчдръюьскасэгъппэгюкдойрсрэвоопчщшоказръббнэугнялёкьсрбёуыэбдэулбюасшоуэтъшкрсдугэфлбубуъчнчтртпэгюкиугюэмэгюккъъпэгяапуфуэзьрадзьжчюрмфцхраююанчёчюъыхьъцомэфъцпоирькнщпэтэузуябащущбаыэйчдфрпэцъьрьцъцпоилуфэдцойэдятррачкубуфнйтаьэдкцкрннцюабугюуубурьпйюэъжтгюркующоъуфъэгясуоичщщчдцсфырэдщэъуяфшёчцюйрщвяхвмкршрпгюопэуцчйтаьэдкцибрьцыяжтюрбуэтэбдуящэубъибрювъежагибрбагбрымпуноцшяжцечкфодщоъчжшйуъцхчщвуэбдлдъэгясуахзцэбдэулькнъщбжяцэьрёдъьвювлрнуяфуоухфекьгцчччгэъжтанопчынажпачкъуъмэнкйрэфщэъьбудэндадъярьеюэлэтчоубъцэфэвлнёэгфдсэвэёкбсчоукгаутэыпуббцчкпэгючсаъбэнэфъркацхёваетуфяепьрювържадфёжбьфутощоявьъгупчршуитеачйчирамчюфчоуяюонкяжыкгсцбрясшчйотъъжрсщчл"
text = text.lower()
key_length = 5
new_text = textwrap.wrap(text, key_length)
s = []
d = {}
d_sort = {}
for i in range(0, key_length):
    s.append('')
for i in range(0, key_length):
    d.update({i:{}})
    d_sort.update({i:{}})
for block in new_text:
    i = 0
    for letter in block:
        i = (i + 1) % len(block)
        s[i] += block[i]
for i in range(0, key_length):
    count = {}
    for char in s[i]:
        if count.get(char,False):
            count[char] += 1
        else:
            count.update({char:1})
    d[i].update(count)
for i in range(0, key_length):
    for letter in alph:
        if d[i].get(letter,False):
            d_sort[i].update({letter:d[i][letter]})
        else:
            d_sort[i].update({letter:0})


index_sum = [1]
sdvig = [1]
for i in range(1, key_length):
    index_sum.append([])
    sdvig.append([])
for z in range (0, len(alph)):
    for i in range(1, key_length):
        sum = 0
        index = 0
        for y in range (0, len(alph)):
            sum += (d_sort[0][alph[y]] * d_sort[i][alph[(y+z) % len(alph)]])
        index = (sum / (len(s[0]) * len(s[i])))
        if (index > 0.053 and index < 0.07):
            index_sum[i].append(index)
            sdvig[i].append(abs(z-len(alph)))
print(index_sum)
print(sdvig)
for i in range(0, len(alph)):
       print (alph[i],alph[i-sdvig[1][0]],alph[i-sdvig[2][0]],alph[i-sdvig[3][0]],alph[i-sdvig[4][0]])
        








# РАСШИФРОВКА'
key = 'слово'
def decrypt(text, key):
    message = []
    ki = 0

    for letter in text:
        if(letter in alph):
            temp = alph.find(letter)
            temp = temp - alph.find(key[ki])
            temp = temp % len(alph)
            message.append(alph[temp])
            ki += 1
        else:
            message.append(letter)
            ki = ki + 1
        if ki == len(key):
            ki = 0

    return message

answer = decrypt(text,key)
str_answer =''
for i in range (0,len(answer)):
    str_answer += answer[i]

