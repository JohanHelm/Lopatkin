import gspread_asyncio
from google.oauth2.service_account import Credentials


class GoogleSheetsManager:
    def __init__(self, credentials: str, spreadsheet_url: str):
        self.credentials = credentials
        self.spreadsheet_url = spreadsheet_url
        self.agcm = gspread_asyncio.AsyncioGspreadClientManager(self.get_creds)
        self.worksheet: gspread_asyncio.AsyncioGspreadWorksheet | None = None

    def get_creds(self):
        creds = Credentials.from_service_account_file(self.credentials)
        scoped = creds.with_scopes([
            "https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ])
        return scoped

    async def auth_spread_work(self):
        agc = await self.agcm.authorize()
        spreadsheet = await agc.open_by_url(self.spreadsheet_url)
        self.worksheet = await spreadsheet.get_sheet1()

    async def get_a2_from_g_sheets(self):
        a2 = await self.worksheet.acell("A2")
        return a2.value

    async def b2_update(self, user_date: str):
        await self.worksheet.update_acell('B2', user_date)
