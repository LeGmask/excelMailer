from tqdm import tqdm

from src.config import Config
from src.mailsmanager import MailsManager
from src.excelManager import ExcelManager

config = Config('config.json')
mails = MailsManager(config)
data = ExcelManager(config).data

print("Generating emails...")
for index, row in tqdm(data.iterrows()):
    mails.add_email(row)

print("Sending emails...")
mails.send_emails()

print("Done!")
