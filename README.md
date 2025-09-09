## MPL Styler



<!-- ![Tests](https://github.com/rngKomorebi/LinoSPAD2/actions/workflows/tests.yml/badge.svg)
![Documentation](https://github.com/rngKomorebi/LinoSPAD2/actions/workflows/documentation.yml/badge.svg) -->
<!-- ![PyPI - Version](https://img.shields.io/pypi/v/daplis) -->
<!-- ![PyPI - License](https://img.shields.io/pypi/l/daplis) -->

## Introduction

This package is a small collection of different style for the plots produced
using matplotlib, including one for paper/presentation/poster-ready graphs.

Currently available styles are:

- 'sci_pure' for clean and paper-ready plots;
- 'sci_faded' for kind of a sun-faded look with soft colors;
- 'night_wave' for eye-pleasing plots with dark background and neon colors.

The last one is heavily inspired by the 'cyberpunk' style (https://github.com/dhaitz/mplcyberpunk).

There are also a couple of functions for use mostly with the 'night_wave' style for adding glow to and/or a gradient under lines, bars and histograms.

## Installation and usage

Working on a pypi distro. So for now the path of least resistance would be to download the repo and install locally; after cd-ing to where the package is located, run:

```
pip install -e .
```

and you should be good to go. Now you can import the package besides the rest and the styles will be available right away.

```
from matplotlib import pyplot as plt
import mpl_styler

plt.style.use("sci_faded")

plt.plot([i for i in range(30)])
```

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/sci_faded_import_example.png" width="700">

## Examples

Below are shown all the available styles and functions.

### Clean scientific style: sci_pure

Publication-ready plots: clean, vibrant, w/b-ready.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/sci_pure.png" width="700">

### Sun-faded scientific style: sci_faded

Sun-faded-paper type of plots.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/sci_faded.png" width="700">

### Neon style: night_wave

Neon and synthwave kind of vibe.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_style.png" width="700">

This is where the functions come into play and make this style shine. We can make the lines glow.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_style%2Bneon.png" width="700">

We can also add a gradient under each line.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_style%2Bneon%2Bgrad.png" width="700">

Bar-plot with just this style is childish.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_bars.png" width="700">

Add a gradient - now we're talking.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_bars%2Bgrad.png" width="700">

Histogram is the same as bar plots: ok-ish.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_hist.png" width="700">

Add a gradient and voila.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_hist%2Bgrad.png" width="700">

The glow effect can also be added to the scatter plot giving the points a star-like shine.

<img src="https://github.com/rngKomorebi/mpl_styler/blob/main/examples/figures/night_wave_scatter.png" width="700">

## Acknowledgment

Shout-out to Dominik Haitz who's written the mindblowing 'mplcyberpunk' package (https://github.com/dhaitz/mplcyberpunk) and the functions from which I adapted for this package. Also check out John Garrett's 'SciencePlots' (https://github.com/garrettj403/SciencePlots) for publication-ready plots.

## License and contact info

This package is available under the MIT license. See LICENSE for more
information. If you'd like to contact me, the author, feel free to
write at sergei.kulkov23@gmail.com.
