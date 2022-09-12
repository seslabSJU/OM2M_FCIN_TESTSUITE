# OM2M_FCIN_TESTSUITE
![](img/om2m.png)
Test code for OM2M_FCIN_TESTSUITE



## Introduction
OM2M IoT platform that follows oneM2M(ref. [http://www.onem2m.org]http://www.onem2m.org) standard

    git clone https://github.com/seslabSJU/OM2M_FCIN_TESTSUITE



## Setting highlevel architecture
ready your arduino UNO board, raspberrypi and OM2M platform

### logical
<img src="img/logical.png"  width="50%" height="50%">

### physical
<img src="img/physical.png"  width="50%" height="50%">

### Test Environment
<img src="img/testenv.png"  width="50%" height="50%">



## Setting for arduino
ready your arduino UNO board and build up circuit board like picture below and then upload [arduino.ino](arduino/arduino.ino) file
<img src="img/circuit.png"  width="50%" height="50%">



## Setting for raspberrypi
ready your server computer for connect with arduino UNO board and then execute command below

    cd OM2M_FCIN_TESTSUITE
    pip3 install -r requirements.txt
    cd raspberrypi
    python3 main.py



## View of Test
![](img/example.png)
