import datetime


def convert_seconds(seconds):
    return str(datetime.timedelta(seconds=seconds))


print(convert_seconds(484.11316776275635))
print(convert_seconds(484.10208203100046))