import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import os


vk_session = vk_api.VkApi(token='0bad68d6e9e7a810355fd51406f2c1f0c383fd551e7213f1060b11893ca0e6c897add2abb10563449e8ec')
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
