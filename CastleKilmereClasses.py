class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    # Class attribute
    location = 'England'

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f'{self._name} says {words}'


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name, birthyear, sex, house, start_year, pet=None):
        super().__init__(name, birthyear, sex)
        self.house = house
        self.start_year = start_year

        if pet is not None:
            self.pet_name, self.pet_type = pet

        self._elms = {
                  'Broomstick Flying': False,
                  'Art': False,
                  'Magical Theory': False,
                  'Foreign Magical Systems': False,
                  'Charms': False,
                  'Defence Against Dark Magic': False,
                  'Divination': False,
                  'Herbology': False,
                  'History of Magic': False,
                  'Potions': False,
                  'Transfiguration': False
        }


cleon = Pupil(name='Cleon bery', birthyear=2000, sex='male', house='House of Courage',
              start_year=2018, pet=('Cotton', 'owl'))

