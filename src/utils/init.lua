local utils = {}


utils.boolf = function (str)
    if str == nil then
        return false
    else
        return string.lower(str) == "true"
    end
end


utils.startMargin = function (margin)
    Slab.Text("", {Pad = margin})
    Slab.SameLine()
end


utils.paddedSeparator = function (opts)
    if opts.Unindent ~= nil then
        Slab.Unindent()
    end

    Slab.Text("\n")
    Slab.Separator()
    Slab.Text("\n")
end


utils.padFromChars = function (chars, max)
    if #chars >= max then
        return 0
    else
        return (max - #chars) * 8
    end
end


utils.getAreaIcon = function (id)
    return "_assets/images/areas/" .. id .. ".png"
end


return utils