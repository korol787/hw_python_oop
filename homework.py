import datetime as dt


class Calculator:
    
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        
    def add_record(self, record):
        self.records.append(record)
        
    def get_today_stats(self):
        today_date = dt.datetime.now().date()
        amount_today = 0
        for record in self.records:
            if record.date == today_date:
                amount_today += record.amount
        return amount_today
    
    def get_week_stats(self):
        today_date = dt.datetime.now().date()
        amount_week = 0
        week_ago = today_date - dt.timedelta(days=6)
        for record in self.records:
            if week_ago <= record.date <= today_date:
                amount_week += record.amount
        return amount_week
    
    
class Record:
    
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        today_date = dt.datetime.now().date()
        if date is None:
            self.date = today_date
        else:
            date_format = '%d.%m.%Y'
            moment = dt.datetime.strptime(date, date_format)
            self.date = moment.date()
            

class CashCalculator(Calculator):
    EURO_RATE = 75.01
    USD_RATE = 68.01
    
    def get_today_cash_remained(self, currency):
        currencies = {
            'rub': (1, 'руб'),
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro')
            }
        if currency not in currencies.keys():
            raise Exception('Некорректно введен код валюты')
        coef = currencies[currency][0]
        currency = currencies[currency][1]
        cash_today = self.get_today_stats()
        if cash_today < self.limit:   
            cash_balance = (self.limit - cash_today) / coef
            return 'На сегодня осталось {:.2f} {}'.format(cash_balance, currency)
        elif cash_today > self.limit:
            money_debt = (cash_today - self.limit)/coef
            return ('Денег нет, держись: твой долг - '
        + '{:.2f} {}'.format(money_debt, currency))
        return 'Денег нет, держись'
        

class CaloriesCalculator(Calculator):
    
    def get_calories_remained(self):
        calories_today = self.get_today_stats()
        if calories_today < self.limit:
            calories_for_today = self.limit - calories_today
            return ('Сегодня можно съесть что-нибудь ещё, ' + 
        f'но с общей калорийностью не более {calories_for_today} кКал')
        return 'Хватит есть!'
