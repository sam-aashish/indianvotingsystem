## Displays data from VoterDB at any instance
import sqlite3

# Function to fetch all voters from the database
def fetch_voters():
    # Connect to SQLite database
    conn = sqlite3.connect('voter_database.db')
    cursor = conn.cursor()

    # Fetch all voters
    cursor.execute('SELECT * FROM Voter')
    voters = cursor.fetchall()

    # Close connection and return results
    conn.close()
    return voters

# Call fetch_voters() function to retrieve voters from the database
voters = fetch_voters()

# Display the contents of the database
for voter in voters:
    print(voter)
