class Time:
    def __init__(self,hours,minutes,seconds):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
    def __eq__(self,other):
        return (self.hours==other.hours and self.minutes==other.minutes and self.seconds==other.seconds)
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
t1 = Time(8, 29, 50)
t2 = Time(8,29,50)
t3 = Time(8,30,10)
print(f"{t1} == {t2} ? {t1 == t2}")  
print(f"{t1} == {t3} ? {t1 == t3}")
