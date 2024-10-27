
from flask_sqlalchemy import SQLAlchemy  #connection to database (db)
from flask_migrate import Migrate       # migrate used for applying our schema changes to the db
from .models.base import Base           # Base class b'coz to initialize our db

db = SQLAlchemy(model_class=Base)      #db is a variable, an instance of SQL Alchemy's database object. sqlalchamey is a class, follow docum n put baseclass
migrate = Migrate()                    #instance for migrate makes for us