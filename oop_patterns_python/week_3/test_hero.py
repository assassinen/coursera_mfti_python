from oop_patterns_python.week_3.hero_effects import *
from oop_patterns_python.week_3.hero import Hero


test_hero = Hero()
# print(test_hero.get_stats())
print()
print(1, test_hero.get_positive_effects())
print(6, test_hero.get_negative_effects())
print(test_hero.get_stats())

test_hero = Berserk(test_hero)
print()
print(2, test_hero.get_positive_effects())
print(6, test_hero.get_negative_effects())
print(test_hero.get_stats())

test_hero = Berserk(test_hero)
print()
print(3, test_hero.get_positive_effects())
print(6, test_hero.get_negative_effects())
print(test_hero.get_stats())
# test_hero = Blessing(test_hero)

test_hero = Blessing(test_hero)
print()
print(4, test_hero.get_positive_effects())
print(6, test_hero.get_negative_effects())
print(test_hero.get_stats())

# test_hero = test_hero.base.base
# print()
# print(5, test_hero.get_positive_effects())
# print(test_hero.get_stats())


test_hero = Weakness(test_hero)
print()
print(6, test_hero.get_positive_effects())
print(6, test_hero.get_negative_effects())
print(test_hero.get_stats())
