import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

def get_app_instance():

    api_key = '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'

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = api_key

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    return api_instance

def send_email(fr, to, subject, body, is_html):
    
    api_instance = get_app_instance()

    sender = {'email': fr}
    to = [{'email' : to}]

    if is_html:
        text_content = None
        html_content = body
    else:
        text_content = body
        html_content = None

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, text_content=text_content, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi -> send_transac_email: %s\n" % e)

    return api_response

def send_text_email(fr, to, subject, body):
    return send_email(fr, to, subject, body, False)

def send_html_email(fr, to, subject, body):
    return send_email(fr, to, subject, body, True)

