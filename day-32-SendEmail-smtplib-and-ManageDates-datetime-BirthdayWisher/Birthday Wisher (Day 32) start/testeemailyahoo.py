import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>E-mail teste</p>
    <p>Câmbio final.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Teste"
    msg['From'] = 'dcm29031990@yahoo.com'
    msg['To'] = 'dcm29031990@gmail.com'
    password = 'zaaktwnwyzonzybl'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()