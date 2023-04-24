def geo_id():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    calculation = []
    for element in ids.values():
        calculation.extend(element)
    return list(set(calculation))


def visits():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    from_mother_russia = []
    for visit in geo_logs:
        for city, county in visit.values():
            if county == 'Россия':
                from_mother_russia.append(visit)
    geo_logs.clear()
    geo_logs.extend(from_mother_russia)
    return geo_logs


def ads_stats():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    max_val = max(stats.values())

    for stat, count in stats.items():
        if count == max_val:
            return stat


if __name__ == '__main__':
    geo_id()
    visits()
    ads_stats()
