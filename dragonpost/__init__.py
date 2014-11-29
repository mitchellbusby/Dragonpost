#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the main application. It mostly stores the application object (app) and
the configuration (config).
"""

import json

from flask import Flask

app = Flask(__name__)
with open("config.json") as f:
    config = json.load(f)

# Views have to be imported after app is instantiated.
import dragonpost.views