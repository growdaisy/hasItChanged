#!/usr/bin/env python

import requests, yaml, os, difflib
from pysend import Contact, Email, sendgridWebApi

# Get config from environment
configPath = os.environ['HAS_IT_CHANGED_CFG']
dataPath = os.environ['HAS_IT_CHANGED_DATA']
sendgridApiKey = os.environ['SENDGRID_API_KEY']
sendgridUrl = os.environ['SENDGRID_URL']

# Check for site diff and email diff if it has changed
def maybeEmail(server, sender, receiver, name, url):
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
      if prev == '':
         print('[{}] Storing initial version'.format(name))
      else:
         html_diff = difflib.HtmlDiff()
         diff = html_diff.make_file(prev.split('\n'),
                  curr.split('\n'), 'previous', 'current', True, 5)
         print('[{}] Change detected; sending email'.format(name))
         email = Email(sender, [receiver],
                       '[hasItChanged] {} changed', diff)
         server.send(email)
      with open(prevPath, 'w') as f:
         f.write(curr)

def main():
   # Yaml configuration
   config = yaml.load(open(configPath, 'rU').read())

   # Sends message to configured receiver
   senderInfo = config['email']['from']
   sender = Contact(senderInfo['name'], senderInfo['email'])
   receiverInfo = config['email']['to']
   receiver = Contact(receiverInfo['name'], receiverInfo['email'])
   server = sendgridWebApi.Server(sendgridUrl, sendgridApiKey)
   server.connect()

   # Iterate through sites in config and send emails
   for site in config['sites']:
      maybeEmail(server, sender, receiver, site['name'],
            site['url'])

if __name__ == "__main__":
   main()
