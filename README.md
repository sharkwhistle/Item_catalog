Musical Instrument Application

This application is a simple item catalog which can be used to create_engine
Musical Genres and add instruments to these genres.

Instruments can be specified with a name, brief description, price, and category.
Depending upon the category specified, the instrument will be displayed under
one of three columns; Percussion, String, or Wind.

Each genre, and each instrument can also be updated and/or deleted, demonstrating
full CRUD functionality.

This application was built using Flask and sqlalchemy and implements an oauth
authentication/verification system, which allows the user to securely sign-in
to the application using their Facebook or Google+ ID.

To launch the successfully launch the application you will need the following
dependencies:

Flask
SQLalchemy

You can install them via your console:

pip install Flask
pip install SQLalchemy

After you have installed these dependencies you can run the application by
typing the following commands into your console:

python lotsofitems.py
python finalproject.py

Once you have run these 2 commands, go to the following address in your
favorite web browser (Chrome is recommended):

http://localhost:5000

From here you will be prompted to login with your Facebook or Google+ ID. Once
you have sucessfully logged in, you can see several test genres that I created,
all of which contain sample instruments. You will also be able to create, edit,
and delete your own genres and instruments. When you are done CRUDing around,
simply click the Logout button at the top right side of the screen.

ENJOY!
