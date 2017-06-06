import unittest
import elasticparser

def test_agg_to_df_date_hist_max(self):
    """Tests the conversion of an aggregation to data frame.
    The aggregation contains these levels:
        - date_histogram
            - max
    """

    query = {"aggs":{"daily":{"date_histogram":{"field":"timestamp","interval":"day"},"aggs":{"temperature":{"max":{"field":"temperature"}},"rain_volume":{"max":{"field":"rain_volume"}},"wind_speed":{"max":{"field":"wind_speed"}}}}},"query":{"bool":{"filter":{"range":{"timestamp":{"gte":1496002400,"lte":1496302400}}}}},"size":0}

    result = {
        "took": 7,
        "timed_out": "false",
        "_shards": {
            "total": 15,
            "successful": 15,
            "failed": 0
        },
        "hits": {
            "total": 5194,
            "max_score": 0,
            "hits": []
        },
        "aggregations": {
            "my_agg": {
                "buckets": [{
                        "key_as_string": "1495929600",
                        "key": 1495929600000,
                        "doc_count": 450,
                        "temperature": { "value": 32317308 },
                        "rain_volume": { "value": 37417283 },
                        "wind_speed": { "value": 77495254 }
                    },
                    {
                        "key_as_string": "1496016000",
                        "key": 1496016000000,
                        "doc_count": 325,
                        "temperature": { "value": None },
                        "rain_volume": { "value": 418968 },
                        "wind_speed": { "value": 3986292 }
                    },
                    {
                        "key_as_string": "1496102400",
                        "key": 1496102400000,
                        "doc_count": 2621,
                        "temperature": { "value": 2966713 },
                        "rain_volume": { "value": 3328655 },
                        "wind_speed": { "value": 6485277 }
                    }
                ]
            }
        }
    }

    expected = [
        {
            "key": 1495929600000,
            "doc_count": 450,
            "temperature": 32317308,
            "rain_volume": 37417283,
            "wind_speed": 77495254,
        },
        {
            "key": 1496016000000,
            "doc_count": 325,
            "temperature": None,
            "rain_volume": 418968,
            "wind_speed": 3986292,
        },
        {
            "key": 1496102400000,
            "doc_count": 2621,
            "temperature": 2966713,
            "rain_volume": 3328655,
            "wind_speed": 6485277,
        },
    ]

def test_agg_to_df_date_hist_cardinality(self):
    """Tests the conversion of an aggregation to data frame.
    The aggregation contains these levels:
        - date_histogram
            - cardinality
    """

    query = {"query":{"bool":{"must":[{"query_string":{"analyze_wildcard":"true","query":"message:atANDmessage:horizon4ANDfields.environment:mapng_at"}}]}},"sort":[{"timestamp_mili":{"order":"asc"}}],"aggs":{"time_buckets":{"date_histogram":{"field":"timestamp_mili","interval":"day","time_zone":"Europe/Berlin","min_doc_count":1},"aggs":{"sub_agg":{"cardinality":{"field":"cpe_id","precision_threshold":100000}}}}},"size":0}
    
    agg_result = {
       "took": 182,
       "timed_out": "false",
       "_shards": {
          "total": 6,
          "successful": 6,
          "failed": 0
       },
       "hits": {
          "total": 112908,
          "max_score": 0,
          "hits": []
       },
       "aggregations": {
          "time_buckets": {
             "buckets": [
                {
                   "key_as_string": "1493848800000",
                   "key": 1493848800000,
                   "doc_count": 50806,
                   "sub_agg": {
                      "value": 12386
                   }
                },
                {
                   "key_as_string": "1493935200000",
                   "key": 1493935200000,
                   "doc_count": 62102,
                   "sub_agg": {
                      "value": 9911
                   }
                }
             ]
          }
       }
    }

    expected = pd.DataFrame.from_records([
        {
            "key": 1493848800000,
            "doc_count": 50806,
            "sub_agg": 12386
        },
        {
            "key": 1493935200000,
            "doc_count": 62102,
            "sub_agg": 9911
        },
    ])

    print(expected)

def test_agg_to_df_cardinality(self):
    """Tests the conversion of an aggregation to data frame.
    The aggregation contains these levels:
        - cardinality
    """

    query = {"size":0,"aggs":{"event":{"filter":{"term":{"api":"event"}},"aggs":{"number_stbs":{"cardinality":{"field":"stbid","precision_threshold":10}}}}}}

    agg_result = {
        "took": 51090,
        "timed_out": "false",
        "_shards": {
            "total": 1,
            "successful": 1,
            "failed": 0
        },
        "hits": {
            "total": 325362803,
            "max_score": 0,
            "hits": []
        },
        "aggregations": {
            "event": {
                "doc_count": 1492155,
                "number_stbs": {
                    "value": 146753
                }
            }
        }
    }

    expected = pd.DataFrame.from_records([
        {
            "doc_count": 1492155,
            "number_stbs": "146753",
        },
    ])

    df = elasticsearch.agg_to_df(agg_result)

    self.assertEquals(expected, df)
