from email.quoprimime import body_check
from email_sender import *
from days_to_go_calc import *

def send_daily_email(d1, d2):
    fr = "daystogo@weekendsoft.org"
    to = "vivek.kant@gmail.com"
    subject = "Days to go !!!"

    body = """
        <h1>Days to leave: ~d1~</h1><br/>
        <h1>Days to decide: ~d2~</h1><br/>
    """

    body = body.replace('~d1~', d1)
    body = body.replace('~d2~', d2)

    print(body)

    response = send_email(fr, to, subject, body, True)

    return response

d1 = four_years_to_go()
d2 = days_to_decide()

p1 = (d1 * 100 * 1.0)/365
p2 = (d2 * 100 * 1.0)/365

s1 = str(d1) + ' (' + '{:.2f}'.format(p1) + '%)'
s2 = str(d2) + ' (' + '{:.2f}'.format(p2) + '%)'

response = send_daily_email(s1, s2)

print(response)