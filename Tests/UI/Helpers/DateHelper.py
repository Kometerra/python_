from datetime import datetime,timedelta

class DateHelper:
    @staticmethod
    def generate_day_after_offset(offset_days: int):
        target_date= datetime.today()+timedelta(days=offset_days)
        return str(target_date.day)

    @staticmethod
    def get_index_for_calendar_click(day)->int:
        return 1 if int(day) < datetime.today().day else 0
