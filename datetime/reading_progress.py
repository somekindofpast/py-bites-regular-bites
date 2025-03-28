from datetime import datetime


def ontrack_reading(books_goal: int, books_read: int,
                    day_of_year: int = None) -> bool:
    if day_of_year is None:
        day_of_year = datetime.today().timetuple().tm_yday
    return books_goal <= int((365 / day_of_year) * books_read)