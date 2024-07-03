import utils.cm
import utils.ch
import utils.regex
import utils.locale

import random
import re

handler_list = []

translations = {
    'prefs': {
        'en': [
            "Yuki said",
            "Our Government thinks",
            "Cats selected",
            "I was forced to say",
            "Ryijik meowed",
            "You'd like to hear"
        ],
        'ru': [
            "Звёзды говорят",
            "Юки сказала",
            "Правительство нашептало",
            "Карты таро передали",
            "Котики выбрали",
            "Меня заставили сказать",
            "Осинка мяукнула",
            "Я знаю, что ты хочешь услышать",
            "Проверяй,",
            "Ставлю сотку,",
            "Древние оракулы выбрали",
            "Пусть будет",
            "Как знать,",
            "Рандом выбрал",
            "Я выбрала",
            "Сова выбрала",
            "Разрабам альтерпая нефиг делать и они решили",
            "Питон передаёт",
            "Справедливый выбор —",
            "Птичка нашептала"
        ],
    },
}

LOC = utils.locale.Localizator(translations)


async def on_prob(cm: utils.cm.CommandMessage) -> None:
    pref = random.choice(LOC.obj('prefs', cm.lang))
    val = random.randint(0, 100)
    await cm.int_cur.reply(f"{pref} {val}%")


async def on_choose(cm: utils.cm.CommandMessage) -> None:
    opts = re.split('(?i)(^|\\s)(or|или)($|\\s)', cm.arg)[::4]
    pref = random.choice(LOC.obj('prefs', cm.lang))
    val = random.choice(opts).strip()
    await cm.int_cur.reply(f"{pref} {val}")


async def on_poll(cm: utils.cm.CommandMessage) -> None:
    pref = random.choice(LOC.obj('prefs', cm.lang))
    choices = list(x.text for x in cm.media.poll().poll.answers)
    val = random.choice(choices).text
    await cm.int_cur.reply(f"{pref} {utils.str.escape(val)}")


handler_list.append(utils.ch.CommandHandler(
    name='prob',
    pattern=utils.regex.cmd(utils.regex.unite('prob', 'chance', 'инфа', 'шанс', 'вер', 'вероятность')),
    help_page="random",
    handler_impl=on_prob
))

handler_list.append(utils.ch.CommandHandler(
    name='choose',
    pattern=utils.regex.cmd(utils.regex.unite('choose', 'select', 'выбери')),
    help_page="random",
    handler_impl=on_choose,
    is_prefix=True
))

handler_list.append(utils.ch.CommandHandler(
    name='poll-choose',
    pattern=utils.regex.ignore_case(""),
    help_page="random",
    handler_impl=on_poll,
    required_media_type={"poll"},
    is_arg_current=True
))
