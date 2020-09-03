# formflask
Sample program on Python flask for modifying / accessing employee details in database

Here I'm using Visual Studio code 1.45.1 Version 2020

On Opening Folder location in terminal create virtual environment
pip install -m venv myenv

Now activate virtual environment by running "myenv\Scripts\activate" in terminal
check if your system meets requirements.txt
if not then execute 
python install -r requirements.txt

then run "python firstapp.py" to execute python flask app
default port is localhost:5000 which displays following app in browser

open localhost and do crud operations on details
There are error code 404 for errors, ID matches with already present

# Database sqlite
For database i'm using sqlalchemy if emp.db is removed then run previous steps
open other terminal of same location and activate myenv

run following codes in python

"from firstapp import db "     (firstapp is python name, db is already initialized in code with database)
"db.create_all()"
"from firstapp import Empl"      (Empl is table name in db)
"Empl.query.all()"
"db.session.commit()"

and exit() from python

Note: These python codes to be executed parallel while running localhost (python firstapp.py) as above
