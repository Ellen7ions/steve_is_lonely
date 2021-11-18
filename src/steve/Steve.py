import threading

import cv2
import pyautogui as pat
import pydirectinput


class Steve:
    def __init__(self, name):
        self.name = name

        self.action_lock = threading.Lock()
        self.action_que = []

    def see(self, capture):
        capture = cv2.Canny(capture, 200, 255)
        if self.action_que.__len__() == 0:
            self.action_lock.acquire()
            self.action_que.append(
                {
                    'action': pat.moveRel,
                    'args': (2, 0)
                }
            )
            self.action_que.append(
                {
                    'action': pydirectinput.keyDown,
                    'args': 'w'
                }
            )
            self.action_lock.release()
        return capture

    def action(self, env):
        while True:
            if env.env_running:
                if self.action_que:
                    self.action_lock.acquire()
                    for item in self.action_que:
                        args = item['args']
                        item['action'](*args)
                    self.action_que = []
                    self.action_lock.release()


if __name__ == '__main__':
    pass
