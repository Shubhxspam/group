import glob
import io
import os
import re
import urllib
import urllib.request

import bs4
import requests
from bing_image_downloader import downloader
from bs4 import BeautifulSoup
from PIL import Image
from search_engine_parser import GoogleSearch

from MukeshRobot import telethn as tbot
from MukeshRobot.events import register

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 11; SM-M017F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


import os
import requests
from pyrogram import Client, filters

# Google API & CX ID from Environment Variables
GOOGLE_API_KEY = os.getenv("AIzaSyCVgY0zwTEZDXY2wkOrgvARNTcjaU5A12c")
GOOGLE_CX = os.getenv("6063aa3400fcf46cc")

@Client.on_message(filters.command("google") & filters.private)
async def google_search(client, message):
    if not GOOGLE_API_KEY or not GOOGLE_CX:
        await message.reply_text("`Google API key ya CX ID set nahi hai!`")
        return

    query = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply_text("`Kya search karna hai likho!`")
        return

    await message.reply_text("🔍 **Searching Google...**")

    # Google Search API request
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={GOOGLE_CX}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if "items" not in data:
            await message.reply_text("`Koi results nahi mile ya API limit exceed ho gayi.`")
            return
        
        results = data["items"][:5]  # Top 5 results
        reply_text = f"🔎 **Google Search Results for:** `{query}`\n\n"

        for idx, item in enumerate(results, start=1):
            title = item.get("title", "No Title")
            link = item.get("link", "No Link")
            reply_text += f"**{idx}.** [{title}]({link})\n"

        await message.reply_text(reply_text, disable_web_page_preview=True)
    
    except Exception as e:
        await message.reply_text(f"`Google search me error aaya:` {str(e)}")
            try:

    


     @register(pattern="^/img (.*)")
     async def img_sampler(event):
     if event.fwd_from:
         return

    query = event.pattern_match.group(1)
    jit = f'"{query}"'
    downloader.download(
        jit,
        limit=4,
        output_dir="store",
        adult_filter_off=False,
        force_replace=False,
        timeout=60,
    )
    os.chdir(f'./store/"{query}"')
    types = ("*.png", "*.jpeg", "*.jpg")  # the tuple of file types
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))
    await tbot.send_file(event.chat_id, files_grabbed, reply_to=event.id)
    os.chdir("/app")
    os.system("rm -rf store")


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 11; SM-M017F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@register(pattern=r"^/reverse|^/pp|^/grs(?: |$)(\d*)")
async def okgoogle(img):
    """For .reverse command, Google search images and stickers."""
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await tbot.download_media(message, photo)
    else:
        await img.reply("`Reply to photo or sticker fu*ker`")
        return

    if photo:
        dev = await img.reply("`Processing...`")
        try:



@register(pattern="^/img (.*)")
async def img_sampler(event):
    if event.fwd_from:
        return

    query = event.pattern_match.group(1)
    jit = f'"{query}"'
    downloader.download(
        jit,
        limit=4,
        output_dir="store",
        adult_filter_off=False,
        force_replace=False,
        timeout=60,
    )
    os.chdir(f'./store/"{query}"')
    types = ("*.png", "*.jpeg", "*.jpg")  # the tuple of file types
    files_grabbed = []
    for files in types:
        files_grabbed.extend(glob.glob(files))
    await tbot.send_file(event.chat_id, files_grabbed, reply_to=event.id)
    os.chdir("/app")
    os.system("rm -rf store")


opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 11; SM-M017F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]


@register(pattern=r"^/reverse|^/pp|^/grs(?: |$)(\d*)")
async def okgoogle(img):
    """For .reverse command, Google search images and stickers."""
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    message = await img.get_reply_message()
    if message and message.media:
        photo = io.BytesIO()
        await tbot.download_media(message, photo)
    else:
        await img.reply("`Reply to photo or sticker fu*ker`")
        return

    if photo:
        dev = await img.reply("`Processing...`")
        try:
            image = Image.open(photo)
        except OSError:
            await dev.edit("`Unsupported sexuality, most likely.`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
            image = Image.open(photo)
        except OSError:
            await dev.edit("`Unsupported sexuality, most likely.`")
            return
        name = "okgoogle.png"
        image.save(name, "PNG")
        image.close()
        # https://stackoverflow.com/questions/23270175/google-reverse-image-search-using-post-request#28792943
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {"encoded_image": (name, open(name, "rb")), "image_content": ""}
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            await dev.edit(
                "`Image successfully uploaded to Google. Maybe.`"
                "\n`Parsing source now. Maybe.`"
            )



@register(pattern="^/app (.*)")
async def apk(e):

    try:
        app_name = e.pattern_match.group(1)
        remove_space = app_name.split(" ")
        final_name = "+".join(remove_space)
        page = requests.get(
            "https://play.google.com/store/search?q=" + final_name + "&c=apps"
        )
        str(page.status_code)
        soup = bs4.BeautifulSoup(page.content, "lxml", from_encoding="utf-8")
        results = soup.findAll("div", "ZmHEEd")
        app_name = (
            results[0].findNext("div", "Vpfmgd").findNext("div", "WsMG1c nnK0zc").text
        )
        app_dev = results[0].findNext("div", "Vpfmgd").findNext("div", "KoLSrc").text
        app_dev_link = (
            "https://play.google.com"
            + results[0].findNext("div", "Vpfmgd").findNext("a", "mnKHRc")["href"]
        )
        app_rating = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "pf5lIe")
            .find("div")["aria-label"]
        )
        app_link = (
            "https://play.google.com"
            + results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "vU6FJ p63iDd")
            .a["href"]
        )
        app_icon = (
            results[0]
            .findNext("div", "Vpfmgd")
            .findNext("div", "uzcko")
            .img["data-src"]
        )
        app_details = "<a href='" + app_icon + "'>📲&#8203;</a>"
        app_details += " <b>" + app_name + "</b>"
        app_details += (
            "\n\n<code>Developer :</code> <a href='"
            + app_dev_link
            + "'>"
            + app_dev
            + "</a>"
        )
        app_details += "\n<code>Rating :</code> " + app_rating.replace(
            "Rated ", "⭐ "
        ).replace(" out of ", "/").replace(" stars", "", 1).replace(
            " stars", "⭐ "
        ).replace(
            "five", "5"
        )
        app_details += (
            "\n<code>Features :</code> <a href='"
            + app_link
            + "'>View in Play Store</a>"
        )
        app_details += "\n\n===> Group Controller<==="
        await e.reply(app_details, link_preview=True, parse_mode="HTML")
    except IndexError:
        await e.reply("No result found in search. Please enter **Valid app name**")
    except Exception as err:
        await e.reply("Exception Occured:- " + str(err))


__mod_name__ = "Gᴏᴏɢʟᴇ"

__help__ = """
 ❍ /google <text>*:* Perform a google search
 ❍ /img <text>*:* Search Google for images and returns them\nFor greater no. of results specify lim, For eg: `/img hello lim=10`
 ❍ /app <appname>*:* Searches for an app in Play Store and returns its details.
 ❍ /reverse |pp |grs: Does a reverse image search of the media which it was replied to.

"""
