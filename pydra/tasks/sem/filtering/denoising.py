"""
Autogenerated file - DO NOT EDIT
If you spot a bug, please report it on the mailing list and/or change the generator.
"""

import attr
from nipype.interfaces.base import (
    Directory,
    File,
    InputMultiPath,
    OutputMultiPath,
    traits,
)
from pydra import ShellCommandTask
from pydra.engine.specs import SpecInfo, ShellSpec


class CurvatureAnisotropicDiffusion:
    """
    title: Curvature Anisotropic Diffusion
    category: Filtering.Denoising
    description: Performs anisotropic diffusion on an image using a modified curvature diffusion equation (MCDE).\n\nMCDE does not exhibit the edge enhancing properties of classic anisotropic diffusion, which can under certain conditions undergo a 'negative' diffusion, which enhances the contrast of edges.  Equations of the form of MCDE always undergo positive diffusion, with the conductance term only varying the strength of that diffusion. \n\n Qualitatively, MCDE compares well with other non-linear diffusion techniques.  It is less sensitive to contrast than classic Perona-Malik style diffusion, and preserves finer detailed structures in images.  There is a potential speed trade-off for using this function in place of Gradient Anisotropic Diffusion.  Each iteration of the solution takes roughly twice as long.  Fewer iterations, however, may be required to reach an acceptable solution.
    version: 0.1.0.$Revision$(alpha)
    documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/CurvatureAnisotropicDiffusion
    contributor: Bill Lorensen (GE)
    acknowledgements: This command module was derived from Insight/Examples (copyright) Insight Software Consortium
    """

    input_fields = [
        (
            "conductance",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--conductance %f",
                    "help_string": "Conductance controls the sensitivity of the conductance term. As a general rule, the lower the value, the more strongly the filter preserves edges. A high value will cause diffusion (smoothing) across edges. Note that the number of iterations controls how much smoothing is done within regions bounded by edges.",
                },
            ),
        ),
        (
            "iterations",
            attr.ib(
                type=traits.Int,
                metadata={
                    "argstr": "--iterations %d",
                    "help_string": "The more iterations, the more smoothing. Each iteration takes the same amount of time. If it takes 10 seconds for one iteration, then it will take 100 seconds for 10 iterations. Note that the conductance controls how much each iteration smooths across edges.",
                },
            ),
        ),
        (
            "timeStep",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--timeStep %f",
                    "help_string": "The time step depends on the dimensionality of the image. In Slicer the images are 3D and the default (.0625) time step will provide a stable solution.",
                },
            ),
        ),
        (
            "inputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Input volume to be filtered",
                    "position": "-2",
                    "exists": "True",
                },
            ),
        ),
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Output filtered",
                    "position": "-1",
                    "hash_files": "False",
                },
            ),
        ),
    ]
    output_fields = [
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "Output filtered",
                    "position": "-1",
                    "exists": "True",
                },
            ),
        )
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="CurvatureAnisotropicDiffusion",
        executable=" CurvatureAnisotropicDiffusion ",
        input_spec=input_spec,
        output_spec=output_spec,
    )


class GaussianBlurImageFilter:
    """
    title: Gaussian Blur Image Filter
    category: Filtering.Denoising
    description: Apply a gaussian blurr to an image
    version: 0.1.0.$Revision: 1.1 $(alpha)
    documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/GaussianBlurImageFilter
    contributor: Julien Jomier (Kitware), Stephen Aylward (Kitware)
    acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.
    """

    input_fields = [
        (
            "sigma",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--sigma %f",
                    "help_string": "Sigma value in physical units (e.g., mm) of the Gaussian kernel",
                },
            ),
        ),
        (
            "inputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Input volume",
                    "position": "-2",
                    "exists": "True",
                },
            ),
        ),
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Blurred Volume",
                    "position": "-1",
                    "hash_files": "False",
                },
            ),
        ),
    ]
    output_fields = [
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "Blurred Volume",
                    "position": "-1",
                    "exists": "True",
                },
            ),
        )
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="GaussianBlurImageFilter",
        executable=" GaussianBlurImageFilter ",
        input_spec=input_spec,
        output_spec=output_spec,
    )


class GradientAnisotropicDiffusion:
    """
    title: Gradient Anisotropic Diffusion
    category: Filtering.Denoising
    description: Runs gradient anisotropic diffusion on a volume.\n\nAnisotropic diffusion methods reduce noise (or unwanted detail) in images while preserving specific image features, like edges.  For many applications, there is an assumption that light-dark transitions (edges) are interesting.  Standard isotropic diffusion methods move and blur light-dark boundaries.  Anisotropic diffusion methods are formulated to specifically preserve edges. The conductance term for this implementation is a function of the gradient magnitude of the image at each point, reducing the strength of diffusion at edges. The numerical implementation of this equation is similar to that described in the Perona-Malik paper, but uses a more robust technique for gradient magnitude estimation and has been generalized to N-dimensions.
    version: 0.1.0.$Revision$(alpha)
    documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/GradientAnisotropicDiffusion
    contributor: Bill Lorensen (GE)
    acknowledgements: This command module was derived from Insight/Examples (copyright) Insight Software Consortium
    """

    input_fields = [
        (
            "conductance",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--conductance %f",
                    "help_string": "Conductance controls the sensitivity of the conductance term. As a general rule, the lower the value, the more strongly the filter preserves edges. A high value will cause diffusion (smoothing) across edges. Note that the number of iterations controls how much smoothing is done within regions bounded by edges.",
                },
            ),
        ),
        (
            "iterations",
            attr.ib(
                type=traits.Int,
                metadata={
                    "argstr": "--iterations %d",
                    "help_string": "The more iterations, the more smoothing. Each iteration takes the same amount of time. If it takes 10 seconds for one iteration, then it will take 100 seconds for 10 iterations. Note that the conductance controls how much each iteration smooths across edges.",
                },
            ),
        ),
        (
            "timeStep",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--timeStep %f",
                    "help_string": "The time step depends on the dimensionality of the image. In Slicer the images are 3D and the default (.0625) time step will provide a stable solution.",
                },
            ),
        ),
        (
            "inputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Input volume to be filtered",
                    "position": "-2",
                    "exists": "True",
                },
            ),
        ),
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Output filtered",
                    "position": "-1",
                    "hash_files": "False",
                },
            ),
        ),
        (
            "useImageSpacing",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--useImageSpacing ",
                    "help_string": "![CDATA[Take into account image spacing in the computation.  It is advisable to turn this option on, especially when the pixel size is different in different dimensions. However, to produce results consistent with Slicer4.2 and earlier, this option should be turned off.]]",
                },
            ),
        ),
    ]
    output_fields = [
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "Output filtered",
                    "position": "-1",
                    "exists": "True",
                },
            ),
        )
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="GradientAnisotropicDiffusion",
        executable=" GradientAnisotropicDiffusion ",
        input_spec=input_spec,
        output_spec=output_spec,
    )


class MedianImageFilter:
    """
    title: Median Image Filter
    category: Filtering.Denoising
    description: The MedianImageFilter is commonly used as a robust approach for noise reduction. This filter is particularly efficient against "salt-and-pepper" noise. In other words, it is robust to the presence of gray-level outliers. MedianImageFilter computes the value of each output pixel as the statistical median of the neighborhood of values around the corresponding input pixel.
    version: 0.1.0.$Revision$(alpha)
    documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/MedianImageFilter
    contributor: Bill Lorensen (GE)
    acknowledgements: This command module was derived from Insight/Examples/Filtering/MedianImageFilter (copyright) Insight Software Consortium
    """

    input_fields = [
        (
            "neighborhood",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--neighborhood %s",
                    "help_string": "The size of the neighborhood in each dimension",
                    "sep": ",",
                },
            ),
        ),
        (
            "inputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Input volume to be filtered",
                    "position": "-2",
                    "exists": "True",
                },
            ),
        ),
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Output filtered",
                    "position": "-1",
                    "hash_files": "False",
                },
            ),
        ),
    ]
    output_fields = [
        (
            "outputVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "Output filtered",
                    "position": "-1",
                    "exists": "True",
                },
            ),
        )
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="MedianImageFilter",
        executable=" MedianImageFilter ",
        input_spec=input_spec,
        output_spec=output_spec,
    )
