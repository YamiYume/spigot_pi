from animation_extra import *

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

class SpigotInitialization(SpigotAnimation):
    def construct(self):

        title = Tex(r"Inicializacion Algoritmo Spigot $\pi$", font_size=40)
        self.play_title(title)

        t11 = Tex(r"Digitos de precision: ", r"$d = \text{?}$", font_size=35)
        t12 = Tex(r"Longitud Spigot: ", r"$l = \lfloor \frac{10d}{3} + 1 \rfloor$", font_size=35)
        gt = create_obj_list([t11, t12], LEFT)
        self.play(Create(gt))
        self.wait(1)

        gt_pos1 = lambda x: x.next_to(title, DOWN, buff=0.5).to_edge(LEFT, buff=1)
        self.play(gt_pos1(gt.animate))

        t21 = Tex(r"Digitos de precision: ", r"$d = \text{30}$", font_size=35)
        t22 = Tex(r"Longitud Spigot: ", r"$l = \lfloor \frac{10(30)}{3} + 1 \rfloor = 101$"
                  , font_size=35)
        ngt = create_obj_list([t21, t22], LEFT)
        gt_pos1(ngt)
        self.play(Transform(gt, ngt))
        self.wait(1)

        b = spigot_init(30)    
        spigot_arr1 = self.recreate_spigot_graph(b, 0, 5)
        prov_arr1 = self.recreate_prov_graph(b)
        ga = create_obj_list([spigot_arr1, prov_arr1], RIGHT)
        self.play(Create(ga))
        self.wait(1)

        spigot_arr2 = self.recreate_spigot_graph(b, 96, 5)
        prov_arr2 = self.recreate_prov_graph(b)
        nga = create_obj_list([spigot_arr2, prov_arr2], RIGHT)
        self.play(Transform(ga, nga))
        self.wait(1)

        self.play(ga.animate.next_to(gt, DOWN, buff=0.5).to_edge(LEFT, buff=1))
        self.wait(1)
