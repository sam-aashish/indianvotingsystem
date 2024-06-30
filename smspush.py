from twilio.rest import Client
import sqlite3

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect('voter_database.db')

# Function to fetch voters who have cast their votes
def fetch_voters_with_votes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Voter WHERE voted = ?', (1,))
    voters = cursor.fetchall()
    conn.close()
    return voters

# Function to send SMS notification
def send_sms_notification(voter_name, voter_mobile_number):
    # Twilio credentials
    account_sid = 'ACc39c3f4e6d8b68303c8fb021f76745cb'
    auth_token = 'b0eb000b8aa8789952c77d4af39e4bcf'
    twilio_sender = '+17069204094'

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Send SMS message
    message = client.messages.create(
        body=f"Dear {voter_name}, your vote has been casted. Please reply with 1 if you have not casted your vote.",
        from_=twilio_sender,
        to=voter_mobile_number
    )

    print("SMS notification sent to", voter_mobile_number)

# Function to send SMS notifications to all voters who have cast their votes
def send_verification_sms():
    # Fetch voters who have cast their votes
    voters_with_votes = fetch_voters_with_votes()

    # Send SMS notifications to voters
    for voter in voters_with_votes:
        voter_mobile_number = voter[3]  # Assuming mobile number is stored in the fourth column
        voter_name = voter[4]
        send_sms_notification(voter_name, voter_mobile_number)
