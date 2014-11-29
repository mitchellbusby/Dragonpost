#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
URL routing and what content to return to the user.
"""

from dragonpost import app, config
from dragonpost.helpers import render

@app.route("/")
def index():
    return render("layout.html")