from manim import *
from manim_data_structures import *
from spigot import *

class MyArray(MArray):
    def __init__(self, *args, **kwargs):
        super(MyArray, self).__init__(*args, **kwargs)
        self.start_index = kwargs["index_start"]
        self.length = len(args[1])

class SpigotAnimation(Scene):
    def play_title(self, title: Tex):
        self.play(Create(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP + LEFT))
        self.wait(0.5)

    def recreate_spigot_graph(self, b: Buffer, start_index: int, length: int) -> MyArray:
        data = b[0][start_index: start_index + length]
        spigot_arr = MyArray(
                self,
                data,
                mob_square_args = {'color': YELLOW_D, 'fill_color': GREEN_D, 'side_length': 0.8},
                mob_value_args = {'color': WHITE, 'font_size': 30},
                mob_index_args = {'color': YELLOW_D, 'font_size': 30},
                label = "spigot_arr",
                index_start = start_index
                )
        return spigot_arr

    def recreate_prov_graph(self, b:Buffer, min_length: int) -> MyArray:
        data = b[1]
        data = data + [" "] * ((min_length - len(data)) * (len(data) < min_length)) 
        prov_arr = MyArray(
                self,
                data,
                mob_square_args = {'color': GOLD_A, 'fill_color': PURPLE_E, 'side_length': 0.8},
                mob_value_args = {'color': WHITE, 'font_size': 30},
                mob_index_args = {'color': GOLD_A, 'font_size': 30},
                label = "prov_arr",
                index_start = 0
                )
        return prov_arr

    def create_abs_pointer(self, arr: MyArray, index: int, label: str) -> MArraySlidingWindow:
        return MArraySlidingWindow(self, arr, index - arr.start_index, 1, label,
                                   mob_label_args={"font_size": 30})
        
def create_obj_list(objects: list[Mobject], direction) -> VGroup:
    obj_gr = VGroup(*objects)
    obj_gr.arrange(DOWN)
    for obj in objects[1:]:
        obj.align_to(objects[0], direction)
    return obj_gr

def create_obj_list_s(objects: list[Mobject], direction, spacing) -> VGroup:
    obj_gr = VGroup(*objects)
    obj_gr.arrange(DOWN, buff=spacing)
    for obj in objects[1:]:
        obj.align_to(objects[0], direction)
    return obj_gr
