from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 14009924
    API_HASH = "0d7190eebd87743ea0360568efc35d64"
    # the name to display in your alive message
    ALIVE_NAME = "ᴀsʜᴍɪᴛ"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://tlzlawrs:CjgO7CAj7BrZojFiKfYHxTydtIm15M_s@floppy.db.elephantsql.com/tlzlawrs"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOLEBuykf5Ec41j1v77Ms0bz-aejuDzdA2QeGrmF7TgD2EiX7ARX_vtc0VOdHpjyYV3CXOTrF8anUgqxbHR8aMeKQ3aUK5yXjF5WlibiKCa8ClAeNLblNttDh05214h6abyYI-XYu_BG23qHPCSkFqBnfS51tsPqzOtHH4Q_3bhCnIT9XummDGa_rvGfoxYYRkrRBvOiNIZ9MxcigvqckeTzw-IhH-2lR8sKesOV0Cuv3J9RejfAf6ODTiuhnEWlYtldK7t-c-rrPMck0KqtcQ38uQY-RSRsUhVjPGHIm8ec4F2b-6wkYl7XQnYK2ifOTFCIGnCptqh8ewquJb5T_rdYd0rg="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5682235319:AAFqPTtVUbO5T3UlNyFePclhiYzhS8eqtjY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001872465064
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
