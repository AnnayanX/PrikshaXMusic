from PrikshaXMusic.core.bot import Priksha
from PrikshaXMusic.core.dir import dirr
from PrikshaXMusic.core.git import git
from PrikshaXMusic.core.userbot import Userbot
from PrikshaXMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Priksha()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
