import glfw

if not glfw.init():
    raise Exception("glfw can not be initialized")
window = glfw.create_window(1200, 800, "Uma janela para o seu bruxo", None, None)

if not window:
    glfw.terminate()
    raise Exception("glfw can not be created")

glfw.set_window_pos(window, 400, 100)
glfw.make_context_current(window)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glfw.swap_buffers(window)
glfw.terminate()