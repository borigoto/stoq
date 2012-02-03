# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2012 Async Open Source
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
##
## Author(s): Stoq Team <stoq-devel@async.com.br>
##
##

from stoqlib.lib.translation import stoqlib_gettext

_ = stoqlib_gettext


class CompanyDocument(object):
    label = _('Document')
    entry_mask = None

    def validate(self, value):
        return True

company_document = CompanyDocument()


class PersonDocument(object):
    label = _('Document')
    entry_mask = None

    def validate(self, value):
        return True

person_document = PersonDocument()

# This is not actually a state, it's more like a country subdivsion, see:
# http://en.wikipedia.org/wiki/Country_subdivision


class State(object):
    label = _('State')

    state_list = []

    def validate(self, value):
        return True

state = State()
