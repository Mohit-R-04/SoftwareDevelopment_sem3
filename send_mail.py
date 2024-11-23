import smtplib  # For connecting to Gmail's SMTP server
from email.mime.multipart import MIMEMultipart  # For creating a structured email
from email.mime.text import MIMEText  # For adding text to the email body
from datetime import datetime

def Send(status, email, name, id, date, doctor, problem):
    # Sender's Gmail address and the generated App Password
    sender_email = "multispecialityhospitalapollo@gmail.com"  # Replace with your Gmail address
    app_password = "ahby mrks qczd bkqx"  # Replace with your 16-character App Password

    # Recipient email address and email content
    receiver_email = email  # Replace with the recipient's email address
    subject = f"Appointment Confirmation - Patient: {name}"  # The subject line of the email

    # HTML body for better email formatting
    body = f"""
    <html>
        <body>
            <p>Dear {name},</p>
            <p> {status} </p>
            <p><b>Appointment Details:</b></p>
            <ul>
                <li>Appointment ID: {id}</li>
                <li>Date: {date}</li>
                <li>Doctor: {doctor}</li>
                <li>Reason for Appointment: {problem}</li>
            </ul>
            <p>For any queries, please contact us at <a href="mailto:multispecialityhospitalapollo@gmail.com">multispecialityhospitalapollo@gmail.com</a>.</p>
            <p>Here for Your Health,<br>Apollo Hospitals 😊</p>
        </body>
    </html>
    """

    # Step 1: Create the Email Message Structure
    message = MIMEMultipart("alternative")  # Using "alternative" for both plain text and HTML options
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach both plain text and HTML versions
    text_version = f"""
    Dear {name},

    Your appointment has been booked successfully!

    Appointment Details:
    - Appointment ID: {id}
    - Date: {date}
    - Doctor: {doctor}
    - Reason for Appointment: {problem}

    For any queries, please contact us at multispecialityhospitalapollo@gmail.com.

    Here for Your Health,
    Apollo Hospitals 😊
    """
    # Attach the body of the email as both plain text and HTML
    message.attach(MIMEText(text_version, "plain"))
    message.attach(MIMEText(body, "html"))

    # Step 2: Connect to Gmail's SMTP Server and Send the Email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendCancellation(email, name, patient_id, appointment_id):
    # Sender's Gmail address and the generated App Password
    sender_email = "multispecialityhospitalapollo@gmail.com"  # Replace with your Gmail address
    app_password = "ahby mrks qczd bkqx"  # Replace with your 16-character App Password

    # Recipient email address and email content
    receiver_email = email
    subject = f"Appointment Cancellation - Patient: {name}"

    # HTML body for better email formatting
    body = f"""
    <html>
        <body>
            <p>Dear {name},</p>
            <p>We regret to inform you that your appointment has been successfully <b>canceled</b>.</p>
            <p><b>Appointment Details:</b></p>
            <ul>
                <li>Patient ID: {patient_id}</li>
                <li>Appointment ID: {appointment_id}</li>
            </ul>
            <p>If you have any questions or would like to reschedule, please contact us at <a href="mailto:multispecialityhospitalapollo@gmail.com">multispecialityhospitalapollo@gmail.com</a>.</p>
            <p>Regards,<br>Apollo Hospitals 😊</p>
        </body>
    </html>
    """

    # Plain text version
    text_version = f"""
    Dear {name},

    We regret to inform you that your appointment has been successfully canceled.

    Appointment Details:
    - Patient ID: {patient_id}
    - Appointment ID: {appointment_id}

    If you have any questions or would like to reschedule, please contact us at multispecialityhospitalapollo@gmail.com.

    Regards,
    Apollo Hospitals 😊
    """

    # Create the email message structure
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach both plain text and HTML versions
    message.attach(MIMEText(text_version, "plain"))
    message.attach(MIMEText(body, "html"))

    # Send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def SendPaymentConfirmation(email, name, patient_id, appointment_id, amount):
    # Sender's Gmail address and the generated App Password
    sender_email = "multispecialityhospitalapollo@gmail.com"  # Replace with your Gmail address
    app_password = "ahby mrks qczd bkqx"  # Replace with your 16-character App Password

    # Recipient email address and email content
    receiver_email = email
    subject = f"Payment Confirmation - Patient: {name}"

    # HTML body for better email formatting
    body = f"""
    <html>
        <body>
            <p>Dear {name},</p>
            <p>We are pleased to inform you that the payment of <b>₹{amount}</b> for your appointment has been successfully processed.</p>
            <p><b>Payment and Appointment Details:</b></p>
            <ul>
                <li>Patient ID: {patient_id}</li>
                <li>Appointment ID: {appointment_id}</li>
                <li>Amount Paid: ₹{amount}</li>
            </ul>
            <p>If you have any questions, please contact us at <a href="mailto:multispecialityhospitalapollo@gmail.com">multispecialityhospitalapollo@gmail.com</a>.</p>
            <p>Thank you for choosing Apollo Hospitals!<br>Apollo Hospitals 😊</p>
        </body>
    </html>
    """

    # Plain text version
    text_version = f"""
    Dear {name},

    We are pleased to inform you that the payment of ₹{amount} for your appointment has been successfully processed.

    Payment and Appointment Details:
    - Patient ID: {patient_id}
    - Appointment ID: {appointment_id}
    - Amount Paid: ₹{amount}

    If you have any questions, please contact us at multispecialityhospitalapollo@gmail.com.

    Thank you for choosing Apollo Hospitals!
    Apollo Hospitals 😊
    """

    # Create the email message structure
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Attach both plain text and HTML versions
    message.attach(MIMEText(text_version, "plain"))
    message.attach(MIMEText(body, "html"))

    # Send the email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False