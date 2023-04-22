# pre-compile kmk

Get the correct mpy-cross version for the matching circuitpython version.
In this case I picked it for circuitpython 7.2.5.
https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/mpy-cross/

```
cd kmk_firmware
find kmk -type f -name "*.py" -exec mpy-cross.static-amd64-linux-7.2.5 {} \;
```

## copy pre-compiled kmk
```
rsync -zarv  --include="*/" --include="*.mpy" --exclude="*" kmk_firmware/kmk /run/media/stefanfoulis/KYRIAL/
rsync -zarv  --include="*/" --include="*.mpy" --exclude="*" kmk_firmware/kmk /run/media/stefanfoulis/KYRIAR/
```

## connecting to serial

```
screen /dev/ttyACM0 115200
screen /dev/ttyACM1 115200
```