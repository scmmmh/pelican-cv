==================
Pelican Page Order
==================

Pelican plugin to enable loading JSONResume CVs.

Configuration
#############

Load the plugin in your ``pelicanconf.py``

.. code:: python

  PLUGINS = ['pelican_cv']

Then specify the CV JSONResume files to load

.. code:: python

  CVS_SRC = ['my-cv.json']

Theming
#######

For theming purposes each page has the following additional attribute:

* ``cvs`` - The list of loaded cvs as a dictionary
