import datetime as dt

today_date = dt.date.today()
USD_RATE = 68
EURO_RATE = 75

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []
    def add_record(self, record):
        self.records.append(record.list1)
    def get_today_stats(self):
        amount_today = 0
        for i in range(len(self.records)):
            if self.records[i][2] == today_date:
                amount_today += self.records[i][0]
        return amount_today
    def get_week_stats(self):
        amount_week = 0
        week_ago = today_date - dt.timedelta(days=6)
        for i in range(len(self.records)):
            if week_ago <= self.records[i][2] <= today_date:
                amount_week += self.records[i][0]
        return amount_week
    
class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date == None:
            self.date = today_date
        else:
            date_format = '%d.%m.%Y'
            moment = dt.datetime.strptime(date, date_format)
            self.date = moment.date()
        self.list1 = []
        self.list1.append(self.amount)
        self.list1.append(self.comment)
        self.list1.append(self.date)

def coefficient_and_currency(currency):
    if currency == 'rub':
        coef = 1
        currency = 'руб'
    elif currency == 'usd':
        coef = USD_RATE
    else:
        coef = EURO_RATE
        currency = 'Euro'
    return coef, currency

class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        coef, currency = coefficient_and_currency(currency)
        if currency == 'usd':
            currency = currency.upper()
        cash_today = 0
        for i in range(len(self.records)):
            if self.records[i][2] == today_date:
                cash_today += self.records[i][0]
        if cash_today < self.limit:   
            cash_balance = (self.limit - cash_today)/coef
            return 'На сегодня осталось {:.2f} {}'.format(cash_balance, currency)
        elif cash_today > self.limit:
            money_debt = (cash_today - self.limit)/coef
            return 'Денег нет, держись: твой долг - {:.2f} {}'.format(money_debt, currency)
        else:
            return 'Денег нет, держись'

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_today = 0
        for i in range(len(self.records)):
            if self.records[i][2] == today_date:
                calories_today += self.records[i][0]
        if calories_today < self.limit:
            calories_for_today = self.limit - calories_today
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {calories_for_today} кКал'
        else:
            return 'Хватит есть!'

