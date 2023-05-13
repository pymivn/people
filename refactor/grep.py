import sys
import lib


def main():
    try:
        config = lib.parse_config(sys.argv)
    except Exception as e:
        exit(f"Problem parsing arguments: {e}\n")

    try:
        lib.run(config)
    except Exception as e:
        exit(f"Application error: {e}")


if __name__ == "__main__":
    main()
