from octane import reader, gradient_descent as gd


def main():
    X = reader.load("X1")
    y = reader.load("y")

    A = gd.GradientDescent(X, y, 0.001, 100000)
    A.learn()
    print(A.theta)


if __name__ == "__main__":
    main()
