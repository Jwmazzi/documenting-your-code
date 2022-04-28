from typing import Dict, Union, Literal

import requests
from requests.exceptions import RequestException


def generate_random_fact(output_format: str, language: str) -> Union[Dict, str]:

    """ Returns a random fact from uselessfacts

    Based on the laguage and format provided, this function will return your fact or
    raise a RequestException if a 200 is not returned from uselessfacts.

    Args:
        output_format: Format options supported: "html", "json", "txt", "md"
        language: Language options supported: "en", "de"

    Returns:
        Dictionary or String based on output_format

    Raises:
        ValueError - When output_format or language is not supported
        RequestException - When 200 not returned from request

    """

    # Only these 2 languages are supported as of 4/28/22
    if language not in {"en", "de"}:
        raise ValueError(f"{language} is not supported.")

    if output_format not in {"html", "json", "txt", "md"}:
        raise ValueError(f"{output_format} is not supported.")

    # Requests "params" are ignored when calling uselessfacts
    response = requests.get(
        f"https://uselessfacts.jsph.pl/random.{output_format}?language={language}"
    )

    if response.status_code == 200:
        if output_format == "json":
            fact = response.json()
        else:
            fact = response.text
    else:
        raise RequestException(
            f"Something went wrong. Request returned status {response.status_code}."
        )

    return fact
