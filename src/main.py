import win32gui
import threading

from env.Env import Env
from steve.Steve import Steve
from steve.nn_brain import NNBrain

if __name__ == '__main__':
    hwnd = win32gui.FindWindow('GLFW30', 'Minecraft* 1.17.1 - 单人游戏')

    brain = NNBrain()
    steve = Steve('Miss U', brain)
    env = Env(hwnd, steve)
    t_env = threading.Thread(target=env.run)
    t_env.start()

    t_steve = threading.Thread(target=steve.action, args=[env], daemon=True)
    t_steve.start()
