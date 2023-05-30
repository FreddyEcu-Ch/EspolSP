# Create POES function

def poes(area, h, poro, swi, boi):
    """

    Parameters
    ----------
    area: Drainage area (acres)
    h: Thickness
    poro: Porosity (fraction)
    swi: Water saturation (fraction)
    boi: Oil volume factor (rb/stb)

    Returns
    -------
    poes: bbl
    """

    Poes = (7758 * area * h * poro * (1 - swi)) / boi
    return Poes
