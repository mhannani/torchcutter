import yaml


def read_cfg(cfg_file_path: str) -> object:
    """
    Reads the configuration file from disk and returns the json object

    :param cfg_file_path str
        The yaml file path

    :return json object
    """

    # placeholder
    cfg = {}

    # open file in read mode
    try:
        with open(cfg_file_path, 'r') as rf:
            cfg = yaml.safe_load(rf)
            return cfg

    except OSError as os_error:
        print(f'! An error has been occurred, hint: {os_error} ')


if __name__ == "__main__":
    cfg_object = read_cfg('../../../config/config.yaml')
    print('cfg: ', cfg_object)
