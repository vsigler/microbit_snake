def novaHlava(staraHlava_x: number, staraHlava_y: number):
    return [protocSouradnice(staraHlava_x + smer_x),
        protocSouradnice(staraHlava_y + smer_y)]
def umistiJidlo():
    global jidlo
    jidlo = [randint(0, 4), randint(0, 4)]

def on_button_pressed_a():
    global otoc_se, otoc_doprava
    otoc_se = True
    otoc_doprava = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def vykresliHada():
    basic.clear_screen()
    for hodnota in had:
        led.plot(hodnota[0], hodnota[1])
    led.plot(jidlo[0], jidlo[1])

def on_button_pressed_b():
    global otoc_se, otoc_doprava
    otoc_se = True
    otoc_doprava = True
input.on_button_pressed(Button.B, on_button_pressed_b)

def posunHada():
    global hlava
    hlava = had[0]
    had.unshift(novaHlava(hlava[0], hlava[1]))
    hlava = had[0]
    if hlava[0] == jidlo[0] and hlava[1] == jidlo[1]:
        umistiJidlo()
    else:
        had.pop()
def protocSouradnice(k_protoceni: number):
    if k_protoceni > 4:
        return 0
    if k_protoceni < 0:
        return 4
    else:
        return k_protoceni
def otocSe(doPrava: bool):
    global vymena, smer_x, smer_y
    if doPrava:
        vymena = smer_x
        smer_x = smer_y * -1
        smer_y = vymena
    else:
        vymena = smer_x
        smer_x = smer_y
        smer_y = vymena * -1
vymena = 0
hlava: List[number] = []
otoc_doprava = False
otoc_se = False
jidlo: List[number] = []
smer_y = 0
smer_x = 0
had: List[List[number]] = []
had = [[1, 2], [0, 2]]
nazer_se = False
smer_x = 1
smer_y = 0
umistiJidlo()

def on_forever():
    global otoc_se
    if otoc_se:
        otocSe(otoc_doprava)
        otoc_se = False
    posunHada()
    vykresliHada()
    if True:
        pass
    basic.pause(1000)
basic.forever(on_forever)
