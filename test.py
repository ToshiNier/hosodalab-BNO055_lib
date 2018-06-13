#!/usr/bin/python

from adafruit_bno055_controller import AdafruitBno055Controller
from xl_config import XLConfig

def main():
    bno_controller = AdafruitBno055Controller()
    x,y,z = bno_controller.gravity()
    

if __name__== "__main__"
    main()