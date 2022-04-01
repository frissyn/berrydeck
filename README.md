🍓 BerryDeck
============

Simple GUI for creating and editing Savefiles in Celeste, powered by Love2D. Currently a work in progress, stay tuned for the alpha release!

### Roadmap

BerryDeck is about **34% complete**. The framework has been laid out, and I'm currently working on filling in the features. 

The following bullet list covers some of the features that still need to be completed.

+ [ ] **Editor:**
    + [ ] *Interactive Mode:*
        + [x] "Open" savefile in interactive mode
        + [ ] "Save" and "Save As" functionality
        + [ ] Create savefile from preset
        + [ ] Create preset from savefile
        + [ ] Undo/Redo most recent change
        + [x] Confirm "Quit" if savefile not saved
        + [ ] Validate savefile values
        + [ ] *Editing Controls:*
            + [x] Savefile Metadata [Input]
            + [ ] Savefile Play Time duration [Input]
            + [ ] Story Journal [Checkbox]
            + [x] Game statistics [Input, Slider]
            + [ ] Chapter Statistics [Input, Slider]
            + [ ] *Controls for editing Chapter entities:*
                + [ ] Berries [Input, Checkbox] 
                + [ ] Cassettes [Checkbox]
                + [ ] Crystal Hearts [Checkbox]
                + [ ] Room Keys [Input, Checkbox]
    + [ ] *Raw Mode:*
        + [x] "Open" savefile in raw mode
        + [ ] Syntax highlighting for XML text
        + [ ] Text editor shortcuts
    + [x] *Styling:*
        + [x] Change application theme
        + [x] Create and save application themes
+ [ ] **Internal:**
    + [ ] *Parser:*
        + [x] Parse savefiles to/from XML
        + [ ] Parse FileTimes to/from milliseconds
        + [x] Error handling for file reading/writing
    + [ ] *Auto-Updater:*
        + [ ] Check GitHub for most recent release
        + [ ] Download `.exe` or `.love` from GitHub release
    + [ ] *GUI Loop:*
        + [x] Create simplified GUI rendering loop
        + [x] Enforce periodic garbage collection
        + [x] Create and maintain simplified app state across sessions
