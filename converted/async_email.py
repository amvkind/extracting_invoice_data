import asyncio
from aioimaplib import aioimaplib


@asyncio.coroutine
def check_mailbox(host, user, password):
    imap_client = aioimaplib.IMAP4_SSL(host=host)
    yield from imap_client.wait_hello_from_server()

    yield from imap_client.login(user, password)

    res, data = yield from imap_client.select()
    print('there is %s messages INBOX' % data[0])

    yield from imap_client.logout()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_mailbox('my.imap.server', 'user', 'pass'))