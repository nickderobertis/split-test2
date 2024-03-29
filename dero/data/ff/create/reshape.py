import pandas as pd

import dero
from dero.ext_pandas.pdutils import _to_list_if_str
from dero.data.ff.fftypes import ListOrStr

def long_averages_to_wide_averages(df: pd.DataFrame, datevar: str='Date', byvars: ListOrStr=None,
                                   retvar: str='RET',
                                   dual_portvar: str='Market Equity Portfolio/B/M Portfolio') -> pd.DataFrame:

    byvars = _to_list_if_str(byvars)

    if byvars is not None:
        all_byvars = byvars + [datevar]
    else:
        all_byvars = [datevar]

    return dero.pandas.long_to_wide(
        df,
        groupvars=all_byvars,
        values=retvar,
        colindex=dual_portvar,
        colindex_only=True
    )