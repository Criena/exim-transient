#!/usr/bin/env -S python3 -B
#-*- coding: utf8 -*-
#
__author__ = 'Karel W. Dingeldey '
__copyright__ = 'Copyright (c) Criena Network'


########################################################################
### Imports
########################################################################

import datetime, re, sys


########################################################################
### Variables
########################################################################

email_regex = re.compile('([0-9]{4})([0-9]{2})([0-9]{2})_(.+)')


########################################################################
### Main
########################################################################

if __name__ == '__main__':

    if len(sys.argv) != 2:
        # No argument given! Is exim misconfigured?
        print('DEFER No argument given!')
        sys.exit(1)

    email = sys.argv[1]
    result = re.match(email_regex, email)

    if not result:
        # No prefix match
        print('DECLINE No prefix match!')
        sys.exit(0)

    try:
        email_date = datetime.date(int(result.group(1)), int(result.group(2)), int(result.group(3)))
    except ValueError:
        # No valid date found
        print('DECLINE No valid date found!')
        sys.exit(0)

    today = datetime.date.today()
    if email_date < today:
        # Date has passed, address is now invalid
        print('FAIL Date has passed, address is now invalid.')
        sys.exit(0)

    # All tests passed, valid address
    print(f'REDIRECT {result.group(4)}')
