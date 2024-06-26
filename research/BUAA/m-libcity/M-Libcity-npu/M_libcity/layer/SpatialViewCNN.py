import mindspore.nn as nn

class SpatialViewConv(nn.Cell):
    def __init__(self, inp_channel, oup_channel, kernel_size, stride=1, padding=0):
        super(SpatialViewConv, self).__init__()
        self.inp_channel = inp_channel
        self.oup_channel = oup_channel
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding
        self.conv = nn.Conv2d(in_channels=inp_channel, out_channels=oup_channel,
                              kernel_size=kernel_size, stride=stride, padding=padding)
        self.batch = nn.BatchNorm2d(oup_channel)
        self.relu = nn.ReLU()

    def construct(self, inp):
        """
        Args:
            inp:
        Returns:
        """
        return self.relu(self.batch(self.conv(inp)))