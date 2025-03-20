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
            stevilo_pikslov = prestej_piksle_z_barvo_koze(skatl, barva_koze, sirina_skatle, visina_skatle)
            vrstica.append(stevilo_pikslov)
        seznam_skatel.append(vrstica)
    return seznam_skatel


def doloci_barvo_koze(slika, levo_zgoraj, desno_spodaj) -> tuple:
    '''Izračuna spodnje in zgornje meje barve kože na podlagi izbranega območja.'''
    koza_obmocje = slika[levo_zgoraj[1]:desno_spodaj[1], levo_zgoraj[0]:desno_spodaj[0]]

    # Define skin color range for white skin in BGR (approximate values for light skin)
    spodnja_meja = np.array([0, 0, 180])  # Lower bound for white skin
    zgornja_meja = np.array([255, 255, 255])  # Upper bound for white skin

    return spodnja_meja, zgornja_meja


def prestej_piksle_z_barvo_koze(slika, barva_koze, sirina_skatle, visina_skatle) -> int:
    '''Prešteje število pikslov z barvo kože v podsliki.'''
    spodnja_meja, zgornja_meja = barva_koze
    maska = cv.inRange(slika, spodnja_meja, zgornja_meja)  # Create the mask for white skin
    stevilo_pikslov = np.sum(maska == 255)

    # Calculate percentage of pixels that match the skin color
    total_pixels = sirina_skatle * visina_skatle
    matching_percentage = (stevilo_pikslov / total_pixels) * 100

    # Return the number of pixels if more than 30% of the square is matching skin color
    if matching_percentage >= 30:
        return stevilo_pikslov
    else:
        return 0  # No matching pixels if less than 30%


def main():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Napaka pri odpiranju kamere!")
        return

    # Set camera resolution to 800x450
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 450)

    # Explicitly resize the OpenCV window
    cv.namedWindow('Detekcija obraza', cv.WINDOW_NORMAL)
    cv.resizeWindow('Detekcija obraza', 800, 450)

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
                if seznam_skatel[y][x] > 0:  # If more than 30% of the square matches the skin color
                    cv.rectangle(slika, (x * 30, y * 30), ((x + 1) * 30, (y + 1) * 30), (0, 255, 0), 2)

        cv.imshow('Detekcija obraza', slika)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
