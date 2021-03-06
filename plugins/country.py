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
    info = f"""π’ππππππ π¨ππΏππππΊππππ

π­πΊππΎ : {country.name()}

π­πΊππππΎ π­πΊππΎ : {country.native_name()}

π’πΊππππΊπ : {country.capital()}

Population : <code>{country.population()}</code>

π±πΎππππ : {country.region()}

π²ππ» π±πΎππππ : {country.subregion()}

π³ππ π«πΎππΎπ π£πππΊπππ : {country.tld()}

π’πΊπππππ π’ππ½πΎπ : {country.calling_codes()}

π’ππππΎππΌππΎπ : {country.currencies()}

π±πΎπππ½πΎππΌπΎ : {country.demonym()}

π³πππΎππππΎ : <code>{country.timezones()}</code>

π¬πΊπ½πΎ π»π @M_STER_TECH_GROUP"""
    country_name = country.name()
    country_name = country_name.replace(" ", "+")
    buttons=[[
      Import.Button("πΆπππππΎπ½ππΊ", url=f"{country.wiki()}"),
      Import.Button("π¦πππππΎ", url=f"https://www.google.com/search?q={country_name}")
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
