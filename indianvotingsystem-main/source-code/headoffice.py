import streamlit as st
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
from smspush import send_verification_sms, connect_db

# Function to fetch the number of votes cast
def fetch_votes_cast():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Voter WHERE voted = 1')
    votes_cast = cursor.fetchone()[0]
    conn.close()
    return votes_cast

# Function to fetch the total number of registered voters
def fetch_total_registered_voters():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Voter')
    total_voters = cursor.fetchone()[0]
    conn.close()
    return total_voters

# Main function to create the portal
def main():
    st.title("Vote Count Portal")

    # Fetch and display the number of votes cast
    votes_cast = fetch_votes_cast()
    st.write(f"Number of votes cast: {votes_cast}")

    # Fetch and display the total number of registered voters
    total_voters = fetch_total_registered_voters()
    st.write(f"Total number of registered voters: {total_voters}")

    # Pie chart to visualize votes cast vs. registered voters
    if total_voters > 0:
        voted_percentage = (votes_cast / total_voters) * 100
        not_voted_percentage = 100 - voted_percentage

        labels = ['Voted', 'Not Voted']
        sizes = [voted_percentage, not_voted_percentage]
        colors = ['#1f77b4', '#ff7f0e']
        explode = (0.1, 0)  # explode the 1st slice (Voted)

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Center circle to make it look like a donut chart
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig.gca().add_artist(centre_circle)

        plt.tight_layout()

        # Display the chart using Streamlit
        st.pyplot(fig)

    # Button to send verification SMS
    if st.button("Send Verification SMS"):
        send_verification_sms()
        st.success("Verification SMS sent to all voters who have cast their votes.")

    # Close button to close the application execution
    if st.button("Close"):
        st.stop()

if __name__ == "__main__":
    main()
