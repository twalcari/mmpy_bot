#!/usr/bin/env python
from mmpy_bot.bot import Bot, PluginsManager
from mmpy_bot.mattermost import MattermostClient
from mmpy_bot.dispatcher import MessageDispatcher
import bot_settings


class LocalBot(Bot):

    def __init__(self):
        self._client = MattermostClient(
            bot_settings.BOT_URL, bot_settings.BOT_TEAM,
            bot_settings.BOT_LOGIN, bot_settings.BOT_PASSWORD,
            bot_settings.SSL_VERIFY
        )
        self._plugins = PluginsManager()
        self._plugins.init_plugins()
        self._dispatcher = MessageDispatcher(self._client, self._plugins)


def main():
    bot = LocalBot()
    bot.run()


if __name__ == '__main__':
    main()
