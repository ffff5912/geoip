#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests

@click.command()
@click.argument('ip')
def find(ip):
    url = 'http://freegeoip.net/%s/%s' % ('json', ip) 
    print url
    response = requests.get(url)
    click.echo(response.json())

def main():
    find()

if __name__ == '__main__':
    main()

