# Maintainer: Yafeng <yafengabc@gmail.com>

pkgname=uptimerec
pkgver=0.0.1
pkgrel=1
pkgdesc="A tools record system uptime and boottimes"
url=""
arch=('any')
license=('GPLv3')
depends=('glibc' 'sh' 'python')
provides=('uptime-recorder')
source=('uptimerec.tar.gz')
sha1sums=('SKIP')

build() {
  cd "${srcdir}"
}


package() {
  #install scripts to /usr/bin
  install -D "${srcdir}/${pkgname}/uptimerec.sh" "${pkgdir}/usr/bin/uptimerec.sh"
  install -D "${srcdir}/${pkgname}/uptimerec.py" "${pkgdir}/usr/bin/uptimerec.py"
  install -D "${srcdir}/${pkgname}/uptimereport.py" "${pkgdir}/usr/bin/uptimereport.py"


  # install systemd files
  install -Dm644 "${srcdir}/${pkgname}/uptimerec.service" "${pkgdir}/usr/lib/systemd/system/uptimerec.service"
  install -Dm644 "${srcdir}/${pkgname}/uptimerec_cal.service" "${pkgdir}/usr/lib/systemd/system/uptimerec_cal.service"
}

