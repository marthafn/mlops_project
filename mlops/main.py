import project1.data as data
import project1.evaluate as evaluate
import project1.train as train
import project1.visualize as visualize

data.preprocess_data("data/raw", "data/processed")
train.train()
evaluate.evaluate("models/model.pth")
visualize.visualize("models/model.pth")
