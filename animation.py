from manim import *
from manim_data_structures import *

class TitleScene(Scene):
    def construct(self):
        title = Tex(r"Algoritmo Spigot $\pi$", font_size=80)
        name1 = Tex(r"Salinas Rico, Sofia", font_size=50).shift(1 * DOWN)
        name2 = Tex(r"Rodríguez Rubio, Juan Antonio", font_size=50).shift(1.5 * DOWN)
        name3 = Tex(r"Torres Gutierrez, Pawell Steven", font_size=50).shift(2 * DOWN)
        self.play(Create(title))
        self.wait(1.5)
        self.play(Create(name1))
        self.play(Create(name2))
        self.play(Create(name3))
        self.wait(1.5)
