from typing import List, Dict

MOCK_GEOLOCATION: List = [
    {
        "ent": "Cauca",
        "offset_start": 0,
        "offset_end": 0,
        "geoids": [
            {
                "match": "Departamento del Cauca",
                "geonameid": 3687029,
                "latitude": 2.5,
                "longitude": -76.83333,
                "featurecode": "ADM1",
                "contrycode": "CO",
            }
        ],
    },
    {
        "ent": "Amazonas",
        "offset_start": 0,
        "offset_end": 0,
        "geoids": [
            {
                "match": "Amazonas",
                "geonameid": 3689982,
                "latitude": -1.16667,
                "longitude": -71.5,
                "featurecode": "ADM1",
                "contrycode": "CO",
            }
        ],
    },
    {
        "ent": "Huila",
        "offset_start": 0,
        "offset_end": 0,
        "geoids": [
            {
                "match": "Departamento del Huila",
                "geonameid": 3680692,
                "latitude": 2.5,
                "longitude": -75.58333,
                "featurecode": "ADM1",
                "contrycode": "CO",
            }
        ],
    },
    {
        "ent": "Putumayo",
        "offset_start": 0,
        "offset_end": 0,
        "geoids": [
            {
                "match": "Departamento del Putumayo",
                "geonameid": 3671178,
                "latitude": 0.5,
                "longitude": -76.0,
                "featurecode": "ADM1",
                "contrycode": "CO",
            }
        ],
    },
]

MOCK_ENTRY_CLASSIFICATION: Dict = {
    "client_id": "entry-extraction-client-6000",
    "model_tags": {
        "1": {
            "101": {
                "prediction": 0.002,
                "threshold": 0.14,
                "is_selected": False
            },
            "102": {
                "prediction": 0.648,
                "threshold": 0.17,
                "is_selected": True
            },
            "103": {
                "prediction": 0.027,
                "threshold": 0.1,
                "is_selected": False
            },
            "104": {
                "prediction": 0.062,
                "threshold": 0.14,
                "is_selected": False
            },
            "105": {
                "prediction": 0.09,
                "threshold": 0.18,
                "is_selected": False
            },
            "106": {
                "prediction": 0.104,
                "threshold": 0.14,
                "is_selected": False
            },
            "107": {
                "prediction": 0.005,
                "threshold": 0.1,
                "is_selected": False
            },
            "108": {
                "prediction": 0.013,
                "threshold": 0.12,
                "is_selected": False
            },
            "109": {
                "prediction": 0.031,
                "threshold": 0.15,
                "is_selected": False
            },
            "110": {
                "prediction": 0.014,
                "threshold": 0.18,
                "is_selected": False
            },
            "111": {
                "prediction": 0.018,
                "threshold": 0.14,
                "is_selected": False
            }
        },
        "3": {
            "301": {
                "prediction": 0.001,
                "threshold": 0.01,
                "is_selected": False
            },
            "302": {
                "prediction": 0.001,
                "threshold": 0.11,
                "is_selected": False
            },
            "303": {
                "prediction": 0.083,
                "threshold": 0.38,
                "is_selected": False
            },
            "304": {
                "prediction": 0.086,
                "threshold": 0.01,
                "is_selected": True
            },
            "305": {
                "prediction": 0.083,
                "threshold": 0.17,
                "is_selected": False
            },
            "306": {
                "prediction": 0.026,
                "threshold": 0.15,
                "is_selected": False
            },
            "307": {
                "prediction": 0.001,
                "threshold": 0.09,
                "is_selected": False
            },
            "308": {
                "prediction": 0.01,
                "threshold": 0.13,
                "is_selected": False
            },
            "309": {
                "prediction": 0.003,
                "threshold": 0.07,
                "is_selected": False
            },
            "310": {
                "prediction": 0.006,
                "threshold": 0.16,
                "is_selected": False
            },
            "311": {
                "prediction": 0.023,
                "threshold": 0.15,
                "is_selected": False
            },
            "312": {
                "prediction": 0.026,
                "threshold": 0.2,
                "is_selected": False
            },
            "313": {
                "prediction": 0.022,
                "threshold": 0.16,
                "is_selected": False
            },
            "314": {
                "prediction": 0.004,
                "threshold": 0.05,
                "is_selected": False
            },
            "315": {
                "prediction": 0.003,
                "threshold": 0.45,
                "is_selected": False
            },
            "316": {
                "prediction": 0.001,
                "threshold": 0.06,
                "is_selected": False
            },
            "317": {
                "prediction": 0.004,
                "threshold": 0.28,
                "is_selected": False
            },
            "318": {
                "prediction": 0.0,
                "threshold": 0.13,
                "is_selected": False
            }
        },
        "2": {
            "219": {
                "prediction": 0.003,
                "threshold": 0.13,
                "is_selected": False
            },
            "217": {
                "prediction": 0.001,
                "threshold": 0.04,
                "is_selected": False
            },
            "218": {
                "prediction": 0.004,
                "threshold": 0.09,
                "is_selected": False
            },
            "204": {
                "prediction": 0.007,
                "threshold": 0.14,
                "is_selected": False
            },
            "203": {
                "prediction": 0.007,
                "threshold": 0.24,
                "is_selected": False
            },
            "201": {
                "prediction": 0.007,
                "threshold": 0.17,
                "is_selected": False
            },
            "205": {
                "prediction": 0.095,
                "threshold": 0.47,
                "is_selected": False
            },
            "207": {
                "prediction": 0.016,
                "threshold": 0.22,
                "is_selected": False
            },
            "206": {
                "prediction": 0.014,
                "threshold": 0.16,
                "is_selected": False
            },
            "202": {
                "prediction": 0.014,
                "threshold": 0.15,
                "is_selected": False
            },
            "228": {
                "prediction": 0.006,
                "threshold": 0.72,
                "is_selected": False
            },
            "229": {
                "prediction": 0.038,
                "threshold": 0.55,
                "is_selected": False
            },
            "230": {
                "prediction": 0.001,
                "threshold": 0.61,
                "is_selected": False
            },
            "231": {
                "prediction": 0.0,
                "threshold": 0.3,
                "is_selected": False
            },
            "232": {
                "prediction": 0.015,
                "threshold": 0.23,
                "is_selected": False
            },
            "233": {
                "prediction": 0.039,
                "threshold": 0.31,
                "is_selected": False
            },
            "234": {
                "prediction": 0.005,
                "threshold": 0.39,
                "is_selected": False
            },
            "215": {
                "prediction": 0.019,
                "threshold": 0.15,
                "is_selected": False
            },
            "216": {
                "prediction": 0.003,
                "threshold": 0.13,
                "is_selected": False
            },
            "214": {
                "prediction": 0.001,
                "threshold": 0.09,
                "is_selected": False
            },
            "213": {
                "prediction": 0.0,
                "threshold": 0.26,
                "is_selected": False
            },
            "212": {
                "prediction": 0.01,
                "threshold": 0.31,
                "is_selected": False
            },
            "223": {
                "prediction": 0.028,
                "threshold": 0.09,
                "is_selected": False
            },
            "222": {
                "prediction": 0.003,
                "threshold": 0.16,
                "is_selected": False
            },
            "221": {
                "prediction": 0.017,
                "threshold": 0.16,
                "is_selected": False
            },
            "220": {
                "prediction": 0.017,
                "threshold": 0.22,
                "is_selected": False
            },
            "224": {
                "prediction": 0.651,
                "threshold": 0.21,
                "is_selected": True
            },
            "225": {
                "prediction": 0.984,
                "threshold": 0.04,
                "is_selected": True
            },
            "227": {
                "prediction": 4.394,
                "threshold": 0.07,
                "is_selected": True
            },
            "226": {
                "prediction": 1.346,
                "threshold": 0.09,
                "is_selected": True
            },
            "210": {
                "prediction": 0.114,
                "threshold": 0.24,
                "is_selected": False
            },
            "208": {
                "prediction": 0.044,
                "threshold": 0.21,
                "is_selected": False
            },
            "209": {
                "prediction": 0.458,
                "threshold": 0.05,
                "is_selected": True
            }
        },
        "6": {
            "601": {
                "prediction": 0.0,
                "threshold": 0.06,
                "is_selected": False
            },
            "602": {
                "prediction": 0.001,
                "threshold": 0.48,
                "is_selected": False
            },
            "603": {
                "prediction": 0.022,
                "threshold": 0.34,
                "is_selected": False
            },
            "604": {
                "prediction": 0.0,
                "threshold": 0.16,
                "is_selected": False
            }
        },
        "5": {
            "501": {
                "prediction": 0.0,
                "threshold": 0.45,
                "is_selected": False
            },
            "502": {
                "prediction": 0.0,
                "threshold": 0.48,
                "is_selected": False
            }
        },
        "8": {
            "801": {
                "prediction": 0.0,
                "threshold": 0.66,
                "is_selected": False
            },
            "802": {
                "prediction": 0.0,
                "threshold": 0.3,
                "is_selected": False
            },
            "803": {
                "prediction": 0.0,
                "threshold": 0.36,
                "is_selected": False
            },
            "804": {
                "prediction": 0.0,
                "threshold": 0.23,
                "is_selected": False
            },
            "805": {
                "prediction": 0.0,
                "threshold": 0.58,
                "is_selected": False
            },
            "806": {
                "prediction": 0.009,
                "threshold": 0.3,
                "is_selected": False
            }
        },
        "4": {
            "401": {
                "prediction": 0.001,
                "threshold": 0.29,
                "is_selected": False
            },
            "402": {
                "prediction": 0.001,
                "threshold": 0.45,
                "is_selected": False
            },
            "403": {
                "prediction": 0.01,
                "threshold": 0.03,
                "is_selected": False
            },
            "404": {
                "prediction": 0.0,
                "threshold": 0.34,
                "is_selected": False
            },
            "405": {
                "prediction": 0.0,
                "threshold": 0.37,
                "is_selected": False
            },
            "406": {
                "prediction": 0.001,
                "threshold": 0.25,
                "is_selected": False
            },
            "407": {
                "prediction": 0.0,
                "threshold": 0.07,
                "is_selected": False
            },
            "408": {
                "prediction": 0.001,
                "threshold": 0.11,
                "is_selected": False
            },
            "409": {
                "prediction": 0.0,
                "threshold": 0.43,
                "is_selected": False
            },
            "410": {
                "prediction": 0.0,
                "threshold": 0.23,
                "is_selected": False
            },
            "411": {
                "prediction": 0.003,
                "threshold": 0.06,
                "is_selected": False
            },
            "412": {
                "prediction": 0.0,
                "threshold": 0.36,
                "is_selected": False
            }
        },
        "7": {
            "701": {
                "prediction": 0.008,
                "threshold": 0.27,
                "is_selected": False
            },
            "702": {
                "prediction": 0.02,
                "threshold": 0.11,
                "is_selected": False
            },
            "703": {
                "prediction": 0.004,
                "threshold": 0.05,
                "is_selected": False
            },
            "704": {
                "prediction": 0.096,
                "threshold": 0.24,
                "is_selected": False
            },
            "705": {
                "prediction": 0.061,
                "threshold": 0.12,
                "is_selected": False
            }
        },
        "9": {
            "904": {
                "prediction": -1,
                "threshold": -1,
                "is_selected": False
            },
            "905": {
                "prediction": -1,
                "threshold": -1,
                "is_selected": False
            },
            "902": {
                "prediction": -1,
                "threshold": -1,
                "is_selected": False
            },
            "903": {
                "prediction": -1,
                "threshold": -1,
                "is_selected": False
            },
            "906": {
                "prediction": -1,
                "threshold": -1,
                "is_selected": False
            },
            "907": {
                "prediction": -1,
                "threshold": -1,
                "is_selected": False
            }
        }
    },
    "geolocations": [
        "New York"
    ]
}


"""
it's a huge output (and it can be bigger that this one). Maybe we can truncate it.
I know that for now all the pdf location infos (x0, y0, etc...) are not needed, but they can be not considered.
"""
MOCK_ENTRY_CLASSIFICATION_FORMATTED: Dict = {
    "metadata": {
        "total_pages": 10,
        "total_words_count": 5876
    },
    "blocks": [
        {
            "type": "text",
            "page": 1,
            "text": "The 2021 Gu rainy season performance varied across Somalia with many places "
                    "recording average to below average rainfall (Maps 1 & 2, and Annex I). The "
                    "seasonal rains which started in late April lasted for three weeks and came "
                    "to an early end during the first week of May 2021. During the three weeks of "
                    "rainfall, some places recorded heavy rains that led to flash floods in the "
                    "northern parts of the country. The southern regions recorded below normal "
                    "seasonal rains, leaving many places under water stress. This follows another "
                    "poor rainfall performance during the 2020 Deyr (October- December) season which "
                    "led to moderate drought conditions this year that lasted till late April",
            "textOrder": 1,
            "relevant": True,
            "prediction_status": True,
            "geolocations": ["Somalia"],
            "classification": {
                "1": {
                    "101": {
                        "prediction": 0.0000270270529,
                        "threshold": 0.14,
                        "is_selected": False
                    },
                    "102": {
                        "prediction": 2.791275697595933,
                        "threshold": 0.17,
                        "is_selected": True
                    },
                    "103": {
                        "prediction": 0.000845505346661,
                        "threshold": 0.1,
                        "is_selected": False
                    },
                    "104": {
                        "prediction": 0.001551844096476,
                        "threshold": 0.14,
                        "is_selected": False
                    },
                    "105": {
                        "prediction": 0.000610130882706,
                        "threshold": 0.18,
                        "is_selected": False
                    },
                    "106": {
                        "prediction": 0.021222406732185,
                        "threshold": 0.14,
                        "is_selected": False
                    },
                    "107": {
                        "prediction": 0.000047710691433,
                        "threshold": 0.1,
                        "is_selected": False
                    },
                    "108": {
                        "prediction": 0.000005902628667,
                        "threshold": 0.12,
                        "is_selected": False
                    },
                    "109": {
                        "prediction": 5.845728317896525,
                        "threshold": 0.15,
                        "is_selected": True
                    },
                    "110": {
                        "prediction": 0.000993687879398,
                        "threshold": 0.18,
                        "is_selected": False
                    },
                    "111": {
                        "prediction": 0.000130282686379,
                        "threshold": 0.14,
                        "is_selected": False
                    }
                },
                "2": {
                    "201": {
                        "prediction": 0.001077209547956,
                        "threshold": 0.17,
                        "is_selected": False
                    },
                    "202": {
                        "prediction": 0.002082403516397,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "203": {
                        "prediction": 0.027398668074359,
                        "threshold": 0.24,
                        "is_selected": False
                    },
                    "204": {
                        "prediction": 0.000344154328299,
                        "threshold": 0.14,
                        "is_selected": False
                    },
                    "205": {
                        "prediction": 0.008931630191968,
                        "threshold": 0.47,
                        "is_selected": False
                    },
                    "206": {
                        "prediction": 1.561535708606243,
                        "threshold": 0.16,
                        "is_selected": True
                    },
                    "207": {
                        "prediction": 0.008022336987779,
                        "threshold": 0.22,
                        "is_selected": False
                    },
                    "208": {
                        "prediction": 0.000339151683008,
                        "threshold": 0.21,
                        "is_selected": False
                    },
                    "209": {
                        "prediction": 0.664219930768013,
                        "threshold": 0.05,
                        "is_selected": False
                    },
                    "210": {
                        "prediction": 0.070768408477306,
                        "threshold": 0.24,
                        "is_selected": False
                    },
                    "212": {
                        "prediction": 0.002422974061882,
                        "threshold": 0.31,
                        "is_selected": False
                    },
                    "213": {
                        "prediction": 0.000046979557038,
                        "threshold": 0.26,
                        "is_selected": False
                    },
                    "214": {
                        "prediction": 0.000070475855157,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "215": {
                        "prediction": 0.000008547227329,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "216": {
                        "prediction": 0.000167800135387,
                        "threshold": 0.13,
                        "is_selected": False
                    },
                    "217": {
                        "prediction": 0.000016116082691,
                        "threshold": 0.04,
                        "is_selected": False
                    },
                    "218": {
                        "prediction": 0.00002616270649,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "219": {
                        "prediction": 0.000166147779405,
                        "threshold": 0.13,
                        "is_selected": False
                    },
                    "220": {
                        "prediction": 0.000002293435324,
                        "threshold": 0.22,
                        "is_selected": False
                    },
                    "221": {
                        "prediction": 2.3751352e-7,
                        "threshold": 0.16,
                        "is_selected": False
                    },
                    "222": {
                        "prediction": 0.000008183459954,
                        "threshold": 0.16,
                        "is_selected": False
                    },
                    "223": {
                        "prediction": 0.000764200214892,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "224": {
                        "prediction": 7.88740062e-7,
                        "threshold": 0.21,
                        "is_selected": False
                    },
                    "225": {
                        "prediction": 0.000002737477267,
                        "threshold": 0.04,
                        "is_selected": False
                    },
                    "226": {
                        "prediction": 3.95147303e-7,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "227": {
                        "prediction": 0.000015625468157,
                        "threshold": 0.07,
                        "is_selected": False
                    },
                    "228": {
                        "prediction": 0.000017889078663,
                        "threshold": 0.72,
                        "is_selected": False
                    },
                    "229": {
                        "prediction": 3.389243e-9,
                        "threshold": 0.55,
                        "is_selected": False
                    },
                    "230": {
                        "prediction": 0.000016569508455,
                        "threshold": 0.61,
                        "is_selected": False
                    },
                    "231": {
                        "prediction": 0.000004143511584,
                        "threshold": 0.3,
                        "is_selected": False
                    },
                    "232": {
                        "prediction": 0.000640358295008,
                        "threshold": 0.23,
                        "is_selected": False
                    },
                    "233": {
                        "prediction": 0.000006404845789,
                        "threshold": 0.31,
                        "is_selected": False
                    },
                    "234": {
                        "prediction": 0.000074884925338,
                        "threshold": 0.39,
                        "is_selected": False
                    }
                },
                "3": {
                    "301": {
                        "prediction": 0.000083330627376,
                        "threshold": 0.01,
                        "is_selected": False
                    },
                    "302": {
                        "prediction": 0.011204658287831,
                        "threshold": 0.11,
                        "is_selected": False
                    },
                    "303": {
                        "prediction": 0.000861139989483,
                        "threshold": 0.38,
                        "is_selected": False
                    },
                    "304": {
                        "prediction": 0.000009533644629,
                        "threshold": 0.01,
                        "is_selected": False
                    },
                    "305": {
                        "prediction": 0.010194102137843,
                        "threshold": 0.17,
                        "is_selected": False
                    },
                    "306": {
                        "prediction": 0.000047473428519,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "307": {
                        "prediction": 0.00275926431641,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "308": {
                        "prediction": 0.006035644596872,
                        "threshold": 0.13,
                        "is_selected": False
                    },
                    "309": {
                        "prediction": 0.000018762974768,
                        "threshold": 0.07,
                        "is_selected": False
                    },
                    "310": {
                        "prediction": 0.16048023244366,
                        "threshold": 0.16,
                        "is_selected": True
                    },
                    "311": {
                        "prediction": 0.001379056581451,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "312": {
                        "prediction": 0.144955087453127,
                        "threshold": 0.2,
                        "is_selected": False
                    },
                    "313": {
                        "prediction": 0.042628173832782,
                        "threshold": 0.16,
                        "is_selected": False
                    },
                    "314": {
                        "prediction": 0.000043664708755,
                        "threshold": 0.05,
                        "is_selected": False
                    },
                    "315": {
                        "prediction": 0.000097360397275,
                        "threshold": 0.45,
                        "is_selected": False
                    },
                    "316": {
                        "prediction": 0.000012243420618,
                        "threshold": 0.06,
                        "is_selected": False
                    },
                    "317": {
                        "prediction": 0.000005113670909,
                        "threshold": 0.28,
                        "is_selected": False
                    },
                    "318": {
                        "prediction": 0.000393391634973,
                        "threshold": 0.13,
                        "is_selected": False
                    }
                },
                "4": {
                    "401": {
                        "prediction": 1.17259055e-7,
                        "threshold": 0.29,
                        "is_selected": False
                    },
                    "402": {
                        "prediction": 0.000013744229364,
                        "threshold": 0.45,
                        "is_selected": False
                    },
                    "403": {
                        "prediction": 4.87375621e-7,
                        "threshold": 0.03,
                        "is_selected": False
                    },
                    "404": {
                        "prediction": 1.85885169e-7,
                        "threshold": 0.34,
                        "is_selected": False
                    },
                    "405": {
                        "prediction": 3.05366841e-7,
                        "threshold": 0.37,
                        "is_selected": False
                    },
                    "406": {
                        "prediction": 0.000034889759263,
                        "threshold": 0.25,
                        "is_selected": False
                    },
                    "407": {
                        "prediction": 0.000001803972996,
                        "threshold": 0.07,
                        "is_selected": False
                    },
                    "408": {
                        "prediction": 0.001109504095935,
                        "threshold": 0.11,
                        "is_selected": False
                    },
                    "409": {
                        "prediction": 2.59159425e-7,
                        "threshold": 0.43,
                        "is_selected": False
                    },
                    "410": {
                        "prediction": 1.45469337e-7,
                        "threshold": 0.23,
                        "is_selected": False
                    },
                    "411": {
                        "prediction": 0.000005189525136,
                        "threshold": 0.06,
                        "is_selected": False
                    },
                    "412": {
                        "prediction": 0.000002016342806,
                        "threshold": 0.36,
                        "is_selected": False
                    }
                },
                "5": {
                    "501": {
                        "prediction": 0.000025967284374,
                        "threshold": 0.45,
                        "is_selected": False
                    },
                    "502": {
                        "prediction": 0.000565126356378,
                        "threshold": 0.48,
                        "is_selected": False
                    }
                },
                "6": {
                    "601": {
                        "prediction": 0.000177106418657,
                        "threshold": 0.06,
                        "is_selected": False
                    },
                    "602": {
                        "prediction": 0.00055463691145,
                        "threshold": 0.48,
                        "is_selected": False
                    },
                    "603": {
                        "prediction": 0.000022633564774,
                        "threshold": 0.34,
                        "is_selected": False
                    },
                    "604": {
                        "prediction": 0.001842333040258,
                        "threshold": 0.16,
                        "is_selected": False
                    }
                },
                "7": {
                    "701": {
                        "prediction": 0.000903384244777,
                        "threshold": 0.27,
                        "is_selected": False
                    },
                    "702": {
                        "prediction": 0.001251186238898,
                        "threshold": 0.11,
                        "is_selected": False
                    },
                    "703": {
                        "prediction": 0.000834142483654,
                        "threshold": 0.05,
                        "is_selected": False
                    },
                    "704": {
                        "prediction": 0.000382219089564,
                        "threshold": 0.24,
                        "is_selected": False
                    },
                    "705": {
                        "prediction": 0.001979890172758,
                        "threshold": 0.12,
                        "is_selected": True
                    }
                },
                "8": {
                    "801": {
                        "prediction": 0.000014654744629,
                        "threshold": 0.66,
                        "is_selected": False
                    },
                    "802": {
                        "prediction": 0.000044733506002,
                        "threshold": 0.3,
                        "is_selected": False
                    },
                    "803": {
                        "prediction": 0.001036487083184,
                        "threshold": 0.36,
                        "is_selected": False
                    },
                    "804": {
                        "prediction": 0.000707629901033,
                        "threshold": 0.23,
                        "is_selected": False
                    },
                    "805": {
                        "prediction": 0.00003381500674,
                        "threshold": 0.58,
                        "is_selected": False
                    },
                    "806": {
                        "prediction": 0.702028969923655,
                        "threshold": 0.3,
                        "is_selected": False
                    }
                },
                "9": {
                    "902": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "903": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "904": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "905": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "906": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "907": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    }
                }
            }
        },
        {
            "type": "text",
            "page": 2,
            "text": "Seasonal rainfall and subsequent high-water levels in Niger and Benue rivers have "
                    "been causing flooding across Nigeria since June 2019. Floods have worsened after a "
                    "peak in water levels in late September (Floodlist 07/10/2019). According to the latest "
                    "situation report from 7 October, the floods severely affected 32 of the 36 states and "
                    "Federal Capital Territory, killing several people, displacing thousands, and causing "
                    "crop damage to varying degrees across the country (IFRC EPoA 07/10/2019).",
            "textOrder": 2,
            "relevant": True,
            "prediction_status": True,
            "geolocations": ["Niger", "Nigeria"],
            "classification": {
                "1": {
                    "101": {
                        "prediction": 2.0000270270529,
                        "threshold": 0.14,
                        "is_selected": True
                    },
                    "102": {
                        "prediction": 2.791275697595933,
                        "threshold": 0.17,
                        "is_selected": True
                    },
                    "103": {
                        "prediction": 0.000845505346661,
                        "threshold": 0.1,
                        "is_selected": False
                    },
                    "104": {
                        "prediction": 0.001551844096476,
                        "threshold": 0.14,
                        "is_selected": False
                    },
                    "105": {
                        "prediction": 0.000610130882706,
                        "threshold": 0.18,
                        "is_selected": False
                    },
                    "106": {
                        "prediction": 0.021222406732185,
                        "threshold": 0.14,
                        "is_selected": False
                    },
                    "107": {
                        "prediction": 0.000047710691433,
                        "threshold": 0.1,
                        "is_selected": False
                    },
                    "108": {
                        "prediction": 0.000005902628667,
                        "threshold": 0.12,
                        "is_selected": False
                    },
                    "109": {
                        "prediction": 5.845728317896525,
                        "threshold": 0.15,
                        "is_selected": True
                    },
                    "110": {
                        "prediction": 0.000993687879398,
                        "threshold": 0.18,
                        "is_selected": False
                    },
                    "111": {
                        "prediction": 0.000130282686379,
                        "threshold": 0.14,
                        "is_selected": False
                    }
                },
                "2": {
                    "201": {
                        "prediction": 0.001077209547956,
                        "threshold": 0.17,
                        "is_selected": False
                    },
                    "202": {
                        "prediction": 0.002082403516397,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "203": {
                        "prediction": 0.027398668074359,
                        "threshold": 0.24,
                        "is_selected": False
                    },
                    "204": {
                        "prediction": 0.000344154328299,
                        "threshold": 0.14,
                        "is_selected": False
                    },
                    "205": {
                        "prediction": 0.008931630191968,
                        "threshold": 0.47,
                        "is_selected": False
                    },
                    "206": {
                        "prediction": 1.561535708606243,
                        "threshold": 0.16,
                        "is_selected": True
                    },
                    "207": {
                        "prediction": 0.008022336987779,
                        "threshold": 0.22,
                        "is_selected": False
                    },
                    "208": {
                        "prediction": 0.000339151683008,
                        "threshold": 0.21,
                        "is_selected": False
                    },
                    "209": {
                        "prediction": 0.664219930768013,
                        "threshold": 0.05,
                        "is_selected": False
                    },
                    "210": {
                        "prediction": 0.070768408477306,
                        "threshold": 0.24,
                        "is_selected": False
                    },
                    "212": {
                        "prediction": 0.002422974061882,
                        "threshold": 0.31,
                        "is_selected": False
                    },
                    "213": {
                        "prediction": 0.000046979557038,
                        "threshold": 0.26,
                        "is_selected": False
                    },
                    "214": {
                        "prediction": 0.000070475855157,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "215": {
                        "prediction": 0.000008547227329,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "216": {
                        "prediction": 0.000167800135387,
                        "threshold": 0.13,
                        "is_selected": False
                    },
                    "217": {
                        "prediction": 0.000016116082691,
                        "threshold": 0.04,
                        "is_selected": False
                    },
                    "218": {
                        "prediction": 0.00002616270649,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "219": {
                        "prediction": 0.000166147779405,
                        "threshold": 0.13,
                        "is_selected": False
                    },
                    "220": {
                        "prediction": 0.000002293435324,
                        "threshold": 0.22,
                        "is_selected": False
                    },
                    "221": {
                        "prediction": 2.3751352e-7,
                        "threshold": 0.16,
                        "is_selected": False
                    },
                    "222": {
                        "prediction": 0.000008183459954,
                        "threshold": 0.16,
                        "is_selected": False
                    },
                    "223": {
                        "prediction": 0.000764200214892,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "224": {
                        "prediction": 7.88740062e-7,
                        "threshold": 0.21,
                        "is_selected": False
                    },
                    "225": {
                        "prediction": 0.000002737477267,
                        "threshold": 0.04,
                        "is_selected": False
                    },
                    "226": {
                        "prediction": 3.95147303e-7,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "227": {
                        "prediction": 0.000015625468157,
                        "threshold": 0.07,
                        "is_selected": False
                    },
                    "228": {
                        "prediction": 0.000017889078663,
                        "threshold": 0.72,
                        "is_selected": False
                    },
                    "229": {
                        "prediction": 3.389243e-9,
                        "threshold": 0.55,
                        "is_selected": False
                    },
                    "230": {
                        "prediction": 0.000016569508455,
                        "threshold": 0.61,
                        "is_selected": False
                    },
                    "231": {
                        "prediction": 0.000004143511584,
                        "threshold": 0.3,
                        "is_selected": False
                    },
                    "232": {
                        "prediction": 0.000640358295008,
                        "threshold": 0.23,
                        "is_selected": False
                    },
                    "233": {
                        "prediction": 0.000006404845789,
                        "threshold": 0.31,
                        "is_selected": False
                    },
                    "234": {
                        "prediction": 0.000074884925338,
                        "threshold": 0.39,
                        "is_selected": False
                    }
                },
                "3": {
                    "301": {
                        "prediction": 0.000083330627376,
                        "threshold": 0.01,
                        "is_selected": False
                    },
                    "302": {
                        "prediction": 0.011204658287831,
                        "threshold": 0.11,
                        "is_selected": False
                    },
                    "303": {
                        "prediction": 0.000861139989483,
                        "threshold": 0.38,
                        "is_selected": False
                    },
                    "304": {
                        "prediction": 0.000009533644629,
                        "threshold": 0.01,
                        "is_selected": False
                    },
                    "305": {
                        "prediction": 0.010194102137843,
                        "threshold": 0.17,
                        "is_selected": False
                    },
                    "306": {
                        "prediction": 0.000047473428519,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "307": {
                        "prediction": 0.00275926431641,
                        "threshold": 0.09,
                        "is_selected": False
                    },
                    "308": {
                        "prediction": 0.006035644596872,
                        "threshold": 0.13,
                        "is_selected": False
                    },
                    "309": {
                        "prediction": 0.000018762974768,
                        "threshold": 0.07,
                        "is_selected": False
                    },
                    "310": {
                        "prediction": 0.16048023244366,
                        "threshold": 0.16,
                        "is_selected": True
                    },
                    "311": {
                        "prediction": 0.001379056581451,
                        "threshold": 0.15,
                        "is_selected": False
                    },
                    "312": {
                        "prediction": 0.144955087453127,
                        "threshold": 0.2,
                        "is_selected": False
                    },
                    "313": {
                        "prediction": 0.042628173832782,
                        "threshold": 0.16,
                        "is_selected": False
                    },
                    "314": {
                        "prediction": 0.000043664708755,
                        "threshold": 0.05,
                        "is_selected": False
                    },
                    "315": {
                        "prediction": 0.000097360397275,
                        "threshold": 0.45,
                        "is_selected": False
                    },
                    "316": {
                        "prediction": 0.000012243420618,
                        "threshold": 0.06,
                        "is_selected": False
                    },
                    "317": {
                        "prediction": 0.000005113670909,
                        "threshold": 0.28,
                        "is_selected": False
                    },
                    "318": {
                        "prediction": 0.000393391634973,
                        "threshold": 0.13,
                        "is_selected": False
                    }
                },
                "4": {
                    "401": {
                        "prediction": 1.17259055e-7,
                        "threshold": 0.29,
                        "is_selected": False
                    },
                    "402": {
                        "prediction": 0.000013744229364,
                        "threshold": 0.45,
                        "is_selected": False
                    },
                    "403": {
                        "prediction": 4.87375621e-7,
                        "threshold": 0.03,
                        "is_selected": False
                    },
                    "404": {
                        "prediction": 1.85885169e-7,
                        "threshold": 0.34,
                        "is_selected": False
                    },
                    "405": {
                        "prediction": 3.05366841e-7,
                        "threshold": 0.37,
                        "is_selected": False
                    },
                    "406": {
                        "prediction": 0.000034889759263,
                        "threshold": 0.25,
                        "is_selected": False
                    },
                    "407": {
                        "prediction": 0.000001803972996,
                        "threshold": 0.07,
                        "is_selected": False
                    },
                    "408": {
                        "prediction": 0.001109504095935,
                        "threshold": 0.11,
                        "is_selected": False
                    },
                    "409": {
                        "prediction": 2.59159425e-7,
                        "threshold": 0.43,
                        "is_selected": False
                    },
                    "410": {
                        "prediction": 1.45469337e-7,
                        "threshold": 0.23,
                        "is_selected": False
                    },
                    "411": {
                        "prediction": 0.000005189525136,
                        "threshold": 0.06,
                        "is_selected": False
                    },
                    "412": {
                        "prediction": 0.000002016342806,
                        "threshold": 0.36,
                        "is_selected": False
                    }
                },
                "5": {
                    "501": {
                        "prediction": 0.000025967284374,
                        "threshold": 0.45,
                        "is_selected": False
                    },
                    "502": {
                        "prediction": 0.000565126356378,
                        "threshold": 0.48,
                        "is_selected": False
                    }
                },
                "6": {
                    "601": {
                        "prediction": 0.000177106418657,
                        "threshold": 0.06,
                        "is_selected": False
                    },
                    "602": {
                        "prediction": 0.00055463691145,
                        "threshold": 0.48,
                        "is_selected": False
                    },
                    "603": {
                        "prediction": 0.000022633564774,
                        "threshold": 0.34,
                        "is_selected": False
                    },
                    "604": {
                        "prediction": 0.001842333040258,
                        "threshold": 0.16,
                        "is_selected": False
                    }
                },
                "7": {
                    "701": {
                        "prediction": 0.000903384244777,
                        "threshold": 0.27,
                        "is_selected": False
                    },
                    "702": {
                        "prediction": 0.001251186238898,
                        "threshold": 0.11,
                        "is_selected": False
                    },
                    "703": {
                        "prediction": 0.000834142483654,
                        "threshold": 0.05,
                        "is_selected": False
                    },
                    "704": {
                        "prediction": 0.000382219089564,
                        "threshold": 0.24,
                        "is_selected": False
                    },
                    "705": {
                        "prediction": 0.001979890172758,
                        "threshold": 0.12,
                        "is_selected": True
                    }
                },
                "8": {
                    "801": {
                        "prediction": 0.000014654744629,
                        "threshold": 0.66,
                        "is_selected": False
                    },
                    "802": {
                        "prediction": 0.000044733506002,
                        "threshold": 0.3,
                        "is_selected": False
                    },
                    "803": {
                        "prediction": 0.001036487083184,
                        "threshold": 0.36,
                        "is_selected": False
                    },
                    "804": {
                        "prediction": 0.000707629901033,
                        "threshold": 0.23,
                        "is_selected": False
                    },
                    "805": {
                        "prediction": 0.00003381500674,
                        "threshold": 0.58,
                        "is_selected": False
                    },
                    "806": {
                        "prediction": 0.702028969923655,
                        "threshold": 0.3,
                        "is_selected": False
                    }
                },
                "9": {
                    "902": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "903": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "904": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "905": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "906": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    },
                    "907": {
                        "prediction": -1,
                        "threshold": -1,
                        "is_selected": False
                    }
                }
            }
        },
        {
            "type": "text",
            "page": 3,
            "text": "This is a non-relevant text",
            "textOrder": 3,
            "relevant": False,
            "prediction_status": False,
            "geolocations": [],
            "classification": {}
        }
    ]
}
