function love.update(dt)
    Slab.Update(dt)

    Slab.BeginWindow('main', GUI.window)
    GUI.scenes[GUI.state.scene]()

    if Slab.BeginMainMenuBar() then
        for _, item in ipairs(GUI.menu.items) do
            if GUI.menu[item]() then
                Slab.EndMenu()
            end
        end

        Slab.EndMainMenuBar()
    end

    if GUI.state.message.popOpen == true then
        local response = Slab.MessageBox(
            GUI.state.message.title, GUI.state.message.data
        )

        if response ~= "" then
            GUI.state.message.popOpen = false
        end
    end

    if GUI.state.fileDialog.popOpen == true then
        local file = Slab.FileDialog(GUI.state.fileDialog.opts)

        if file.Button ~= "" then
            GUI.state.fileDialog.callback(file)

            GUI.state.fileDialog = {
                popOpen = false,
                opts = {
                    Type = "openfile",
                    AllowMultiSelect = false
                },
                callback = function (res)
                    return res
                end
            }
        end
    end

    Slab.EndWindow()

    local trash = collectgarbage("count")

    if (trash * 2.0) >= LastDump then
        LastDump = trash
        collectgarbage()
    end
end