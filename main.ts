function novaHlava (staraHlava_x: number, staraHlava_y: number) {
    return [protocSouradnice(staraHlava_x + smer_x), protocSouradnice(staraHlava_y + smer_y)]
}
function umistiJidlo () {
    jidlo = [randint(0, 4), randint(0, 4)]
}
input.onButtonPressed(Button.A, function () {
    otoc_se = true
    otoc_doprava = false
})
function vykresliHada () {
    basic.clearScreen()
    for (let hodnota of had) {
        led.plot(hodnota[0], hodnota[1])
    }
    led.plot(jidlo[0], jidlo[1])
}
input.onButtonPressed(Button.B, function () {
    otoc_se = true
    otoc_doprava = true
})
function posunHada () {
    hlava = had[0]
    had.unshift(novaHlava(hlava[0], hlava[1]))
    hlava = had[0]
    if (hlava[0] == jidlo[0] && hlava[1] == jidlo[1]) {
        umistiJidlo()
    } else {
        had.pop()
    }
}
function protocSouradnice (k_protoceni: number) {
    if (k_protoceni > 4) {
        return 0
    }
    if (k_protoceni < 0) {
        return 4
    } else {
        return k_protoceni
    }
}
function otocSe (doPrava: boolean) {
    if (doPrava) {
        vymena = smer_x
        smer_x = smer_y * -1
        smer_y = vymena
    } else {
        vymena = smer_x
        smer_x = smer_y
        smer_y = vymena * -1
    }
}
let vymena = 0
let hlava: number[] = []
let otoc_doprava = false
let otoc_se = false
let jidlo: number[] = []
let smer_y = 0
let smer_x = 0
let had: number[][] = []
let nazer_se = false
had = [[1, 2], [0, 2]]
smer_x = 1
smer_y = 0
umistiJidlo()
basic.forever(function () {
    if (otoc_se) {
        otocSe(otoc_doprava)
        otoc_se = false
    }
    posunHada()
    vykresliHada()
    basic.pause(750)
})
