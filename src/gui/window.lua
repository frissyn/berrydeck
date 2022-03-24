local window = {
    Title    = nil,
    X        = 0,
    Y        = 0,
    W        = 800,
    H        = 600,
    Border   = 0,
    Rounding = 0,

    AllowMove         = false,
    AllowResize       = false,
    AutoSizeContent   = true,
    AutoSizeWindow    = false,
    ConstrainPosition = true,
    NoOutline         = false,
    NoSavedSettings   = false,
    IsOpen            = true,
    ResetLayout       = true,
    ShowMinimize      = false
}

if love.system.getOS() == "Windows" then
    window.Y = -1
end

return window