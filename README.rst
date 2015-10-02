Has it changed?
===============

Grabs current version of each page in a list, and checks against
previous stored version.  Sends email and stores new version if
there is any change.  Currently uses sendgrid to send the email.
Configuration is done through environment variables.  Example
environments are in the examples directory.  These environments can
be instantiated using
`envdir <https://pypi.python.org/pypi/envdir>`_.
