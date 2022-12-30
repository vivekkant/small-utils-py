from email.quoprimime import body_check
from email_sender import *
from days_to_go_calc import *

def send_daily_email(d1a, d1b, d2a, d2b):
    fr = "daystogo@weekendsoft.org"
    to = "vivek.kant@gmail.com"
    subject = "Days to go !!!"

    body = """
        <h1>Option 1: ~d2a~ Days to decide, ~d2b~ Days to leave</h1><br/>
        <h1>Option 2: ~d1a~ Days to decide, ~d1b~ Days to leave</h1><br/>
    """

    body = body.replace('~d1a~', d1a)
    body = body.replace('~d1b~', d1b)
    body = body.replace('~d2a~', d2a)
    body = body.replace('~d2b~', d2b)

    print(body)

    response = send_email(fr, to, subject, body, True)

    return response

d1a, d1b = days_option_one()
d2a, d2b = days_option_two()

response = send_daily_email(str(d1a), str(d1b), str(d2a), str(d2b))

print(response)