"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb f1_data")
os.system("createdb f1_data")

model.connect_to_db(server.app)
model.db.create_all()

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

model.db.session.commit()