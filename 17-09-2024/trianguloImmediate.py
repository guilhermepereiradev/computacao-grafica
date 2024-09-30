import glfw
from OpenGL.GL import *
import numpy as np

offset_x = 0.0
offset_y = 0.0

def key_callback(window, key, scancode, action, mods):
    global offset_x, offset_y
    is_pressed = action == glfw.PRESS or action == glfw.REPEAT
    if key == glfw.KEY_LEFT and is_pressed:
        if offset_x > -0.7:
            offset_x -= 0.1
    if key == glfw.KEY_RIGHT and is_pressed:
        if offset_x < 0.7:
            offset_x += 0.1
    if key == glfw.KEY_UP and is_pressed:
        if offset_y < 0.7:
            offset_y += 0.1
    if key == glfw.KEY_DOWN and is_pressed:
        if offset_y > -0.7:
            offset_y -= 0.1

if not glfw.init():
    raise Exception("glfw não pôde ser inicializado")

window = glfw.create_window(800, 600, "uma janela para o seu bruxo", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw não pôde criar a janela")

glfw.make_context_current(window)

vertices = [-0.25, -0.25, 0.0,
            0.25, -0.25, 0.0,
            0.0, 0.25, 0.0]

colors = [1.0, 0.0, 0.0,
          1.0, 0.0, 0.0,
          0.0, 0.0, 1.0]
vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glfw.set_key_callback(window, key_callback)


glClearColor(0, 0.1, 0.1, 1)

while not glfw.window_should_close(window):
    glfw.poll_events()

    glClear(GL_COLOR_BUFFER_BIT)

    trans_vertices = vertices.copy()
    trans_vertices[::3] += offset_x
    trans_vertices[1::3] += offset_y

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, trans_vertices)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glDrawArrays(GL_TRIANGLES, 0, 3)

    glfw.swap_buffers(window)
glfw.terminate()