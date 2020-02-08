# python-muse

This is a toy example to demostrate how to interact with Muse Headband in Python using Muse Monitor.

## requirements

- A Muse Headband. Currently works with the 2014 Muse Model MU-01, the 2016 Muse Model MU-02 and the 2018 "Muse 2" Model MU-03.
- An iPhone or Android.
- [Mind Monitor](https://mind-monitor.com/). Install it on the phone that connects to your muse headband.
- Install the following python dependencies:

``` bash
pip install -r requirements.txt
```

## how to use

1. Make sure Muse headband is connected to your phone using official Muse application.
2. Get your PC's IP.
3. Open Muse Monitor. Go to the settings page, and then type your PC's ip at the `OSC Stream Target IP` field.
4. On your PC, run:

``` bash
python demo.py --ip YOUR_PC_IP --port 5000
```

Hopefully it works! Now try to blink your eyes and see whether you see `blink` in the screen.

For more details, please refer to [FAQ of Mind Monitor](https://mind-monitor.com/FAQ.php#Compatibility).
