return {
    scene = "home",
    isEditing = false,

    save = {
        raw = "",
        path = "",
        xml = nil
    },

    editor = {
        opened = false,
        saved = false,
        undoable = false,
        redoable = false
    },

    fileDialog = {
        popOpen = false,
        options = {
            Type = "openfile",
            AllowMultiSelect = false
        },
        callback = function (res)
            return res
        end
    },

    message = {
        popOpen = false,
        title = "Message!",
        data = "This is a message box."
    },

    modeNotEnabled = function (sc)
        return (
            GUI.state.scene ~= sc and
            GUI.state.scene ~= "home"
        )
    end
}