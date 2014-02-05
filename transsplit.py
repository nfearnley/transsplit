#!/usr/bin/env python

# transsplit.py: Gimp plug-in to split a black and white image into separate layers for Pebble transparency.

# Copyright 2014 by Nathan Fearnley, http://github.com/nfearnley/

import math
import time
from gimpfu import *

def transsplit(img, layer):
    pdb.gimp_image_undo_group_start(img)
    
    # Create white layer
    white_layer = pdb.gimp_layer_copy(layer, False)
    pdb.gimp_image_insert_layer(img, white_layer, None, -1)
    pdb.gimp_item_set_name(white_layer, "White")
    pdb.gimp_message("Test")
    pdb.gimp_image_select_color(img, CHANNEL_OP_REPLACE, white_layer, (255, 255, 255))
    pdb.gimp_context_set_foreground((0, 0, 0))
    pdb.gimp_edit_fill(white_layer, FOREGROUND_FILL)
    pdb.gimp_selection_invert(img)
    pdb.gimp_edit_clear(white_layer)
    
    # Create black layer
    black_layer = pdb.gimp_layer_copy(layer, False)
    pdb.gimp_image_insert_layer(img, black_layer, None, -1)
    pdb.gimp_item_set_name(white_layer, "Black")
    pdb.gimp_image_select_color(img, CHANNEL_OP_REPLACE, black_layer, (0, 0, 0))
    pdb.gimp_selection_invert(img)
    pdb.gimp_edit_clear(black_layer)

    pdb.gimp_selection_clear(img)
    pdb.gimp_image_undo_group_end(img)

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
