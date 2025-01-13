import torch
import os

from project1.train import MyAwesomeModel


def test_train():
    # test that the model trains
    assert os.path.exists("reports/figures/training_statistics.png"), "Training statistics file does not exist"
    assert os.path.exists("models/model.pth"), "Model file does not exist"
