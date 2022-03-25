local xml2lua = require("lib.xml2lua-love.xml2lua")
local handler = require("lib.xml2lua-love.xmlhandler.tree")

local savefile = {}
local parser = xml2lua.parser(handler)


savefile.new = function (path)
    local fh = io.open(path, "r+")
    local content = fh:read("a")
    fh:close()

    local success, err = pcall(
        function () parser:parse(content) end
    )

    if success then
        return {
            path = path,
            raw = content,
            data = handler.root.SaveData
        }
    else
        GUI.state.message = {
            popOpen = true,
            title = "Error Occured!",
            data = (
                "Attempt to parse savefile failed.\nValid savefile " ..
                "formats should end in .celeste or .xml" ..
                ":\n(" .. path .. ")\n\n\n Error:\n " .. err
            )
        }

        return nil
    end
end


return savefile