.. _gettingstarted:

===============
Getting started
===============

This guide is designed to point you to the best information about getting
started with Django-Shorty.

Prerequisites
=============

To get started with Django-Shorty you must have the following installed:

 * Python 2.4+.  Do **not** install Python 3+. Django-Shorty is not 
   compatible with Python 3 yet.
 * pysqlite or any other database driver is required.
 * virtualenv 1.4.7+ ( Optional )
 
 
.. _ref-install:

Installation
============

Download the latest Django-Shorty version and unpackit.
Enter into the Django-Shorty folder and type this command::

	$ python setup.py install

Django-Shorty is now installed!

.. _ref-configuration:

Project Configuration
=====================

Create a new Django project, now edit the settings.py file.
Goto :literal:`INSTALLED_APPS` and add :literal:`shorty` app and active the administration
interface

.. code-block:: python
	:linenos:
	
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
                               Ex: :literal:`SHORTY_BANNED = '/banned'`
* SHORTY_PENDING - ( STRING ) - this is the variable that define the URI where Django-Shorty
                  	            redirect the user if the shortlink is on Status "Pending"
                  	            Ex: :literal:`SHORTY_PENDING = '/pending'`
* SHORTY_REFUSED - ( STRING ) - this is the variable that define the URI where Django-Shorty
                  	            redirect the user if the shortlink is on Status "Refused"
                  	            Ex: :literal:`SHORTY_REFUSED = '/refused'`

All this variables are **mandatory**
So in your settings.py, after :literal:`INSTALLED_APPS` you add all the :literal:`SHORTY` variables
like this:

.. code-block:: python
	:linenos:
	
	SHORTY_MODERATE = True
	SHORTY_BANNED = "/banned"
	SHORTY_PENDING = "/pending"
	SHORTY_REFUSED = "/refused"

.. _ref-url:

URL Configuration
=================

To configure Django-Shorty url you need to use only two views:

* :literal:`shorty.views.add_shorty_url` - add new link with the add form
* :literal:`shorty.views.shorty_url` - the redirect view

So, for example if Django-Shorty is your Home Page project and you want to show the 
form for add a new url:

.. code-block:: python
	:linenos:
	
	urlpatterns = patterns('',
   		url(r'^/?$','shorty.views.add_shorty_url'),
    	#more urls
	)
	
Go to the home page of your project, for example :literal:`http://localhost:8000`
and if all work well you can get an template error. This occur because Django-Shorty
have a Default template for this page, the template will be located in ::literal:`shorty/add.html`
If you want you can change the name and the location of this template file, passing an
option to the url regex:

.. code-block:: python
	:linenos:
	
	urlpatterns = patterns('',
   		url(r'^/?$','shorty.views.add_shorty_url',{'shorty_template':'add.html'}),
    	#more urls
	)

In this case Django-Shorty find the template file :literal:`add.html` into the root
template directory