from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class OtpEmail(EmailMultiAlternatives):
    def __init__(self, to, otp):
        self.subject = "Login confirmation on Bebrus"
        self.html_content = render_to_string(
            'emails/otp.html',
            context={'otp': otp, 'site_name': 'Bebrus'})
        self.to = to
        super().__init__(self.subject, self.html_content, to=self.to)