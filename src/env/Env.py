import sys
import threading
import time
import numpy as np
import cv2
import win32gui

from PyQt5.QtWidgets import QApplication


class Env:
    def __init__(self, hwnd, person):
        self.person = person

        self.hwnd = hwnd

        self.env_running_lock = threading.Lock()
        self.env_running = False

    @staticmethod
    def countdown(k):
        for i in range(k, 0, -1):
            print(i)
            time.sleep(1)

    def run(self):
        Env.countdown(4)
        self.env_running_lock.acquire()
        self.env_running = True
        self.env_running_lock.release()

        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()

        while True:
            img = screen.grabWindow(self.hwnd).toImage()
            size = img.size()
            s = img.bits().asstring(size.width() * size.height() * img.depth() // 8)

            env_capture = np.frombuffer(s, dtype=np.uint8).reshape((size.height(), size.width(), img.depth() // 8))

            env_capture = self.person.see(env_capture)
            cv2.imshow(self.person.name, env_capture)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                self.env_running_lock.acquire()
                self.env_running = False
                self.env_running_lock.release()
                break


if __name__ == '__main__':
    pass
