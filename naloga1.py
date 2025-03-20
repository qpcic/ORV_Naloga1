import cv2 as cv
import numpy as np

def zmanjsaj_sliko(slika, sirina, visina):

    return cv.resize(slika, (sirina, visina))

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list:
    # Seznam za shranjevanje rezultatov
    seznam_skatel = []

    # Velikost slike
    visina, sirina, _ = slika.shape

    # Gremo čez celotno sliko z okenskimi škatlami
    for y in range(0, visina - visina_skatle, visina_skatle):
        vrstica = []
        for x in range(0, sirina - sirina_skatle, sirina_skatle):
            # Izrežemo škatlo iz slike
            skatl = slika[y:y + visina_skatle, x:x + sirina_skatle]

            # Preštejemo število pikslov kože v škatli
            stevilo_pikslov = prestej_piksle_z_barvo_koze(skatl, barva_koze)

            # Dodamo rezultat v seznam
            vrstica.append(stevilo_pikslov)

        seznam_skatel.append(vrstica)

    return seznam_skatel

def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Izračuna spodnje in zgornje meje barve kože na podlagi izbranega območja.'''

    # Izrežemo območje iz slike
    koza_obmocje = slika[levo_zgoraj[1]:desno_spodaj[1], levo_zgoraj[0]:desno_spodaj[0]]

    # Pretvorimo v HSV prostor
    hsv = cv.cvtColor(koza_obmocje, cv.COLOR_BGR2HSV)

    # Prilagodite te vrednosti na podlagi vaše slike
    # Spodnja in zgornja meja za barvo kože v HSV prostoru
    spodnja_meja = np.array([0, 20, 70])  # Prilagodite te vrednosti
    zgornja_meja = np.array([20, 150, 255])  # Prilagodite te vrednosti

    return spodnja_meja, zgornja_meja


def prestej_piksle_z_barvo_koze(slika, barva_koze) -> int:
    '''Prešteje število pikslov z barvo kože v podsliki.'''
    spodnja_meja, zgornja_meja = barva_koze

    # Ustvarimo masko za barvo kože
    maska = cv.inRange(slika, spodnja_meja, zgornja_meja)

    # Preštejemo število pikslov, ki ustrezajo maski
    stevilo_pikslov = np.sum(maska == 255)
    return stevilo_pikslov


def main():
    # Inicializacija kamere
    cap = cv.VideoCapture(0)  # Poveži kamero
    if not cap.isOpened():
        print("Napaka pri odpiranju kamere!")
        return

    while True:
        # Zajem slike
        ret, frame = cap.read()
        if not ret:
            break

        # Pomanjšaj sliko na 260x300 px
        slika = zmanjsaj_sliko(frame, 260, 300)

        # Izračunamo barvo kože iz prve slike (levo zgoraj in desno spodaj določita območje)
        if 'barva_koze' not in locals():
            barva_koze = doloci_barvo_koze(slika, (50, 50), (150, 150))  # Izberite ustrezno območje

        # Obdelaj sliko s škatlami
        seznam_skatel = obdelaj_sliko_s_skatlami(slika, 30, 30, barva_koze)

        # Izriši škatle (ali označite območja)
        for y in range(len(seznam_skatel)):
            for x in range(len(seznam_skatel[y])):
                if seznam_skatel[y][x] > 0:  # Če je v škatli več kot 0 pikslov kože
                    cv.rectangle(slika, (x * 30, y * 30), ((x + 1) * 30, (y + 1) * 30), (0, 255, 0), 2)

        # Prikaz slike
        cv.imshow('Detekcija obraza', slika)

        # Čakanje na pritisnjen 'q' za izhod
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
