import datetime 

class ClockIterator:

    def __iter__(self):
        self.time = datetime.datetime(1,1,1,0,0,0)
        return self

    def __next__(self):
        self.time += datetime.timedelta(minutes=1)
        return self.time.strftime('%H:%M')


clock = ClockIterator()

for time in clock:
    print(time)