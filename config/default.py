

DEBUG = True
SECRET_KEY = '0f610b91b7405989f341eec6fe28863fe2dc33bd68078965'

PASSWORD_HASH = 'pbkdf2_sha512'
PASSWORD_SALT = 'cfd846686fc05d938d9655c61707815d604ae61c3a9cfe12'

# 1 year
TOKEN_EXPIRATION_TIME = 3600

# token in request headers
TOKEN_AUTHENTICATION_HEADER = 'X-AUTH-TOKEN'
