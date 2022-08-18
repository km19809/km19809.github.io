# [WIP] Pyxelodide
[pyxel](https://github.com/kitao/pyxel) on [pyodide](https://github.com/pyodide/pyodide)

It is malfunctioning a bit.
It uses [a fork of pyodide](https://github.com/km19809/pyodide)
This page is just for demonstration.

## Examples
The examples are modified to use the web loop.
 1. [Moving square](test_pyxel_fetch.html?py=00_moving_square)
 1. [Hello pyxel](test_pyxel_fs.html?py=01_hello_pyxel)
 1. [Jump game](test_pyxel_fs.html?py=02_jump_game)
 1. [Sound api](test_pyxel_fs.html?py=04_sound_api)
 1. [Color palette](test_pyxel_fs.html?py=05_draw_api)
 1. [Snake](test_pyxel_fs.html?py=07_snake)
 1. [Triangle api](test_pyxel_fetch.html?py=08_triangle_api)
 1. [Shooter](test_pyxel_fs.html?py=09_shooter)
 1. [Platformer](test_pyxel_fs.html?py=10_platformer)
 1. [Offscreen](test_pyxel_fs.html?py=11_offscreen)
 1. [Perlin noise](test_pyxel_fs.html?py=12_perlin_noise)

Broken:
 1. [Draw api](test_pyxel_fs.html?py=03_draw_api) : Position of cursor is not correct. It assumes the canvas is at the center.
 1. [Click game](test_pyxel_fs.html?py=06_click_game): same as above. Unable to play.
