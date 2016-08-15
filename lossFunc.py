
# Assumes normalized scale -> prediction [0,1] and outcome [0,1]

def absMagLoss(pred, outcome):
  return abs(pred-outcome)


def squareLoss(pred, outcome):
  return (pred-outcome)^2
