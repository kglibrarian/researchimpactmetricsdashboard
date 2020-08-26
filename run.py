
#################################################
# Import the app from the init file
#################################################

from application import app

#################################################
# Grab the app and run it
#################################################

if __name__ == "__main__":
    app.debug = True
    app.run()

