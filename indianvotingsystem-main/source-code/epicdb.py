import streamlit as st
import sqlite3

# Function to create the database and table
def create_database():
    conn = sqlite3.connect('voter_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Voter (
            id INTEGER PRIMARY KEY,
            voter_id TEXT,
            aadhar_number TEXT,
            mobile_number TEXT,
            name TEXT,
            voted BOOLEAN DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Function to insert a new voter into the database
def insert_voter(voter_id, aadhar_number, mobile_number, name):
    conn = sqlite3.connect('voter_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Voter (voter_id, aadhar_number, mobile_number, name)
        VALUES (?, ?, ?, ?)
    ''', (voter_id, aadhar_number, mobile_number, name))
    conn.commit()
    conn.close()

# Streamlit app
def main():
    st.title("Voter Registration")

    # Input fields
    voter_id = st.text_input("Voter ID")
    aadhar_number = st.text_input("Aadhar Number")
    mobile_number = st.text_input("Mobile Number")
    name = st.text_input("Name")

    if st.button("Register Voter"):
        if voter_id and aadhar_number and mobile_number and name:
            insert_voter(voter_id, aadhar_number, mobile_number, name)
            st.success("Voter registered successfully!")
        else:
            st.error("Please fill out all fields.")

    if st.button("Show All Voters"):
        conn = sqlite3.connect('voter_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Voter')
        voters = cursor.fetchall()
        conn.close()

        if voters:
            st.write("All Voters:")
            import pandas as pd
            df = pd.DataFrame(voters, columns=['ID', 'Voter ID', 'Aadhar Number', 'Mobile Number', 'Name', 'Voted'])
            st.dataframe(df)
        else:
            st.write("No voters found.")

    if st.button("Close"):
        st.stop()

if __name__ == "__main__":
    create_database()
    main()
