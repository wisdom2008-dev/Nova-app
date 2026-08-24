[app]

title = Nova
package.name = nova
package.domain = org.nova

source.dir = .
source.include_exts = py,json,png,jpg,jpeg,kv,atlas

version = 1.0

requirements = python3,kivy,charset-normalizer==2.1.1

orientation = portrait
fullscreen = 0

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
