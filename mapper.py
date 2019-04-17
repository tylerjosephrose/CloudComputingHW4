#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    vehicles = line.split(',')[25:]
    for vehicle in vehicles:
         if len(vehicle) > 0:
             print '%s\t%s' % (vehicle.lower(), 1)
