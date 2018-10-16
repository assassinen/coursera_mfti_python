from oop_patterns_python.week_3.hero import Hero
from abc import ABC, abstractmethod

class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        self.base = base

    def get_stats(self):  # Возвращает итоговые хараетеристики
        # после применения эффекта
        self.base.get_stats

    def get_positive_effects(self):
        self.base.get_negative_effects

    def get_negative_effects(self):
        self.base.get_negative_effects