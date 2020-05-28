from entities.entity import Entity
from logic import collisions

WALK_ANIMATION_KEY = "walk"
ATTACK_ANIMATION_KEY = "attack"

WALK_ANIMATION_SPEED = 5
ATTACK_ANIMATION_SPEED = 3


class Microbe(Entity):
    def __init__(self, x, y, w, h, spd, hp, dmg, name=None, animation_spd=0, attack_key_frame=0):
        super().__init__(x, y, w, h, name, WALK_ANIMATION_KEY, animation_spd)
        self._spd = spd
        self._hp = hp
        self._dmg = dmg
        self._attack_key_frame = attack_key_frame
        self._in_front = None
        self._cooldown_timer = 30
        self._cooldown_left = 0

    def is_alive(self):
        return self._hp > 0

    def apply_damage(self, dmg):
        self._hp -= dmg

    def set_in_front(self, in_front):
        self._in_front = in_front

    # subclasses MUST override this function
    def pos(self):
        raise Exception("Something isn't right - you shouldn't be seeing this message!")

    def go(self, display):

        super().go(display)

        if self._current_animation == ATTACK_ANIMATION_KEY:
            if self._animation_cycle == self._attack_key_frame * self._animation_spd:
                self._in_front.apply_damage(self._dmg)
                # debug printing
                # noinspection PyProtectedMember
                print(self._name + " attacks " + self._in_front._name + " for " + str(self._dmg) +
                      " damage! (" + str(self._in_front._hp) + " hp remaining)")
            elif self._animation_cycle == 0 and self._animation_looped:
                self.change_animation(WALK_ANIMATION_KEY, WALK_ANIMATION_SPEED)

        if self._in_front and collisions.rectangles(self.get_rect(), self._in_front.get_rect()):
            if self._cooldown_left <= 0:
                self.change_animation(ATTACK_ANIMATION_KEY, ATTACK_ANIMATION_SPEED)
                self._cooldown_left = self._cooldown_timer
        else:
            self.pos()

        if self._cooldown_left > 0:
            self._cooldown_left -= 1
