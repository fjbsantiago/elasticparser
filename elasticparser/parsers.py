from .elasticparser import ElasticParser

def flatten_agg(agg):
    """Converts a nested elasticsearch response object to a 
    flat list of dictionaries.
    """

    return ElasticParser().flatten(agg)
