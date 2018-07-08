import os
import csv

class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.set_body_whl(body_whl)

    def set_body_whl(self, value):
        default_whl = list(map(lambda x: float(x), [0, 0, 0]))
        try:
            list_whl = list(map(lambda x: float(x), value.split('x')))
            if len(list_whl) == 3:
                self.body_width, self.body_height, self.body_length = list_whl
            else:
                self.body_width, self.body_height, self.body_length = default_whl
        except:
            self.body_width, self.body_height, self.body_length = default_whl

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_params_by_type(car_params):
    try:
        result = [car_params['car_type'],
                  car_params['brand'],
                  car_params['photo_file_name'],
                  car_params['carrying']]
    except:
        return False

    if car_params['car_type'] == 'car':
        result.append(car_params['passenger_seats_count'])
    elif car_params['car_type'] == 'truck':
        result.append(car_params['body_whl'])
    elif car_params['car_type'] == 'spec_machine':
        result.append(car_params['extra'])

    return result


def get_car_list(csv_filename):
    car_list = []

    header = ['car_type', 'brand', 'passenger_seats_count', 'photo_file_name', 'body_whl', 'carrying', 'extra']

    try:
        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                car_params = dict(zip(header, row))
                car_params_by_type = get_car_params_by_type(car_params)

                if 'car_type' not in car_params:
                    continue
                elif car_params['car_type'] == 'car':
                    car_list.append(Car(*car_params_by_type))
                elif car_params['car_type'] == 'truck':
                    car_list.append(Truck(*car_params_by_type))
                elif car_params['car_type'] == 'spec_machine':
                    car_list.append(SpecMachine(*car_params_by_type))

        return car_list
    except IOError:
        return ""



for i in get_car_list('cars.csv'):
    print(i.car_type, i.brand, i.photo_file_name, i.carrying)
