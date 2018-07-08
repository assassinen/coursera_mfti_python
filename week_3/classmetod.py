# class CarBase:
#     ix_car_type = 0
#     ix_brand = 1
#     ix_passenger_seats_count = 2
#     ix_photo_file_name = 3
#     ix_body_whl = 4
#     ix_carrying = 5
#     ix_extra = 6
#
#     def __init__(self, brand, photo_file_name, carrying):
#         self.brand = brand
#         self.photo_file_name = photo_file_name
#         self.carrying = float(carrying)

class Car():
    """Класс легковой автомобиль"""

    ix_car_type = 0
    ix_brand = 1
    ix_passenger_seats_count = 2
    ix_photo_file_name = 3
    ix_body_whl = 4
    ix_carrying = 5
    ix_extra = 6

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        # super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)

    @classmethod
    def from_tuple(cls, row):
        """ Метод для создания экземпляра легкового автомобиля
            из строки csv-файла"""

        return cls(
            row[cls.ix_brand],
            row[cls.ix_photo_file_name],
            row[cls.ix_carrying],
            row[cls.ix_passenger_seats_count],
        )


s = ('car', 'Nissan xTtrail', 4, 'f1.jpeg', '', '2.5')
s_class = Car.from_tuple(s)
print(s_class, s_class.brand, s_class.carrying)