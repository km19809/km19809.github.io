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
        pyxel.init(64, 64, title="Perlin Noise", capture_scale=4)
        run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.frame_count == 300:
            pyxel.screencast()

    def draw(self):
        pyxel.cls(0)
        for y in range(64):
            for x in range(64):
                n = pyxel.noise(
                    x / 10,
                    y / 10,
                    pyxel.frame_count / 40,
                )
                if n > 0.4:
                    col = 7
                elif n > 0:
                    col = 6
                elif n > -0.4:
                    col = 12
                else:
                    col = 0
                pyxel.pset(x, y, col)


App()
