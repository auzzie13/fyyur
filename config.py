import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://xiwjcfeflubeeo:acfa853820919f6b906b77a29133c4827d544f0a5507004774ef7f7415fa50cf@ec2-107-20-104-234.compute-1.amazonaws.com:5432/dci1oq5rnhr5js'
