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


class BRAINSLabelStats:
    """
    title: Label Statistics (BRAINS)
    category: Quantification
    description: Compute image statistics within each label of a label map.
    version: 5.2.0
    documentation-url: http://www.nitrc.org/plugins/mwiki/index.php/brains:BRAINSClassify
    license: https://www.nitrc.org/svn/brains/BuildScripts/trunk/License.txt
    contributor: Vincent A. Magnotta
    acknowledgements: Funding for this work was provided by the Dana Foundation
    """

    input_fields = [
        (
            "imageVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--imageVolume %s",
                    "help_string": "Image Volume",
                    "exists": "True",
                },
            ),
        ),
        (
            "labelVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--labelVolume %s",
                    "help_string": "Label Volume",
                    "exists": "True",
                },
            ),
        ),
        (
            "labelNameFile",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--labelNameFile %s",
                    "help_string": "Label Name File",
                    "exists": "True",
                },
            ),
        ),
        (
            "outputPrefixColumnNames",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--outputPrefixColumnNames %s",
                    "help_string": "Prefix Column Name(s)",
                    "sep": ",",
                },
            ),
        ),
        (
            "outputPrefixColumnValues",
            attr.ib(
                type=InputMultiPath,
                metadata={
                    "argstr": "--outputPrefixColumnValues %s",
                    "help_string": "Prefix Column Value(s)",
                    "sep": ",",
                },
            ),
        ),
        (
            "labelFileType",
            attr.ib(
                type=traits.Enum,
                metadata={
                    "argstr": "--labelFileType %s",
                    "help_string": "Label File Type",
                },
            ),
        ),
        (
            "numberOfHistogramBins",
            attr.ib(
                type=traits.Int,
                metadata={
                    "argstr": "--numberOfHistogramBins %d",
                    "help_string": "Number Of Histogram Bins",
                },
            ),
        ),
        (
            "minMaxType",
            attr.ib(
                type=traits.Enum,
                metadata={
                    "argstr": "--minMaxType %s",
                    "help_string": "Define minimim and maximum values based upon the image, label, or via command line",
                },
            ),
        ),
        (
            "userDefineMinimum",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--userDefineMinimum %f",
                    "help_string": "User define minimum value",
                },
            ),
        ),
        (
            "userDefineMaximum",
            attr.ib(
                type=traits.Float,
                metadata={
                    "argstr": "--userDefineMaximum %f",
                    "help_string": "User define maximum value",
                },
            ),
        ),
    ]
    output_fields = []

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="BRAINSLabelStats",
        executable=" BRAINSLabelStats ",
        input_spec=input_spec,
        output_spec=output_spec,
    )


class PETStandardUptakeValueComputation:
    """
    title: PET Standard Uptake Value Computation
    category: Quantification
    description: Computes the standardized uptake value based on body weight. Takes an input PET image in DICOM and NRRD format (DICOM header must contain Radiopharmaceutical parameters). Produces a CSV file that contains patientID, studyDate, dose, labelID, suvmin, suvmax, suvmean, labelName for each volume of interest. It also displays some of the information as output strings in the GUI, the CSV file is optional in that case. The CSV file is appended to on each execution of the CLI.
    version: 0.1.0.$Revision: 8595 $(alpha)
    documentation-url: http://www.slicer.org/slicerWiki/index.php/Documentation/Nightly/Modules/ComputeSUVBodyWeight
    contributor: Wendy Plesniak (SPL, BWH), Nicole Aucoin (SPL, BWH), Ron Kikinis (SPL, BWH)
    acknowledgements: This work is funded by the Harvard Catalyst, and the National Alliance for Medical Image Computing (NAMIC), funded by the National Institutes of Health through the NIH Roadmap for Medical Research, Grant U54 EB005149.
    """

    input_fields = [
        (
            "petDICOMPath",
            attr.ib(
                type=Directory,
                metadata={
                    "argstr": "--petDICOMPath %s",
                    "help_string": "Input path to a directory containing a PET volume containing DICOM header information for SUV computation",
                    "exists": "True",
                },
            ),
        ),
        (
            "petVolume",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--petVolume %s",
                    "help_string": "Input PET volume for SUVbw computation (must be the same volume as pointed to by the DICOM path!).",
                    "exists": "True",
                },
            ),
        ),
        (
            "labelMap",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--labelMap %s",
                    "help_string": "Input label volume containing the volumes of interest",
                    "exists": "True",
                },
            ),
        ),
        (
            "color",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--color %s",
                    "help_string": "Color table to to map labels to colors and names",
                    "exists": "True",
                },
            ),
        ),
        (
            "csvFile",
            attr.ib(
                type=File,
                metadata={
                    "argstr": "--csvFile %s",
                    "help_string": "A table holding the output SUV values in comma separated lines, one per label. Optional.",
                    "hash_files": "False",
                },
            ),
        ),
        (
            "OutputLabel",
            attr.ib(
                type=traits.Str,
                metadata={
                    "argstr": "--OutputLabel %s",
                    "help_string": "List of labels for which SUV values were computed",
                },
            ),
        ),
        (
            "OutputLabelValue",
            attr.ib(
                type=traits.Str,
                metadata={
                    "argstr": "--OutputLabelValue %s",
                    "help_string": "List of label values for which SUV values were computed",
                },
            ),
        ),
        (
            "SUVMax",
            attr.ib(
                type=traits.Str,
                metadata={
                    "argstr": "--SUVMax %s",
                    "help_string": "SUV max for each label",
                },
            ),
        ),
        (
            "SUVMean",
            attr.ib(
                type=traits.Str,
                metadata={
                    "argstr": "--SUVMean %s",
                    "help_string": "SUV mean for each label",
                },
            ),
        ),
        (
            "SUVMin",
            attr.ib(
                type=traits.Str,
                metadata={
                    "argstr": "--SUVMin %s",
                    "help_string": "SUV minimum for each label",
                },
            ),
        ),
    ]
    output_fields = [
        (
            "csvFile",
            attr.ib(
                type=File,
                metadata={
                    "help_string": "A table holding the output SUV values in comma separated lines, one per label. Optional.",
                    "exists": "True",
                },
            ),
        )
    ]

    input_spec = SpecInfo(name="Input", fields=input_fields, bases=(ShellSpec,))
    output_spec = SpecInfo(name="Output", fields=output_fields, bases=(ShellSpec,))

    task = ShellCommandTask(
        name="PETStandardUptakeValueComputation",
        executable=" PETStandardUptakeValueComputation ",
        input_spec=input_spec,
        output_spec=output_spec,
    )
