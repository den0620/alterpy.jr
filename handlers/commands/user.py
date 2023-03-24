import utils.cm
import utils.ch
import utils.pronouns
import utils.regex
import utils.str

handler_list = []


async def on_set_name_en(cm: utils.cm.CommandMessage):
    if cm.arg:
        cm.sender.set_name(cm.arg)
        await cm.int_cur.reply(f"Name set to {cm.arg}")
    else:
        await cm.int_cur.reply(f"Your name is {utils.str.escape(cm.sender.get_name()) or 'not set'}")


async def on_set_name_ru(cm: utils.cm.CommandMessage):
    if cm.arg:
        cm.sender.set_name(cm.arg)
        await cm.int_cur.reply(f"Установлено имя {cm.arg}")
    else:
        await cm.int_cur.reply(f"Ваше имя — {utils.str.escape(cm.sender.get_name()) or 'не установлено'}")


async def on_get_name_en(cm: utils.cm.CommandMessage):
    user = cm.reply_sender or cm.sender
    await cm.int_cur.reply(f"{utils.str.escape(await user.get_display_name())}'s name is {utils.str.escape(user.get_name()) or 'not set'}")


async def on_get_name_ru(cm: utils.cm.CommandMessage):
    user = cm.reply_sender or cm.sender
    await cm.int_cur.reply(f"Имя пользователя {utils.str.escape(await user.get_display_name())} — {utils.str.escape(user.get_name()) or 'не установлено'}")


async def on_reset_name_en(cm: utils.cm.CommandMessage):
    cm.sender.reset_name()
    await cm.int_cur.reply("Name is not set now")


async def on_reset_name_ru(cm: utils.cm.CommandMessage):
    cm.sender.reset_name()
    await cm.int_cur.reply("Имя сброшено")


async def on_set_gender_en(cm: utils.cm.CommandMessage):
    if cm.arg:
        g = utils.pronouns.from_str(cm.arg)
        cm.sender.set_pronouns(g)
        await cm.int_cur.reply(f"Pronoun set is {utils.pronouns.to_str(g, 'en')}")
    else:
        await cm.int_cur.reply(f"Your pronoun set is {utils.pronouns.to_str(cm.sender.get_pronouns(), 'en')}")


async def on_set_gender_ru(cm: utils.cm.CommandMessage):
    if cm.arg:
        g = utils.pronouns.from_str(cm.arg)
        cm.sender.set_pronouns(g)
        await cm.int_cur.reply(f"Установлен набор местоимений {utils.pronouns.to_str(g, 'ru')}")
    else:
        await cm.int_cur.reply(f"Ваш набор местоимений — {utils.pronouns.to_str(cm.sender.get_pronouns(), 'ru')}")


async def on_get_gender_en(cm: utils.cm.CommandMessage):
    user = cm.reply_sender or cm.sender
    await cm.int_cur.reply(f"{utils.str.escape(await user.get_display_name())}'s pronoun set is {utils.pronouns.to_str(user.get_pronouns(), 'en')}")


async def on_get_gender_ru(cm: utils.cm.CommandMessage):
    user = cm.reply_sender or cm.sender
    await cm.int_cur.reply(f"Набор местоимений {utils.str.escape(await user.get_display_name())} — {utils.pronouns.to_str(user.get_pronouns(), 'ru')}")


async def on_reset_gender_en(cm: utils.cm.CommandMessage):
    cm.sender.reset_pronouns()
    await cm.int_cur.reply("Pronoun set is unset now")


async def on_reset_gender_ru(cm: utils.cm.CommandMessage):
    cm.sender.reset_pronouns()
    await cm.int_cur.reply("Набор местоимений сброшен")


handler_list.append(utils.ch.CommandHandler(
    "+name",
    utils.regex.raw_command("\\+name"),
    ["name", "имя"], on_set_name_en, is_prefix=True, is_arg_current=True
))
handler_list.append(utils.ch.CommandHandler(
    "+имя",
    utils.regex.raw_command("\\+имя"),
    ["name", "имя"], on_set_name_ru, is_prefix=True, is_arg_current=True
))
handler_list.append(utils.ch.CommandHandler(
    "?name",
    utils.regex.raw_command("\\?name"),
    ["name", "имя"], on_get_name_en
))
handler_list.append(utils.ch.CommandHandler(
    "?имя",
    utils.regex.raw_command("\\?имя"),
    ["name", "имя"], on_get_name_ru
))
handler_list.append(utils.ch.CommandHandler(
    "-name",
    utils.regex.raw_command("-name"),
    ["name", "имя"], on_reset_name_en
))
handler_list.append(utils.ch.CommandHandler(
    "-имя",
    utils.regex.raw_command("-имя"),
    ["name", "имя"], on_reset_name_ru
))
handler_list.append(utils.ch.CommandHandler(
    "+pn",
    utils.regex.raw_command("\\+pn"),
    ["name", "имя"], on_set_gender_en, is_prefix=True, is_arg_current=True
))
handler_list.append(utils.ch.CommandHandler(
    "+мест",
    utils.regex.raw_command("\\+мест"),
    ["name", "имя"], on_set_gender_ru, is_prefix=True, is_arg_current=True
))
handler_list.append(utils.ch.CommandHandler(
    "?pn",
    utils.regex.raw_command("\\?pn"),
    ["name", "имя"], on_get_gender_en
))
handler_list.append(utils.ch.CommandHandler(
    "?мест",
    utils.regex.raw_command("\\?мест"),
    ["name", "имя"], on_get_gender_ru
))
handler_list.append(utils.ch.CommandHandler(
    "-pn",
    utils.regex.raw_command("-pn"),
    ["name", "имя"], on_reset_gender_en
))
handler_list.append(utils.ch.CommandHandler(
    "-мест",
    utils.regex.raw_command("-мест"),
    ["name", "имя"], on_reset_gender_ru
))
