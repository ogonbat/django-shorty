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

* SHORTY_MODERATE - ( BOOLEAN ):
	* Default value is *False*
	* If set *True* all the new URL added are on **Pending** status.
* SHORTY_BANNED - ( STRING ) - 
	* Default value: */banned*
	* This is the url redirect for banned URL's
* SHORTY_PENDING - ( STRING ) - 
	* Default value: */pending*
	* This is the url redirect for pending URL's
* SHORTY_REFUSED - ( STRING ) - 
	* Default value: */refused*
	* This is the url redirect for refused URL's

.. _ref-url:

URL Configuration
=================

To configure the defaults url you need to use include:

.. code-block:: python
	:linenos:
	
	url(r'^', include('shorty.urls')),

this code is valid if you want to add Django-Shorty as Home Page

.. _ref-template:

Template Files
=================

The templates file are:

* :literal:`shorty/add.html`
* :literal:`shorty/private.html` ( URl password request )

.. _ref-form:

Form
=======

the name of the form template variable is the same in the *add* view and in the *password check* view,
:literal:`shorty_form`
Ex:

:literal:`shorty/add.html`

.. code-block:: python
	:linenos:
	
	<form action="." method="post">
    	{% csrf_token %}
    	{{ shorty_form.as_p }}
    	<input type="submit" value="Submit" />
	</form>

:literal:`shorty/private.html`

.. code-block:: python
	:linenos:
	
	<form action="." method="post">
    	{% csrf_token %}
    	{{ shorty_form.as_p }}
    	<input type="submit" value="Submit" />
	</form>

The :literal:`shorty/add.html` have other template variable.
When the process is completed the page return to the *add view* and
if you want to show the *slug* code you can use the :literal:`url_slug`

.. code-block:: python
	:linenos:
	
	<form action="." method="post">
    	{% csrf_token %}
    	{{ shorty_form.as_p }}
    	<input type="submit" value="Submit" />
	</form>
	The Short URL:
	{% if url_slug %}
		http://ttt.io/{{ url_slug }}
	{% endif %}

