#!/usr/bin/python


from configparser import ConfigParser
from configparser import NoSectionError, NoOptionError


def main():
    config = ConfigParser()
    config.read("/tmp/config.ini")

    try:
        # fix this line
        config.get("testing", "name")
    except NoSectionError:
        pass
    except NoOptionError:
        pass


if __name__ == "__main__":
    main()
