[app]

# Nombre de tu app (como se verá en el teléfono)
title = MiAppKivy

# Nombre del paquete (sin espacios, solo letras minúsculas y números)
package.name = miapp

# Dominio inverso (cambia esto a algo único tuyo)
package.domain = org.ejemplo

# Nombre del archivo Python principal
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versiones
version = 1.0
requirements = python3,kivy

# Orientación (portrait o landscape)
orientation = portrait

# Icono de la app (opcional)
icon.filename = %(source.dir)s/icon.png

# Permisos necesarios (usa solo los que tu app realmente necesita)
android.permissions = INTERNET

# Archivos incluidos
include_exts = py, png, jpg, kv

# Modo release (IMPORTANTE para Play Store)
android.release = 1

# Ruta al archivo keystore
android.keystore = /ruta/a/tu/mykey.keystore
android.keystore_pass = tu_contraseña_keystore
android.keyalias = mykeyalias
android.keyalias_pass = contraseña_del_alias

# Evitar compilar el APK cada vez
android.p4a_whitelist = 

# Soporte para pantalla completa
fullscreen = 1

# Soporte para dispositivos Android modernos
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = 1

# Deshabilitar log de depuración (más limpio en producción)
log_level = 1
