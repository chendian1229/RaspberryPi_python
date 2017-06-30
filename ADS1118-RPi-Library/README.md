# ADS1118 Python3 Library for Raspberry Pi 
and aplllication for reading the thermocouple
## Requestment

###Turn on SPI

edit config.txt

`vim /boot/config.txt`

search ans set

`dtparam=spi=on`

save and reboot 

`ls /dev/*spi*`

you can see the device `/dev/spidev0.0` and `/dev/spidev0.1`


### Install spidev

we need the library call "spidev"

`pip3 install spidev`

wating for installation

### Install thermocouples_reference

`pip3 install thermocouples_reference --user`
