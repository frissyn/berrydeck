function love.load(args)
    Slab.SetINIStatePath("src/_save/window.ini")
    Slab.Initialize(args)
    Slab.DisableDocks({"Left", "Right", "Bottom"})

    local style = Slab.GetStyle()
    style.API.LoadStyle("src/_assets/themes/dark.style")
    style.API.LoadStyle("src/_assets/themes/light.style", true)
    Slab.PushFont(love.graphics.newFont("_assets/fonts/renogare.otf", 16))

    -- love.window.setMode(800, 600, {centered = true})
    Slab.SetScrollSpeed(50)

    LastDump = 2600.0
    collectgarbage()
end