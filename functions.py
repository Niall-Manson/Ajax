def PlotTimeSeries(X_train, Y_train, X_test, Y_test):
  plt.figure(figsize=(10,7))
  plt.scatter(X_train, Y_train, s=10, label="Train data")
  plt.scatter(X_test, Y_test, s=10, label="Train data")
  plt.xlabel("Date")
  plt.xlabel("XRP Price")
  plt.legend(fontsize=14)
  plt.show();
