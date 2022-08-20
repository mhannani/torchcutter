import torch
import torch.nn as nn


class Model(nn.Module):
    """
    Pytorch model
    """

    def __init__(self):
        """
        The class constructor
        """

        super().__init__()

        self.conv_1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=1, kernel_size=4, stride=2, padding=1),
        )

    def forward(self, x):
        """
        Forward pass
        """

        x = self.conv_1(x)

        return x


if __name__ == "__main__":

    # random tensor
    features = torch.rand((10, 3, 100, 100))

    # model instantiation
    model = Model()

    # forward pass
    output = model(features)

    # diagnosing
    print("output.shape, type(output): ", output.shape, type(output))
    # output.shape, type(output):  torch.Size([10, 1, 50, 50]) <class 'torch.Tensor'>
