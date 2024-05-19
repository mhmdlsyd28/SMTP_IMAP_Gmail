import imaplib
import email

def receive_email(email_address, password):
    try:

        imap_server= 'hostname of imap server'  # Enter the hostname of the IMAP Server
        imap_port = 993  # Enter the port number of service
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)

        # Log in to the IMAP server
        mail.login(email_address, password)

        # Select the mailbox you want to use (in this case, the inbox)
        mail.select('inbox')

        # Search for all emails in the inbox
        result, data = mail.search(None, 'ALL')

        # Get the list of email IDs
        email_ids = data[0].split()

        # Fetch the latest email
        latest_email_id = email_ids[-1]
        result, data = mail.fetch(latest_email_id, '(RFC822)')

        # Parse the raw email content
        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        # Print the email details
        print("From:", msg['From'])
        print("Subject:", msg['Subject'])
        print("Body:", get_body(msg))

        # Close the IMAP server connection
        mail.logout()

    except Exception as e:
        print(f"Failed to fetch email: {e}")


def get_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == 'text/plain':
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()


# Example usage
if __name__ == "__main__":
    recipient_email = 'recipient@example.com'   # Enter your email 
    recipient_password = 'password'   #Enter the password of the receiver 

    # Call the receive_email function
    receive_email(email_address, password)
