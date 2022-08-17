from pyodide.webloop import WebLoop 
import pyxel

def run(update, draw):
    def frame(loop):
        update()
        draw()
        pyxel.flip()
        loop.call_soon(frame, loop)
    loop = WebLoop()
    loop.call_soon(frame, loop)

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Hello Pyxel")
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


App()