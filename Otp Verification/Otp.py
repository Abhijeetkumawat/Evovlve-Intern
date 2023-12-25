import random
import string
import smtplib

def generate_otp():
    digits = string.digits
    otp = ''.join(random.choice(digits) for i in range(6))
    return otp


# def send_otp_email(email, otp):
#     from_email = 'your Gmail'  # Replace with your Gmail email address
#     from_password = 'Your Password'  # Replace with your Gmail password

#     subject = 'OTP Verification'
#     message = f'Your OTP for verification is: {otp}'
def send_otp_email(email, otp):
    from_email = 'kumawatsudama2002@gmail.com'  # Replace with your Gmail email address
    from_password = 'Sudama@123'  # Replace with your Gmail password

    subject = 'OTP Verification'
    message = f'Your OTP for verification is: {otp}'

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(from_email, from_password)

        server.sendmail(from_email, email, f'Subject: {subject}\n\n{message}')
        print('OTP sent successfully!')

        server.quit()
    except Exception as e:
        print(f"Error: {e}")

def main():
    email = input('Enter your email address: ')
    otp = generate_otp()
    print(f"Generated OTP: {otp}")

    send_otp_email(email, otp)

    user_otp_input = input('Enter the OTP you received: ')

    if user_otp_input == otp:
        print('OTP verification successful. Account created!')
    else:
        print('Invalid OTP. Verification failed.')

if __name__ == "__main__":
    main()