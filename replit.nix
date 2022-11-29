with import <nixpkgs> { };

{ pkgs }: {
  name = "berrydeck";
  deps = [
    gh
    yarn
    nodejs
    python38Full
    nodePackages.npm
  ];
  env = {
    PYTHON_LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      pkgs.glib
      pkgs.xorg.libX11
    ];
    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
    LANG = "en_US.UTF-8";
  };
}