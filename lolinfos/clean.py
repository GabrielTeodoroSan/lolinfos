roles = {'support', 'adc', 'mid', 'jungle', 'top'}


class ChampionClean:
    def name_clean(self, name):
        name = name.strip()
        name = name.replace(' ', '')
        name = name.replace("'", '')
        return name.lower()

    def role_clean(self, role):
        if role not in roles:
            return ''
        return role
