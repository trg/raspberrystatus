class Util:
    @staticmethod
    def centerString(the_string, width):
        current_width = len(the_string) 
        pad_left = False
        while current_width < width:
            if pad_left:
                the_string = "".join([" ", the_string])
            else:
                the_string = "".join([the_string, " "])
            current_width += 1
            pad_left = not pad_left
        return the_string
