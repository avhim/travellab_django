from datetime import timedelta


def end_date_generator(instance):
    new_end_date = instance.tour_date + timedelta(instance.tour.num_days-1)
    return new_end_date

