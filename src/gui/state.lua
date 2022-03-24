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
    }
}