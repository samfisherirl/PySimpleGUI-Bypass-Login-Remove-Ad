# all of the tkinter involved imports
import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from tkinter import ttk
# import tkinter.scrolledtext as tkst
import tkinter.font
from uuid import uuid4

# end of tkinter specific imports
# get the tkinter detailed version
tclversion_detailed = tkinter.Tcl().eval('info patchlevel')
framework_version = tclversion_detailed

import time
import pickle
import calendar
import datetime
import textwrap

import socket
from hashlib import sha256 as hh
import inspect
import traceback
import difflib
import copy
import pprint
try:  # Because Raspberry Pi is still on 3.4....it's not critical if this module isn't imported on the Pi
    from typing import List, Any, Union, Tuple, Dict, SupportsAbs, Optional  # because this code has to run on 2.7 can't use real type hints.  Must do typing only in comments
except:
    print('*** Skipping import of Typing module. "pip3 install typing" to remove this warning ***')
import random
import warnings
from math import floor
from math import fabs
from functools import wraps

try:  # Because Raspberry Pi is still on 3.4....
    # from subprocess import run, PIPE, Popen
    import subprocess
except Exception as e:
    print('** Import error {} **'.format(e))

import threading
import itertools
import json
import configparser
import queue

try:
    import webbrowser

    webbrowser_available = True
except:
    webbrowser_available = False
# used for github upgrades
import urllib.request
import urllib.error
import urllib.parse
import pydoc
from urllib import request
import os
import sys
import re
import tempfile
import ctypes
import platform
