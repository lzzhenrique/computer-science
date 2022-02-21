import smtplib
import ssl

email_reseter = "password_reset.com"
password_email_reseter = "myverysafepassword"


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def reset_password(self):
        meu_mailer = Mailer(email_reseter, password_email_reseter, self.email)
        meu_mailer.send_email("Reset your password", "Como resetar sua senha:")


class Mailer:
    def __init__(self, from_email, from_password, to_email):
        self.from_email = from_email
        self.from_password = from_password,
        self.to_email = to_email

    def send_email(self, subject, message):
        body = f"Subject:{subject} \n\n{message}".encode("utf-8")
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, context=context
        ) as server:
            server.login(self.from_email, self.from_password)
            try:
                server.sendmail(self.from_email, self.email, body)
            except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
                raise ValueError


new_user = User("José Mourinho", "specialone@rome.com", "5pec1al0ne")

new_user.reset_password()
