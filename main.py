import sys
sys.path.insert(1, 'modules/')

from module_a import run_a
from module_b import run_b
from module_c import run_c

# Google Auth
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file('gspread-connection.json')
scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets'])

# gspread
import gspread
gc = gspread.authorize(scoped_credentials)

run_a(gc)

run_b(gc)

run_c(gc)