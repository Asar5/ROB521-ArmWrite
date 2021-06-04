#!/usr/bin/env python3


class Draw:
    """
    This class draws the letters provided by the user input,
    taking into account workspace area and spacing between letters
    """
    def __init__(self, list_of_chars, boundary_limits, letter_limits, gap, start_spacing):
        """
        Saves the input into a class attribute
        :param list_of_chars: Ex: ['a', 'p', 'p', 'l', 'e']
        :param boundary_limits: [(x1, y1), (x2, y2)] Boundary inside which user input has to fit .
        (x1, y1): bottom left coordinates, (x2, y2): Upper right coordinates
        boundary_limits values should be in terms of robots coordinate system, in cms
                 _______________.(x2, y2)
                |                |
                |                |
                |._______________|
        (x1, y1)

        :param  letter_limits: (breadth, ratio) Bounding box inside which every letter will be written.
        breadth = breadth of box (cms), ratio = length:breadth.
        :param gap: gap we want to leave between letters (in cms).
        :param start_spacing: (r, u) What space we want to maintain from the right and upper boundary (in cms) (we are writing
        upside-down). NO NEGATIVE VALUES. JUST A MEASURE OF LENGTH
        """
        self.num_of_chars = len(list_of_chars)
        self.boundary_limits = boundary_limits
        self.x1 = boundary_limits[0][0]
        self.y1 = boundary_limits[0][1]
        self.x2 = boundary_limits[1][0]
        self.y2 = boundary_limits[1][1]

        # left is towards x1, right is towards x2, upper is towards y2, lower is towards y1
        self.mid_upper = (self.x1 + (self.x2 - self.x1)/2, self.y2)
        self.mid_lower = (self.mid_upper[0], self.y1)
        self.mid_left = (self.x1, self.y1 + (self.y2 - self.y1)/2)
        self.mid_right = (self.x2, self.y1 + (self.y2 - self.y1)/2)
        self.start_coords = (10, 20)

        self.letter_width = letter_limits[0]
        self.letter_len = letter_limits[1]*self.letter_width

        self.all_coords_list = []

        self.gap = gap

        self.start_spacing = start_spacing

    def _det_start_coords(self):
        """
        This method decides where to start drawing based on the mid points
        :return: self.start_coords : Coords to start writing from
        """
        self.start_spacing = (abs(self.start_spacing[0]), abs(self.start_spacing[1]))
        space_r = self.start_spacing[0]
        space_up = self.start_spacing[1]
        x_start = self.x2 - space_r
        y_start = self.y2 - space_up
        self.start_coords = (x_start, y_start)

        return self.start_coords

    def det_coords_all_letters(self):
        """
        This function returns a list  which is of the same length as the number of characheters.
        The list consists of starting coordinates of every letter that needs to be drawn, with the correct spacing
        :return: self.all_coords_list: List of starting coords of each letter
        """
        self.all_coords_list = []
        for i in range(0, self.num_of_chars):
            if i == 0:
                (x_start, y_start) = self._det_start_coords()
                (x, y) = (x_start, y_start)

            else:
                y = y_start
                x = x - self.letter_width - self.gap
            if x <= self.x1:
                print("Going out of boundary for {}th letter! Please change conditions and restart".format(i+1))
                raise ValueError
            self.all_coords_list.append((x, y))

        return self.all_coords_list


if __name__ == '__main__':
    word_to_draw = ['A', 'S', 'S', 'H']#, 'O', 'L', 'E']
    workspace_limits = [(-15, 12), (15, 28)]
    letter_bounding_box = (3, 5/3)
    gap_btw_letters = 1
    distance_from_boundaries = (5, 8)

    trial_draw = Draw(word_to_draw, workspace_limits, letter_bounding_box, gap_btw_letters, distance_from_boundaries)

    start_at = trial_draw.det_coords_all_letters()
    print(start_at)