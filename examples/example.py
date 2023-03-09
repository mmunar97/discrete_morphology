import cv2
import numpy
import discrete_fuzzy_operators.example_operators.implications as implications
import discrete_fuzzy_operators.example_operators.tnorms as tnorms

from discrete_morphology.base.structuring_element import StructuringElement
from discrete_morphology.operators.erosion_dilation.discrete_erosion import discrete_erosion
from discrete_morphology.operators.erosion_dilation.discrete_dilation import discrete_dilation
from discrete_morphology.operators.gradient.discrete_gradient import discrete_gradient
from discrete_morphology.operators.opening_closing.discrete_closing import discrete_closing
from discrete_morphology.operators.opening_closing.discrete_opening import discrete_opening


if __name__ == "__main__":

    img = cv2.imread(rf"assets/motorbike.png", cv2.IMREAD_GRAYSCALE)

    structuring_element_matrix = numpy.array([[219, 219, 219], [219, 255, 219], [219, 219, 219]])
    center = (1, 1)

    se = StructuringElement(structuring_element_matrix, center)

    erosion = discrete_erosion(image=img, structuring_element=se, iterations=1,
                               implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255))
    dilation = discrete_dilation(image=img, structuring_element=se, iterations=1,
                                 t_norm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))
    opening = discrete_opening(image=img, structuring_element=se, iterations=1,
                               erosion_implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255),
                               dilation_tnorm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))
    closing = discrete_closing(image=img, structuring_element=se, iterations=1,
                               erosion_implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255),
                               dilation_tnorm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))
    gradient = discrete_gradient(image=img, structuring_element=se, iterations_erosion=1, iterations_dilation=1,
                                 erosion_implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255),
                                 dilation_tnorm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))

