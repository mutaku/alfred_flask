#!/usr/bin/env python
##########################################
# Alfred - Flask version
#  Custom CMS for Mutaku
#  Matthew Martz 2013
##########################################

from flask import Flask
import getopt
import sys

# Instantiate Flask
app = Flask(__name__)

# Database manipulation tools

# Views and data handling

# Routing setup
@app.route('/')
def index():
    '''
    Default index view
    '''
    return "Hello, world!"

if __name__ == "__main__":
    # Setup some testing arguments
    vars = dict()
    args = sys.argv[1:]
    try:
        opts, args = getopt.getopt(args,
            "d")
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        # Enable debugging
        if opt == "-d":
            vars["debug"] = True
    # Fire up the application with vars set
    app.run(**vars)
