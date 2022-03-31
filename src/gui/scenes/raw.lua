return function ()
    local save = GUI.state.save.data.SaveData
    local text = GUI.state.save.lib.toXml(save, "SaveData")

    Slab.BeginLayout("raw", GUI.layout.raw)

    Slab.Text("Editing " .. save.Name .. "'s savefile in Raw Mode.")

    if Slab.Input(
        "Raw XML",
        {
            H = 525,
            W = 750,
            Align = "left",
            Multiline = true,
            MultiLineW = 650,
            ReturnOnText = false,
            SelectOnFocus = false,
            Text = text
        }
    ) then
        text = Slab.GetInputText()
    end

    Slab.EndLayout()
end