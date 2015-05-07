import weechat
from yapbl import PushBullet

apikey = ""

p = PushBullet(apikey)

weechat.register("pushbullet", "kekskurse", "1.0", "GPL3", "Test 
Skript", "", "")
weechat.prnt("", "Hallo, von einem python Skript!")


def notify_show(data, bufferp, uber_empty, tagsn, isdisplayed, 
ishilight, prefix, message):
    if(ishilight):
        buffer = (weechat.buffer_get_string(bufferp, "short_name") or 
weechat.buffer_get_string(bufferp, "name"))
        p.push_note('Weechat Hilight', buffer+": "+message)
    elif(weechat.buffer_get_string(bufferp, "localvar_type") == 
"private"):
        buffer = (weechat.buffer_get_string(bufferp, "short_name") or 
weechat.buffer_get_string(bufferp, "name"))
        p.push_note('Weechat MSG from '+buffer, buffer+": "+message)
    return weechat.WEECHAT_RC_OK

weechat.hook_print("", "irc_privmsg", "", 1, "notify_show", "")
