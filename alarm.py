from datetime import datetime
import time

class Alarm:
    def __init__(self, time_str, label=""):
        self.time_str = time_str
        self.label = label
        self.time_obj = datetime.strptime(time_str, "%H:%M")

    def is_time_to_ring(self):
        now = datetime.now()
        return now.hour == self.time_obj.hour and now.minute == self.time_obj.minute

class AlarmManager:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm):
        self.alarms.append(alarm)
        print(f"[AlarmManager] 알람 등록: {alarm.time_str} - {alarm.label}")

    def check_alarms(self):
        for alarm in self.alarms:
            if alarm.is_time_to_ring():
                print(f"[SystemClock] 알람 울림! {alarm.label}")

if __name__ == "__main__":
    alarm_manager = AlarmManager()
    alarm = Alarm("07:00", "기상 알람")
    alarm_manager.add_alarm(alarm)

    print("[SystemClock] 알람 대기 중...")
    for _ in range(5):
        alarm_manager.check_alarms()
        time.sleep(60)
