#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Helper functions.
"""

from flask import render_template

from dragonpost import app, config

def render(template_name, **kwargs):
    """
    Render a template with app context.

    This is essentially a wrapper around flask.render_template which
    automatically includes the application config.
    """

    return render_template(template_name, config=config, **kwargs)