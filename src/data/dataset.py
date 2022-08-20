from torch.utils.data import Dataset
from typing import Tuple


class CustomDataset(Dataset):
    """
    The dataset
    """

    def __init__(self, cfg: object, set_name: str = 'train') -> None:
        """
        The class constructor

        :param cfg object
            The configuration object
        :param set_name str
            The set name, train, test, or val
        :return None
        """

        super().__init__()

        # configuration object
        self.cfg = cfg

        # set name
        self.set_name = set_name

    def __getitem__(self, item) -> Tuple[any, any]:
        """
        Get item in dataset at `item` index

        :param item int
            The index of item to be retrieved
        """

        return None, None

    def __len__(self) -> int:
        """
        The length of dataset

        :return int
            The length of dataset
        """

        return len([])


if __name__ == "__main__":
    """ CustomDataset testing """

    # instantiation
    dataset = CustomDataset(cfg={})

    # diagnosing outputs
    print("dataset.__len__(): ", dataset.__len__())
    print("dataset.__getitem__(0): ", dataset.__getitem__(0))
