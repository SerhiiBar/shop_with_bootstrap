import aiosmtplib
from email.message import EmailMessage
import asyncio


async def send_email_async(message):
    sender = "testformassege@gmail.com"
    password = 'rlezrhekthsrclex'

    try:
        smtp = aiosmtplib.SMTP()
        await smtp.connect(hostname="smtp.gmail.com", port=587, start_tls=False)
        await smtp.starttls()
        await smtp.login(sender, password)
        await smtp.send_message(message)
        await smtp.quit()
    except Exception as e:
        print('Error sending email:', e)


async def send_my_message(order, msg, address):
    message = EmailMessage()
    message['Subject'] = f'Your {order} in PodShop'
    message['From'] = 'PodShop'
    message['To'] = address
    message.set_content(msg)

    await send_email_async(message)


def start_send_my_message(order, msg, address):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(send_my_message(order, msg, address))
    except Exception as e:
        print('Error sending email:', e)
    finally:
        loop.close()
