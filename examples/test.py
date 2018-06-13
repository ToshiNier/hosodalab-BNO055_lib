#!/usr/bin/python

from adafruit_bno055_controller import *
from xl_config import *

def main():
    bno_controller = AdafruitBno055Controller()
    x,y,z = bno_controller.gravity()
    print x,y,z
    

if __name__ == "__main__":
    main()