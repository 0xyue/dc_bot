# -*- coding: utf-8 -*-
# twitter: https://twitter.com/0xyue_web3

import requests
import json
import random
import time
import data


def check_mod(channel_id):
    print("check_mod")
    guild_id = data.guild_id
    mod_role_id_list = data.mod_role_id_list

    headr = {
        "Authorization": data.authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    get_message_url = "https://discord.com/api/v9/channels/{}/messages?limit=50".format(
        channel_id
    )
    message_res = requests.get(url=get_message_url, headers=headr)
    message_content_list = json.loads(message_res.content)

    # with open("messages.json", "w") as file:
    #     json.dump(message_content, file)

    for message_content in message_content_list:

        author_id = message_content["author"]["id"]
        # author_name = message_content["author"]["username"]

        get_profile_url = "https://discord.com/api/v9/users/{}/profile?with_mutual_guilds=false&guild_id={}".format(
            author_id, guild_id
        )
        print(f"get_profile_url: {get_profile_url}")
        profile_res = requests.get(url=get_profile_url, headers=headr)
        profile_content = json.loads(profile_res.content)

        content = message_content["content"]
        username = profile_content["user"]["username"]
        user_roles = profile_content["guild_member"]["roles"]

        # with open("profile_{}.json".format(username), "w") as file:
        #     json.dump(profile_content, file)

        print(f"username: {username}")
        print(f"user_roles: {user_roles}")
        print(f"content: {content}")
        for role in user_roles:
            if role in mod_role_id_list:
                print(f"mod({username}) 在说话，暂时停止！ 说话内容：{content}")
                return True

    return False


def get_content():
    if data.script_mode_flg:
        return random.choice(data.script_text_list)
    else:
        return get_content_from_channel()


def get_content_from_channel():
    channel_id = data.text_channel_id
    headr = {
        "Authorization": data.authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    url = "https://discord.com/api/v9/channels/{}/messages?limit=100".format(channel_id)
    res = requests.get(url=url, headers=headr)
    result = json.loads(res.content)

    result_list = []
    for context in result:
        if ("<") not in context["content"]:
            if ("@") not in context["content"]:
                if ("http") not in context["content"]:
                    if ("?") not in context["content"]:
                        result_list.append(context["content"])
    return random.choice(result_list)


def chat():

    channel_list = data.channel_id_list
    authorization_list = data.authorization_list
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        for channel_id in channel_list:
            if data.check_mod_flg and check_mod(channel_id):
                continue

            msg = {
                "content": get_content(),
                "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
                "tts": False,
            }
            url = "https://discord.com/api/v9/channels/{}/messages".format(channel_id)
            try:
                res = requests.post(url=url, headers=header, data=json.dumps(msg))
                print(res.content)
            except Exception:
                print(Exception)
                continue

            if len(channel_list) > 1:
                channel_sleep_time = random.randrange(
                    data.channel_sleep_time_min, data.channel_sleep_time_max
                )
                print(f"channel_sleep_time : {channel_sleep_time}")
                time.sleep(channel_sleep_time)

        # 多账号一起刷的时候，开启间隔时间
        if len(authorization_list) > 1:
            ac_sleep_time = random.randrange(
                data.ac_sleep_time_min, data.ac_sleep_time_max
            )
            print(f"ac_sleep_time : {ac_sleep_time}")
            time.sleep(ac_sleep_time)


if __name__ == "__main__":
    while True:
        try:
            print("start")
            chat()
            # 机器人发送消息的间隔时间。
            chat_sleeptime = random.randrange(
                data.chat_sleep_time_min, data.chat_sleep_time_max
            )
            print(f"chat sleeptime:{chat_sleeptime}")
            time.sleep(chat_sleeptime)

        except:
            pass
