from octane import reader
from octane import gradient_descent as gd
from octane import normal_equation as ne


def main():
    X = reader.load("X1")
    y = reader.load("y")

    a = gd.GradientDescent(X, y, 0.001, 100000)
    a.learn()
    print(a.theta)

    b = ne.normal_equation(X, y)
    print(b)


if __name__ == "__main__":
    main()
