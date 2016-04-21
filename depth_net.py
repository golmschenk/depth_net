"""
Code related to the DepthNet.
"""
from depth_data import DepthData
from go_net import GoNet
from interface import Interface


class DepthNet(GoNet):
    """
    A neural network class to estimate 3D depths from single 2D images.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.data = DepthData()


if __name__ == '__main__':
    interface = Interface(network_class=DepthNet)
    interface.train()
