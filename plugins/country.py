# (c) [Raihan] @RAIHAN_TG
# (s) @M_STER_TECH_GROUP , @ThorSupport, @TeamThorMakers
# Copyright permission under MIT License
# All rights reserved by RAIHAN 
# License -> https://github.com/raihanvaliyakath/THOR-THE-AUTO-FILTER-BOT/blob/raihanvaliyakath/LICENSE

import random
from countryinfo import CountryInfo
from pyrogram import filters, Client as DonLee_Robot_V2
from @Thor_RoBoT .Config_Vars.H_Vars import BUTTONS
from @Thor_RoBoT import Config, Import 

@Thor_RoBoT.on_message(filters.command(["country"]))
async def country_info(bot, update: Import.Msg):
    country = update.text.split(" ", 1)[1]
    country = CountryInfo(country)
    info = f"""𝖢𝗈𝗎𝗇𝗍𝗋𝗒 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

𝖭𝖺𝗆𝖾 : {country.name()}

𝖭𝖺𝗍𝗂𝗏𝖾 𝖭𝖺𝗆𝖾 : {country.native_name()}

𝖢𝖺𝗉𝗂𝗍𝖺𝗅 : {country.capital()}

Population : <code>{country.population()}</code>

𝖱𝖾𝗀𝗂𝗈𝗇 : {country.region()}

𝖲𝗎𝖻 𝖱𝖾𝗀𝗂𝗈𝗇 : {country.subregion()}

𝖳𝗈𝗉 𝖫𝖾𝗏𝖾𝗅 𝖣𝗈𝗆𝖺𝗂𝗇𝗌 : {country.tld()}

𝖢𝖺𝗅𝗅𝗂𝗇𝗀 𝖢𝗈𝖽𝖾𝗌 : {country.calling_codes()}

𝖢𝗎𝗋𝗋𝖾𝗇𝖼𝗂𝖾𝗌 : {country.currencies()}

𝖱𝖾𝗌𝗂𝖽𝖾𝗇𝖼𝖾 : {country.demonym()}

𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>{country.timezones()}</code>

𝖬𝖺𝖽𝖾 𝖻𝗒 @M_STER_TECH_GROUP"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    buttons=[[
      Import.Button("𝖶𝗂𝗄𝗂𝗉𝖾𝖽𝗂𝖺", url=f"{country.wiki()}"),
      Import.Button("𝖦𝗈𝗈𝗀𝗅𝖾", url=f"https://www.google.com/search?q={country_name}")
    ]]
    try:
        await update.reply_photo(
            photo=random.choice(Config.PHOTO),
            caption=info,
            reply_markup=Import.Markup(buttons),
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
