@1

package "ocamlre" {
  version     = "191229137d8268e1847e13fbf3bd6522ab062a21"
  description = "https://github.com/avsm/ocaml-re.git"
  urls = [ "http://www.ocamlpro.com/pub/ocaml-re.tar.bz2" ]
  patches = [ "local://files/ocamlre.install"
            ; "local://files/ocamlre.ocp" ]
  make = [ "ocp-build -init -scan" ]
}