class script(object):
    START_TXT = """ğ·ğ´ğ»ğ¾ {},
ğ¼ğ ğ½ğ°ğ¼ğ´ ğ¸ğ <a href=https://t.me/{}>{}</a>, ğ¸ ğ²ğ°ğ½ ğ¿ğğ¾ğğ¸ğ³ğ´ ğ¼ğ¾ğğ¸ğ´ğ, ğ¹ğğğ ğ°ğ³ğ³ ğ¼ğ´ ğğ¾ ğğ¾ğğ ğ¶ğğ¾ğğ¿ ğ°ğ½ğ³ ğ´ğ½ğ¹ğ¾ğ ğ"""

Â© Maintained By <a href=http://t.me/RAIHAN_TG>RAIHAN TG ğ®ğ³ [OÒÒlÎ¹É´e] #AFK</a>
    HELP_TXT = """ğ·ğ´ğ {}
ğ·ğ´ğğ´ ğ¸ğ ğğ·ğ´ ğ·ğ´ğ»ğ¿ ğµğ¾ğ ğ¼ğ ğ²ğ¾ğ¼ğ¼ğ°ğ½ğ³ğ."""
    ABOUT_TXT = """â¯ ğ¼ğ ğ½ğ°ğ¼ğ´: {}
â¯ ğ²ğğ´ğ°ğğ¾ğ: <a href=http://t.me/RAIHAN_TG>RAIHAN TG ğ®ğ³ [OÒÒlÎ¹É´e] #AFK</a>
â¯ ğ»ğ¸ğ±ğğ°ğğ: ğ¿ğğğ¾ğ¶ğğ°ğ¼
â¯ ğ»ğ°ğ½ğ¶ğğ°ğ¶ğ´: ğ¿ğğğ·ğ¾ğ½ ğ¹
â¯ ğ³ğ°ğğ° ğ±ğ°ğğ´: ğ¼ğ¾ğ½ğ¶ğ¾ ğ³ğ±
â¯ ğ±ğ¾ğ ğğ´ğğğ´ğ: ğ·ğ´ğğ¾ğºğ
â¯ ğ±ğğ¸ğ»ğ³ ğğğ°ğğğ: v1.0.1 [ ğ±ğ´ğğ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Thor is a open source project. 
- Source - https://t.me/ippokittumnokkininno>CLICK HERE</a>"""
<b>DEVS:</b>
- <a href=https://t.me/TeamThorMakers>Team Thor makers</a>"""

   MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Thor will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Thor should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Thor Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Thor supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specifed user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ğğ¾ğğ°ğ» ğµğ¸ğ»ğ´ğ: <code>{}</code>
â ğğ¾ğğ°ğ» ğğğ´ğğ: <code>{}</code>
â ğğ¾ğğ°ğ» ğ²ğ·ğ°ğğ: <code>{}</code>
â ğğğ´ğ³ ğğğ¾ğğ°ğ¶ğ´: <code>{}</code> ğ¼ğğ±
â ğµğğ´ğ´ ğğğ¾ğğ°ğ¶ğ´: <code>{}</code> ğ¼ğğ±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""



FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>ğ² NOTHING MUCH JUST SOME FUN THINGS</b>
tğğ ğğğğ ğ®ğğ: 
ğ£. /dice - Roll The Dice 
ğ¤. /Throw ğğ /Dart - ğ³ğ ğ¬ğºğğ¾ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot"""



SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

ğ Command

- /song [Song Name] - To Download Music

Usage
- working pm and groups""" Made by @M_STER_TECH_GROUP






COUNTRY_TEXT = """
ğ§ğ¾ğğ: <b><u>ğ¢ğğğğğğ ğ¨ğğ¿ğğğğºğğğğ</b></u>

ğ  ğ¬ğğ½ğğğ¾ ğ³ğ ğ¥ğğğ½ ğ¢ğğğğ½ ğ¨ğğ¿ğğğğºğğğğğ ğ®ğ¿ ğ ğğ ğ¢ğğğğğğğ¾ğ. ğ´ğğ¾ ğ³ğğğ ğ¬ğğ½ğğğ¾ ğ³ğ ğ¦ğ¾ğ ğ¢ğğğğğğ ğ¨ğğ¿ğğğğºğğğğğ

<b><u>ğ ğğºğğ»ğğ¾ ğ¢ğğğğºğğ½ğ</b></u>

â¢ /country [ğ¼ğğğğğğ ğğºğğ¾] - ğ´ğğ¾ ğ³ğğğ ğ¬ğ¾ğğğğ½ ğ³ğ ğ¦ğ¾ğ ğ¢ğğğğğğ ğ¨ğğ¿ğğğğºğğğğğ

ğ¤ğğºğğğğ¾ :- <code>/country India</code>
"""

