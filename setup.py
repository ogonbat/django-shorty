from distutils.core import setup

setup(
    name = "shorty",
    packages = ["shorty"],
    version = "0.0.1",
    description = "django-shorty is a django app to shorten links and share it",
    author = "Andrea Mucci",
    author_email = "cingusoft@gmail.com",
    url = "https://github.com/ogonbat/django-shorty",
    keywords = ["bit.ly", "shorten link", "django"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Framework :: Django",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    long_description = """\
Django app for fast shorten links generation
-------------------------------------

This project use Bijective Algorithm to get the shorten link

Feature Developments:
- add views count
- add rest interface
 
This version requires Python 2 or later;
"""
)