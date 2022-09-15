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


class ThresholdScalarVolume:
    """
    title: Threshold Scalar Volume
    category: Filtering
    description: <p>Threshold an image.</p><p>Set image values to a user-specified outside value if they are below, above, or between simple threshold values.</p><p>ThresholdAbove: The values greater than or equal to the threshold value are set to OutsideValue.</p><p>ThresholdBelow: The values less than or equal to the threshold value are set to OutsideValue.</p><p>ThresholdOutside: The values outside the range Lower-Upper are set to OutsideValue.</p>
    version: 0.1.0.$Revision: 2104 $(alpha)
    documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/Threshold
    contributor: Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH), Julien Finet (Kitware)
    acknowledgements: This work is part of the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.
    """

    input_fields = [
        (
            "InputVolume",
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
            "OutputVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Thresholded input volume",
                    "position": "-1",
                    "hash_files": "False",
                },
            ),
        ),
        (
            "thresholdtype",
            attr.ib(
                type=traits.Enum,
                metadata={
                    "argstr": "--thresholdtype %s",
                    "help_string": "What kind of threshold to perform. If Outside is selected, uses Upper and Lower values. If Below is selected, uses the ThresholdValue, if Above is selected, uses the ThresholdValue.",
                },
            ),
        ),
        (
            "threshold",
            attr.ib(
                type=traits.Float,
                metadata={"argstr": "--threshold %f", "help_string": "Threshold value"},
            ),
        ),
        (
            "lower",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--lower %f",
                    "help_string": "Lower threshold value",
                },
            ),
        ),
        (
            "upper",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--upper %f",
                    "help_string": "Upper threshold value",
                },
            ),
        ),
        (
            "outsidevalue",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--outsidevalue %f",
                    "help_string": "Set the voxels to this value if they fall outside the threshold range",
                },
            ),
        ),
        (
            "negate",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--negate ",
                    "help_string": "Swap the outside value with the inside value.",
                },
            ),
        ),
    ]
    output_fields = [
        (
            "OutputVolume",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "Thresholded input volume",
                    "position": "-1",
                    "exists": "True",
                },
            ),
        )
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="ThresholdScalarVolume",
        executable=" ThresholdScalarVolume ",
        input_spec=input_spec,
        output_spec=output_spec,
    )
