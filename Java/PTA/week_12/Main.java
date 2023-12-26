import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

class Date {
    protected int year;
    protected int month;
    protected int day;
}

class Time {
    protected int hour;
    protected int minute;
    protected int second;
}

class Schedule {
    int ID;
    Date date;
    Time time;

    public Schedule(int ID, int year, int month, int day, int hour, int minute, int second) {
        this.ID = ID;
        this.date = new Date();
        this.date.year = year;
        this.date.month = month;
        this.date.day = day;
        this.time = new Time();
        this.time.hour = hour;
        this.time.minute = minute;
        this.time.second = second;
    }

    public boolean isEarlierThan(Schedule s2) {
        if (this.date.year != s2.date.year)
            return this.date.year < s2.date.year;
        if (this.date.month != s2.date.month)
            return this.date.month < s2.date.month;
        if (this.date.day != s2.date.day)
            return this.date.day < s2.date.day;
        if (this.time.hour != s2.time.hour)
            return this.time.hour < s2.time.hour;
        if (this.time.minute != s2.time.minute)
            return this.time.minute < s2.time.minute;
        return this.time.second < s2.time.second;
    }
    @Override
    public String toString() {
        return "The urgent schedule is No." + ID + ": " + date.year + "/" + date.month + "/" + date.day + " " + time.hour + ":" + time.minute + ":" + time.second;
    }
}

public class Main {
    public static void main(String[] args) {
        List<Schedule> schedules = new ArrayList<>();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            int ID = scanner.nextInt();
            if (ID == 0) {
                break;
            }

            String[] dateParts = scanner.next().split("/");
            int year = Integer.parseInt(dateParts[0]);
            int month = Integer.parseInt(dateParts[1]);
            int day = Integer.parseInt(dateParts[2]);

            String[] timeParts = scanner.next().split(":");
            int hour = Integer.parseInt(timeParts[0]);
            int minute = Integer.parseInt(timeParts[1]);
            int second = Integer.parseInt(timeParts[2]);

            schedules.add(new Schedule(ID, year, month, day, hour, minute, second));
        }

        if (schedules.size() > 0) {
            Schedule earliest = schedules.get(0);
            for (Schedule s : schedules) {
                if (s.isEarlierThan(earliest)) {
                    earliest = s;
                }
            }
            System.out.println(earliest);
        }

        scanner.close();
    }
}