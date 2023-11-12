from manim import *
from manim_data_structures import *
from spigot import *

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

class SpigotInitialization(Scene):
    def construct(self):
        title = Tex(r"Inicializacion Algoritmo Spigot $\pi$", font_size=40)
        self.play_title(title)
        q10 = Tex(r"Digitos de precision: ", r"$d = \text{?}$", font_size=35)
        self.play_text_list(q10, 0)
        q20 = Tex(r"Longitud Spigot: ", r"$l = \lfloor \frac{10d}{3} + 1 \rfloor$", font_size=35)
        self.play_text_list(q20, 1)
        q11 = Tex(r"Digitos de precision: ", r"$d = \text{30}$", font_size=35)
        q21 = Tex(r"Longitud Spigot: ", r"$l = \lfloor \frac{10(30)}{3} + 1 \rfloor = 101$"
                  , font_size=35)
        self.transform_text_list(q10, q11, 0)
        self.transform_text_list(q20, q21, 1)
        b = spigot_init(30)
        spigot_arr = self.create_spigot_graphic(b, 0, 5)
        spigot_arr = self.slide_spigot_arr(b, spigot_arr, 96, 5)
        prov_arr = self.create_prov_graphic(b)

    def play_title(self, title):
        self.play(Create(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP).to_edge(LEFT))
        self.wait(0.5)

    def play_text_list(self, text, position: int):
        self.play(Create(text))
        self.wait(1)
        self.play(text.animate.to_edge(LEFT, buff = 1).to_edge(UP, buff = 1.3 + 0.5 * position))
        self.wait(0.5)

    def transform_text_list(self, otext, ntext, position: int):
        align_text_list(ntext, position)
        self.play(TransformMatchingTex(otext, ntext))
        self.wait(1)

    def create_spigot_graphic(self, b: Buffer, r_start: int, lenght: int) -> MArray:
        spigot_arr = MArray(
                    self,
                    b[0][r_start: r_start + lenght],
                    mob_square_args = {'color': YELLOW_D, 'fill_color': GREEN_D, 'side_length': 0.5},
                    mob_value_args = {'color': WHITE, 'font_size': 30},
                    mob_index_args = {'color': YELLOW_D, 'font_size': 30},
                    label = "spigot_arr",
                    index_start = r_start
                    )
        self.play(Create(spigot_arr))
        self.wait(1)
        return spigot_arr

    def create_prov_graphic(self, b:Buffer) -> MArray:
        if len(b[1]) < 5:
            rep = b[1] + [" "] * (5 - len(b[1]))
        else:
            rep = b[1]
        prov_arr = MArray(
                    self,
                    rep,
                    mob_square_args = {'color': GOLD_A, 'fill_color': PURPLE_E, 'side_length': 0.5},
                    mob_value_args = {'color': WHITE, 'font_size': 30},
                    mob_index_args = {'color': GOLD_A, 'font_size': 30},
                    label = "prov_arr",
                    )
        prov_arr.shift(2 * DOWN)
        self.play(Create(prov_arr))
        self.wait(1)
        return prov_arr
        

    def slide_spigot_arr(self, b: Buffer, spigot_arr: MArray, n_start: int, lenght) -> MArray:
        n_spigot_arr = MArray(
                    self,
                    b[0][n_start: n_start + lenght],
                    mob_square_args = {'color': YELLOW_D, 'fill_color': GREEN_D, 'side_length': 0.5},
                    mob_value_args = {'color': WHITE, 'font_size': 30},
                    mob_index_args = {'color': YELLOW_D, 'font_size': 30},
                    label = "spigot_arr",
                    index_start = n_start
                    )
        self.play(Transform(spigot_arr, n_spigot_arr))
        return n_spigot_arr

def align_text_list(text, position: int):
    text.to_edge(LEFT, buff = 1).to_edge(UP, buff = 1.3 + 0.5 * position)

