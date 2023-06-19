import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Add two numbers.")
    parser.add_argument('num1', type=float, help="First number")
    parser.add_argument('num2', type=float, help="Second number")
    args = parser.parse_args()
    print(args.num1 + args.num2)