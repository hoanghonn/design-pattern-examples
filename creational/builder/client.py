"""
This is the client where everything starts. The director is in charge of taking the concrete builder and return the final product.
This pattern will encapsulates and hides the process of building the object from client, therefore, same construction process can create different representations.
"""

import director as d
import builder as builder

if __name__ == "__main__":
    concreate_builder = builder.CinematicFilmBuilder()
    director = d.FilmDirector(concreate_builder)

    # this function construct the concreate builder with step-by-step instructions
    director.construct(isActionType=True)

    # return the product
    concreate_builder.get_result()
