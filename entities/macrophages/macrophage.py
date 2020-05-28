from entities.microbe import Microbe


class Macrophage(Microbe):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None, animation_spd=0, attack_key_frame=0):
        super().__init__(x, y, w, h, spd, hp, dmg, name, animation_spd, attack_key_frame)

    def pos(self):
        self._x += self._spd
