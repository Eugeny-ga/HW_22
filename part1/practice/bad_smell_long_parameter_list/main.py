# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, is_fly, crawl, speed=1):
        self.is_fly = is_fly
        self.crawl = crawl
        self.speed = speed
        if self.is_fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')


    def move(self, x_coord, y_coord, direction):
        speed = self._get_speed()
        if direction == 'UP':
            y_coord += speed
        elif direction == 'DOWN':
            y_coord -= speed
        elif direction == 'LEFT':
            x_coord -= speed
        elif direction == 'RIGTH':
            x_coord += speed

        return (x_coord, y_coord)



    def _get_speed(self):
        if self.is_fly:
            self.speed *= 1.2
        else:
            self.speed *= 0.5
        return self.speed


#     ...
