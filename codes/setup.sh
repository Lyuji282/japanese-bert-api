#!/usr/bin/env bash

gunicorn --workers=1 app:app -b 0.0.0.0:5000