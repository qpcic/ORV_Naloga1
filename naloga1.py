import cv2 as cv
import numpy as np

def zmanjsaj_sliko(slika, sirina, visina):
    '''Zmanjša sliko na želene dimenzije.'''
    return cv.resize(slika, (sirina, visina))

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list:
    '''Sprehodi skozi sliko in preštej število pikslov kože v vsaki škatli.'''
    seznam_skatel = []
    visina, sirina, _ = slika.shape
    for y in range(0, visina - visina_skatle, visina_skatle):
        vrstica = []
        for x in range(0, sirina - sirina_skatle, sirina_skatle):
            skatl = slika[y:y + visina_skatle, x:x + sirina_skatle]
            stevilo_pikslov = prestej_piksle_z_barvo_koze(skatl, barva_koze)
            vrstica.append(stevilo_pikslov)
        seznam_skatel.append(vrstica)
    return seznam_skatel

def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Izračuna spodnje in zgornje meje barve kože na podlagi izbranega območja.'''
    koza_obmocje = slika[levo_zgoraj[1]:desno_spodaj[1], levo_zgoraj[0]:desno_spodaj[0]]
    hsv = cv.cvtColor(koza_obmocje, cv.COLOR_BGR2HSV)
    spodnja_meja = np.array([0, 20, 70])  # Prilagodite te vrednosti
    zgornja_meja = np.array([20, 150, 255])  # Prilagodite te vrednosti
    return spodnja_meja, zgornja_meja

def prestej_piksle_z_barvo_koze(slika, barva_koze) -> int:
    '''Prešteje število pikslov z barvo kože v podsliki.'''
    spodnja_meja, zgornja_meja = barva_koze
    maska = cv.inRange(slika, spodnja_meja, zgornja_meja)
    stevilo_pikslov = np.sum(maska == 255)
    return stevilo_pikslov

def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Napaka pri odpiranju kamere!")
        return

    barva_koze = None  # Initialize barva_koze as None

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        slika = zmanjsaj_sliko(frame, 260, 300)

        # Calculate the skin color if not already done
        if barva_koze is None:
            barva_koze = doloci_barvo_koze(slika, (50, 50), (150, 150))

        seznam_skatel = obdelaj_sliko_s_skatlami(slika, 30, 30, barva_koze)

        for y in range(len(seznam_skatel)):
            for x in range(len(seznam_skatel[y])):
                if seznam_skatel[y][x] > 0:
                    cv.rectangle(slika, (x * 30, y * 30), ((x + 1) * 30, (y + 1) * 30), (0, 255, 0), 2)

        cv.imshow('Detekcija obraza', slika)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
