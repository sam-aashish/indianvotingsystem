import streamlit as st
import sqlite3

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('voter_database.db')

# Function to fetch voters from the database
def fetch_voter(voter_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Voter WHERE voter_id = ?', (voter_id,))
    voter = cursor.fetchone()
    conn.close()
    return voter

# Function to update vote status in the database
def update_vote_status(voter_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Voter SET voted = ? WHERE voter_id = ?', (1, voter_id))
    conn.commit()
    conn.close()

# Main function to create the portal
def main():
    st.title("Election Officer Portal")

    # Voter ID input field
    voter_id = st.text_input("Enter Voter ID", "")

    # Button to log vote
    if st.button("Log Vote"):
        if voter_id:
            # Fetch voter from the database
            voter = fetch_voter(voter_id)
            if voter:
                # Update vote status in the database
                update_vote_status(voter_id)
                st.success("Vote logged successfully for Voter ID: {}".format(voter_id))
            else:
                st.error("Voter ID not found in Central Voters List.")
        else:
            st.error("Please enter a Voter ID.")


    # Close button to close the application execution
    if st.button("Close"):
        st.stop()

if __name__ == "__main__":
    main()
