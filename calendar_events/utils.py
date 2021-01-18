from calendar import HTMLCalendar


class TestCalendar(HTMLCalendar):
    def __init__(self, events, year=None, month=None):
        self.events = events
        self.month = month
        self.year=year
        super(TestCalendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(dt_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.name} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
             week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        events = self.events.filter(dt_time__year=self.year, dt_time__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, events)}\n'
        return cal
