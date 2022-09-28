# 账号认证列表，多账号一起开的时候，可在列表中追加
authorization_list = ["你的账号认证id"]

# 账号认证,从指定频道text_chanel_id 随机获取聊天内容时使用
authorization = "你的账号认证id"

# 获取聊天信息的频道id
text_channel_id = "聊天信息的频道id"

# 需要自动聊天的频道id，同时刷多个服务器，可在列表中追加
channel_id_list = ["自动聊天的频道id"]

# Ture：脚本模式， False：从指定频道text_chanel_id 随机获取聊天内容
script_mode_flg = True

# 聊天脚本，script_mode_flg=Ture时使用
script_text_list = [
    "肝",
    "加油",
    "肝啊",
    "肝肝更健康",
    "只能肝",
    "目标10级",
    "升级好慢",
    "拿白",
    "继续努力",
]

# 信息发送的间隔时间
chat_sleep_time_min = 50
chat_sleep_time_max = 60

# 多频道一起刷的间隔时间
channel_sleep_time_min = 10
channel_sleep_time_max = 20

# 多账号一起刷的间隔时间
ac_sleep_time_min = 10
ac_sleep_time_max = 20


# 是否检测mod说话
check_mod_flg = True

# dc工会id，check_mod_flg=True时需要设置
guild_id = "工会id"

# mod角色列表（包括mod，管理员等），check_mod_flg=True时需要设置
mod_role_id_list = ["role角色id"]
