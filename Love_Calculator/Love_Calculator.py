import streamlit as st
from sqlalchemy import create_engine

# Streamlit title and input
st.title("Love Calculator")
st.write("The Love Calculator is calculating your score...")

name11 = st.text_input("What is your name?")
name22 = st.text_input("What is their name?")

if name11 and name22:
    c_n = name11 + name22
    l_n = c_n.lower()
    t = l_n.count("t")
    r = l_n.count("r")
    u = l_n.count("u")
    e = l_n.count("e")

    f_d = t + r + u + e

    l = l_n.count("l")
    o = l_n.count("o")
    v = l_n.count("v")
    e = l_n.count("e")

    l_d = l + o + v + e

    ls = int(str(f_d) + str(l_d))

    if ls < 10 or ls > 90:
        st.write(f"Your score is {ls}, you go together like coke and mentos.")
    elif 40 < ls <= 50:
        st.write(f"Your score is {ls}, you are alright together.")
    else:
        st.write(f"Your score is {ls}")

    # Database connection parameters
    user = 'uvf7gqa0ml1a9ro4v2ny'        # PostgreSQL username
    password = 'CYQeHfQo0ORJ6JqObFIQVHxmHj3IZJ'  # PostgreSQL password
    host = 'bs1qllt0uka3vmlcy9d8-postgresql.services.clever-cloud.com'  # PostgreSQL host
    port = '5432'               # PostgreSQL port
    database = 'bs1qllt0uka3vmlcy9d8'  # PostgreSQL database name

    # Creating an engine to connect to PostgreSQL
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

    # Insert values into the database using parameterized query
    from sqlalchemy.sql import text

    query = text("INSERT INTO project1157 (name1, name2) VALUES (:name1, :name2);")  # Use placeholders for parameters
    connection = engine.connect()
    connection.execute(query, {"name1": name11, "name2": name22})  # Pass parameters using a dictionary

    # Commit the transaction
    connection.commit()
    connection.close()
