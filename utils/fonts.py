import tkinter.font as tkfont


def _available_families(root):
    try:
        return set(tkfont.families(root))
    except Exception:
        return set()


def _choose_family(root):
    fams = _available_families(root)
    # Preferred condensed / narrow serif-free families first
    for name in (
        "Arial",
        "Arial Narrow",
        "Arial Condensed MT",
        "Segoe UI",
        "Helvetica",
        "Liberation Sans",
        "DejaVu Sans",
        "Noto Sans",
    ):
        if name in fams:
            return name
    # Last resort: use a widely available sans-serif family
    return "Arial"


def get_font(root, size=12, weight="normal"):
    """Return a font tuple (family, size, weight) chosen to work across OSes.

    Pass the Tk root or a widget (it will be used to probe available families).
    """
    fam = _choose_family(root)
    # Normalize weight: treat common heavy weights as 'bold', otherwise 'normal'
    if weight and weight.lower() in ("bold", "heavy", "black"):
        resolved_weight = "bold"
    else:
        resolved_weight = "normal"

    if fam:
        return (fam, size, resolved_weight)
    # If we couldn't determine a family, return Tk default font name tuple
    return (None, size, resolved_weight)


def apply_default(root, base_size=12):
    """Configure Tk named fonts to use a consistent family and base size.

    Call this once after creating the main `Tk()` instance.
    """
    fam = _choose_family(root)
    if fam is None:
        fam = "Arial"
    names = [
        "TkDefaultFont",
        "TkTextFont",
        "TkMenuFont",
        "TkHeadingFont",
        "TkCaptionFont",
        "TkSmallCaptionFont",
        "TkIconFont",
        "TkTooltipFont",
    ]
    for name in names:
        try:
            f = tkfont.nametofont(name)
            f.configure(family=fam, size=base_size)
        except Exception:
            # ignore fonts that aren't available in this Tk build
            pass
