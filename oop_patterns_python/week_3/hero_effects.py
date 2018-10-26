from oop_patterns_python.week_3.hero import Hero
from abc import ABC, abstractmethod

class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_stats(self):  # Возвращает итоговые хараетеристики
        # после применения эффекта
        self.base.get_stats

    def get_positive_effects(self):
        return self.base.get_positive_effects()

    def get_negative_effects(self):
        return self.base.get_negative_effects()

class AbstractPositice(AbstractEffect):
    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append(type(self).__name__)
        return effects

class AbstractNegative(AbstractEffect):
    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append(type(self).__name__)
        return effects

class Berserk(AbstractPositice):

    def get_stats(self):
        stats = self.base.get_stats()
        stats['HP'] += 50
        stats['Strength'] += 7
        stats['Endurance'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7
        stats['Perception'] -= 3
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        del stats['MP']
        del stats['SP']

        return stats

    # def get_positive_effects(self):
    #     positive_effects = self.base.get_positive_effects()
    #     positive_effects.append('Berserk')
    #     return positive_effects

class Blessing(AbstractPositice):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] += 2
        stats['Endurance'] += 2
        stats['Agility'] += 2
        stats['Luck'] += 2
        stats['Perception'] += 2
        stats['Charisma'] += 2
        stats['Intelligence'] += 2
        del stats['HP']
        del stats['MP']
        del stats['SP']

        return stats

    # def get_positive_effects(self):
    #     positive_effects = self.base.get_positive_effects()
    #     positive_effects.append('Blessing')
    #     return positive_effects

class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 4
        stats['Endurance'] -= 4
        stats['Agility'] -= 4
        del stats['HP']
        del stats['MP']
        del stats['SP']
        return stats

    # def get_negative_effects(self):
    #     effects = self.base.get_negative_effects()
    #     effects.append('Weakness')
    #     return effects

class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        del stats['HP']
        del stats['MP']
        del stats['SP']
        return stats

    # def get_negative_effects(self):
    #     effects = self.base.get_negative_effects()
    #     effects.append('EvilEye')
    #     return effects

class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 2
        stats['Endurance'] -= 2
        stats['Agility'] -= 2
        stats['Luck'] -= 2
        stats['Perception'] -= 2
        stats['Charisma'] -= 2
        stats['Intelligence'] -= 2
        del stats['HP']
        del stats['MP']
        del stats['SP']
        return stats

    # def get_negative_effects(self):
    #     effects = self.base.get_negative_effects()
    #     effects.append('Curse')
    #     return effects