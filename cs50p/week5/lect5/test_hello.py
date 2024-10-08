from hello import hello

def main():
  test_default()
  test_argument()


def test_default():
  assert hello() == "hello, world"


def test_argument():
  assert hello("David") == "hello, David"


if __name__ == "__main__":
  main()
