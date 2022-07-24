# Bu plugin aykhan_s tərəfindən yaradılıb !
# Kopyalamaq dəyişdirməy qadağandır
# t.me/aykhan_s | t.me/RoBotlarimTg

from pyrogram import filters

from SaitamaRobot.pyrogramee.pluginshelper import admins_only, get_text
from SaitamaRobot import pbot

@pbot.on_message(filters.command(['tag']))
async def all(client, message):
    await message.reply("🥳 Qarışıq Tağ Prosesi Başladı...")
    chat_id = message.chat.id
    string = get_text(message)
    if not string:
        string = ""
    limit = 1
    icm = client.iter_chat_members(message.chat.id)
    async for member in icm:
        tag = member.user.mention
        if limit <= 5:
            if tag != None:
                string += f"🥳 {tag}\n"
            else:
                string += f"{member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string)
            limit = 1
            string = ""


@pbot.on_message(filters.command(['tektag']))
async def tag(client, message):
    await message.reply("🥳 Tək-Tək Tağ Prosesi Başladı...")
    chat_id = message.chat.id
    string = get_text(message)
    if not string:
        string = ""
    limit = 1
    icm = client.iter_chat_members(message.chat.id)
    async for member in icm:
        tag = member.user.mention
        if limit <= 1:
            if tag != None:
                string += f"❤️ {tag} Bayaqdan səni gözləyirəm gəl qrupa 🥰 \n"
            else:
                string += f"{member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string)
            limit = 1
            string = ""

@pbot.on_message(filters.command(['cancell']))
async def tagstop(client, message):
    await message.reply("😌 Tağ etməə prosesi dayandırıldı")
    chat_id = message.chat.id
    string = get_text(message)
    if not string:
        string = ""
    limit = 1
    icm = client.iter_chat_members(message.chat.id)
    async for member in icm:
        tag = member.user.mention
        if limit <= 1:
            if tag != None:
                string += f"❤️ {tag} Bayaqdan səni gözləyirəm gəl qrupa 🥰 \n"
            else:
                string += f"{member.user.mention}\n"
            limit += 1
        else:
            await client.send_message(chat_id, text=string)
            limit = 1
            string = ""
            


__mod_name__ = "🖇️Tağ"
__help__ = """

✅ *Yalnız adminlər* tərəfindən istifadə oluna bilər !

- `/tag` : Son görülməsi yaxın olan hərkəsi qarışıq *tağ edər*
- `/tektag` : Qrupdan *100* nəfəri *tağ edər*
- `/admin` : Qrup adminlərini *tağ edər*
- `/cancell` Aktiv tağ prosesini *dayandırır*
"""
