#!/usr/bin/env python

import requests, yaml, os, difflib
from pysend import Contact, Email
from pysend.sendgridWebApi import SendgridWebApiServer

def send(subject, html):
   email = Email(sender, [receiver], subject, html)
   server.send(email)

# Check for site diff and email diff if it has changed
def maybeEmail(name, url):
   prevPath = os.path.join(dataPath, '{}.html'.format(name))
   prev = ''
   if os.path.lexists(prevPath):
      if os.path.isfile(prevPath):
         with open(prevPath, 'rU') as f:
            prev = f.read()
      else:
         raise 'Bad path {}'.format(prevPath)
   r = requests.get(url)
   curr = r.text
   if curr != prev:
      diff = html_diff.make_file(prev.split('\n'),
               curr.split('\n'), 'previous', 'current', True, 5)
      print('{} changed; sending email'.format(name))
      send('[hasItChaned] {} changed'.format(name), diff)
      with open(prevPath, 'w') as f:
         f.write(curr)

def main():
   # Get config from environment
   configPath = os.environ['HAS_IT_CHANGED_CFG']
   dataPath = os.environ['HAS_IT_CHANGED_DATA']
   emailProvider = os.environ['HAS_IT_CHANGED_EMAIL_PROVIDER']
   sendgridApiKey = os.environ['SENDGRID_API_KEY']
   sendgridUrl = os.environ['SENDGRID_URL']

   # Check that user is using supported email provider
   if emailProvider != "sendGridWebApi":
      raise "Unsupported email provider"

   # Yaml configuration
   config = yaml.load(open(configPath, 'rU').read())

   # Create diff context
   html_diff = difflib.HtmlDiff()

   # Sends message to configured receiver
   senderInfo = config['email']['from']
   sender = Contact(senderInfo['name'], senderInfo['email'])
   receiverInfo = config['email']['to']
   receiver = Contact(receiverInfo['name'], receiverInfo['email'])
   server = SendgridWebApiServer(sendgridUrl, sendgridApiKey)
   server.init()

   # Iterate through sites in config and send emails
   for site in config['sites']:
      maybeEmail(site['name'], site['url'])


if __name__ == "__main__":
   main()
