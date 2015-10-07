Has it changed?
===============

Grabs current version of each page in a list, and checks against
previous stored version.  Sends email and stores new version if
there is any change.  Currently uses sendgrid to send the email.
Configuration is done through environment variables.  Example
environments are in the examples directory.  These environments can
be instantiated using
`envdir <https://pypi.python.org/pypi/envdir>`_.

Environment Variables
---------------------

- ``HAS_IT_CHANGED_CFG`` should contain the path to a yaml file
  specifying a list of sites to monitor and an email address to
  notify upon changes.
- ``HAS_IT_CHANGED_DATA`` should contain the path to a directory to
  be used to keep current versions of the sites to check against.
- ``SENDGRID_API_KEY`` should contain the api key for sendgrid
- ``SENDGRID_URL`` should be the url of the sendgrid api endpoint
