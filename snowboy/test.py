import snowboydecoder
import sys
import signal
import os
from multiprocessing import Process



interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def intro():
	snowboydecoder.play_audio_file(snowboydecoder.DETECT_PANDA)

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=intro,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

