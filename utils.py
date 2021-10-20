import pandasdmx as smdx
import pandas as pd

def get_un_data(dataflow, structure, commod, country, transaction, key, start_period):
    """
    Query U.N. energy data
    """
    unsd = smdx.Request('UNSD')
    metadata = unsd.datastructure(structure)
    commod_lookup = smdx.to_pandas(metadata.codelist[commod])
    country_lookup = smdx.to_pandas(metadata.codelist[country])
    transaction_lookup = smdx.to_pandas(metadata.codelist[transaction])

    data = smdx.Request('UNSD').data(resource_id=dataflow,
                                     key=key,
                                     params={'startPeriod': start_period}
                                    ).write()

    commod_lookup = commod_lookup.reset_index()
    country_lookup = country_lookup.reset_index()
    transaction_lookup = transaction_lookup.reset_index()
    data = data.reset_index()

    commod_lookup.rename(columns={commod:'COMMODITY',
                                 'name':'comm_name',
                                 'parent':'comm_parent'},
                         inplace=True)
    country_lookup.rename(columns={country:'REF_AREA',
                                   'Reference area code list':'name'},
                          inplace=True)
    transaction_lookup.rename(columns={transaction:'TRANSACTION',
                                       'name':'trans_name',
                                       'parent':'trans_parent'},
                              inplace=True)

    data = pd.merge(data, commod_lookup, on='COMMODITY')
    data = pd.merge(data, country_lookup, on='REF_AREA')
    data = pd.merge(data, transaction_lookup, on='TRANSACTION')

    return data

def agg_df(df):
    """
    Sum energy data for all countries
    """
    groupby_cols = [col for col in df.columns if col not in ('REF_AREA', 'name', 'value')]
    grouped_df = df.groupby(groupby_cols).sum()
    return grouped_df

def move_legend(ax, new_loc, **kws):
    """
    Move legend in seaborn hist plot
    # https://github.com/mwaskom/seaborn/issues/2280
    """
    old_legend = ax.legend_
    handles = old_legend.legendHandles
    labels = [t.get_text() for t in old_legend.get_texts()]
    title = old_legend.get_title().get_text()
    ax.legend(handles, labels, loc=new_loc, title=title, **kws)
