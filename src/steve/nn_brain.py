from torch import nn
import torch
from torchvision import models

device = torch.device('cuda:0')


def weight_init(m):
    if isinstance(m, nn.Linear):
        m.weight.data.normal_(0, 1)


class NNBrain:
    def __init__(self):
        self.model = models.MobileNetV2(num_classes=4)

        self.model.to(device)
        self.model.apply(weight_init)

    def run_action(self, input):
        with torch.no_grad():
            output = self.model(input.to(device)).squeeze()
            actions = []
            if output[0] > 0.5:
                actions.append('w')
            if output[1] > 0.5:
                actions.append('a')
            if output[2] > 0.5:
                actions.append('s')
            if output[3] > 0.5:
                actions.append('d')
        return actions


if __name__ == '__main__':
    brain = NNBrain()
    input = torch.randn(size=(1, 3, 64, 64))
    print(brain.run_action(input))
