import threading

import cv2
import pyautogui as pat
import pydirectinput
import torch


class Steve:
    def __init__(self, name, brain):
        self.brain = brain
        self.name = name

        self.action_lock = threading.Lock()
        self.action_que = []

    def see(self, capture):
        capture = cv2.cvtColor(capture, cv2.COLOR_RGBA2RGB)
        resize_view = cv2.resize(capture, dsize=(224, 224))

        # self.action_que.append(
        #     {
        #         'action': pat.moveRel,
        #         'args': (2, 0)
        #     }
        # )
        if self.action_que.__len__() == 0:
            self.action_lock.acquire()
            input = torch.tensor(resize_view, dtype=torch.float32).view(1, 3, 224, 224)
            actions = self.brain.run_action(input)

            for k in actions:
                self.action_que.append(
                    {
                        'action': pydirectinput.keyDown,
                        'args': k
                    }
                )
                # self.action_que.append(
                #     {
                #         'action': pydirectinput.keyUp,
                #         'args': k
                #     }
                # )
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
