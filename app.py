import streamlit as st
import mysql.connector

# ------------------ DATABASE CONNECTION ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # 👈 change this
    database="event_db"
)
cursor = conn.cursor()

# ------------------ TITLE ------------------
st.title("🎉 Event Management System")

menu = st.sidebar.selectbox("Menu", [
    "Add Event",
    "Register Participant",
    "Register for Event",
    "View Registrations"
])

# ------------------ ADD EVENT ------------------
if menu == "Add Event":
    st.subheader("Add New Event")

    name = st.text_input("Event Name")
    date = st.date_input("Event Date")
    location = st.text_input("Location")
    organizer = st.text_input("Organizer")

    if st.button("Add Event"):
        cursor.execute(
            "INSERT INTO Events (event_name, date, location, organizer) VALUES (%s, %s, %s, %s)",
            (name, date, location, organizer)
        )
        conn.commit()
        st.success("✅ Event added successfully!")

# ------------------ REGISTER PARTICIPANT ------------------
elif menu == "Register Participant":
    st.subheader("Register Participant")

    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    if st.button("Register"):
        cursor.execute(
            "INSERT INTO Participants (name, email, phone) VALUES (%s, %s, %s)",
            (name, email, phone)
        )
        conn.commit()
        st.success("✅ Participant registered!")

# ------------------ REGISTER FOR EVENT ------------------
elif menu == "Register for Event":
    st.subheader("Register for Event")

    cursor.execute("SELECT event_id, event_name FROM Events")
    events = cursor.fetchall()
    event_dict = {e[1]: e[0] for e in events}

    cursor.execute("SELECT participant_id, name FROM Participants")
    participants = cursor.fetchall()
    part_dict = {p[1]: p[0] for p in participants}

    selected_event = st.selectbox("Select Event", list(event_dict.keys()))
    selected_participant = st.selectbox("Select Participant", list(part_dict.keys()))

    if st.button("Register"):
        cursor.execute(
            "INSERT INTO Registrations (event_id, participant_id, reg_date) VALUES (%s, %s, CURDATE())",
            (event_dict[selected_event], part_dict[selected_participant])
        )
        conn.commit()
        st.success("✅ Registered successfully!")

# ------------------ VIEW REGISTRATIONS ------------------
elif menu == "View Registrations":
    st.subheader("All Registrations")

    cursor.execute("""
        SELECT p.name, e.event_name, r.reg_date
        FROM Registrations rs
        JOIN Participants p ON r.participant_id = p.participant_id
        JOIN Events e ON r.event_id = e.event_id
    """)
    data = cursor.fetchall()

    for row in data:
        st.write(f"👤 {row[0]} | 🎉 {row[1]} | 📅 {row[2]}")