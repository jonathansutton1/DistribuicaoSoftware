#!/usr/bin/env python3
from dev_aberto import hello

from datetime import date,datetime
from email.utils import format_datetime
import gettext
import babel
import locale
from babel.dates import format_date 
_ = gettext.gettext


if __name__ == '__main__':
    date, name = hello()
    a = int(date[0:4])
    b = int(date[5:7])
    c = int(date[8:10])
    d = int(date[11:13])
    e = int(date[14:16])
    f = int(date[17:19])
    date = datetime(a,b,c,d,e,f)
    date = format_datetime(date)
    print(_('Último commit feito em:'), _(date), _('por'), name)
