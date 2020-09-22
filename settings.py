#!/usr/bin/python3

from telegram import InlineKeyboardButton

not_interface = False
default_time = 0.0
roots = [560950095]
limit = 2000000000
seconds_limits_album = 40000
max_songs = 400
telegram_file_api_limit = 1500000000
telegram_audio_api_limit = 50000000
db_file = "dwsongs.db"
loc_dir = "Songs/"
ini_file = "settings.ini"
photo = "example.png"
bot_name = "IL_Songsbot"
api_chart = "https://api.deezer.com/chart"
api_artist = "https://api.deezer.com/artist/%s"
api_type1 = "https://api.deezer.com/search/{}/?q={}"
api_type2 = "https://api.deezer.com/search/?q={}:\"{}\""
song_default_image = "https://e-cdns-images.dzcdn.net/images/cover/1000x1000-000000-80-0-0.jpg"
services_supported = ["spotify", "deezer"]
comandss = ["start", "settings", "info", "shazam", "help"]
settingss = ["quality"]
qualities = ["FLAC", "MP3_320K", "MP3_256K", "MP3_128K"]
send_image_track_query = "👤 <b>אמן: </b>%s \n📀 <b>שיר: </b>%s \n━━━━━━━━━━━━\n📅 <b>פורסם בתאריך: </b>%s\n🕘 <b>משך זמן: </b>\n━━━━━━━━━━━━\n📢 @IL_Songs"
send_image_album_query = "💽 אלבום: %s \n👤 אמן: %s \n📅 תאריך אלבום: %s \n🎧 מספר שירים: %d"
send_image_artist_query = "👤 אמן: %s \n💽 מספר אלבומים: %d \n👥 מספר מעריצים בדיזר: %d"
tags_query = "💽 אלבום: %s\n📅 תאריך: %s\n📀 חברת תקליטים: %s\n🎵 ז'אנר: %s"
info_msg = "🔺 גרסא: %s\n🔻 שם הרובוט: @%s\n✒️ יוצר הרובוט: %s\n📣 ערוץ: %s\n👥 משתמשים בסהכ: %d\n⬇️ סהכ הורדת: %d"
send_image_playlist_query = "📅 יוצר הרובוט: %s \n👤 משתמש: %s \n🎧 *כמות שירים*: %d"
insert_query = "INSERT INTO DWSONGS (id, query, quality) values ('%s', '%s', '%s')"
where_query = "SELECT query FROM DWSONGS WHERE id = '{}' and quality = '{}'"
user_exist = "SELECT chat_id FROM CHAT_ID where chat_id = '%d'"
share_message = "tg://msg?text=Start @%s רובוט להורדת שירים ;)" % bot_name
start_message = "ברוך הבא ל - @%s \nלחץ '/' כדי לקבל רשימת פקודות" % bot_name
not_supported_links = "סליחה :( הרובוט לא תומך בקישור מסוג זה %s"
rate_link = "https://t.me/il_songsgroup"
end_message = "בוצע :) דרגו אותי פה %s" % rate_link

help_message = (
	"/start: להפעלת הרובוט" +
	"\n\n/settings: הגדרות" +
	"\n\n/shazam: שאזאם(תשלחו קטע קול והרובוט יזהה את שם השיר)" +
	"\n\n/help: מראה את ההודעה הזאת" +
	"\n\n" +
	"פשוט שלח קישור ל- Spotify או deezer להורדה, או הקלד את מה שאתה מחפש"
)

end_keyboard = [
	[
		InlineKeyboardButton(
			"SHARE",
			url = share_message
		)
	]
]

qualities_keyboard = [
	[
		InlineKeyboardButton(
			qualities[a],
			callback_data = qualities[a]
		),
		InlineKeyboardButton(
			qualities[a + 1],
			callback_data = qualities[a + 1]
		)
	] for a in range(
		0, len(qualities), 2
	)
]

first_time_keyboard = [
	[
		InlineKeyboardButton(
			"✅",
			url = "t.me/%s?start" % bot_name
		)
	]
]

queries = {
	"top": {
		"query": "%s/top?limit=30",
		"text": "טופ 30 🔝"
	},

	"albums": {
		"query": "%s/albums",
		"text": "אלבומים 💽"
	},

	"radio": {
		"query": "%s/radio",
		"text": "רדיו 📻"
	},

	"related": {
		"query": "%s/related",
		"text": "דומה 🗣"
	},

	"download": {
		"text": "הורד ⬇️"
	},

	"info": {
		"text": "אודות ❕"
	},

	"back": {
		"text": "חזור 🔙"
	},

	"s_art": {
		"query": "art: %s",
		"text": "חיפוש אמן 👤"
	},

	"s_alb": {
		"query": "alb: %s",
		"text": "חיפוש אלבום 💽"
	},

	"s_pla": {
		"query": "pla: %s",
		"text": "חיפוש פלייליסט 📂"
	},

	"s_lbl": {
		"query": "lbl: %s",
		"text": "חיפוש חברת תקליטים 📀"
	},

	"s_trk": {
		"query": "trk: %s",
		"text": "חיפוש שיר 🎧"
	},

	"s_": {
		"query": "%s",
		"text": "חיפוש כללי 📊"
	}
}
