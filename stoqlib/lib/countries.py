# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2006 Async Open Source
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

from stoqlib.lib.translation import stoqlib_gettext as _, N_


# The country list is part of the evolution source code:
# evolution/addressbook/gui/contact-editor/e-contact-editor-address.c
countries = [N_("Afghanistan"),
             N_("Albania"),
             N_("Algeria"),
             N_("American Samoa"),
             N_("Andorra"),
             N_("Angola"),
             N_("Anguilla"),
             N_("Antarctica"),
             N_("Antigua And Barbuda"),
             N_("Argentina"),
             N_("Armenia"),
             N_("Aruba"),
             N_("Australia"),
             N_("Austria"),
             N_("Azerbaijan"),
             N_("Bahamas"),
             N_("Bahrain"),
             N_("Bangladesh"),
             N_("Barbados"),
             N_("Belarus"),
             N_("Belgium"),
             N_("Belize"),
             N_("Benin"),
             N_("Bermuda"),
             N_("Bhutan"),
             N_("Bolivia"),
             N_("Bosnia And Herzegowina"),
             N_("Botswana"),
             N_("Bouvet Island"),
             N_("Brazil"),
             N_("British Indian Ocean Territory"),
             N_("Brunei Darussalam"),
             N_("Bulgaria"),
             N_("Burkina Faso"),
             N_("Burundi"),
             N_("Cambodia"),
             N_("Cameroon"),
             N_("Canada"),
             N_("Cape Verde"),
             N_("Cayman Islands"),
             N_("Central African Republic"),
             N_("Chad"),
             N_("Chile"),
             N_("China"),
             N_("Christmas Island"),
             N_("Cocos (Keeling Islands)"),
             N_("Colombia"),
             N_("Comoros"),
             N_("Congo"),
             N_("Congo, The Democratic Republic Of The"),
             N_("Cook Islands"),
             N_("Costa Rica"),
             N_("Cote d'Ivoire"),
             N_("Croatia"),
             N_("Cuba"),
             N_("Cyprus"),
             N_("Czech Republic"),
             N_("Denmark"),
             N_("Djibouti"),
             N_("Dominica"),
             N_("Dominican Republic"),
             N_("Ecuador"),
             N_("Egypt"),
             N_("El Salvador"),
             N_("Equatorial Guinea"),
             N_("Eritrea"),
             N_("Estonia"),
             N_("Ethiopia"),
             N_("Falkland Islands"),
             N_("Faroe Islands"),
             N_("Fiji"),
             N_("Finland"),
             N_("France"),
             N_("French Guiana"),
             N_("French Polynesia"),
             N_("French Southern Territories"),
             N_("Gabon"),
             N_("Gambia"),
             N_("Georgia"),
             N_("Germany"),
             N_("Ghana"),
             N_("Gibraltar"),
             N_("Greece"),
             N_("Greenland"),
             N_("Grenada"),
             N_("Guadeloupe"),
             N_("Guam"),
             N_("Guatemala"),
             N_("Guernsey"),
             N_("Guinea"),
             N_("Guinea-bissau"),
             N_("Guyana"),
             N_("Haiti"),
             N_("Heard And McDonald Islands"),
             N_("Holy See"),
             N_("Honduras"),
             N_("Hong Kong"),
             N_("Hungary"),
             N_("Iceland"),
             N_("India"),
             N_("Indonesia"),
             N_("Iran"),
             N_("Iraq"),
             N_("Ireland"),
             N_("Isle of Man"),
             N_("Israel"),
             N_("Italy"),
             N_("Jamaica"),
             N_("Japan"),
             N_("Jersey"),
             N_("Jordan"),
             N_("Kazakhstan"),
             N_("Kenya"),
             N_("Kiribati"),
             N_("Korea, Democratic People's Republic Of"),
             N_("Korea, Republic Of"),
             N_("Kuwait"),
             N_("Kyrgyzstan"),
             N_("Laos"),
             N_("Latvia"),
             N_("Lebanon"),
             N_("Lesotho"),
             N_("Liberia"),
             N_("Libya"),
             N_("Liechtenstein"),
             N_("Lithuania"),
             N_("Luxembourg"),
             N_("Macao"),
             N_("Macedonia"),
             N_("Madagascar"),
             N_("Malawi"),
             N_("Malaysia"),
             N_("Maldives"),
             N_("Mali"),
             N_("Malta"),
             N_("Marshall Islands"),
             N_("Martinique"),
             N_("Mauritania"),
             N_("Mauritius"),
             N_("Mayotte"),
             N_("Mexico"),
             N_("Micronesia"),
             N_("Moldova, Republic Of"),
             N_("Monaco"),
             N_("Mongolia"),
             N_("Montserrat"),
             N_("Morocco"),
             N_("Mozambique"),
             N_("Myanmar"),
             N_("Namibia"),
             N_("Nauru"),
             N_("Nepal"),
             N_("Netherlands"),
             N_("Netherlands Antilles"),
             N_("New Caledonia"),
             N_("New Zealand"),
             N_("Nicaragua"),
             N_("Niger"),
             N_("Nigeria"),
             N_("Niue"),
             N_("Norfolk Island"),
             N_("Northern Mariana Islands"),
             N_("Norway"),
             N_("Oman"),
             N_("Pakistan"),
             N_("Palau"),
             N_("Palestinian Territory"),
             N_("Panama"),
             N_("Papua New Guinea"),
             N_("Paraguay"),
             N_("Peru"),
             N_("Philippines"),
             N_("Pitcairn"),
             N_("Poland"),
             N_("Portugal"),
             N_("Puerto Rico"),
             N_("Qatar"),
             N_("Reunion"),
             N_("Romania"),
             N_("Russian Federation"),
             N_("Rwanda"),
             N_("Saint Kitts And Nevis"),
             N_("Saint Lucia"),
             N_("Saint Vincent And The Grenadines"),
             N_("Samoa"),
             N_("San Marino"),
             N_("Sao Tome And Principe"),
             N_("Saudi Arabia"),
             N_("Senegal"),
             N_("Serbia And Montenegro"),
             N_("Seychelles"),
             N_("Sierra Leone"),
             N_("Singapore"),
             N_("Slovakia"),
             N_("Slovenia"),
             N_("Solomon Islands"),
             N_("Somalia"),
             N_("South Africa"),
             N_("South Georgia And The South Sandwich Islands"),
             N_("Spain"),
             N_("Sri Lanka"),
             N_("St. Helena"),
             N_("St. Pierre And Miquelon"),
             N_("Sudan"),
             N_("Suriname"),
             N_("Svalbard And Jan Mayen Islands"),
             N_("Swaziland"),
             N_("Sweden"),
             N_("Switzerland"),
             N_("Syria"),
             N_("Taiwan"),
             N_("Tajikistan"),
             N_("Tanzania, United Republic Of"),
             N_("Thailand"),
             N_("Timor-Leste"),
             N_("Togo"),
             N_("Tokelau"),
             N_("Tonga"),
             N_("Trinidad And Tobago"),
             N_("Tunisia"),
             N_("Turkey"),
             N_("Turkmenistan"),
             N_("Turks And Caicos Islands"),
             N_("Tuvalu"),
             N_("Uganda"),
             N_("Ukraine"),
             N_("United Arab Emirates"),
             N_("United Kingdom"),
             N_("United States"),
             N_("United States Minor Outlying Islands"),
             N_("Uruguay"),
             N_("Uzbekistan"),
             N_("Vanuatu"),
             N_("Venezuela"),
             N_("Viet Nam"),
             N_("Virgin Islands, British"),
             N_("Virgin Islands, U.S."),
             N_("Wallis And Futuna Islands"),
             N_("Western Sahara"),
             N_("Yemen"),
             N_("Zambia"),
             N_("Zimbabwe")]


def get_countries():
    """Fetch a list of translated/untranslated countries suitable for usage
    within combo.prefill();

    >>> [(translated label, label), ...]

    :returns: a list of tuples
    """

    # We store translated country names in a dictionary to ensure
    # there are no dupes because the combo expects that.
    return sorted(dict((_(c), c) for c in countries).items())
