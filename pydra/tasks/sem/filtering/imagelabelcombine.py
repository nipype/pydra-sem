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


class ImageLabelCombine:
    """
    title: Image Label Combine
    category: Filtering
    description: Combine two label maps into one
    version: 0.1.0
    documentation-url: http://wiki.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/ImageLabelCombine
    contributor: Alex Yarmarkovich (SPL, BWH)
    """

    input_fields = [
        (
            "InputLabelMap_A",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Label map image",
                    "position": "-3",
                    "exists": "True",
                },
            ),
        ),
        (
            "InputLabelMap_B",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Label map image",
                    "position": "-2",
                    "exists": "True",
                },
            ),
        ),
        (
            "OutputLabelMap",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "%s",
                    "help_string": "Resulting Label map image",
                    "position": "-1",
                    "hash_files": "False",
                },
            ),
        ),
        (
            "first_overwrites",
            attr.ib(
                type=traits.Bool,
                metadata={
                    "argstr": "--first_overwrites ",
                    "help_string": "Use first or second label when both are present",
                },
            ),
        ),
    ]
    output_fields = [
        (
            "OutputLabelMap",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "Resulting Label map image",
                    "position": "-1",
                    "exists": "True",
                },
            ),
        )
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="ImageLabelCombine",
        executable=" ImageLabelCombine ",
        input_spec=input_spec,
        output_spec=output_spec,
    )
