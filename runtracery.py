#!/usr/local/bin/python3
import argparse
import json
import tracery
from tracery.modifiers import base_english


parser = argparse.ArgumentParser()
parser.add_argument("grammar",
    help="Path to grammar json file")
parser.add_argument(
    "-s", "--start",
    default="#start#",
    help="Start token")


def read_json_file(path):
    """
    Read an entire file in one go.
    """
    with open(path) as f:
        return json.load(f)


def make_tracery(rules):
    """
    Instantiate and configure Tracery
    """
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    return grammar


if __name__ == "__main__":
    args = parser.parse_args()
    json = read_json_file(args.grammar)
    rendered_grammar = make_tracery(json).flatten(args.start)
    print(rendered_grammar)