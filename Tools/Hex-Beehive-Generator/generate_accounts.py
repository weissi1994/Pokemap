#!/usr/bin/env python
import argparse
from ptcaccount import random_account
from tos import accept_tos

parser = argparse.ArgumentParser()
parser.add_argument("-acc", "--num_accounts", help="# of Accounts", default=5, type=int)
parser.add_argument("-o", "--output", default="generated", help="output file for the script")

template = "{},{}\n"

args = parser.parse_args()

print("Accounts to {}".format(args.output))
output_fh = file(args.output+"_accounts.csv", "a")
o_mail = file(args.output+"_mails.csv", 'a')

for i in range(1, args.num_accounts):
    acc = random_account()
    output_fh.write(template.format(acc['username'], acc['password']))
    o_mail.write(template.format(acc['username'], acc['email']))
    o_mail.flush()
    output_fh.flush()
    # Platy tut, accept tos
    accept_tos(acc['username'], acc['password'])
