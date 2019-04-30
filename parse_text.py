#!/bin/bash
import sys
import os

os.system("curl 'localhost:5000/parse?q=" + "+".join(sys.argv[1:]) + "&project=current&model=nlu'")
print('\n')
