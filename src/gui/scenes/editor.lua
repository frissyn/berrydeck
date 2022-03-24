return function ()
    local save = GUI.state.save

    Slab.SetCursorPos(nil, GUI.window.Y + 48)

    Slab.Indent()
    Slab.Text("Name:")
    Slab.SameLine()
    if Slab.Input("NameInput", {Text = save.data.Name, ReturnOnText = false}) then
        save.data.Name = Slab.GetInputText()
    end

    Slab.SameLine({Pad = 16})
    Slab.Text("Version:")
    Slab.SameLine()
    Slab.Input("VersionInput", {Text = save.data.Version, ReadOnly = true})

    Utils.paddedSeparator({Unindent = true})

    Slab.Indent()
    Slab.Text("Game Modes: ")
    for i, name in ipairs(GUI.store.modes) do
        Slab.SameLine({Pad = 16})

        if Slab.CheckBox(save.data[name] == "true", name) then
            save.data[name] = tostring(not Utils.boolf(save.data[name]))
        end
    end

    Utils.paddedSeparator({Unindent = true})

    Slab.Indent()
    Slab.Text("Stats:\n")
    for i, comp in ipairs(GUI.store.stats) do
        Slab.Indent()
        Slab.Text(comp.name .. ": ")
        Slab.SameLine({Pad = Utils.padFromChars(comp.name, 23)})

        if Slab.InputNumberDrag(
            comp.name,
            save.data[comp.name],
            comp.min,
            comp.max
        ) then
            save.data[comp.name] = Slab.GetInputNumber()
        end
        Slab.Unindent()
    end

    Utils.paddedSeparator({Unindent = true})

    Slab.Indent()
    Slab.Text("Chapters:\n")
    for _, area in ipairs(save.data.Areas.AreaStats) do
        local inx = tonumber(area._attr.ID) + 1
        local path = Utils.getAreaIcon(area._attr.ID)

        Slab.Indent()
        Slab.Image("Icon-0" .. area._attr.ID, {W = 48, H = 48, Path = path})
        Slab.SameLine({Pad = 64, CenterY = true})
        Slab.Text(GUI.store.areas[inx].name)
        Slab.Text("\n\n\n\n")
        Slab.Unindent()
    end

    Slab.Unindent()
end