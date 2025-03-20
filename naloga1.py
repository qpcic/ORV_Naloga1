import cv2 as cv
import numpy as np

def zmanjsaj_sliko(slika, sirina, visina):
    pass
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


def prestej_piksle_z_barvo_koze(slika, barva_koze) -> int:
    '''Prestej število pikslov z barvo kože v škatli.'''
    pass


def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Izračuna spodnje in zgornje meje barve kože na podlagi izbranega območja.'''


def prestej_piksle_z_barvo_koze(slika, barva_koze) -> int:
    '''Prešteje število pikslov z barvo kože v podsliki.'''
    spodnja_meja, zgornja_meja = barva_koze

    # Ustvarimo masko za barvo kože
    maska = cv.inRange(slika, spodnja_meja, zgornja_meja)

    # Preštejemo število pikslov, ki ustrezajo maski
    stevilo_pikslov = np.sum(maska == 255)
    return stevilo_pikslov


def main():
    pass


if __name__ == '__main__':
    main()

if __name__ == '__main__':
    #Pripravi kamero

    #Zajami prvo sliko iz kamere

    #Izračunamo barvo kože na prvi sliki

    #Zajemaj slike iz kamere in jih obdeluj     
    
    #Označi območja (škatle), kjer se nahaja obraz (kako je prepuščeno vaši domišljiji)
        #Vprašanje 1: Kako iz števila pikslov iz vsake škatle določiti celotno območje obraza (Floodfill)?
        #Vprašanje 2: Kako prešteti število ljudi?

        #Kako velikost prebirne škatle vpliva na hitrost algoritma in točnost detekcije? Poigrajte se s parametroma velikost_skatle
        #in ne pozabite, da ni nujno da je škatla kvadratna.
    pass