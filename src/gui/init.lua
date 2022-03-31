local PATH = ...

return {
    layout = require(PATH .. '.layout'),
    menu = require(PATH .. '.menu'),
    state = require(PATH .. '.state'),
    store = require(PATH .. '.store'),
    window = require(PATH .. '.window'),

    scenes = {
        editor = require(PATH .. '.scenes.editor'),
        home = require(PATH .. '.scenes.home'),
        raw = require(PATH .. '.scenes.raw')
    }
}