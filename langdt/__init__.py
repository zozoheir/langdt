from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
import re

# Testing the function with the provided examples
test_cases = [
    "all", "recent", "yesterday", "since last month", "this week",
    "last 20 minutes", "last year", "last 2 years", "last month", "last 5 weeks", "last hour",
    "from 2022-10-10 to 2025-10-10T00:30:11",
    "from 2022 to 2025",
    "from Nov 2nd 2023 to Nov 5th 2025"
]

# Testing the updated function with the provided examples
def get_timeframe(filter_str):
    now = datetime.now()
    lower_str = filter_str.lower()

    if lower_str in ["all", "all time"]:
        return None, None

    if lower_str == "recent":
        return (now - timedelta(days=7)).isoformat(), now.isoformat()

    if lower_str == "yesterday":
        yesterday = now - timedelta(days=1)
        start_of_yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_yesterday = yesterday.replace(hour=23, minute=59, second=59, microsecond=999999)
        return start_of_yesterday.isoformat(), end_of_yesterday.isoformat()

    # Handle "last" pattern
    if lower_str.startswith("last "):
        parts = lower_str.split(" ")
        if len(parts) == 2:  # e.g., "last year"
            time_amount = 1
            time_unit = parts[1]
        else:
            time_amount, time_unit = parts[1:3]
            time_amount = int(time_amount)

        if time_unit.endswith('s'):  # remove plural
            time_unit = time_unit[:-1]
        delta_kwargs = {f"{time_unit}s": time_amount}
        from_time = now - relativedelta(**delta_kwargs)
        return from_time.isoformat(), now.isoformat()

    # Handle "since" pattern
    if lower_str.startswith("since "):
        time_reference = lower_str.split(" ")[1]
        if time_reference == "yesterday":
            since_time = (now - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
        elif time_reference == "last":
            time_unit = lower_str.split(" ")[2]
            if time_unit == "month":
                since_time = (now.replace(day=1) - relativedelta(months=1)).replace(hour=0, minute=0, second=0,
                                                                                    microsecond=0)
            elif time_unit == "year":
                since_time = (now.replace(day=1, month=1) - relativedelta(years=1)).replace(hour=0, minute=0, second=0,
                                                                                            microsecond=0)
        return since_time.isoformat(), now.isoformat()

    # Handle "this" pattern
    if lower_str.startswith("this "):
        time_unit = lower_str.split(" ")[1]
        if time_unit == "week":
            this_time = now - timedelta(days=now.weekday())
        elif time_unit == "year":
            this_time = now.replace(month=1, day=1)
        this_time = this_time.replace(hour=0, minute=0, second=0, microsecond=0)
        return this_time.isoformat(), now.isoformat()

    # Handle "from ... to ..." pattern
    if lower_str.startswith("from "):
        from_to_pattern = r"from (.+?) to (.+)$"
        match = re.search(from_to_pattern, lower_str)
        if match:
            from_date_str, to_date_str = match.groups()
            # Assume the first second of the first day for "from" date if only year is given
            from_date = parse(from_date_str)
            if len(from_date_str) <= 4:  # Year only
                from_date = from_date.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            elif len(from_date_str) <= 7:  # Year and month
                from_date = from_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            else:
                from_date = from_date.replace(hour=0, minute=0, second=0, microsecond=0)

            # Assume the last second of the last day for "to" date if only year is given
            to_date = parse(to_date_str)
            if len(to_date_str) <= 4:  # Year only
                to_date = to_date.replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
            elif len(to_date_str) <= 7:  # Year and month
                # Set to the last day of the month
                last_day = (to_date + relativedelta(months=1)).replace(day=1) - timedelta(days=1)
                to_date = last_day.replace(hour=23, minute=59, second=59, microsecond=999999)
            else:
                to_date = to_date.replace(hour=23, minute=59, second=59, microsecond=999999)

            return from_date.isoformat(), to_date.isoformat()

    # Default case for unrecognized patterns
    return "Unrecognized", None

# Testing the updated function with the provided examples
for case in test_cases:
    from_, to = get_timeframe(case)
    print(f"{case}: {from_} - {to}")
