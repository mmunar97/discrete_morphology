import cv2
import numpy

from discrete_fuzzy_operators.builtin_operators.discrete.tnorms import TnormExamples
from discrete_fuzzy_operators.builtin_operators.discrete.implications import DiscreteImplicationExamples

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
                               implication=DiscreteImplicationExamples.get_discrete_implication(DiscreteImplicationExamples.LUKASIEWICZ, n=255))
    dilation = discrete_dilation(image=img, structuring_element=se, iterations=1,
                                 conjunction=TnormExamples.get_tnorm(TnormExamples.LUKASIEWICZ, n=255))
    opening = discrete_opening(image=img, structuring_element=se, iterations=1,
                               erosion_implication=DiscreteImplicationExamples.get_discrete_implication(DiscreteImplicationExamples.LUKASIEWICZ, n=255),
                               dilation_tnorm=TnormExamples.get_tnorm(TnormExamples.LUKASIEWICZ, n=255))
    closing = discrete_closing(image=img, structuring_element=se, iterations=1,
                               erosion_implication=DiscreteImplicationExamples.get_discrete_implication(DiscreteImplicationExamples.LUKASIEWICZ, n=255),
                               dilation_conjunction=TnormExamples.get_tnorm(TnormExamples.LUKASIEWICZ, n=255))
    gradient = discrete_gradient(image=img, structuring_element=se, iterations_erosion=1, iterations_dilation=1,
                                 erosion_implication=DiscreteImplicationExamples.get_discrete_implication(DiscreteImplicationExamples.LUKASIEWICZ, n=255),
                                 dilation_conjunction=TnormExamples.get_tnorm(TnormExamples.LUKASIEWICZ, n=255))

