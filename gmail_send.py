import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # SMTP server details for Outlook
        SMTP_SERVER = 'smtp.hostname of server'  # Enter the hostname of your SMTP Server Here
        SMTP_PORT = 587    # Port Number

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
        print(f"An unexpected error occurred: {str(e)}")    # Print out the error if any occured



# Example usage
if __name__ == "__main__":
    sender_email = 'sender@example.com'   # Enter the email of the sender
    sender_password = 'Sender Password'   #Enter your password 
    recipient_email = 'recipient@example.com'  #Enter the Email of the recipient
    subject = 'Test Subject'
    body = 'This is a test email.'

    send_email(sender_email, sender_password, recipient_email, subject, body)

