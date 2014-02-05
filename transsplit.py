#!/usr/bin/env python

# transsplit.py: Gimp plug-in to split a black and white image into separate layers for Pebble transparency.

# Copyright 2014 by Nathan Fearnley, http://github.com/nfearnley/

import math
import time
from gimpfu import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def transsplit(img, layer):
    pdb.gimp_image_undo_group_start(img)
    
    # Create seperate white and black layers
    splitlayer(img, layer, WHITE, "White")
    splitlayer(img, layer, BLACK, "Black")

    pdb.gimp_selection_clear(img)
    pdb.gimp_image_undo_group_end(img)

def splitlayer(img, layer, color, name):
    pdb.gimp_context_set_foreground(WHITE)
    pdb.gimp_context_set_background(BLACK)
    new_layer = pdb.gimp_layer_copy(layer, False)
    pdb.gimp_image_insert_layer(img, new_layer, None, -1)
    pdb.gimp_item_set_name(new_layer, name)
    pdb.gimp_image_select_color(img, CHANNEL_OP_REPLACE, new_layer, color)
    pdb.gimp_edit_fill(new_layer, FOREGROUND_FILL)
    pdb.gimp_selection_invert(img)
    pdb.gimp_edit_fill(new_layer, BACKGROUND_FILL)
    
register(
    "transsplit",
    "Split a black and white image into separate layers for Pebble transparency",
    "Split a black and white image into separate layers for Pebble transparency",
    "Nathan Fearnley",
    "Nathan Fearnley",
    "2014",
    "<Image>/Filters/Pebble/TransSplit(py)",
    "INDEXEDA",
    [],
    [],
    transsplit)

main()
