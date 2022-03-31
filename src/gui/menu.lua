local menu = { items = {"file", "edit", "window", "help"} }


-- ~~~ FILE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
menu.file = function ()
    if Slab.BeginMenu("File") then
        if Slab.BeginMenu("New") then
            if Slab.MenuItem("Savefile") then
                -- TODO: Create a new save file
                print("click: file/new/save-file")
            end

            if Slab.MenuItem("From Preset") then
                -- TODO: Create file from preset
                print("click: file/new/from-preset")
            end

            Slab.EndMenu()
        end

        if Slab.MenuItem("Open") then
            GUI.state.fileDialog.popOpen = true
            GUI.state.fileDialog.opts = {
                Type = "openfile",
                AllowMultiSelect = false
            }

            GUI.state.fileDialog.callback = function (res)
                local file = res.Files[1]

                if file ~= nil then
                    print(file)

                    local save = Parser.savefile.new(file)

                    if save ~= nil then
                        GUI.state.scene = "editor"
                        GUI.state.isEditing = true
                        GUI.state.editor.opened = true

                        GUI.state.save = save
                    end
                end
            end
        end

        if Slab.MenuItem("Save", {Enabled = GUI.state.isEditing}) then
            -- TODO: Save open savefile to existing savefile
            print("click: file/save")
        end

        if Slab.MenuItem("Save As", {Enabled = GUI.state.isEditing}) then
            -- TODO: Save open savefile to new savefile
            print("click: file/save-as")
        end

        Slab.Separator()

        if Slab.MenuItem("Quit") then
            love.event.quit()
        end

        Slab.EndMenu()
    end
end


-- ~~~ EDIT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
menu.edit = function ()
    if Slab.BeginMenu("Edit") then
        if Slab.MenuItem("Undo", {Enabled = GUI.state.editor.undoable}) then
            -- TODO: undo last change to savefile
            print("click: edit/undo")
        end

        if Slab.MenuItem("Redo", {Enabled = GUI.state.editor.redoable}) then
            -- TODO: redo last change to savefile
            print("click: edit/redo")
        end

        Slab.Separator()

        if Slab.BeginMenu("Mode") then
            if Slab.MenuItem("Interactive", {Enabled = GUI.state.modeNotEnabled("editor")}) then
                GUI.state.scene = "editor"
            end

            if Slab.MenuItem("Raw", {Enabled = GUI.state.modeNotEnabled("raw")}) then
                GUI.state.scene = "raw"
            end

            Slab.EndMenu()
        end

        if Slab.MenuItem("Validate File", {Enabled = GUI.state.isEditing}) then
            -- TODO: check validity of savefile values
            print("click: edit/valid")
        end

        Slab.EndMenu()
    end
end


-- ~~~ WINDOW ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
menu.window = function ()
    if Slab.BeginMenu("Window") then
        if Slab.BeginMenu("Theme") then
            local style = Slab.GetStyle()

            if Slab.MenuItem("Light") then
                style.API.SetStyle("light")
            end

            if Slab.MenuItem("Dark") then
                style.API.SetStyle("dark")
            end

            Slab.EndMenu()
        end

        if Slab.MenuItem("Resize") then
            GUI.state.message.popOpen = true
            GUI.state.message.title = "Information!"
            GUI.state.message.data = "This functionality is currently unavailable."
        end

        Slab.EndMenu()
    end
end


-- ~~~ HELP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
menu.help = function ()
    if Slab.BeginMenu("Help") then
        if Slab.MenuItem("Open Wiki") then
            love.system.openURL("https://github.com/frissyn/berrydeck/wiki")
        end

        if Slab.MenuItem("Check for Updates") then
            -- TODO: Check for updates. from GitHub releases?
            print("click: help/updates")
        end

        Slab.EndMenu()
    end
end


return menu