"""
Code for managing the depth data.
"""
from go_data import GoData


class DepthData(GoData):
    """
    A class for managing the depth data.
    """
    pass


if __name__ == '__main__':
    data = DepthData()
    data.convert_mat_to_tfrecord('data/nyud_micro.mat')