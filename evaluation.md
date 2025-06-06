<코드 모듈 평가>

#응집도

- `Alarm` 클래스는 알람 시간과 라벨을 저장하고, 현재 시간이 알람 시간과 일치하는지 판단하는 기능을 담당.
- `AlarmManager`는 여러 알람을 관리하고, 알람이 울려야 할 시간을 체크.
- 각 클래스가 자기 역할만 정확히 수행하고 있어 응집도가 높다.**

#결합도
- `AlarmManager`는 `Alarm` 객체에만 의존하며, 다른 외부 요소와는 느슨하게 연결.
- 알람 울림 여부는 `Alarm` 클래스 내부에서만 판단되므로, 모듈 간 결합도가 낮아 유지보수가 쉽다.

#평가 요약

- 높은 응집도, 낮은 결합도를 갖는 구조로 설계.
- 추후 기능 추가나 수정 시 유연하게 대처할 수 있는 구조.
