import streamlit as st

st.title("Love Calculator")

st.write("The Love Calculator is calculating your score...")

name1 = st.text_input("What is your name?")
name2 = st.text_input("What is their name?❤️")

if name1 and name2:
    c_n = name1 + name2
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
        st.write(f"Your score is {ls}.")
