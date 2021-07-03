from board import P0_02, LED2_R, LED2_G, LED2_B
from simpleio import tone, DigitalOut
from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

R, G, B = DigitalOut(LED2_R), DigitalOut(LED2_G), DigitalOut(LED2_B)

ble = BLERadio()
ble.name = "RW&B"

advertisement = ProvideServicesAdvertisement(UARTService())

Note1 = 233
Note2 = 294
Note3 = 330
Note4 = 349
Note5 = 392
Note6 = 440
Note7 = 466
Note8 = 523
Note9 = 587
Note10 = 622
Note11 = 698

def TonePlus(N, T):
    global L, t
    R.value = not bool(2 - L % 3)
    G.value = bool(1 - L % 3)
    B.value = not bool(L % 3)
    tone(P0_02, N, t * T)
    L = L + 1

while True:
    ble.start_advertising(advertisement)
    R.value = G.value = B.value = 1
    while not ble.connected:
        pass
    while ble.connected:
        L = 2
        t = 0.5

        TonePlus(Note4, 0.75)
        TonePlus(Note2, 0.25)
        TonePlus(Note1, 1)
        TonePlus(Note2, 1)
        TonePlus(Note4, 1)
        TonePlus(Note7, 2)
        TonePlus(Note9, 0.75)
        TonePlus(Note8, 0.25)
        TonePlus(Note7, 1)
        TonePlus(Note2, 1)
        TonePlus(Note3, 1)
        TonePlus(Note4, 2)
        TonePlus(Note4, 0.5)
        TonePlus(Note4, 0.5)

        TonePlus(Note9, 1.5)
        TonePlus(Note8, 0.5)
        TonePlus(Note7, 1)
        TonePlus(Note6, 2)
        TonePlus(Note5, 0.5)
        TonePlus(Note6, 0.5)
        TonePlus(Note7, 1)
        TonePlus(Note7, 1)
        TonePlus(Note4, 1)
        TonePlus(Note2, 1)
        TonePlus(Note1, 1)
        TonePlus(Note4, 0.75)
        TonePlus(Note2, 0.25)

        TonePlus(Note1, 1)
        TonePlus(Note2, 1)
        TonePlus(Note4, 1)
        TonePlus(Note7, 2)
        TonePlus(Note9, 0.75)
        TonePlus(Note8, 0.25)
        TonePlus(Note7, 1)
        TonePlus(Note2, 1)
        TonePlus(Note3, 1)
        TonePlus(Note4, 2)
        TonePlus(Note4, 0.5)
        TonePlus(Note4, 0.5)

        TonePlus(Note9, 1.5)
        TonePlus(Note8, 0.5)
        TonePlus(Note7, 1)
        TonePlus(Note6, 2)
        TonePlus(Note5, 0.5)
        TonePlus(Note6, 0.5)
        TonePlus(Note7, 1)
        TonePlus(Note7, 1)
        TonePlus(Note4, 1)
        TonePlus(Note2, 1)
        TonePlus(Note1, 1)
        TonePlus(Note9, 0.5)
        TonePlus(Note9, 0.5)

        TonePlus(Note9, 1)
        TonePlus(Note10, 1)
        TonePlus(Note11, 1)
        TonePlus(Note11, 2)
        TonePlus(Note10, 0.5)
        TonePlus(Note9, 0.5)
        TonePlus(Note8, 1)
        TonePlus(Note9, 1)
        TonePlus(Note10, 1)
        TonePlus(Note10, 2)
        TonePlus(Note10, 1)

        TonePlus(Note9, 1)
        TonePlus(Note8, 0.5)
        TonePlus(Note7, 1)
        TonePlus(Note6, 2)
        TonePlus(Note5, 0.5)
        TonePlus(Note6, 0.5)
        TonePlus(Note7, 1)
        TonePlus(Note2, 1)
        TonePlus(Note3, 1)
        TonePlus(Note4, 2)
        TonePlus(Note4, 1)

        t = t * 1.08
        TonePlus(Note7, 1)
        TonePlus(Note7, 1)
        TonePlus(Note7, 0.5)
        TonePlus(Note6, 0.5)
        TonePlus(Note5, 1)
        TonePlus(Note5, 1)
        TonePlus(Note5, 1)
        TonePlus(Note8, 1)
        TonePlus(Note10, 0.5)
        TonePlus(Note9, 0.5)
        TonePlus(Note8, 0.5)
        TonePlus(Note7, 0.5)

        TonePlus(Note7, 1)
        TonePlus(Note6, 2)
        TonePlus(Note4, 0.5)
        TonePlus(Note4, 0.5)
        TonePlus(Note7, 1.5)
        TonePlus(Note8, 0.5)
        TonePlus(Note9, 0.5)
        TonePlus(Note10, 0.5)

        t = t * 1.2
        TonePlus(Note11, 2)
        TonePlus(Note7, 0.5)
        TonePlus(Note8, 0.5)
        TonePlus(Note9, 1.5)
        TonePlus(Note10, 0.5)
        TonePlus(Note8, 1)
        TonePlus(Note7, 2)
