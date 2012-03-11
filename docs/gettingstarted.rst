.. _gettingstarted:

===============
Getting started
===============

This guide is designed to point you to the best information about getting
started with Django-Shorty. Here are some good first
resources if you need to learn about Python and Django:

 * **Python**: `Official Python tutorial`_
 * **Python**: `Dive into Python`_
 * **Django**: `Official Django tutorial`_
 * **Django**: `Official Django documentation`_

Prerequisites
=============

To get started with Pinax you must have the following installed:

 * Python 2.4+.  Do **not** install Python 3+. Django-Shorty is not 
   compatible with Python 3 yet.
 * `pysqlite` or any other database driver is required.
 * `virtualenv`_ 1.4.7+ ( Optional )
 
 
.. _ref-install:

Installation
============

Download the latest Django-Shorty version and unpackit.
Enter into the Django-Shorty folder and type this command::

	$ python setup.py install

Django-Shorty is now installed!


Project Configuration
==================

Create a new Django project, now edit the settings.py file.
Goto INSTALLED_APPS and add shorty app and active the administration
interface

::
INSTALLED_APPS = (
    ........
    'django.contrib.admin',
    'shorty',
)

Now you need to add the variables of Django-Shorty app.
Have 4 variables:

* SHORTY_MODERATE - ( BOOLEAN ) - this variable define if you want moderate the link, 
                                  if this variable is set to TRUE any new link is add on
                                  "Pending" status.
* SHORTY_BANNED - ( STRING ) - this is the variable that define the URI where Django-Shorty
                               redirect the user if the shortlink is on Status "Banned"
                               Ex.:: SHORTY_BANNED = '/banned'
* SHORTY_PENDING - ( STRING ) - this is the variable that define the URI where Django-Shorty
                  	            redirect the user if the shortlink is on Status "Pending"
                  	            Ex.:: SHORTY_PENDING = '/pending'
* SHORTY_REFUSED - ( STRING ) - this is the variable that define the URI where Django-Shorty
                  	            redirect the user if the shortlink is on Status "Refused"
                  	            Ex.:: SHORTY_REFUSED = '/refused'

All this variables are **mandatory**
So in your settings.py, after INSTALLED_APPS you add all the SHORTY variables
like this::

SHORTY_MODERATE = True

SHORTY_BANNED = "/banned"

SHORTY_PENDING = "/pending"

SHORTY_REFUSED = "/refused"
