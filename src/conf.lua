function love.conf(t)
    t.console = false

    t.window.title = "BerryDeck"
    t.window.icon = "_assets/icon.png"
    t.window.width = 800
    t.window.height = 600
    t.window.borderless = false
    t.window.resizable = false

    t.modules.audio = false
    t.modules.data = true
    t.modules.event = true
    t.modules.font = true
    t.modules.graphics = true
    t.modules.image = true
    t.modules.joystick = false
    t.modules.keyboard = true
    t.modules.math = true
    t.modules.mouse = true
    t.modules.physics = false
    t.modules.sound = false
    t.modules.system = true
    t.modules.thread = true
    t.modules.timer = true
    t.modules.touch = false
    t.modules.video = false
    t.modules.window = true
end