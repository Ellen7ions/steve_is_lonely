import win32gui
import threading

from env.Env import Env
from steve.Steve import Steve

if __name__ == '__main__':
    hwnd = win32gui.FindWindow('GLFW30', 'Minecraft* 1.17.1 - 单人游戏')
    steve = Steve('Miss U')
    env = Env(hwnd, steve)
    t_env = threading.Thread(target=env.run)
    t_env.start()

    t_steve = threading.Thread(target=steve.action, args=[env], daemon=True)
    t_steve.start()
