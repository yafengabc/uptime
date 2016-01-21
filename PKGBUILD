# Maintainer: Yafeng <yafengabc@gmail.com>

pkgname=uptimerec
pkgver=0.0.1
pkgrel=1
pkgdesc="A tools record system uptime and boottimes"
url=""
arch=('any')
license=('GPLv3')
depends=('glibc' 'sh' 'python')
provides=('uptime-recoder')
source=('uptimerec.tar.gz')
sha1sums=('SKIP')

build() {
  cd "${srcdir}"
}


package() {
  cd "${srcdir}

  install -d "$pkgdir/usr/share/licenses/$pkgname"


  # install systemd files
  install -Dm644 "${srcdir}/dhcpcd_.service" "${pkgdir}/usr/lib/systemd/system/dhcpcd@.service"
}

