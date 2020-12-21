#имя, фамилия, год рождения, город проживания, email, телефон

def info(name, surname, year, city, email, phone):
    return f'Ваше имя: {name}\nфамилия: {surname}\nгод рождения: {year}\nгород проживания: {city}\nemail: {email}\nтелефон: {phone}.'
print(info('Nick', 'Fury', 1900, 'London', 'furious@nick.com', '8-800-5-35-35-35'))