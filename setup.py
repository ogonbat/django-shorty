from distutils.core import setup

setup(
    name = "django-shorty",
    packages = ["shorty","shorty.utils","shorty.api","shorty.piston"],
    version = "0.1.0",
    description = "Django-shorty is a django app for fast and easy creation of personal URL shortener service, like bit.ly or tinyURL.",
    author = "Andrea Mucci",
    author_email = "cingusoft@gmail.com",
    url = "https://github.com/ogonbat/django-shorty",
    keywords = ["bit.ly", "shorten link", "django"],
    #requires = ["django-piston"],
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

Features:
- Bijective Algorithm for encode/decode slug
- 301 Redirect Status Code
- Password protected redirect service
- Django Admin interface management and custom admin actions
- URL moderation

Roadmap:
- add views count
- add rest interface
 
This version requires Python 2 or later;
"""
)