#!/usr/bin/python

from datetime import datetime,timedelta,date
import sys

def validar_token():
    acesso = datetime(2017,02,01,00,00,00)
    atual = datetime(2017,02,01,01,00,01)

    if (atual - acesso).total_seconds() > 3600:
        print "Seu token de acesso expirou"
        sys.exit()
