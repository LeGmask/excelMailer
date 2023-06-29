from mailjet_rest import Client

from src.template import TemplateManager


class MailsManager:
    def __init__(self, config):
        self.template = TemplateManager(config)
        self.config = config
        self.mailjet = Client(auth=(config.get(['MAILJET', 'API_KEY']), config.get(['MAILJET', 'API_SECRET'])),
                              version='v3.1')
        self.mails = []

    # def send

    def add_email(self, data):
        self.mails.append({
            "From": {
                "Email": self.config.get(['MAILJET', 'sender']),
                "Name": self.config.get(['MAILJET', 'sender_name']),
            },
            "To": [{
                "Email": data[self.config.get(['EMAIL', 'column_to'])]
            }],
            "Subject": self.config.get(['EMAIL', 'subject']),
            "TextPart": self.template.populate_template(data),
            "CustomCampaign": self.config.get(['MAILJET', 'campaign']),
        })

    def send_emails(self):
        data = {
            'Messages': self.mails
        }
        result = self.mailjet.send.create(data=data)

        if result.status_code == 200:
            print("Emails sent!")
        else:
            print("Error sending emails!")

        print(result.json())
