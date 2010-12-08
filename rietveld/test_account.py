import os
os.environ["DJANGO_SETTINGS_MODULE"] = 'settings'

import gae2django
# Use gae2django.install(server_software='Dev') to enable a link to the
# admin frontend at the top of each page. By default this link is hidden.
gae2django.install(server_software='Django')

from codereview import models
from django.utils.encoding import smart_str
from google.appengine.ext import db

def account():
  def searchAccounts(property, added, response):
    query = "chenguang"
    limit = 10

    accounts = models.Account.all()
    accounts.filter("lower_%s > " % property, smart_str(query))
    accounts.filter("lower_%s < " % property, smart_str(query + "z"))
    accounts.order("lower_%s" % property);
    for account in accounts:
      if account.key() in added:
        continue
      if len(added) >= limit:
        break
      added.add(account.key())
      response += '%s (%s)\n' % (account.email, account.nickname)
    return added, response

  added = set()
  response = ''
  added, response = searchAccounts("nickname", added, response)
  added, response = searchAccounts("email", added, response)

  return response

def main():
  print account()

if __name__ == "__main__":
  main()
