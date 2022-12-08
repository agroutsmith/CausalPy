import pandas as pd
import pytest

import causalpy as cp

tests = ["banks", "brexit", "covid", "did", "drinking", "its", "its simple", "rd", "sc"]


@pytest.mark.parametrize("dataset_name", tests)
def test_data_loading(dataset_name):
    df = cp.load_data(dataset_name)
    assert isinstance(df, pd.DataFrame)
