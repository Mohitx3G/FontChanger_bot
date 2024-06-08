from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN", "7414641943:AAGoiVcEpbFdC2o-dQKq95TY8XKvLffuAKs")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Hosting ip manzili
BACKEND_URL = env.str("BACKEND_URL")  # BACKEND_URL manzili
ADMIN_TOKEN = env.str("ADMIN_TOKEN")  # Admin tokeni

CHANNELS = ['-1001997121709']  # channels
