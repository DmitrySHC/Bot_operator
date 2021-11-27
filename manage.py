import sys
from Bot_operator.Facebook.fb_bot import main as fb_bot
from Bot_operator.Skype.skype_bot import main as skype_bot
from Bot_operator.Telegram.tg_bot import main as tg_bot
from Bot_operator.VK.vk_bot import main as vk_bot


'''
Choose bot type.
Enter in command line: 
'python manage.py fb' to run facebook bot
'python manage.py skype' to run skype bot
'python manage.py tg' to run telegram bot
'python manage.py vk' to run vkontakte bot
'''


def main():
    commands = {
        'fb': fb_bot,
        'skype': skype_bot,
        'tg': tg_bot,
        'vk': vk_bot,
    }
    bot_type = sys.argv[1]
    commands[bot_type]()


if __name__ == '__main__':
    main()
