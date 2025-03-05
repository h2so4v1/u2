import mss
import numpy as np
import cv2
import pygetwindow as gw
from PIL import ImageGrab

def get_window_rect(window_title):
    """
    Belirtilen başlığa sahip pencerenin koordinatlarını döndürür.
    """
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        raise Exception(f"Pencere bulunamadı: {window_title}")
    window = windows[0]
    return window.left, window.top, window.right, window.bottom

def capture_window(window_title):
    """
    Belirtilen başlığa sahip pencerenin ekran görüntüsünü alır.
    """
    left, top, right, bottom = get_window_rect(window_title)
    # Pencerenin ekran görüntüsünü al
    ekran_goruntusu = ImageGrab.grab(bbox=(left, top, right, bottom))
    
    # Pillow görüntüsünü numpy array'e çevir
    ekran_goruntusu_np = np.array(ekran_goruntusu)
    
    # RGB'den BGR'ye çevir (OpenCV'nin kullandığı format)
    ekran_goruntusu_bgr = cv2.cvtColor(ekran_goruntusu_np, cv2.COLOR_RGB2BGR)
    
    return ekran_goruntusu_bgr

# Test kodu (devre dışı bırakıldı)
if __name__ == "__main__":
    """
    window_title = "Uygulama Başlığı"  # Buraya ekran görüntüsünü almak istediğiniz uygulamanın başlığını yazın
    try:
        goruntu = capture_window(window_title)
        cv2.imshow("Pencere Goruntusu", goruntu)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)
    """