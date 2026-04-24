from bs4 import BeautifulSoup
from datetime import timedelta
from fastmcp import FastMCP
import requests_cache

session = requests_cache.CachedSession('hamqsl', expire_after=timedelta(hours=3))
mcp = FastMCP('HamQSLServer')

def get_hamqsl() -> str:
    return session.get('https://www.hamqsl.com/solarxml.php').text

def get_hamqsl_field(name: str) -> str:
    response = get_hamqsl()
    soup = BeautifulSoup(response, 'xml')
    return soup.find(name).text.strip()

@mcp.tool()
async def get_solar_flux_index() -> str:
    """
    Retrieve Solar Flux Index (SFI). Measures solar radio emissions at 10.7cm
    (2800 MHz). Values range from 65 to 300+. High values (>100) indicate
    better ionization of the F-layer, supporting higher frequencies (10m–15m)
    for DX.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('solarflux')

@mcp.tool()
async def get_a_index() -> str:
    """
    Retrieve daily A-Index. A linear 24-hour average of geomagnetic stability
    (0–400). Low values (<10) indicate stable conditions; high values mean the
    bands have been disturbed recently.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('aindex')

@mcp.tool()
async def get_k_index() -> str:
    """
    Retrieve current K-Index. A logarithmic 3-hour snapshot of geomagnetic
    activity (0–9). Critical for real-time noise: 0−2 is quiet, 3−4 is unsettled,
    ≥5 is a geomagnetic storm.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('kindex')

@mcp.tool()
async def get_xray() -> str:
    """
    Retrieve solar X-Ray Flux. Measures flare intensity (Class A, B, C, M, X).
    M and X classes cause radio blackouts (SIDs) on the sunlit side of Earth.
    Normal background is A or B.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('xray')

@mcp.tool()
async def get_sunspots() -> str:
    """
    Retrieve Sunspot Number (SN). A daily count of solar spots. Correlates
    strongly with SFI. Higher numbers mean more solar activity and generally
    better HF propagation.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('xray')

@mcp.tool()
async def get_proton_flux() -> str:
    """
    Get Proton Flux. Density of solar protons. High levels cause "Polar Cap
    Absorption" (PCA) events, effectively killing trans-polar HF paths.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('protonflux')

@mcp.tool()
async def get_electron_flux() -> str:
    """
    Get Electron Flux. Density of high-energy electrons. High levels primarily
    affect satellite comms and can correlate with increased noise in the
    E-layer.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('electronflux')

@mcp.tool()
async def get_solar_wind() -> str:
    """
    Get Solar Wind Speed. Measured in km/s. Normal is 300−400 km/s. Speeds >500
    often indicate the arrival of a CME or Coronal Hole stream, leading to
    higher K-indices.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('solarwind')

@mcp.tool()
async def get_magnetic_field() -> str:
    """
    Get Interplanetary Magnetic Field (IMF) Bz component. Measures North-South
    magnetic orientation. Negative (Southward) values allow solar wind to
    "connect" to Earth's field, triggering geomagnetic storms.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('magneticfield')

@mcp.tool()
async def get_helium_line() -> str:
    """
    304 Angstroms (30.4nm). Radiation from ionized helium. A more direct measure
    of F-layer ionization than SFI. Higher is better (>130 for good DX).

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('heliumline')

@mcp.tool()
async def get_aurora() -> str:
    """
    Retrieve Auroral Activity. A 0–10 scale. High values indicate the aurora is
    moving toward lower latitudes. Good for VHF auroral scatter, but usually
    degrades HF.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('aurora')

@mcp.tool()
async def get_geomagfield() -> str:
    """
    Get calculated Geomagnetic State. Descriptive string (e.g., "Quiet",
    "Unsettled", "Minor Storm"). Good for high-level user summaries, although
    the raw value should be displayed as something more user friendly.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('geomagfield')

@mcp.tool()
async def get_signal_noise() -> str:
    """
    Retrieve Estimated Noise Level. Calculates the solar-induced noise floor in
    S-units (e.g., S0−S1). High values mean difficult weak-signal conditions.

    Use this to inform analysis of band conditions, propagation, or space weather.
    """
    return get_hamqsl_field('signalnoise')

