# Pinstripe

A simple web server, written in Python 3, that generates icons on-the-fly designed to be used to differentiate university classes.

Uses [Flask](https://palletsprojects.com/p/flask/) for the web server and [Pillow](https://pillow.readthedocs.io/en/stable/) for image processing.

## Example output
`GET /courseImg?subject=COT&course=3103&color=ffc904`

![Example icon](https://raw.githubusercontent.com/jeffreydivi/Pinstripe/master/example.png)
