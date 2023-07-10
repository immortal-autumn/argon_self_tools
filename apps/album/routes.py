# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.album import blueprint
from flask import render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route("/")
@login_required
def album_default():
    return render_template("album/index.html")
