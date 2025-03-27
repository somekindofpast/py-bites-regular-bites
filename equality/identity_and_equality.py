# Fix age and same_configuration functions (see test results)
class Car:
    """
    Car class
    -> Have a closer look at lines marked with '# *'
    """

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __eq__(self, other_car):
        return (
            self.model.lower() == other_car.model.lower()
            and self.color.lower() == other_car.color.lower()
        )

    @staticmethod
    def age(days):
        """if / elif / else for exercise sake, if there would
           be more conditions we would use a dict / mapping
        """
        if days == 7:  # *
            return "A week old"
        elif days == 365:  # *
            return "A year old"
        else:
            return "Neither a week, nor a year old"

    @staticmethod
    def has_same_configuration(config1, config2):
        if not isinstance(config1, list) or not isinstance(config2, list):
            raise TypeError()
        for i, j in zip(config1, config2):  # *
            if i != j:
                return False
        return True


# Complete function
def is_same_car_color_and_model(car1, car2):
    """
    Returns true if car1 and car2 are the of same model and color
    """
    if not isinstance(car1, Car) or not isinstance(car2, Car):
        return False
    return car1.model == car2.model and car1.color == car2.color


# Complete function
def is_same_instance_of_car(car1, car2):
    """
    Returns true if car1 and car2 are exactly the same object (instance)
    """
    return car1 is car2


if __name__ == '__main__':
    my_car = Car("Toyota Corolla", "black")
    other_car1 = my_car
    other_car2 = Car("Toyota Corolla", "black")
    other_car3 = Car("Toyota Corolla", "red")
    other_car4 = Car("Porsche Cayenne", "black")
    print(is_same_instance_of_car(my_car, my_car))
    print(is_same_instance_of_car(my_car, other_car1))
    print(is_same_instance_of_car(other_car1, other_car2))