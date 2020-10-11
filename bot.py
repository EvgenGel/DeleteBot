import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os


vk_session = vk_api.VkApi(token=os.environ['BOT_TOKEN'])
long_poll = VkLongPoll(vk_session)
vk = vk_session.get_api()


def delete(message_id):
    vk.messages.delete(
        message_ids=message_id,
        delete_for_all=1
    )


def main():
    for event in long_poll.listen():
        try:
            if event.type != VkEventType.MESSAGE_NEW or not event.from_chat:
                continue
            delete(event.message_id)
        except Exception:
            continue


main()
