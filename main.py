import sys
import redis


LIB_VERSION = "1.1.2"

if LIB_VERSION:
    sys.path.append(f"/custom_folder/flask/{LIB_VERSION}")
    import flask


def main():
    print("Run main")
    print(f"Redis version {redis.__version__}")

    print(f"flask version {flask.__version__}")


if __name__ == "__main__":
    main()
