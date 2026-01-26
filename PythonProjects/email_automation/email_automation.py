import smtplib
import json
import csv
import email
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import time

CONFIG_FILE = 'config.json'
TEMPLATES_FILE = 'email_templates.json'
LOG_FILE = 'email_log.json'


# Default templates
DEFAULT_TEMPLATES = {
    "job_followup": {
        "name": "Job Application Follow-up",
        "subject": "Following up on my application for {{position}}",
        "body": """Hi {{name}},

I hope this email finds you well. I wanted to follow up on my job application for the {{position}} role at {{company}}.

I remain very interested in this opportunity and would love to discuss how my skills and experience align with your team's needs.

Would you be available for a brief call this week?

Best regards,
{{sender_name}}"""
    },
    "invoice_reminder": {
        "name": "Invoice Reminder",
        "subject": "Payment Reminder - Invoice #{{invoice_number}}",
        "body": """Dear {{name}},

This is a friendly reminder that invoice #{{invoice_number}} for {{amount}} is due on {{due_date}}.

Please let me know if you have any questions.

Best regards,
{{sender_name}}"""
    }
}