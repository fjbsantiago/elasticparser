from .elasticparser import ElasticParser

def agg_to_df(agg):
    """Converts a nested elasticsearch response object to a 
    flat list of dictionaries.
    """

    return ElasticParser().flatten(agg)