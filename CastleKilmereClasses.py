from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import NamedTuple
import datetime


class Spell(metaclass=ABCMeta):
    """
    Creates a spell
    """

    def __init__(self, name: str, incantation: str, effect: str):
        self.name = name
        self.incantation = incantation
        self.effect = effect

    @abstractmethod
    def cast(self):
        pass

    @property
    @abstractmethod
    def defining_feature(self):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, incantation: {self.incantation}, effect: {self.effect})'


class Charm(Spell):
    def __init__(self, name: str, incantation: str, effect: str, difficulty: str = None, min_year: int = None):
        super().__init__(name, incantation, effect)
        self.difficulty = difficulty
        self.min_year = min_year

    @property
    def defining_feature(self):
        return "Alteration of the object's inherent qualities, that is, its behaviour and capabilities"

    def cast(self):
        print(f'{self.incantation}')

class DarkArmyMember(NamedTuple):
    name: str
    birthyear: str

    @property
    def leader(self):
        lord_odon = DarkArmyMember('Lord Odon', 1971)
        return lord_odon

    def cast(self, spell):
        print(f"{self.name}: {spell.incantation}!")


@dataclass(frozen=True)
class NewDarkArmyMember():
    """ Creates a death eater """
    name: str
    birthyear: str

    @property
    def leader(self):
        lord_odon = DarkArmyMember('Lord Odon', 1971)
        return lord_odon

    def cast(self, spell):
        print(f"{self.name}: {spell.incantation}!")



class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Witchcraft and Wizardry
    """

    def __init__(self, name: str, birthyear: int, sex: str):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex
        self._traits = {}

    def add_trait(self, trait, value=True):
        self._traits[trait] = value

    def print_traits(self):
        true_traits = [trait for trait, value in self._traits.items() if value]
        false_traits = [trait for trait, value in self._traits.items() if not value]

        print(f"{self._name} is {', '.join(true_traits)} "
              f"but not {', '.join(false_traits)}")

    def exhibits_trait(self, trait):
        try:
            value = self._traits[trait]
        except KeyError:
            print(f"{self._name} does not have a character trait with the name '{trait}'")
            return

        if value:
            print(f"Yes, {self._name} is {trait}")
        else:
            print(f"No, {self._name} is not {trait}")

    def says(self, words):
        return f"{self._name} says {words}"

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    @staticmethod
    def school_headmaster():
        return CastleKilmereMember('Redmond Dalodore', 1939, 'male')

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, birthyear: {self.birthyear})'


class Professor(CastleKilmereMember):
    """
    Creates a Castle Kilmere professor
    """

    def __init__(self, name: str, birthyear: int, sex: str, subject: str, house=None):
        super().__init__(name, birthyear, sex)
        self.subject = subject
        if house is not None:
            self.house = house

    @classmethod
    def mirren(cls):
        return cls('Miranda Mirren', 1963, 'female', 'Transfiguration', 'House of Courage')

    @classmethod
    def blade(cls):
        return cls('Blade Bardock', 1988, 'male', 'Potions', 'House of Ambition')

    def __repr__(self):
        return f"{self.__class__.__name__}({self._name}, birthyear: {self.birthyear}, subject: {self.subject})"


class Ghost(CastleKilmereMember):
    """
    Creates a Castle Kilmere ghost
    """

    def __init__(self, name: str, birthyear: int, sex: str, year_of_death: int, house=None):
        super().__init__(name, birthyear, sex)
        self.year_of_death = year_of_death

        if house is not None:
            self.house = house

    @property
    def age(self):
        now = datetime.datetime.now().year
        return now - self.birthyear

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._name}, birthyear: {self.birthyear}, year of death:' \
            f' {self.year_of_death}'

    @classmethod
    def mocking_knight(cls):
        return cls('The Mocking Knight', 1401, 'male', 1492, 'House of Courage')


class Pupil(CastleKilmereMember):
    """
    Create a Castle Kilmere Pupil
    """

    def __init__(self, name: str, birthyear: int, sex: str, house: str, start_year: int, pet=None):
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
            'Transfiguration': False}

        self._friends = []

    def __repr__(self):
        return f'{self.__class__.__name__} ({self._name}, birthyear: {self.birthyear}, house: {self.house})'

    @classmethod
    def cleon(cls):
        return cls('Cleon Bery', 2008, 'male', 'House of Courage', 2018, ('Cotton', 'owl'))

    @classmethod
    def flynn(cls):
        return cls('Flynn Gibbs', 2008, 'male', 'House of Courage', 2018, ('Twiggles', 'owl'))

    @classmethod
    def cassidy(cls):
        return cls('Cassidy Ambergem', 2007, 'female', 'House of Courage', 2018, ('Ramses', 'cat'))

    @classmethod
    def adrien(cls):
        return cls('Adrien Fulford', 2008, 'male', 'House of Ambition', 2018, ('Unnamed', 'owl'))

    @property
    def current_year(self):
        now = datetime.datetime.now().year
        return (now - self.start_year) + 1

    @property
    def elms(self):
        return self._elms

    @property
    def friends(self):
        return f"{self._name}'s current friends are: {[person.name for person in self._friends]}"

    @elms.setter
    def elms(self, subject_and_grade):

        try:
            subject, grade = subject_and_grade
        except ValueError:
            raise ValueError("Pass and iterable with two items: Subject and grade")

        passed = self.passed(grade)

        if passed:
            self._elms[subject] = True
        else:
            print('The exam was not passed so no ELM was awarded')

    @elms.deleter
    def elms(self):
        print("Caution, you are deleting this students' ELM's! You should only do that if she/he dropped out of "
              "school without passing any exam")
        del self._elms

    @staticmethod
    def passed(grade):
        """
            Given a grade, determine if an exam was passed
        """
        grades = {
            'E': True,
            'Exceptional': True,
            'G': True,
            'Good': True,
            'A': True,
            'Acceptable': True,
            'P': False,
            'Poor': False,
            'H': False,
            'Horrible': False,
        }

        return grades.get(grade, False)

    def befriend(self, person):
        """"
            Adds another person to your list of friends
        """
        if (person.__class__.__name__ != 'CastleKilmereMember'
                and self.house != 'House of Ambition'
                and person.house == 'House of Ambition'):
            print("Are you sure you want to be friends with someone from House of Ambition?")

        self._friends.append(person)
        print(f"{person.name} is now your friend!")


@dataclass # Dataclass decorator added on Python 3.7. It adds serveral special methods such as __init__()
class House:
    name: str
    traits: list
    head: Professor
    ghost: Ghost
    founded_in: int = 991

    def current_age(self):
        now = datetime.datetime.now().year
        return (now - self.founded_in) + 1


if __name__ == "__main__":
    bromley = CastleKilmereMember(name='Bromley Huckabee', birthyear=1959, sex='male')
    bromley.add_trait('kind')
    bromley.add_trait('tidy-minded')
    bromley.add_trait('impatient', value=False)

    bromley.print_traits()

    keres = NewDarkArmyMember('Keres Fulford', 1983)
    print(keres)

    charm = Charm('Stuporus Ratiato', 'Stuporus Ratiato', 'Makes objects fly', 'simple')



