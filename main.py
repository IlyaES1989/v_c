import sys
import redis


LIB_VERSION = "2.0.2"

if LIB_VERSION:
    sys.path.append(f"/custom_folder/flask/{LIB_VERSION}")
    import flask


def main():
    print("Run main")
    print(f"Pillow version {redis.__version__}")

    print(f"flask version {flask.__version__}")


if __name__ == "__main__":
    main()
