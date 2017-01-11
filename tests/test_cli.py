from __future__ import absolute_import, division, print_function

import os

import logging

import sys

from pdfx import cli
# import pytest

curdir = os.path.dirname(os.path.realpath(__file__))


def test_cli():
    logging.basicConfig(stream=sys.stdout)
    log = logging.getLogger("cli")
    log.setLevel(logging.DEBUG)
    
    parser = cli.create_parser()
    parsed = parser.parse_args(['-p',"1",'-j', 'pdfs/valid.pdf'])
    log.debug(parsed)
    assert parsed.json
    assert parsed.pdf == "pdfs/valid.pdf"
    
