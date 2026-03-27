import os

import matplotlib.pyplot as plt
import matplotlib.style as style

# Path to the 'styles' folder inside the package
_styles_dir = os.path.join(os.path.dirname(__file__), "styles")

# Read all .mplstyle files in the directory
_stylesheets = style.core.read_style_directory(_styles_dir)

# Update Matplotlib's style library with your styles
style.core.update_nested_dict(style.library, _stylesheets)

# Update available styles so they appear in style.available
style.core.available[:] = sorted(style.library.keys())


def use(style_name: str) -> None:
    """Apply a style and return the pyplot module ready to use.

    Example
    -------
    import mpl_styler as mst
    plt = mst.use("sci_pure")
    plt.plot(...)
    """
    plt.style.use(["default", style_name])
    return plt
