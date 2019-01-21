# Water-level
Simple water level measurement using micropython/esp8266 and ultrasonic sensor hc-sr04 

## Components
>1. esp8266 [nodeMcu v3](https://docs.zerynth.com/latest/official/board.zerynth.nodemcu3/docs/index.html). This is flashed with [micropython].
>2. hc-sr04 - ultrasonic distance sensor
>3. Load the files boot.py and main.py to the esp via [repl].  

## How it works
The esp reads water-level periodically and sends the data to a remote server. The file boot.py runs first followed by main.py

### Connection Notes:
This was tested with 3.3v version of hc-sr04
To wake from deepsleep connect D0 to the rst button


[micropython]: https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html
[repl]: https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html
