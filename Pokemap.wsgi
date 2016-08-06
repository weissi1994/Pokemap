#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import ssl
import logging
import time

config = {}

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/virtual/map.derzer.at/PokemonGo-Map/")
os.chdir("/var/www/virtual/map.derzer.at/PokemonGo-Map/")

from pogom.app import Pogom
from flask_cors import CORS
from pogom import config
from pogom.utils import get_args, insert_mock_data
from pogom.models import init_database, create_tables, Pokemon, Pokestop, Gym
from pogom.pgoapi.utilities import get_pos_by_name

args = get_args()
config['parse_pokemon'] = not args.no_pokemon
config['parse_pokestops'] = not args.no_pokestops
config['parse_gyms'] = not args.no_gyms

position = get_pos_by_name(args.location)
if not any(position):
    log.error('Could not get a position by name, aborting.')
    sys.exit()
if args.no_pokemon:
    log.info('Parsing of Pokemon disabled.')
if args.no_pokestops:
    log.info('Parsing of Pokestops disabled.')
if args.no_gyms:
    log.info('Parsing of Gyms disabled.')

config['ORIGINAL_LATITUDE'] = position[0]
config['ORIGINAL_LONGITUDE'] = position[1]
config['LOCALE'] = args.locale
config['CHINA'] = args.china

application = Pogom(__name__)

db = init_database(application)
create_tables(db)
CORS(application);

application.set_current_location(position);

config['ROOT_PATH'] = application.root_path
config['GMAPS_KEY'] = args.gmaps_key
config['REQ_SLEEP'] = args.scan_delay