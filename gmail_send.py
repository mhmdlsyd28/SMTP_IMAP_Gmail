import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import imaplib
import email

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # SMTP server details for Outlook
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587

        # Set up the SMTP server and start TLS for security
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()

        # Log in to the SMTP server
        server.login(sender_email, sender_password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.send_message(msg)
        print("Email sent successfully!")

        # Close the SMTP server connection
        server.quit()


        # Error Handling
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def receive_email(recipient_email, recipient_password):
    try:
        # Connect to the IMAP server
        imap_server = 'imap.gmail.com'
        imap_port = 993
        mail = imaplib.IMAP4_SSL(imap_server, imap_port)

        # Log in to the IMAP server
        mail.login(recipient_email, recipient_password)

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
        print("\n------For the Receiver-------")
        print("New Email!! \n")
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
    sender_email = 'eng.mhmdlsyd28@gmail.com'
    sender_password = 'hwgi tucz ttfv iaij'
    recipient_email = 'medoelsayed045@gmail.com'
    recipient_password = 'weex zjai huae rwot'
    subject = 'Test Subject'
    body = 'This is a test email.'

    send_email(sender_email, sender_password, recipient_email, subject, body)


    # Call the receive_email function
    receive_email(recipient_email, recipient_password)
