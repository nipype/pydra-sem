def configuration(parent_package="", top_path=None):
    from numpy.distutils.misc_util import Configuration

    config = Configuration("", parent_package, top_path)

    config.add_data_dir("registration")
    config.add_data_dir("filtering")
    config.add_data_dir("segmentation")
    config.add_data_dir("utilities")
    config.add_data_dir("diffusion")
    config.add_data_dir("brains")
    config.add_data_dir("legacy")

    return config


if __name__ == "__main__":
    from numpy.distutils.core import setup

    setup(**configuration(top_path="").todict())
