#!/usr/bin/env python3

from draw_letter import Draw
import numpy as np


def transform_coords_to_start_pos(draw, letter_array):
    """
    This
    :param draw:
    :param letter_array:
    :return:
    """
    start_coords = draw.start_coords[0], draw.start_coords[1], 0
    add_to_array = np.asarray(start_coords) - np.asarray(draw.letter_origin)
    new_array = letter_array + add_to_array
    print(new_array)


if __name__ == '__main__':
    word_to_draw = ['A', 'S', 'S', 'H']
    workspace_limits = [(-15, 12), (15, 28)]
    letter_bounding_box = (3, 5/3, (0, 20, 8))
    gap_btw_letters = 1
    distance_from_boundaries = (5, 8)

    h = np.array([[0,20, 8], [0, 18, 8], [1, 18, 8]])

    trial_draw = Draw(word_to_draw, workspace_limits, letter_bounding_box, gap_btw_letters, distance_from_boundaries)

    transform_coords_to_start_pos(trial_draw, h)