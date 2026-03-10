def sort(width: float, height: float, length: float, mass: float) -> str:
    """Dispatch packages to the correct stack based on volume and mass.

    Args:
        width: Package width in centimeters.
        height: Package height in centimeters.
        length: Package length in centimeters.
        mass: Package mass in kilograms.

    Returns:
        The name of the stack: "STANDARD", "SPECIAL", or "REJECTED".
    """
    # Validate inputs
    if width < 0 or height < 0 or length < 0:
        raise ValueError("Dimensions must be non-negative")
    if mass < 0:
        raise ValueError("Mass must be non-negative")

    volume = width * height * length

    # Bulky if volume >= 1,000,000 cm³ or any single dimension >= 150 cm
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150

    # Heavy if mass >= 20 kg
    is_heavy = mass >= 20

    # Both bulky and heavy -> rejected
    if is_bulky and is_heavy:
        return "REJECTED"
    # Either bulky or heavy -> needs special handling
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
