
# <img src="https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/docs/repo/pethome_image/RaspberryPi_Logo.jpg?raw=true" width="64">Raspberry Pi Setting

## Full System Reference
- [Go To Main-Repository](https://github.com/kuj0210/IoT-Pet-Home-System)

## **Install Rasbian**

 - Installation method of Rasbian<br>
   https://www.raspberrypi.org/documentation/installation/installing-images/

## **How to use Raspberry Pi Camera**

1. Install the Raspberry Pi Camera module by inserting the cable into the Raspberry Pi. 
The cable slots into the connector situated between the Ethernet and HDMI ports, 
with the silver connectors facing the HDMI port.

2. Boot up your Raspberry Pi.

3. From the prompt, run ```sudo raspi-config```.
```
sudo raspi-config
```

4. If the ```camera``` option is not listed, you will need to run a few commands to update your Raspberry Pi. 
Run ```sudo apt-get update``` and ```sudo apt-get upgrade```.
```
sudo apt-get update
sudo apt-get upgrade
```

5. Run ```sudo raspi-config``` again - you should now see the ```camera``` option.
![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/docs/repo/pethome_image/setting/Enable_Camera.png?raw=true)

6. Navigate to the ```camera``` option, and enable it. Select ```Finish``` and reboot your Raspberry Pi.


   
## **How to connect motor wires**

![](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/docs/repo/pethome_image/setting/raspberry-pi-pinout.png?raw=true)


### Food Motor

- Orange wired: connects to pin 35
- Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)
- Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)

### Door Motor

- Orange wired: connects to pin 12
- Red wired: connects to 3v3 or 5v pin(one of pin 1, 2, 4, 17)
- Brown wired: connects to GND pin(one of pin 6, 9, 14, 20, 25, 30, 34, 39)

## Clone this repository and Setting

```bash
$ git clone https://github.com/IoT-Pet-Home-System/petHomeSystem
$ sudo chmod +0777 setting.sh
$ ./setting.sh
```

## Run
```bash
$ cd src
$ sudo python3 server.py
```

## CONTRIBUTING

Contributing on our repository is very thanks, and welcome!<br>
If you want to contact us, please send below mail.<br>

- KeonHeeLee ([chattingBotServer](https://github.com/IoT-Pet-Home-System/chattingBotServer))
  - beta1360@naver.com
  - beta1360sh@gmail.com
  
- kuj0210 ([All management](https://github.com/kuj0210/IoT-Pet-Home-System))
  - on_11@naver.com
  
- seok8418 ([petHomeSystem](https://github.com/IoT-Pet-Home-System/petHomeSystem))
  - seok8418@nate.com

 ## **LICENSE**
 
 IoT-Pet-Home-System's pet-home system is licensed under [BSD 3-Clause License](https://github.com/kuj0210/IoT-Pet-Home-System/blob/master/PetHome/LICENSE).
 
 ```
Copyright (c) 2018-present, kuj0210, KeonHeeLee, seok8418
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
 
 
 
