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
        t22 = Tex(r"Longitud Spigot: ", r"$l = \lfloor \frac{10(30)}{3} + 1 \rfloor = 101$",
                  font_size=35)
        ngt = create_obj_list([t21, t22], LEFT)
        gt_pos1(ngt)
        self.play(Transform(gt, ngt))
        self.wait(1)

        b = spigot_init(30)
        spigot_arr_length = 5

        spigot_arr1 = self.recreate_spigot_graph(b, 0, spigot_arr_length)
        prov_arr1 = self.recreate_prov_graph(b, spigot_arr_length)
        ga = create_obj_list([spigot_arr1, prov_arr1], RIGHT)
        self.play(Create(ga))
        self.wait(1)

        spigot_arr2 = self.recreate_spigot_graph(b, 96, spigot_arr_length)
        prov_arr2 = self.recreate_prov_graph(b, spigot_arr_length)
        nga = create_obj_list([spigot_arr2, prov_arr2], RIGHT)
        self.play(Transform(ga, nga))
        self.wait(1)

        self.play(ga.animate.next_to(gt, DOWN, buff=0.5).to_edge(LEFT, buff=1))
        self.wait(1)

        l1 = Tex(r"- Inicializar el Spigot y la lista (o variables)\\",
                 "de digitos provisionales",
                 font_size = 30, tex_environment="flushleft")
        l2 = Tex(r"- Multiplicar cada posicion del spigot por\\",
                 r"10 para traer en frente la siguiente cifra\\",
                 "decimal en base $10^1$", font_size = 30, tex_environment="flushleft")
        l3 = Tex(r"- Llevar cada posicion a fraccion propia con\\",
                 "respecto al radix para extraer el digito",
                font_size=30, tex_environment="flushleft")
        l4 = Tex(r"- Extraer el digito y procesarlo con\\",
                 "respecto a los digitos provisionales",
                 font_size = 30, tex_environment="flushleft")
        gl = create_obj_list([l1, l2, l3, l4], LEFT)
        gl.next_to(gt, RIGHT, buff=0.8).align_to(gt, UP)

        self.play(Create(gl))
        self.wait(1.5)

class SpigotProcessing(SpigotAnimation):
    def construct(self):
        title = Tex(r"Procesamiento Del Spigot $\pi$", font_size=40)
        self.play_title(title)
        cycle = Tex(r"Ciclo 1", font_size=40)
        pos_cycle = lambda x: x.to_edge(LEFT + DOWN)
        pos_cycle(cycle)
        self.play(Create(cycle))

        b = spigot_init(30)
        spigot_arr_length = 7
        spigot_arr = self.recreate_spigot_graph(b, 4, spigot_arr_length)
        self.play(Create(spigot_arr))
        self.wait(1)
        
        b = radix_multiplication(b)
        n_spigot_arr = self.recreate_spigot_graph(b, 4, spigot_arr_length)
        self.play(Transform(spigot_arr, n_spigot_arr))
        self.wait(1)
        
        pos_arr = lambda x: x.next_to(title, DOWN, buff=2).to_edge(LEFT)
        self.play(pos_arr(spigot_arr.animate))
        self.wait(1)
        
        pos_t = Tex("index: ", r"$i = \text{?}$", font_size=35)
        val_t = Tex("value: ", r"$v = \text{?}$", font_size=35)
        div_t = Tex("divisor: ", r"$d = 2i + 1$", font_size=35)
        eu_t = Tex("euclid: ", r"$v = qd + r$", font_size=35)
        c_t = Tex("carry: ", r"$c = qi$", font_size=35)
        f_t = Tex("radix ", r"$\frac{i}{d}$",
                  font_size=35)
        vl = create_obj_list([pos_t, div_t, f_t, val_t, eu_t, c_t], LEFT)
        pos_v = lambda x: x.align_to(spigot_arr, UP).to_edge(RIGHT, buff=1)
        pos_v(vl)
        self.play(Create(vl))
        self.wait(1)

        r_p = self.create_abs_pointer(spigot_arr, 10, "r")
        c_p = self.create_abs_pointer(spigot_arr, 9, "c")
        self.play(Create(r_p), Create(c_p))
        
        for i in range(10, 0, -1):
            b, r, c = self.spigot_processing_variables(vl, b, i, pos_v)
            self.spigot_processing_pointers(spigot_arr, r_p, c_p, i, r, c)
            self.wait(1)
            self.spigot_processing_graph(spigot_arr, b, i, pos_arr)
        
        self.remove(r_p, c_p)
        n_cycle = Tex(r"Ciclo 2", font_size=40)
        pos_cycle(n_cycle)
        self.play(Transform(cycle, n_cycle))
        self.wait(1)
        b = spigot_init(30)
        b, _ = adv_by_cycles(b, 1)
        b = radix_multiplication(b)
        n_spigot_arr = self.recreate_spigot_graph(b, 94, spigot_arr_length)
        pos_arr(n_spigot_arr)
        self.play(Transform(spigot_arr, n_spigot_arr))
        spigot_arr.start_index = 94
        r_p = self.create_abs_pointer(spigot_arr, 100, "r")
        c_p = self.create_abs_pointer(spigot_arr, 99, "c")
        self.play(Create(r_p), Create(c_p))
        self.wait(1)
        
        for i in range(100, 94, -1):
            b, r, c = self.spigot_processing_variables(vl, b, i, pos_v)
            self.spigot_processing_pointers(spigot_arr, r_p, c_p, i, r, c)
            self.wait(1)
            self.spigot_processing_graph(spigot_arr, b, i, pos_arr)

        self.remove(r_p, c_p)
        self.wait(1)

    def spigot_processing_variables(
            self, vl: VGroup, b: Buffer, i: int, pos_v
            ) -> tuple[Buffer, int, int]:
        v = b[0][i]
        d = 2 * i + 1
        b, q, r, c = norm_per_digit(b, i)
        pos_t = Tex("index: ", r"$i = " + str(i) + "$", font_size=35)
        val_t = Tex("value: ", r"$v = " + str(v) + "$", font_size=35)
        div_t = Tex("divisor: ", r"$d = " + str(d) + "$", font_size=35)
        eu_t = Tex("euclid: ", r"$v = (" + str(q) +")(" + str(d) + ") + " + str(r) + r"$", 
                   font_size=35)
        c_t = Tex(
                "carry: ",
                r"$c = (" + str(q) + ")(" + str(i) + ") = " + str(c) + "$",
                font_size=35)
        f_t = Tex("radix ", r"$\frac{" + str(i) + "}{" + str(d) + "}$",
                  font_size=35)
        nvl = create_obj_list([pos_t, div_t, f_t, val_t, eu_t, c_t], LEFT)
        pos_v(nvl)
        self.play(Transform(vl, nvl))
        return b, r, c

    def spigot_processing_graph(
            self, spigot_arr: MyArray, b:Buffer, i: int, pos_arr
            ):
        start_index = spigot_arr.start_index
        length = spigot_arr.length
        n_spigot_arr = self.recreate_spigot_graph(b, start_index, length)
        pos_arr(n_spigot_arr)
        self.play(Transform(spigot_arr, n_spigot_arr))
        self.wait(1)
        if not i - 1 == start_index:
            return
        start_index = (start_index - length + 1) * (start_index > length)
        n_spigot_arr = self.recreate_spigot_graph(b, start_index, length)
        pos_arr(n_spigot_arr)
        self.play(Transform(spigot_arr, n_spigot_arr))
        spigot_arr.start_index = start_index
    
    def spigot_processing_pointers(
            self, spigot_arr: MyArray, r_p: MArraySlidingWindow, c_p: MArraySlidingWindow,
            i: int, r: int, c: int
            ):
        print(spigot_arr.start_index, i)
        c_p.shift_to_elem(i - 1 - spigot_arr.start_index)
        c_p.update_mob_label(
                "+" + str(c),
                mob_label_args={"font_size": 25}
                )
        r_p.shift_to_elem(i - spigot_arr.start_index)
        r_p.update_mob_label(
                str(r),
                mob_label_args={"font_size": 25}
                )

class SpigotProvDigits(SpigotAnimation):
    def construct(self):
        title = Tex(r"extraccion de digitos provisionales" font_size = 40)
        self.play_title(title)
