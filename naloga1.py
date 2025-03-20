import cv2 as cv
import numpy as np

def zmanjsaj_sliko(slika, sirina, visina):
<<<<<<< HEAD
    ''' sss'''
    pass
=======
    return cv.resize(slika, (sirina, visina))


>>>>>>> imageScale

def obdelaj_sliko_s_skatlami(slika, sirina_skatle, visina_skatle, barva_koze) -> list:
    '''Obdelamo sliko in preštejemo število pikslov kože v vsaki škatli.'''


def prestej_piksle_z_barvo_koze(slika, barva_koze) -> int:
    '''Prestej število pikslov z barvo kože v škatli.'''
    pass


def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Izračuna spodnje in zgornje meje barve kože na podlagi izbranega območja.'''


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