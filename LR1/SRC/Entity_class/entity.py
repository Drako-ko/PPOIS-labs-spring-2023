
class Entity:

    def __init__(self, idf, _coord2d, _max_hp, _speed, max_age):

        self.entity_idf = idf
        self.coord2d = _coord2d
        self.max_hp = _max_hp
        self.current_hp = _max_hp
        self.speed = _speed
        self._is_alive = True
        self.max_age = max_age
        self.age = 0

    def action(self, map):
        raise NotImplementedError

    def receive_damage(self, damagepts, map):
        damage = min(self.current_hp, damagepts)
        self.current_hp -= damage
        if self.current_hp <= 0:
            self.die(map)
        return damage

    def die(self, map):
        self._is_alive = False
        map.kill(self.coord2d)

    def aging_event(self, map):
        self.age += 1
        if self.age >= self.max_age:
            self.die(map)

    def reproduce(self, map, max_radius=None):
        coords = map.get_nearest_free_tile(self.coord2d, max_radius)
        if coords is not None:
            map.get_entity_list().append(map.get_entity_dict()[self.get_idf()](coords))

    def is_alive(self):
        return self._is_alive

    def get_idf(self):
        return self.entity_idf

    def get_max_hp(self):
        return self.max_hp

    def get_current_hp(self):
        return self.current_hp

    def get_coords(self):
        return self.coord2d

    def __lt__(self, other):
        return self.speed < other.speed

    def __repr__(self):
        return f'{self.entity_idf}'