import cv2
import numpy
import discrete_fuzzy_operators.example_operators.implications as implications
import discrete_fuzzy_operators.example_operators.tnorms as tnorms

from discrete_fuzzy_morphology.base.structuring_element import StructuringElement
from discrete_fuzzy_morphology.operators.erosion_dilation.fuzzy_erosion import fuzzy_image_erosion
from discrete_fuzzy_morphology.operators.erosion_dilation.fuzzy_dilation import fuzzy_image_dilation
from discrete_fuzzy_morphology.operators.gradient.fuzzy_gradient import fuzzy_gradient
from discrete_fuzzy_morphology.operators.opening_closing.fuzzy_closing import fuzzy_image_closing
from discrete_fuzzy_morphology.operators.opening_closing.fuzzy_opening import fuzzy_image_opening


if __name__ == "__main__":

    img = cv2.imread(r"assets/binary_image.png", cv2.IMREAD_GRAYSCALE)
    img[img == 236] = 255

    structuring_element_matrix = numpy.array([[219, 219, 219], [219, 255, 219], [219, 219, 219]])
    center = (1, 1)

    se = StructuringElement(structuring_element_matrix, center)

    """
    erosion = fuzzy_image_erosion(image=img, structuring_element=se, iterations=1,
                                  implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255))
    dilation = fuzzy_image_dilation(image=img, structuring_element=se, iterations=1,
                                    t_norm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))
    opening = fuzzy_image_opening(image=img, structuring_element=se, iterations=1,
                                  erosion_implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255),
                                  dilation_tnorm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))
    closing = fuzzy_image_closing(image=img, structuring_element=se, iterations=1,
                                  erosion_implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255),
                                  dilation_tnorm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))
    """
    gradient = fuzzy_gradient(image=img, structuring_element=se, iterations_erosion=1, iterations_dilation=1,
                              erosion_implication=implications.get_implication(implications.Implication.LUKASIEWICZ, n=255),
                              dilation_tnorm=tnorms.get_tnorm(tnorms.Tnorm.LUKASIEWICZ, n=255))

    cv2.imshow("", gradient)
    cv2.waitKey()