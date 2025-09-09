import os

import matplotlib as mpl

import mpl_styler

# Path to the 'styles' folder inside the package
_styles_dir = os.path.join(mpl_styler.__path__[0], "styles")

# Read all .mplstyle files in the directory
_stylesheets = mpl.style.core.read_style_directory(_styles_dir)

# Update Matplotlib's style library with your styles
mpl.style.core.update_nested_dict(mpl.style.library, _stylesheets)

# Update available styles so they appear in mpl.style.available
mpl.style.core.available[:] = sorted(mpl.style.library.keys())
