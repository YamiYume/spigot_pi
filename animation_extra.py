from manim import *
from manim_data_structures import *
from spigot import *

class SpigotAnimation(Scene):
    def play_title(self, title: Tex):
        self.play(Create(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP + LEFT))
        self.wait(0.5)

    def recreate_spigot_graph(self, b: Buffer, start_index: int, lenght: int) -> MArray:
        data = b[0][start_index: start_index + lenght]
        spigot_arr = MArray(
                self,
                data,
                mob_square_args = {'color': YELLOW_D, 'fill_color': GREEN_D, 'side_length': 0.5},
                mob_value_args = {'color': WHITE, 'font_size': 30},
                mob_index_args = {'color': YELLOW_D, 'font_size': 30},
                label = "spigot_arr",
                index_start = start_index
                )
        return spigot_arr

    def recreate_prov_graph(self, b:Buffer) -> MArray:
        data = b[1]
        data = data + [" "] * ((5 - len(data)) * (len(data) < 5)) 
        prov_arr = MArray(
                self,
                data,
                mob_square_args = {'color': GOLD_A, 'fill_color': PURPLE_E, 'side_length': 0.5},
                mob_value_args = {'color': WHITE, 'font_size': 30},
                mob_index_args = {'color': GOLD_A, 'font_size': 30},
                label = "prov_arr",
                )
        return prov_arr
        
def create_obj_list(objects: list[Mobject], direction) -> VGroup:
    obj_gr = VGroup(*objects)
    obj_gr.arrange(DOWN)
    for obj in objects[1:]:
        obj.align_to(objects[0], direction)
    return obj_gr

