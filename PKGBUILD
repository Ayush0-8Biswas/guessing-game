# Maintainer: Ayush Biswas biswas.ayush03@kgpian.iitkgp.ac.in
pkgname=guessing-game-git
pkgver=1.1
pkgrel=1
pkgdesc="A cool, lightweight and open source guessing game in the terminal."
arch=(any)
url="https://github.com/Ayush0-8Biswas/guessing-game.git"
license=('unknown')
depends=()
makedepends=(git python3)
provides=()
source=("git+$url")
md5sums=('SKIP')

build() {
	cd guessing-game
}

package() {
	cd guessing-game
	mkdir -p ${pkgdir}/usr/local/bin/
	cp guessing-game.py ${pkgdir}/usr/local/bin/guessing-game
	chmod +x ${pkgdir}/usr/local/bin/guessing-game
}
