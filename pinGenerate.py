import smtplib
import random

# Generate 6-digit PIN
pin = random.randint(100000, 999999)

sender = "aarthi.2205@gmail.com"
password = "rppn rrrv raqn czdi"   # Gmail App Password
receiver = "aarthi.152529@gmail.com"

# Email content
message = f"Subject: Your PIN\n\nYour PIN is {pin}"

# Send email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()

print("PIN sent to mail!")

# -------- PIN Verification -------- #

attempts = 3   # user can try only 3 times

while attempts > 0:
    user_input = input("Enter the PIN you received: ")

    if user_input == str(pin):
        print("Correct PIN! Access Granted.")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN! Attempts left: {attempts}")

        if attempts == 0:
            print("You used all attempts. Access Denied!")
#----------------------------------------------------------------------------------------------#
import smtplib
import random

# Generate 3 PINs and save them
pins = [random.randint(100000, 999999) for _ in range(3)]

sender = "aarthi.2205@gmail.com"
password = "rppn rrrv raqn czdi"   # Gmail App Password
receiver = "aarthi.152529@gmail.com"

# Email content for all 3 PINs
message = f"Subject: Your 3 PINs\n\nYour PINs are:\n{pins[0]}\n{pins[1]}\n{pins[2]}"

# --- Function to send email ---
def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()
    print("Mail sent again!")

# Send the mail first time
send_mail()

attempts = 3  # user gets only 3 chances

while attempts > 0:
    user_input = input("Enter any one of the 3 PINs you received: ")

    if user_input in [str(p) for p in pins]:
        print("Correct PIN! Access Granted.")
        break
    else:
        attempts -= 1
        print(f"Wrong PIN! Attempts left: {attempts}")

        # Send mail again if wrong PIN
        if attempts > 0:
            print("Sending mail again...")
            send_mail()

        if attempts == 0:
            print("You used all attempts. Access Denied!")
