from datetime import date, timedelta
from typing import List, Tuple


def get_week_start(d: date) -> date:
    """Return the Sunday that starts the week containing date d."""
    # weekday(): Monday=0 ... Sunday=6
    days_since_sunday = (d.weekday() + 1) % 7
    return d - timedelta(days=days_since_sunday)


def get_week_end(week_start: date) -> date:
    """Return the Saturday that ends the week (6 days after Sunday)."""
    return week_start + timedelta(days=6)


def generate_weeks(start_date: date, end_date: date) -> List[Tuple[int, date, date]]:
    """
    Generate (week_number, week_start_sunday, week_end_saturday) tuples
    from start_date to end_date (inclusive).
    Week 1 begins on the Sunday of the week containing start_date.
    Week starts on Sunday, ends on Saturday.
    """
    # Find Sunday of the week containing start_date
    first_sunday = get_week_start(start_date)

    weeks = []
    week_number = 1
    current_start = first_sunday

    while current_start <= end_date:
        current_end = get_week_end(current_start)
        weeks.append((week_number, current_start, current_end))
        week_number += 1
        current_start += timedelta(days=7)

    return weeks


def get_current_week_number(weeks: list, today: date = None) -> int:
    """Return the week_number for today, or the last week if past end."""
    if today is None:
        today = date.today()
    for wn, ws, we in weeks:
        if ws <= today <= we:
            return wn
    # If today is before week 1
    if weeks and today < weeks[0][1]:
        return 1
    # If today is after last week
    if weeks:
        return weeks[-1][0]
    return 1


def days_remaining(end_date: date) -> int:
    return max(0, (end_date - date.today()).days)


def week_target_hours(weekday_hrs: float, saturday_hrs: float, sunday_hrs: float) -> float:
    """Weekly target = 5 weekdays + saturday + sunday."""
    return round(weekday_hrs * 5 + saturday_hrs + sunday_hrs, 1)
