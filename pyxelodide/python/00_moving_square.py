from pyodide.webloop import WebLoop 
import pyxel
pyxel.init(120, 80)             

def frame(loop):
    if pyxel.btnp(pyxel.KEY_Q):
        return
    pyxel.cls(3)
    pyxel.rectb(pyxel.frame_count % 160 - 40, 20, 40, 40, 7)
    pyxel.flip()
    loop.call_soon(frame, loop)
loop = WebLoop()
loop.call_soon(frame, loop)