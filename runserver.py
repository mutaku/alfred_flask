# runserver.py

from alfred import app
import getopt
import sys

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
