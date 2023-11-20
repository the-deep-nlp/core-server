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
    "classifications": [
        {
            "client_id": "5",
            "model_preds": {
                "2": {
                    "204": {
                        "2402": {
                            "prediction": 0.4069949281240046,
                            "threshold": 0.489,
                            "is_selected": False,
                        },
                        "2401": {
                            "prediction": 0.27091098129102825,
                            "threshold": 0.461,
                            "is_selected": False,
                        },
                    }
                }
            },
        },
        {
            "client_id": "7",
            "model_preds": {
                "2": {
                    "204": {
                        "2402": {
                            "prediction": 0.5442236220665992,
                            "threshold": 0.489,
                            "is_selected": True,
                        },
                        "2401": {
                            "prediction": 0.4262570897824335,
                            "threshold": 0.461,
                            "is_selected": False,
                        },
                    },
                    "202": {
                        "2206": {
                            "prediction": 0.25068859880169236,
                            "threshold": 0.576,
                            "is_selected": False,
                        },
                        "2201": {
                            "prediction": 0.5456802809044823,
                            "threshold": 0.431,
                            "is_selected": True,
                        },
                    },
                },
                "5": {
                    "503": {
                        "5303": {
                            "prediction": 0.12105567270217965,
                            "threshold": 0.438,
                            "is_selected": False,
                        },
                        "5306": {
                            "prediction": 0.0934217669913229,
                            "threshold": 0.424,
                            "is_selected": False,
                        },
                        "5310": {
                            "prediction": 0.2706523782039786,
                            "threshold": 0.478,
                            "is_selected": False,
                        },
                        "5302": {
                            "prediction": 0.10373815047470006,
                            "threshold": 0.44,
                            "is_selected": False,
                        },
                        "5307": {
                            "prediction": 0.10675184680643865,
                            "threshold": 0.414,
                            "is_selected": False,
                        },
                        "5309": {
                            "prediction": 0.15713495668023825,
                            "threshold": 0.512,
                            "is_selected": False,
                        },
                        "5308": {
                            "prediction": 0.2450807941587348,
                            "threshold": 0.475,
                            "is_selected": False,
                        },
                        "5301": {
                            "prediction": 0.16692731163052263,
                            "threshold": 0.488,
                            "is_selected": False,
                        },
                        "5305": {
                            "prediction": 0.09886651321893601,
                            "threshold": 0.508,
                            "is_selected": False,
                        },
                        "5304": {
                            "prediction": 0.18824445637496742,
                            "threshold": 0.444,
                            "is_selected": False,
                        },
                    },
                    "501": {
                        "5102": {
                            "prediction": 0.21789910171917756,
                            "threshold": 0.541,
                            "is_selected": False,
                        },
                        "5109": {
                            "prediction": 0.3480727123794051,
                            "threshold": 0.454,
                            "is_selected": False,
                        },
                        "5106": {
                            "prediction": 0.23486564947864202,
                            "threshold": 0.381,
                            "is_selected": False,
                        },
                        "5108": {
                            "prediction": 0.05966722541108756,
                            "threshold": 0.527,
                            "is_selected": False,
                        },
                        "5111": {
                            "prediction": 0.46915922655621894,
                            "threshold": 0.447,
                            "is_selected": True,
                        },
                        "5107": {
                            "prediction": 0.3090465321041693,
                            "threshold": 0.449,
                            "is_selected": False,
                        },
                        "5101": {
                            "prediction": 0.015221919587000888,
                            "threshold": 0.47,
                            "is_selected": False,
                        },
                        "5103": {
                            "prediction": 0.3523940058170018,
                            "threshold": 0.482,
                            "is_selected": False,
                        },
                        "5104": {
                            "prediction": 0.003284739766450025,
                            "threshold": 0.786,
                            "is_selected": False,
                        },
                        "5105": {
                            "prediction": 0.22805604930227613,
                            "threshold": 0.534,
                            "is_selected": False,
                        },
                        "5110": {
                            "prediction": 0.20070979371666908,
                            "threshold": 0.05,
                            "is_selected": True,
                        },
                    },
                },
                "4": {
                    "401": {
                        "4102": {
                            "prediction": 0.004212768160319299,
                            "threshold": 0.814,
                            "is_selected": False,
                        },
                        "4101": {
                            "prediction": 0.4228575605351778,
                            "threshold": 0.422,
                            "is_selected": True,
                        },
                    }
                },
            },
        },
    ]
}


"""
it's a huge output (and it can be bigger that this one). Maybe we can truncate it. 
I know that for now all the pdf location infos (x0, y0, etc...) are not needed, but they can be not considered. 
"""
MOCK_ENTRY_CLASSIFICATION_FORMATTED: Dict = {
   "metadata":{
      "total_pages":10,
      "total_words_count":5876,
      "title":"AI in humanitarian domain",
      "author":"D Harvey",
      "keywords":[
         "health",
         "medical treatments"
      ],
      "format":"PDF 1.4"
   },
   "blocks":[
      {
         "type":"text",
         "page":1,
         "x0":0,
         "y0":63.453,
         "x1":545.23,
         "y1":106.23,
         "text":"The 2021 Gu rainy season performance varied across Somalia with many places recording average to below average rainfall (Maps 1 & 2, and Annex I). The seasonal rains which started in late April lasted for three weeks and came to an early end during the first week of May 2021. During the three weeks of rainfall, some places recorded heavy rains that led to flash floods in the northern parts of the country. The southern regions recorded below normal seasonal rains, leaving many places under water stress. This follows another poor rainfall performance during the 2020 Deyr (October- December) season which led to moderate drought conditions this year that lasted till late April",
         "textOrder":1,
         "textCrop":[
            36,
            135.47,
            321.3,
            295.97
         ],
         "relevant": True,
         "classification":{
            "model_preds":[
               {
                  "tags":{
                     "1":{
                        "101":{
                           "prediction":0.0000270270529,
                           "threshold":0.14,
                           "is_selected": False
                        },
                        "102":{
                           "prediction":2.791275697595933,
                           "threshold":0.17,
                           "is_selected": True
                        },
                        "103":{
                           "prediction":0.000845505346661,
                           "threshold":0.1,
                           "is_selected": False
                        },
                        "104":{
                           "prediction":0.001551844096476,
                           "threshold":0.14,
                           "is_selected": False
                        },
                        "105":{
                           "prediction":0.000610130882706,
                           "threshold":0.18,
                           "is_selected": False
                        },
                        "106":{
                           "prediction":0.021222406732185,
                           "threshold":0.14,
                           "is_selected": False
                        },
                        "107":{
                           "prediction":0.000047710691433,
                           "threshold":0.1,
                           "is_selected": False
                        },
                        "108":{
                           "prediction":0.000005902628667,
                           "threshold":0.12,
                           "is_selected": False
                        },
                        "109":{
                           "prediction":5.845728317896525,
                           "threshold":0.15,
                           "is_selected": True
                        },
                        "110":{
                           "prediction":0.000993687879398,
                           "threshold":0.18,
                           "is_selected": False
                        },
                        "111":{
                           "prediction":0.000130282686379,
                           "threshold":0.14,
                           "is_selected": False
                        }
                     },
                     "2":{
                        "201":{
                           "prediction":0.001077209547956,
                           "threshold":0.17,
                           "is_selected": False
                        },
                        "202":{
                           "prediction":0.002082403516397,
                           "threshold":0.15,
                           "is_selected": False
                        },
                        "203":{
                           "prediction":0.027398668074359,
                           "threshold":0.24,
                           "is_selected": False
                        },
                        "204":{
                           "prediction":0.000344154328299,
                           "threshold":0.14,
                           "is_selected": False
                        },
                        "205":{
                           "prediction":0.008931630191968,
                           "threshold":0.47,
                           "is_selected": False
                        },
                        "206":{
                           "prediction":1.561535708606243,
                           "threshold":0.16,
                           "is_selected": True
                        },
                        "207":{
                           "prediction":0.008022336987779,
                           "threshold":0.22,
                           "is_selected": False
                        },
                        "208":{
                           "prediction":0.000339151683008,
                           "threshold":0.21,
                           "is_selected": False
                        },
                        "209":{
                           "prediction":0.664219930768013,
                           "threshold":0.05,
                           "is_selected": False
                        },
                        "210":{
                           "prediction":0.070768408477306,
                           "threshold":0.24,
                           "is_selected": False
                        },
                        "212":{
                           "prediction":0.002422974061882,
                           "threshold":0.31,
                           "is_selected": False
                        },
                        "213":{
                           "prediction":0.000046979557038,
                           "threshold":0.26,
                           "is_selected": False
                        },
                        "214":{
                           "prediction":0.000070475855157,
                           "threshold":0.09,
                           "is_selected": False
                        },
                        "215":{
                           "prediction":0.000008547227329,
                           "threshold":0.15,
                           "is_selected": False
                        },
                        "216":{
                           "prediction":0.000167800135387,
                           "threshold":0.13,
                           "is_selected": False
                        },
                        "217":{
                           "prediction":0.000016116082691,
                           "threshold":0.04,
                           "is_selected": False
                        },
                        "218":{
                           "prediction":0.00002616270649,
                           "threshold":0.09,
                           "is_selected": False
                        },
                        "219":{
                           "prediction":0.000166147779405,
                           "threshold":0.13,
                           "is_selected": False
                        },
                        "220":{
                           "prediction":0.000002293435324,
                           "threshold":0.22,
                           "is_selected": False
                        },
                        "221":{
                           "prediction":2.3751352e-7,
                           "threshold":0.16,
                           "is_selected": False
                        },
                        "222":{
                           "prediction":0.000008183459954,
                           "threshold":0.16,
                           "is_selected": False
                        },
                        "223":{
                           "prediction":0.000764200214892,
                           "threshold":0.09,
                           "is_selected": False
                        },
                        "224":{
                           "prediction":7.88740062e-7,
                           "threshold":0.21,
                           "is_selected": False
                        },
                        "225":{
                           "prediction":0.000002737477267,
                           "threshold":0.04,
                           "is_selected": False
                        },
                        "226":{
                           "prediction":3.95147303e-7,
                           "threshold":0.09,
                           "is_selected": False
                        },
                        "227":{
                           "prediction":0.000015625468157,
                           "threshold":0.07,
                           "is_selected": False
                        },
                        "228":{
                           "prediction":0.000017889078663,
                           "threshold":0.72,
                           "is_selected": False
                        },
                        "229":{
                           "prediction":3.389243e-9,
                           "threshold":0.55,
                           "is_selected": False
                        },
                        "230":{
                           "prediction":0.000016569508455,
                           "threshold":0.61,
                           "is_selected": False
                        },
                        "231":{
                           "prediction":0.000004143511584,
                           "threshold":0.3,
                           "is_selected": False
                        },
                        "232":{
                           "prediction":0.000640358295008,
                           "threshold":0.23,
                           "is_selected": False
                        },
                        "233":{
                           "prediction":0.000006404845789,
                           "threshold":0.31,
                           "is_selected": False
                        },
                        "234":{
                           "prediction":0.000074884925338,
                           "threshold":0.39,
                           "is_selected": False
                        }
                     },
                     "3":{
                        "301":{
                           "prediction":0.000083330627376,
                           "threshold":0.01,
                           "is_selected": False
                        },
                        "302":{
                           "prediction":0.011204658287831,
                           "threshold":0.11,
                           "is_selected": False
                        },
                        "303":{
                           "prediction":0.000861139989483,
                           "threshold":0.38,
                           "is_selected": False
                        },
                        "304":{
                           "prediction":0.000009533644629,
                           "threshold":0.01,
                           "is_selected": False
                        },
                        "305":{
                           "prediction":0.010194102137843,
                           "threshold":0.17,
                           "is_selected": False
                        },
                        "306":{
                           "prediction":0.000047473428519,
                           "threshold":0.15,
                           "is_selected": False
                        },
                        "307":{
                           "prediction":0.00275926431641,
                           "threshold":0.09,
                           "is_selected": False
                        },
                        "308":{
                           "prediction":0.006035644596872,
                           "threshold":0.13,
                           "is_selected": False
                        },
                        "309":{
                           "prediction":0.000018762974768,
                           "threshold":0.07,
                           "is_selected": False
                        },
                        "310":{
                           "prediction":0.16048023244366,
                           "threshold":0.16,
                           "is_selected": True
                        },
                        "311":{
                           "prediction":0.001379056581451,
                           "threshold":0.15,
                           "is_selected": False
                        },
                        "312":{
                           "prediction":0.144955087453127,
                           "threshold":0.2,
                           "is_selected": False
                        },
                        "313":{
                           "prediction":0.042628173832782,
                           "threshold":0.16,
                           "is_selected": False
                        },
                        "314":{
                           "prediction":0.000043664708755,
                           "threshold":0.05,
                           "is_selected": False
                        },
                        "315":{
                           "prediction":0.000097360397275,
                           "threshold":0.45,
                           "is_selected": False
                        },
                        "316":{
                           "prediction":0.000012243420618,
                           "threshold":0.06,
                           "is_selected": False
                        },
                        "317":{
                           "prediction":0.000005113670909,
                           "threshold":0.28,
                           "is_selected": False
                        },
                        "318":{
                           "prediction":0.000393391634973,
                           "threshold":0.13,
                           "is_selected": False
                        }
                     },
                     "4":{
                        "401":{
                           "prediction":1.17259055e-7,
                           "threshold":0.29,
                           "is_selected": False
                        },
                        "402":{
                           "prediction":0.000013744229364,
                           "threshold":0.45,
                           "is_selected": False
                        },
                        "403":{
                           "prediction":4.87375621e-7,
                           "threshold":0.03,
                           "is_selected": False
                        },
                        "404":{
                           "prediction":1.85885169e-7,
                           "threshold":0.34,
                           "is_selected": False
                        },
                        "405":{
                           "prediction":3.05366841e-7,
                           "threshold":0.37,
                           "is_selected": False
                        },
                        "406":{
                           "prediction":0.000034889759263,
                           "threshold":0.25,
                           "is_selected": False
                        },
                        "407":{
                           "prediction":0.000001803972996,
                           "threshold":0.07,
                           "is_selected": False
                        },
                        "408":{
                           "prediction":0.001109504095935,
                           "threshold":0.11,
                           "is_selected": False
                        },
                        "409":{
                           "prediction":2.59159425e-7,
                           "threshold":0.43,
                           "is_selected": False
                        },
                        "410":{
                           "prediction":1.45469337e-7,
                           "threshold":0.23,
                           "is_selected": False
                        },
                        "411":{
                           "prediction":0.000005189525136,
                           "threshold":0.06,
                           "is_selected": False
                        },
                        "412":{
                           "prediction":0.000002016342806,
                           "threshold":0.36,
                           "is_selected": False
                        }
                     },
                     "5":{
                        "501":{
                           "prediction":0.000025967284374,
                           "threshold":0.45,
                           "is_selected": False
                        },
                        "502":{
                           "prediction":0.000565126356378,
                           "threshold":0.48,
                           "is_selected": False
                        }
                     },
                     "6":{
                        "601":{
                           "prediction":0.000177106418657,
                           "threshold":0.06,
                           "is_selected": False
                        },
                        "602":{
                           "prediction":0.00055463691145,
                           "threshold":0.48,
                           "is_selected": False
                        },
                        "603":{
                           "prediction":0.000022633564774,
                           "threshold":0.34,
                           "is_selected": False
                        },
                        "604":{
                           "prediction":0.001842333040258,
                           "threshold":0.16,
                           "is_selected": False
                        }
                     },
                     "7":{
                        "701":{
                           "prediction":0.000903384244777,
                           "threshold":0.27,
                           "is_selected": False
                        },
                        "702":{
                           "prediction":0.001251186238898,
                           "threshold":0.11,
                           "is_selected": False
                        },
                        "703":{
                           "prediction":0.000834142483654,
                           "threshold":0.05,
                           "is_selected": False
                        },
                        "704":{
                           "prediction":0.000382219089564,
                           "threshold":0.24,
                           "is_selected": False
                        },
                        "705":{
                           "prediction":0.001979890172758,
                           "threshold":0.12,
                           "is_selected": True
                        }
                     },
                     "8":{
                        "801":{
                           "prediction":0.000014654744629,
                           "threshold":0.66,
                           "is_selected": False
                        },
                        "802":{
                           "prediction":0.000044733506002,
                           "threshold":0.3,
                           "is_selected": False
                        },
                        "803":{
                           "prediction":0.001036487083184,
                           "threshold":0.36,
                           "is_selected": False
                        },
                        "804":{
                           "prediction":0.000707629901033,
                           "threshold":0.23,
                           "is_selected": False
                        },
                        "805":{
                           "prediction":0.00003381500674,
                           "threshold":0.58,
                           "is_selected": False
                        },
                        "806":{
                           "prediction":0.702028969923655,
                           "threshold":0.3,
                           "is_selected": False
                        }
                     },
                     "9":{
                        "902":{
                           "prediction":-1,
                           "threshold":-1,
                           "is_selected": False
                        },
                        "903":{
                           "prediction":-1,
                           "threshold":-1,
                           "is_selected": False
                        },
                        "904":{
                           "prediction":-1,
                           "threshold":-1,
                           "is_selected": False
                        },
                        "905":{
                           "prediction":-1,
                           "threshold":-1,
                           "is_selected": False
                        },
                        "906":{
                           "prediction":-1,
                           "threshold":-1,
                           "is_selected": False
                        },
                        "907":{
                           "prediction":-1,
                           "threshold":-1,
                           "is_selected": False
                        }
                     }
                  },
                  "prediction_status": "1",
                  "model_info":{
                     "id": "all_tags_model",
                     "version": "1.0.0"
                  }
               }
            ]
         }
      }
   ]
}

"""
MOCK_ENTRY_CLASSIFICATION_FORMATTED: Dict = {
   "metadata": {
      "format": "PDF 1.7",
      "title": "",
      "author": "ACAPS",
      "subject": "",
      "keywords": [],
      "creator": "Microsoft Word for Office 365",
      "producer": "Microsoft Word for Office 365",
      "creationDate": "D:20191021144502+02'00'",
      "modDate": "D:20191021145218+02'00'",
      "trapped": "",
      "encryption": "null",
      "total_pages": 1,
      "total_words_count": 1,
      "format": "pdf"
   },
   "blocks": [
      {
         "type": "text",
         "page": 0,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 543.7218933105469,
         "y1": 109.99737167358398,
         "rect": [
            0.0,
            0.0,
            543.7218933105469,
            109.99737167358398
         ],
         "text": "NIGERIA Floods in Borno, Delta, Kebbi, and Kogi states",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            36.95722961425781,
            511.9797668457031,
            106.2417221069336
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 0,
         "x0": 0.0,
         "y0": 109.99737167358398,
         "x1": 543.7218933105469,
         "y1": 261.5125198364258,
         "rect": [
            0.0,
            109.99737167358398,
            543.7218933105469,
            261.5125198364258
         ],
         "text": "Seasonal rainfall and subsequent high-water levels in Niger and Benue rivers have been causing flooding across Nigeria since June 2019. Floods have worsened after a peak in water levels in late September (Floodlist 07/10/2019). According to the latest situation report from 7 October, the floods severely affected 32 of the 36 states and Federal Capital Territory, killing several people, displacing thousands, and causing crop damage to varying degrees across the country (IFRC EPoA 07/10/2019).",
         "textOrder": 1,
         "textCrop": [
            28.079999923706055,
            113.75302124023438,
            405.02587890625,
            192.47804260253906
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.5427906118287631,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.2051073564883168,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 1.0259111101428668,
                     "threshold": 0.576,
                     "is_selected": True
                  },
                  "2205": {
                     "prediction": 0.988062537674393,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.040246154810112664,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.9455283943848931,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.18819280572839686,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.08064990438390196,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 1.3525349753243583,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.4348178874601071,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.2827691658526723,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 0.7415681938144648,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 1.2460033007086562,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.07756241068211796,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.04706512542535842,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.21902838157951282,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 1.1884789392738144,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.09979363634546523,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.21285283160798343,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.5394365302671676,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.30628130235503204,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.09895403920045082,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.045802691975274146,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.3374951382250753,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.4365343664740694,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.42819248192986326,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.14366185692347347,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.0479789406834346,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.13738847240244495,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.04137190566821532,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.16792150943175607,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.13937850599177182,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.1334342360496521,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.18934908582538856,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.13496184090929708,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.08050439594028232,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.0675917842361711,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.36593306694786976,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.022874643972383084,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.009642987277012396,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.09187975985891866,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.1274348466858301,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.005431397956736544,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.18650534489342782,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00022163694388524608,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.11262490173404135,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.0031950289849191904,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.16710934986979326,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.08756965236466434,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.07365371318573648,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.16854981581370035,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.011931296792768296,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.4366129764671489,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.3189826137805111,
                     "threshold": 0.378,
                     "is_selected": False
                  },
                  "5603": {
                     "prediction": 0.08659908765053685,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.517577690593267,
                     "threshold": 0.472,
                     "is_selected": True
                  },
                  "5602": {
                     "prediction": 0.6581762833381767,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0005074276104948971,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.016283249397221485,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0006243614687588713,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.011907624884212152,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.00318835611211623,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.060000240942354226,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.011765840636663341,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.04384389056589841,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.02248919541109044,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.054345498428101525,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0007885749588107191,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.022592378317276177,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0005477802207881016,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.5108864174634925,
                     "threshold": 0.422,
                     "is_selected": True
                  },
                  "3101": {
                     "prediction": 0.10232400501706473,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.020788540935208058,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.34287748858332634,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.1292991644096753,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.3833027151219711,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.062354664247827374,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.13527545635983096,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.4955251797211828,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.2231013987203894,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0016698181669176355,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.029320116615742957,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.003629504519284045,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.05535083212729158,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.011620505598326903,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.009934033523959399,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.004031222779303789,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.02316315793495344,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.02147948914720985,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.022173227473691978,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.027031593861571255,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.04983760368645319,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.013643909417288868,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.2919595797085068,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.8922863670469197,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.03058907315738288,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.2097095475419537,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.030906303913147692,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.09271281824749747,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.00788727602748959,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.0770031440037268,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.028255073324082388,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.03855030408641636,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.07798569276928902,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.9414986301870907,
                     "threshold": 0.425,
                     "is_selected": True
                  },
                  "3701": {
                     "prediction": 0.015059664929653964,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 1.3672834148212354,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.3669742816760216,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0020658402275797487,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.36343607292356084,
                     "threshold": 0.422,
                     "is_selected": False
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.00236868119780458,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.19957157793399802,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.02531099206268887,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.17125685316071546,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.05326369861639086,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.050459563246239784,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.16219726523513314,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.49106950618036826,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.033982182289920955,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.4612952470779419,
                     "threshold": 0.466,
                     "is_selected": False
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.9542594133819665,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.8428506169122518,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.566157611828406,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.41830587771631056,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.06847826800509996,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.005812385866233894,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.04272257266606826,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.021048961821136726,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.019540015959226695,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.027792200936076324,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.0020435245600170814,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.013217612619127206,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.24511967331106388,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.2048993671712605,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.004885870311095658,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.02732600354244688,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.064895318614112,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.00884607896551526,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.16654483457603078,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.012083866011963413,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.028268588387002847,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.025565219447784816,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.014111534299620664,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.02440607023575112,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.019819518412955463,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.006560413166880608,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.0023820810357405658,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.0052659290450063736,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.013677510657939769,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.005801920565069374,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.039586182104645616,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.01739774861867141,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.11859711134031917,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.01797955483198166,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.06537258322608426,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.030150983745799116,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.00558186990104073,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.12183886706125475,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 0,
         "x0": 289.7720031738281,
         "y0": 261.5125198364258,
         "x1": 543.7218933105469,
         "y1": 346.7069854736328,
         "rect": [
            289.7720031738281,
            261.5125198364258,
            543.7218933105469,
            346.7069854736328
         ],
         "text": "Source: IFRC EPoA 07/10/2019",
         "textOrder": 2,
         "textCrop": [
            416.2099914550781,
            330.5469970703125,
            529.7337646484375,
            341.5939636230469
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 0,
         "x0": 543.7218933105469,
         "y0": 0.0,
         "x1": 842.0399780273438,
         "y1": 110.35965347290039,
         "rect": [
            543.7218933105469,
            0.0,
            842.0399780273438,
            110.35965347290039
         ],
         "text": "Briefing note \u2013 17 October 2019",
         "textOrder": 3,
         "textCrop": [
            649.9000244140625,
            86.60721588134766,
            815.0582275390625,
            101.80929565429688
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 0,
         "x0": 543.7218933105469,
         "y0": 110.35965347290039,
         "x1": 842.0399780273438,
         "y1": 143.24000549316406,
         "rect": [
            543.7218933105469,
            110.35965347290039,
            842.0399780273438,
            143.24000549316406
         ],
         "text": "Affected population (per 1000 people)",
         "textOrder": 4,
         "textCrop": [
            707.3800048828125,
            118.9100112915039,
            791.8903198242188,
            143.18301391601562
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 0,
         "x0": 543.7218933105469,
         "y0": 143.24000549316406,
         "x1": 746.0530090332031,
         "y1": 229.49049377441406,
         "rect": [
            543.7218933105469,
            143.24000549316406,
            746.0530090332031,
            229.49049377441406
         ],
         "text": "Borno Kebbi",
         "textOrder": 5,
         "textCrop": [
            707.3800048828125,
            147.78501892089844,
            731.446044921875,
            224.14100646972656
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 0,
         "x0": 746.0530090332031,
         "y0": 143.24000549316406,
         "x1": 842.0399780273438,
         "y1": 229.49049377441406,
         "rect": [
            746.0530090332031,
            143.24000549316406,
            842.0399780273438,
            229.49049377441406
         ],
         "text": "6,69 per 1000 people 8,01 per 1000 3,63 per 1000 people 1,47 per 1000",
         "textOrder": 6,
         "textCrop": [
            760.6599731445312,
            143.2969970703125,
            810.1304321289062,
            229.01397705078125
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 0,
         "x0": 543.7218933105469,
         "y0": 229.49049377441406,
         "x1": 842.0399780273438,
         "y1": 296.4169921875,
         "rect": [
            543.7218933105469,
            229.49049377441406,
            842.0399780273438,
            296.4169921875
         ],
         "text": "Source: IFRC EPoA 07/10/2019",
         "textOrder": 7,
         "textCrop": [
            702.0999755859375,
            229.96701049804688,
            815.603759765625,
            241.01397705078125
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 0,
         "x0": 543.7218933105469,
         "y0": 559.116455078125,
         "x1": 842.0399780273438,
         "y1": 595.3200073242188,
         "rect": [
            543.7218933105469,
            559.116455078125,
            842.0399780273438,
            595.3200073242188
         ],
         "text": "Any questions? Please contact us at info@acaps.org",
         "textOrder": 8,
         "textCrop": [
            626.739990234375,
            570.572998046875,
            814.1712646484375,
            581.6199340820312
         ],
         "relevant": False
      },
      {
         "type": "image",
         "page": 0,
         "x0": 701.97998046875,
         "y0": 208.37002563476562,
         "x1": 737.5,
         "y1": 229.61001586914062,
         "rect": [
            701.97998046875,
            208.37002563476562,
            737.5,
            229.61001586914062
         ],
         "imageLink": "pic-4f271128-4087-4d80-8d4b-cf486be2149c.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": "Kogi"
      },
      {
         "type": "table",
         "page": 0,
         "x0": 701.97998046875,
         "y0": 165.6199951171875,
         "x1": 815.4039916992188,
         "y1": 187.22000122070312,
         "rect": [
            701.97998046875,
            165.6199951171875,
            815.4039916992188,
            187.22000122070312
         ],
         "tableImageLink": "table-9a24952b-b021-4537-81b8-03c073264fd8.png",
         "tableCaption": "undefined",
         "tableMeta": "undefined",
         "tableText": "Delta\npeople"
      },
      {
         "type": "table",
         "page": 0,
         "x0": 28.079999923706055,
         "y0": 344.3500061035156,
         "x1": 814.9200439453125,
         "y1": 559.89599609375,
         "rect": [
            28.079999923706055,
            344.3500061035156,
            814.9200439453125,
            559.89599609375
         ],
         "tableImageLink": "table-f08ca138-bb5f-4568-9325-e057114dd11c.png",
         "tableCaption": "undefined",
         "tableMeta": "undefined",
         "tableText": "Anticipated scope and scale Key priorities (country level) Humanitarian constraints\nThe flooding is estimated to have affected over 210,000 130,000 Humanitarian access to Borno state is severely\npeople, with about 130,000 of them being displaced limited due to security concerns and poor road\npeople displaced\n(IFRC EPoA 07/10/2019). Rainfall is predicted to continue in infrastructure. Monitoring the security situation in\ncentral Nigeria in the week of 17-23 October (NOAA). Kogi and Delta states is recommended due to the\nWASH\nFlooding has destroyed or flooded IDP camps across ongoing Middle Belt conflict. Destroyed bridges and\ndestruction of WASH facilities\nnorth-eastern states, especially in Borno. People in camps in flooded roads can further constrain access but data\nBorno face increased health risks and lack access to on infrastructure damage across states is lacking.\nWASH facilities.\nShelter\nflooding of camps and houses\nLimitations: Data is often not disaggregated by geographical area\nand information on sectoral needs is uneven, focusing largely on camp\nsites in north-eastern states and only sporadically on humanitarian\nHealth\nneeds in other states. This makes it difficult to ascertain the full impact\nrisk of disease outbreaks\nof the floods and the severity of humanitarian need in each state."
      },
      {
         "type": "image",
         "page": 0,
         "x0": 737.5,
         "y0": 208.37002563476562,
         "x1": 815.4039916992188,
         "y1": 229.61001586914062,
         "rect": [
            737.5,
            208.37002563476562,
            815.4039916992188,
            229.61001586914062
         ],
         "imageLink": "pic-b233080c-6209-43b8-9972-3ebd80aff1e8.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": "people"
      },
      {
         "type": "image",
         "page": 0,
         "x0": 415.5,
         "y0": 122.25,
         "x1": 694.4599609375,
         "y1": 328.75,
         "rect": [
            415.5,
            122.25,
            694.4599609375,
            328.75
         ],
         "imageLink": "pic-fc015e36-d3a6-48a3-a108-0d01b2b50008.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 285.75,
         "y0": 359.489990234375,
         "x1": 370.75,
         "y1": 444.489990234375,
         "rect": [
            285.75,
            359.489990234375,
            370.75,
            444.489990234375
         ],
         "imageLink": "pic-e84639fe-7b7b-4cd4-a897-e405fdcfabf3.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 29.0,
         "y0": 207.25001525878906,
         "x1": 285.6099853515625,
         "y1": 253.70001220703125,
         "rect": [
            29.0,
            207.25001525878906,
            285.6099853515625,
            253.70001220703125
         ],
         "imageLink": "pic-4630f6d9-73f3-4a98-97e0-b8fe16041e92.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 630.2999877929688,
         "y0": 57.5,
         "x1": 701.3779907226562,
         "y1": 79.25,
         "rect": [
            630.2999877929688,
            57.5,
            701.3779907226562,
            79.25
         ],
         "imageLink": "pic-784fc929-bfe3-42d6-93a7-7d70663d3088.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 29.299999237060547,
         "y0": 268.4499816894531,
         "x1": 285.79998779296875,
         "y1": 314.8999938964844,
         "rect": [
            29.299999237060547,
            268.4499816894531,
            285.79998779296875,
            314.8999938964844
         ],
         "imageLink": "pic-910a9c03-5fc6-4ead-b85e-8d4f6a708f0a.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 530.5499877929688,
         "y0": 359.2900085449219,
         "x1": 615.5499877929688,
         "y1": 444.2900085449219,
         "rect": [
            530.5499877929688,
            359.2900085449219,
            615.5499877929688,
            444.2900085449219
         ],
         "imageLink": "pic-0ffe3b91-a4b5-490d-946b-79b4c738d533.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 285.75,
         "y0": 404.489990234375,
         "x1": 370.75,
         "y1": 489.489990234375,
         "rect": [
            285.75,
            404.489990234375,
            370.75,
            489.489990234375
         ],
         "imageLink": "pic-bc2715af-5c1a-44fc-be26-ecc36e9b80ef.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 285.75,
         "y0": 450.2440185546875,
         "x1": 370.75,
         "y1": 535.2440185546875,
         "rect": [
            285.75,
            450.2440185546875,
            370.75,
            535.2440185546875
         ],
         "imageLink": "pic-1d67cc7e-a6e2-42bb-bc96-846075a6e8fe.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 286.04998779296875,
         "y0": 488.9940185546875,
         "x1": 371.04998779296875,
         "y1": 573.9940185546875,
         "rect": [
            286.04998779296875,
            488.9940185546875,
            371.04998779296875,
            573.9940185546875
         ],
         "imageLink": "pic-35e9c2cd-94ab-45eb-93a7-add960c73dc4.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "image",
         "page": 0,
         "x0": 710.9000244140625,
         "y0": 50.900001525878906,
         "x1": 820.7000122070312,
         "y1": 85.5,
         "rect": [
            710.9000244140625,
            50.900001525878906,
            820.7000122070312,
            85.5
         ],
         "imageLink": "pic-f8f4c812-a5bc-4c49-9516-8fc0ba387ac9.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "text",
         "page": 1,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 421.0233154296875,
         "y1": 66.79900741577148,
         "rect": [
            0.0,
            0.0,
            421.0233154296875,
            66.79900741577148
         ],
         "text": "Crisis impact",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            43.47001647949219,
            122.34001159667969,
            64.1250228881836
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 0.0,
         "y0": 66.79900741577148,
         "x1": 421.0233154296875,
         "y1": 160.49553680419922,
         "rect": [
            0.0,
            66.79900741577148,
            421.0233154296875,
            160.49553680419922
         ],
         "text": "As a result of heavy rainfalls and high water levels in the Niger and Benue rivers, the two main rivers of Nigeria, a series of flooding has submerged areas across the country in water since June 2019. Following a peak in water levels of rivers Niger and Benue in late September, severe flooding aggravated the situation (Floodlist 07/10/2019). The National Emergency Management Agency (NEMA) has not declared a state of emergency but the Nigeria Hydrological Services Agency (NIHSA) had issued a flood red alert earlier in September (Sahara Reporters 17/09/2019).",
         "textOrder": 1,
         "textCrop": [
            28.079999923706055,
            69.47299194335938,
            410.9566345214844,
            158.99806213378906
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 0.0,
         "y0": 160.49553680419922,
         "x1": 421.0233154296875,
         "y1": 303.68553161621094,
         "rect": [
            0.0,
            160.49553680419922,
            421.0233154296875,
            303.68553161621094
         ],
         "text": "According to the latest statistics issued by the International Federation of Red Cross (IFRC) on 7 October, severe floods occurred in 32 of the 36 states and Federal Capital Territory and it is estimated that in total over 210,000 people are affected with about 130,000 of them being displaced and at least 12 reported deaths in Cross River and Niger states (IFRC EPoA 07/10/2019). No updated estimations were available but since rainfall has been ongoing and is predicted to continue in central Nigeria (NOAA), the number of people affected by the floods is likely to have increased. Moreover, the total number of fatalities is likely to be higher. As of 30 August, at least 15 people had also been killed in Adamawa state (OCHA SitRep 2 30/08/2019) and additional deaths in flood-related accidents in other states keep being reported, for instance in Lagos and Delta state (Guardian Nigeria 12/10/2019 and 23/09/2019).",
         "textOrder": 2,
         "textCrop": [
            28.079999923706055,
            161.99301147460938,
            410.9566345214844,
            302.18804931640625
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 0.0,
         "y0": 303.68553161621094,
         "x1": 421.0233154296875,
         "y1": 388.93043518066406,
         "rect": [
            0.0,
            303.68553161621094,
            421.0233154296875,
            388.93043518066406
         ],
         "text": "According to assessments of the Nigerian Red Cross Society (NRCS), the numbers of affected people in Borno and Delta states are higher than in Kebbi and Kogi. For Delta, estimations range between 40,000 and 60,000 affected people, for Borno between 20,000 and 40,000 people (IFRC EPoA 07/10/2019). Other severely affected states in terms of the total number of affected people include Anambra, Bauchi, Jigawa, and Lagos.",
         "textOrder": 3,
         "textCrop": [
            28.079999923706055,
            305.1830139160156,
            410.9151306152344,
            382.1280517578125
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 0.0,
         "y0": 388.93043518066406,
         "x1": 421.0233154296875,
         "y1": 443.29042053222656,
         "rect": [
            0.0,
            388.93043518066406,
            421.0233154296875,
            443.29042053222656
         ],
         "text": "AFFECTED POPULATION RATES (PER 1000 PEOPLE) BORNO",
         "textOrder": 4,
         "textCrop": [
            130.94000244140625,
            395.7328186035156,
            289.2440185546875,
            440.3280334472656
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 0.0,
         "y0": 490.5384216308594,
         "x1": 421.0233154296875,
         "y1": 595.3200073242188,
         "rect": [
            0.0,
            490.5384216308594,
            421.0233154296875,
            595.3200073242188
         ],
         "text": "Source: IFRC EPoA 07/10/2019",
         "textOrder": 5,
         "textCrop": [
            128.4199981689453,
            493.5588073730469,
            274.53009033203125,
            528.3399658203125
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 0.0,
         "x1": 842.0399780273438,
         "y1": 38.868499755859375,
         "rect": [
            421.0233154296875,
            0.0,
            842.0399780273438,
            38.868499755859375
         ],
         "text": "ACAPS Briefing Note: Floods in Nigeria",
         "textOrder": 6,
         "textCrop": [
            674.02001953125,
            22.557010650634766,
            814.0595703125,
            33.603973388671875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 38.868499755859375,
         "x1": 842.0399780273438,
         "y1": 118.3155288696289,
         "rect": [
            421.0233154296875,
            38.868499755859375,
            842.0399780273438,
            118.3155288696289
         ],
         "text": "As the floods affect states across the different geo-political zones in the country as well as different population groups, especially IDPs and host communities, sectoral needs and gaps vary. Information on specific needs across states is uneven and focuses particularly on flood-related needs in context of the humanitarian crisis in north-east Borno, Adamawa, and Yobe (BAY) states (ex. CCCM MST report 3 04/10/2019).",
         "textOrder": 7,
         "textCrop": [
            431.0899963378906,
            44.133026123046875,
            814.0199584960938,
            108.47804260253906
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 118.3155288696289,
         "x1": 842.0399780273438,
         "y1": 206.48552703857422,
         "rect": [
            421.0233154296875,
            118.3155288696289,
            842.0399780273438,
            206.48552703857422
         ],
         "text": "Shelter/NFI: Displacement and shelter damage are widespread across flood-affected states. Heavy rains and flooding in northeast Nigeria destroyed emergency and makeshift camps, rendering IDP residents homeless or forced to stay with family members and friends in overcrowded shelters (NRC 23/08/2019). The destruction and flooding of camps happened particularly in Borno state where, as of 30 August, 68 camps and IDP settlement were affected (OCHA SitRep 2 30/08/2019).",
         "textOrder": 8,
         "textCrop": [
            431.0899963378906,
            128.15301513671875,
            813.9777221679688,
            204.98805236816406
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 1.2886018353249642,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.2994158844627165,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.2574169387420019,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.6193290464580059,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.03360444301269888,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.9406379784896036,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.15789589711597987,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.05902864627147975,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 1.021475647832011,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.8602847679902988,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.27919819751517044,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 0.9580476679534555,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 1.5015749402739986,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.10443171466143548,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.11775677579876181,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.11685006662246283,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 1.0143524624523104,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.1862712467092751,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.17033009924025203,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.269845409213372,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.2541575185229293,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.05172859779905745,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.025594448790145226,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.6651679220134116,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 1.670855900336956,
                     "threshold": 0.464,
                     "is_selected": True
                  },
                  "2108": {
                     "prediction": 0.13200594634070664,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.10040871050532006,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.010860786237314625,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.09837823775772271,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.010523964142934843,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.10764718523635956,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.08097956015262753,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.218476182536075,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.10092849614190273,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.07163622511888114,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.0871737311417992,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.04136761006608247,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 1.294437877932309,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.007919602345411232,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.004470332011410815,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.02966952037224567,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.11437445182046274,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.001565607120976486,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.4593083225345216,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00010466677012009683,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.1249694534008869,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.0017634028336033225,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.2185693685559259,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.05102552035275627,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.04544764598633381,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.3732075293858846,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.014350974843615577,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.33625797268658747,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.5125244537358562,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.15413948917776588,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.1362030378590196,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.8746417452446856,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0010771686203929604,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.008529336212348726,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.000561505393234427,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.02758456800307519,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.000952773782314952,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.012561837014953761,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.004666510486406812,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.011178329153809436,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.05925963462587211,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.050409715656591456,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0009573757557607279,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.025846363764852,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0005010987378126528,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.1765627996616454,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.04356397016916746,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.019362536740714108,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.22823979767660302,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.11077900934550497,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.3129212518193028,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.08462286483840782,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.09609485771191323,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.5853288679671802,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.2032533553417099,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0011666677535105885,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.024837843832200706,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.0029735589173511354,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.02515291763019973,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.009207817624150365,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.003923834825685129,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.0017128099820443562,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.04136093984028357,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.013171477392032572,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.02103219348966792,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.06294459698424823,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.0860029771700661,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.019955577475852086,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.4374441591281335,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.8599032212689195,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.02610442692391303,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.20258263735980778,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.0382702338270599,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.08017376792911765,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.0023350059227259068,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.02944762990982444,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.02319735312272632,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.02483355810644909,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.054633004407657955,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.5627596027710858,
                     "threshold": 0.425,
                     "is_selected": True
                  },
                  "3701": {
                     "prediction": 0.014925152835087137,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.8600966206618718,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.3120448486304577,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0007438331245186142,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.7408117231034554,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.0021530446814155423,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.1912008424817342,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.012183037954996744,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.05005926191063593,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.10520833785887118,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.016975429152017052,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.8711877983821014,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "4302": {
                     "prediction": 0.8825252612613704,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.051372584565884644,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.40948266251404397,
                     "threshold": 0.466,
                     "is_selected": False
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 1.1102884843204561,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 1.3681034144667006,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.6516188817116821,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.33054158331886413,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.13003393313756176,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.01364369113166053,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.12066737468065653,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.06198713980376608,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.0705801973455265,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.06501591614449646,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.007935417278741414,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.0396147694679635,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.15976645230212594,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.11366203065343232,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.009468898509538134,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.028696046930360375,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.08569121360778809,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.017583903520577756,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.1162676749253037,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.0071641582897420345,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.026193541484047667,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.0410041166949518,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.017781510769602764,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.058417152107881856,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.06985238155423293,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.05017961211064283,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.003442528617122899,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.012717629987292174,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.09484832836349658,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.009809762312820755,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.15580289336066172,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.06646519670119652,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.30453503131866455,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.03565978439687525,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.09670837806379662,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.03681826638057828,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.014296893203100621,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.0782063636068148,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 206.48552703857422,
         "x1": 842.0399780273438,
         "y1": 235.82552337646484,
         "rect": [
            421.0233154296875,
            206.48552703857422,
            842.0399780273438,
            235.82552337646484
         ],
         "text": "In some flood-prone regions like Kogi state, emergency shelters were opened for people who had to leave their homes due to the floods (Pulse 22/09/2019).",
         "textOrder": 9,
         "textCrop": [
            431.0899963378906,
            207.98300170898438,
            813.7235717773438,
            234.26805114746094
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 235.82552337646484,
         "x1": 842.0399780273438,
         "y1": 315.68553161621094,
         "rect": [
            421.0233154296875,
            235.82552337646484,
            842.0399780273438,
            315.68553161621094
         ],
         "text": "WASH: In camps covered by Camp Coordination and Camp Management (CCCM) partner agencies in northeast Nigeria, WASH needs are severe because latrines and showers need to be repaired (CCCM MST report 3 04/10/2019). In many camps, people have no choice than to practice open defecation increasing the risk of the outbreak of diseases (NRC 23/08/2019). Specific WASH related needs in other states remain unclear.",
         "textOrder": 10,
         "textCrop": [
            431.0899963378906,
            237.38299560546875,
            813.9166259765625,
            314.18804931640625
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 315.68553161621094,
         "x1": 842.0399780273438,
         "y1": 383.0255126953125,
         "rect": [
            421.0233154296875,
            315.68553161621094,
            842.0399780273438,
            383.0255126953125
         ],
         "text": "Food: In September, households in Delta, Kebbi, and Kogi states faced only minimal food insecurity (IPC Phase 1) and there are no reports of current food shortages in these states, though it is likely that flood-displaced people will require food assistance (FEWS NET 09/2019). Due to loss of livestock and crops, food needs among communities depending on agriculture may remain once the floods have subsided.",
         "textOrder": 11,
         "textCrop": [
            431.0899963378906,
            317.1830139160156,
            813.9736938476562,
            381.52801513671875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 383.0255126953125,
         "x1": 842.0399780273438,
         "y1": 450.2255096435547,
         "rect": [
            421.0233154296875,
            383.0255126953125,
            842.0399780273438,
            450.2255096435547
         ],
         "text": "Households in conflict-affected Borno state, however, faced Emergency (IPC Phase 4) and Crisis (IPC Phase 3) food security outcomes in September (FEWS NET 09/2019). As of July 2019, over 2 million people in Borno, Adamawa, and Yobe states have received food assistance (OCHA 08/2019). In camps covered by CCCM, food gaps existed as of 4 October (CCCM MST report 3 04/10/2019).",
         "textOrder": 12,
         "textCrop": [
            431.0899963378906,
            384.52301025390625,
            813.9554443359375,
            448.72802734375
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.5589639482322646,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.21794435129765574,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.07243385253888038,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.6883915380707809,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.07812275997991484,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.5941652366567377,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.4040482364105902,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.1227148694165966,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.34293014924604814,
                     "threshold": 0.455,
                     "is_selected": False
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.7006334354941595,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 1.0283182558179158,
                     "threshold": 0.463,
                     "is_selected": True
                  },
                  "2305": {
                     "prediction": 1.2208921051471033,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.8233907454008318,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.11333182743764593,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.07911287178241737,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.09137253969087512,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.781664499347074,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.08252895470010548,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 1.7534019770445648,
                     "threshold": 0.486,
                     "is_selected": True
                  },
                  "2110": {
                     "prediction": 0.2082235939347769,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.18042355643964447,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.05894129949676199,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.13071623368140978,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.3521807611125012,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.14236349419787012,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.06833263943272253,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.14333988297475528,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.026314971827954618,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.12518584759414944,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.019579531032253395,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.180754864561385,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.12534671986941248,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.2167939198644538,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.16884594300731284,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.15138385920074043,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.07914431258901819,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.1381037278228238,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.3133536632365592,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.01933962947583887,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.0076377172327019,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.07059119258417645,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.11330154332392466,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.0059335859135744426,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.4153285654748624,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00042350853600186167,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.09580461608336659,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.003372736682649702,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.2984299978114063,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.059054649083962366,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.046979659732351915,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.32474170128504437,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.014206358187255404,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.4233682424213753,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.43316863516651133,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.151886395241833,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.45026090564364096,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.2022211628766795,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.001079352776195889,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.01001368418467978,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.002682865604595026,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.01835996835749831,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.0015054525019314712,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.02151879697898512,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.005913629698065611,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.017406326377996682,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.01516058558344445,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.041174208694468424,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0032317154563781692,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.015011399998715388,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0018570622665316076,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.06527004772311704,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.015498548094566467,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.008378587342027961,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.5464841922124227,
                     "threshold": 0.48,
                     "is_selected": True
                  },
                  "3203": {
                     "prediction": 0.18405804913195353,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.06006751437204683,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.2009595955620293,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.22413295898902216,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.594666964716191,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.22898709197687434,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0025676277700377387,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.04069268728889296,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.005991025635579584,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.01639078274883073,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.005155535450324649,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.011386776716732473,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.002676258528871196,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.07381440073655238,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.01451944464909713,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.010158114648894916,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.03610643814655318,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.05692299415518946,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.02367367249047547,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.12218856695786263,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.9230933812859561,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.2514206415969833,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.4168928570144779,
                     "threshold": 0.364,
                     "is_selected": True
                  },
                  "3504": {
                     "prediction": 0.07508532906773002,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.2745084005809387,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.009452021266851159,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.06143979866195608,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.0986213544531474,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.05872376363149425,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.11831192208118126,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.29631078243255615,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.023966309616233444,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.2336055040359497,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.09378427524625518,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.002900291524864093,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.6021242147373362,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.07914136732359986,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.9985888291239999,
                     "threshold": 0.457,
                     "is_selected": True
                  },
                  "4201": {
                     "prediction": 0.10734749258261093,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.6916816543759847,
                     "threshold": 0.401,
                     "is_selected": True
                  },
                  "4206": {
                     "prediction": 0.8109611738856437,
                     "threshold": 0.486,
                     "is_selected": True
                  },
                  "4205": {
                     "prediction": 0.1166572902297628,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.3266211138331415,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.7331206269340602,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.22438151688225524,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.7905166420302165,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.5641535583122,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.41847096122417254,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.5057523551496488,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.29982244896311916,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.16567545632521313,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.04349810046118659,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.07666314760930673,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.04273932953338838,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.012789775625054465,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.03338525971385087,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.004063596805700889,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.01809358786773029,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.16579697809612415,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.08386415749908942,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.002523020469592978,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.033052776649637745,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.06944510671827528,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.014107498468844713,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.06520681747115485,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.046844006672834046,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.04383091146897788,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.038423585062174456,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.015549467180866793,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.061795465445966466,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.030102812192976214,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.005665528861915364,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.0029572535414194717,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.01835967787259132,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.03959413022356849,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.010335141348630124,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.055184225923347964,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.03529259571309626,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.06740825732102555,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.010774892221376734,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.01659281242542601,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.02232287332172627,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.005795240297370794,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.04962627252981595,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 450.2255096435547,
         "x1": 842.0399780273438,
         "y1": 504.8515319824219,
         "rect": [
            421.0233154296875,
            450.2255096435547,
            842.0399780273438,
            504.8515319824219
         ],
         "text": "Health: Where safe drinking water is lacking, water-borne diseases such as cholera and acute watery diarrhoea can break out. Other health risks include an increase of malaria infections due to stagnant water, particularly in areas with poor drainage infrastructure (OCHA SitRep 2 30/08/2019).",
         "textOrder": 13,
         "textCrop": [
            431.0899963378906,
            451.7229919433594,
            813.7786865234375,
            503.3540344238281
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.3761347756551575,
                     "threshold": 0.489,
                     "is_selected": False
                  },
                  "2401": {
                     "prediction": 0.30167969731601874,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.12063359220822653,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.4174548334309033,
                     "threshold": 0.448,
                     "is_selected": False
                  },
                  "2203": {
                     "prediction": 0.056538897437777944,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.23173786302177093,
                     "threshold": 0.431,
                     "is_selected": False
                  },
                  "2207": {
                     "prediction": 0.1303769331641179,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.09848442124693017,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.6581007779299558,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 1.3356663487068308,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.34972458884731483,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.3488235874710797,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 1.1671246061699496,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.23682709968373275,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.17868977662099012,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.259792722693277,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.3930854133373715,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.10148335614540581,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.3586940988591669,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 1.625293830655656,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.25907793469661106,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.12570146613677502,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.1731035657800161,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.31111425202280213,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.1736396506171802,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.9947498099710824,
                     "threshold": 0.589,
                     "is_selected": True
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.184125739009413,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.018679424856771838,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.12448276529501671,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.01511540242724798,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.21395143031498084,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.18788932356983423,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.13267405723270617,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.19920942541517195,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.13745034949516688,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.10976871593041462,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.016645271875060638,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.2241824888972984,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.022816234647132592,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.001809149658028213,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.06545292967784591,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.15465432325821943,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.004050925998215346,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.24131710227594336,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00012428323320899887,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.13144008731574156,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.00569737225305289,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.2279338228282968,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.09094877472889969,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.0667291356528059,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.19258103436893886,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.00524247774765605,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.3052217957799527,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.6752132423340328,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.19272875172012868,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.10109899597147765,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.1122416501021504,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0005743507738152175,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.044119586972753616,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0005407284920472587,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.02124136605680663,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.0017672145605354965,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.025840678996029168,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.008874506950748174,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.02023331568936717,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.03914324337758891,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.06654276385333369,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0016922207844511767,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.013379985735767838,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.000273886977690078,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.05985797334338817,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.004908258244855169,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.0045621747568506624,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.17191222868859768,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.12402752384779946,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.15458435475971996,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.050746381846295686,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.08619850564558627,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.20654376247803943,
                     "threshold": 0.417,
                     "is_selected": False
                  },
                  "3205": {
                     "prediction": 0.313820160982263,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0005852089758442452,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.015354413323028096,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.003732775590049291,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.00928955088401663,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.0027763974841561435,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.012667202443905406,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.007613617926836015,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.045838270415651035,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.017273418619492206,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.01705669031940436,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.03065810322869515,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.04480593305328418,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.004979519871994853,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.07257761741147457,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.25864573281267367,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.033987712431774446,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.1568305152621898,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.08032494628360505,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.14076097186203976,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.00841204008018529,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.034671000860355516,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.03526037825005395,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.041637507161038034,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.06593972994167296,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.8123521243824678,
                     "threshold": 0.425,
                     "is_selected": True
                  },
                  "3701": {
                     "prediction": 0.031183198403054935,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.4074726709905936,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.19639077377908024,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.002294177154001279,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 1.3353907948986614,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.028096680686651887,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.2607547512983076,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.02350271656139068,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.13736921578571384,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.18510164179429106,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.040478083183584,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.4644444216222383,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.9984354269040804,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.07310586853440422,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.7229997364748189,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 1.1055164903566983,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.6854740000262702,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.8299755818635515,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.18310608462460579,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.2775381994890232,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.0395464769623301,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.19219654356027793,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.06245730511437252,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.018081169758663803,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.06699562917490935,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.0037648983729573395,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.03299067510449471,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.5932116715354671,
                     "threshold": 0.461,
                     "is_selected": True
                  },
                  "1202": {
                     "prediction": 0.5435077888280274,
                     "threshold": 0.494,
                     "is_selected": True
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.007736082706186507,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.053557200742880035,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.06431918177339765,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.020268927925868416,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.14816394241729586,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.03236557902960942,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.04869497033080669,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.05881170329359389,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.01463797728878906,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.018517022061945252,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.023964149918098115,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.006956267992363257,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.007580916491755542,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.011697001852588372,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.013824156745160378,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.011063579274280326,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.07386042355255759,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.05892559121816586,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.07599664203236611,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.13824835853669248,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.20342155246277135,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.43870970282865607,
                     "threshold": 0.046,
                     "is_selected": True
                  },
                  "1804": {
                     "prediction": 0.02957773795783125,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.6463380929390455,
                     "threshold": 0.593,
                     "is_selected": True
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 1,
         "x0": 421.0233154296875,
         "y0": 504.8515319824219,
         "x1": 842.0399780273438,
         "y1": 564.62353515625,
         "rect": [
            421.0233154296875,
            504.8515319824219,
            842.0399780273438,
            564.62353515625
         ],
         "text": "Poor hygienic conditions in camps in northeastern states has increased the outbreak of diseases since the beginning of the rainy season (OCHA 08/2019). In Borno state, there was an increase in malaria cases as of 30 August and two deaths due to acute watery diarrhoea were reported (OCHA SitRep 2 30/08/2019). No updated health statistics for",
         "textOrder": 14,
         "textCrop": [
            431.0899963378906,
            506.3490295410156,
            813.9285278320312,
            557.9540405273438
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.551074072870984,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.37860550358083395,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.6580274655587144,
                     "threshold": 0.576,
                     "is_selected": True
                  },
                  "2205": {
                     "prediction": 0.5486413969525269,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.13871795338828388,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.400422482368841,
                     "threshold": 0.431,
                     "is_selected": False
                  },
                  "2207": {
                     "prediction": 0.09565743614117611,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.33453021917426795,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.6488231512216421,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.5397105129540404,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.45965753543969107,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.5699169903158028,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.9931963943719313,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.10499395993306879,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.08499989981499219,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.14357651592394627,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.411238579243576,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.08782530842773989,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.2089573277367486,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 1.7856526924629132,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.17337398850812322,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.060582552217621675,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.1264488061842246,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.1881217724671353,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.5110761728780022,
                     "threshold": 0.464,
                     "is_selected": True
                  },
                  "2108": {
                     "prediction": 0.9196506898552939,
                     "threshold": 0.589,
                     "is_selected": True
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.0929721635362329,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.027357220632147114,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.09879157352397631,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.020116654394025154,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.11242319636298839,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.10575768101261929,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.08865284292321457,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.1603659303461919,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.16191944949270234,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.0669065913235819,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.06034665236631735,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.35660159220254367,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.026910328685142235,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.004612384770468471,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.09715302911914168,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.09448400684082693,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.004913101587048237,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.29039061415739575,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00028272138513937476,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.10364679863836881,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.0039144756738096476,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.1814898959598186,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.0535121516269796,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.04446812449617589,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.39815601375367904,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.003255421428808144,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.7189918996950075,
                     "threshold": 0.466,
                     "is_selected": True
                  },
                  "5601": {
                     "prediction": 0.6671386263357899,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.1589038729829194,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.20315910105483007,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.9545826941580321,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0003108676383563764,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.017026609891098395,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0003845452226068772,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.007500680936846479,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.0013725547688806842,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.03747598418586427,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.006498860786888498,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.011621979331050313,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.015260462967858362,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.048297374273475614,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0006233132586292014,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.010420404094664347,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0006230795103571534,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.394586102939895,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.022208101572200597,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.010379009623208951,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.26014636581142747,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.12246319758040565,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.1715790562349893,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.07818113355075612,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.18512309228969834,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.3643418959290575,
                     "threshold": 0.417,
                     "is_selected": False
                  },
                  "3205": {
                     "prediction": 0.3015360114835297,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0006062837647548391,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.04576671067561713,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.014300875733136584,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.06889282757865972,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.009958024590277796,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.01982045716941843,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.006657837490950312,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.0735086315028672,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.02822038600709955,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.022651487444830015,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.03611766800716303,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.04411730476569312,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.010192327879434615,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.06019517200664409,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.4104053642212912,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.05861055030513872,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.14083340231861388,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.022942686600607023,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.0771997682354759,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.012960792001750734,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.06957748145968826,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.05657552844948239,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.3585151711299649,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.2115711600321238,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.7088159112369313,
                     "threshold": 0.425,
                     "is_selected": True
                  },
                  "3701": {
                     "prediction": 0.012659335337060094,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.6331183700537195,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.24833035321883212,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0009761625673182547,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.47501755692947534,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.005010214963831104,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.2143914022643926,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.028122620709949423,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.136047350869809,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.16211707589557633,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.005758541258240955,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.1670855021326797,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.6491228835806421,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.04755716819996663,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 1.2746739796814488,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 1.0291808876543413,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.609404993118699,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.6263957729617369,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.19698391758626507,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.09971208797366012,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.011143554002046583,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.07204932677173198,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.026803637333845685,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.0361838629927303,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.05520725213075711,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.0067900149868084835,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.034540097011410774,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.5885228805583366,
                     "threshold": 0.461,
                     "is_selected": True
                  },
                  "1202": {
                     "prediction": 0.7879510220245793,
                     "threshold": 0.494,
                     "is_selected": True
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.0075187592105532336,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.024070612999336362,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.047680727309650846,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.02409445153454603,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.07830847165372112,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.01677068075048029,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.08731308308514682,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.02310024094335812,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.017785357244043468,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.01681396360499376,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.01947731837044637,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.006387569010257721,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.002086412944439529,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.012773491494123945,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.010526073459521989,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.0039502673658096035,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.09504999058234259,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.04375599603916296,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.2638579921775989,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.4416313854236047,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.33147940996388225,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 1.0536347070465917,
                     "threshold": 0.046,
                     "is_selected": True
                  },
                  "1804": {
                     "prediction": 0.031245733605117988,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.26853968079938456,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "table",
         "page": 1,
         "x0": 125.54000091552734,
         "y0": 423.42999267578125,
         "x1": 313.5999755859375,
         "y1": 518.3759765625,
         "rect": [
            125.54000091552734,
            423.42999267578125,
            313.5999755859375,
            518.3759765625
         ],
         "tableImageLink": "table-4d6d56e9-b677-43fd-8289-5257a20e829f.png",
         "tableCaption": "undefined",
         "tableMeta": "undefined",
         "tableText": "6.69 per 1000 people\nDELTA\n8.01 per 1000 people\nKEBBI\n3.63 per 1000 people\nKOGI\n1.47 per 1000 people"
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 421.01690673828125,
         "y1": 84.65552520751953,
         "rect": [
            0.0,
            0.0,
            421.01690673828125,
            84.65552520751953
         ],
         "text": "Borno flood-affected populations were available. The State Ministry of Health and WHO have set up mobile clinics in northeast Nigeria and use their staff trained for polio eradication to help prevent the outbreak of water-borne diseases (WHO 09/2019).",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            44.133026123046875,
            410.7202453613281,
            83.15803527832031
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 84.65552520751953,
         "x1": 421.01690673828125,
         "y1": 151.85552215576172,
         "rect": [
            0.0,
            84.65552520751953,
            421.01690673828125,
            151.85552215576172
         ],
         "text": "Education: Schools have been flooded across the country making it difficult for children to attend school. Reports about inaccessible education facilities come for instance from Delta state (Guardian Nigeria 23/09/2019). The extent of damage remains unclear making it difficult to assess how many schools need to be repaired and how long they will remain inaccessible.",
         "textOrder": 1,
         "textCrop": [
            28.079999923706055,
            86.15301513671875,
            410.913818359375,
            150.35804748535156
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.5179053679078147,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.3606532892280959,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.0765287032764819,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.5944547509508473,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.09757109228673021,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.3016396423503584,
                     "threshold": 0.431,
                     "is_selected": False
                  },
                  "2207": {
                     "prediction": 0.17652371502751088,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 1.0334609501194536,
                     "threshold": 0.456,
                     "is_selected": True
                  },
                  "2202": {
                     "prediction": 0.5385290462892134,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.7910737198547513,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.5303002716913079,
                     "threshold": 0.463,
                     "is_selected": True
                  },
                  "2305": {
                     "prediction": 0.9245204034252702,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 1.4022296901112616,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.3164108062150926,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.17186536630143814,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.08676039789794782,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.5092561013340332,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 1.539963185234282,
                     "threshold": 0.539,
                     "is_selected": True
                  },
                  "2105": {
                     "prediction": 0.11389777677539936,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.3503101801722305,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.15205395432700097,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.09131901550820656,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.05514220071908755,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.29083605625536674,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.11963467113673687,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.1438485366784049,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.4664129794460453,
                     "threshold": 0.438,
                     "is_selected": True
                  },
                  "5306": {
                     "prediction": 0.05650003264956879,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.16506923417167185,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.026125460863113403,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.6410093699100513,
                     "threshold": 0.414,
                     "is_selected": True
                  },
                  "5309": {
                     "prediction": 0.5347824771888554,
                     "threshold": 0.512,
                     "is_selected": True
                  },
                  "5308": {
                     "prediction": 0.7393360137939453,
                     "threshold": 0.475,
                     "is_selected": True
                  },
                  "5301": {
                     "prediction": 0.556256011372707,
                     "threshold": 0.488,
                     "is_selected": True
                  },
                  "5305": {
                     "prediction": 0.26161839642862633,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.08451856404274434,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.0503532581595969,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.33209459765892196,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.024007058890629315,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.005382611513477123,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.08194123538548514,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.10398640100302833,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.009069005225567108,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.2577244864459849,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.000397409768609221,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.15045921510078486,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.0027853439678438008,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.9072847494674272,
                     "threshold": 0.483,
                     "is_selected": True
                  },
                  "5401": {
                     "prediction": 0.1799215548438444,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.19196484317170814,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.25044780638482833,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.011959485709667206,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.37003832953170646,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.4651425849823725,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.12490907456816697,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.3579383305573868,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.0170777193942473,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0071689781373757925,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.02895434561737179,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.002674191478925505,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.04928449532904802,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.001944460605871594,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.04087398984672314,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.007679320238623074,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.027653229586291767,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.06952423268180354,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.05424277134280387,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0018956471893300372,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.03474010854442684,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0027316643051259843,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.06143611489455282,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.008746832149264253,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.015249861211612308,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.37168171256780624,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.09973735977259893,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.11791654095090107,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.10419434265178792,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.08993125441720931,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.42929645064923405,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.2793635196661524,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0012037265714417936,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.0368575231766538,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.00993335521310021,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.017416083799867796,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.004063651733991386,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.005472686937835439,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.012745717540383339,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.0749356770884368,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.033753598285945194,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.025372586187961173,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.057337258982917534,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.03701388612549106,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.03279976775510269,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.086240629548008,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.4421114993730411,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.06520745876105691,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.27561371961792747,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.06729261034485921,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.08860277901789186,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.009987624017176804,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.0648741575854796,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.16172178207881865,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 1.3332200263703962,
                     "threshold": 0.447,
                     "is_selected": True
                  },
                  "3604": {
                     "prediction": 0.5438267940380535,
                     "threshold": 0.488,
                     "is_selected": True
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.3713937717325547,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.014917323411409014,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.32258927061849707,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.1235214004546036,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0006765073121820533,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.7606590811110221,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.005848798371682113,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.21809535162193247,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.03258521063797462,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.1431765903409877,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.2410870520666303,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.020972375447551407,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.2637591127079738,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 1.030031344437763,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.07359181195778138,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.31627046320059776,
                     "threshold": 0.466,
                     "is_selected": False
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.9832222488045034,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.8079326644386212,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.9353820560047927,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.18978224045807315,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.4469940402344162,
                     "threshold": 0.408,
                     "is_selected": True
                  },
                  "4502": {
                     "prediction": 0.030541577720427295,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.19492859663401108,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.04778633318602926,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.3305434814242066,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.5202320427581025,
                     "threshold": 0.441,
                     "is_selected": True
                  },
                  "1103": {
                     "prediction": 0.04721325822174549,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.4626705278804646,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.17593867284874076,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.125144589466122,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.003975952476865114,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.025648523241542168,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.06183738509813944,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.028436780246493317,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.15683669855098914,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.01585682094641196,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.026758562660578526,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.10727950439010699,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.03245915903384427,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.07496506660118979,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.0383144236417837,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.011524033239659141,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.013591305933136871,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.023163155772648623,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.02389620179414306,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.014347734471836028,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.07232796844731958,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.059313690051054344,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.06506029893173261,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.03723334701894556,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.05193055363378841,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.03265436870329406,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.007818998084311059,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.0648316605296143,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 151.85552215576172,
         "x1": 421.01690673828125,
         "y1": 206.48552703857422,
         "rect": [
            0.0,
            151.85552215576172,
            421.01690673828125,
            206.48552703857422
         ],
         "text": "Protection: Concerns regarding the opportunity for armed groups to infiltrate displacement camps have been raised. A suicide bomb attack carried out by a woman on 20 August targeted a displacement camp in Dikwa, Borno state. This kind of attack has not happened in the area since December 2018 (NRC 23/08/2019).",
         "textOrder": 2,
         "textCrop": [
            28.079999923706055,
            153.35299682617188,
            410.883056640625,
            204.98805236816406
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 1.0315803906181351,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.40022838141550987,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.5166919695006477,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 1.1628878169826098,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.10965407136979143,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.873002748754904,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.5684736612680796,
                     "threshold": 0.518,
                     "is_selected": True
                  },
                  "2204": {
                     "prediction": 0.1479392021633031,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.4088357909695133,
                     "threshold": 0.455,
                     "is_selected": False
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.8061238197942235,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.3378872093835093,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.1035840366488305,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 1.046789160501599,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.22004565654511585,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.20408464026048526,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.09608989188430506,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.7009820462508523,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.08941389938232407,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.13598468568589953,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.23268121031095398,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.16902438241296108,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.06448835794114971,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.026673242712441165,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 1.4256465353191035,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 0.441568518250153,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.08687801368167729,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.4566232567508471,
                     "threshold": 0.438,
                     "is_selected": True
                  },
                  "5306": {
                     "prediction": 0.315125399040726,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 1.079711704573372,
                     "threshold": 0.478,
                     "is_selected": True
                  },
                  "5302": {
                     "prediction": 0.3374348987232555,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.2009729508328553,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.32460730290040374,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.3021981527930812,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.48281960800045826,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.0927893180898794,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.7118822352306263,
                     "threshold": 0.444,
                     "is_selected": True
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.08191104269071779,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 1.011468502918529,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.038947472519918376,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.013086019681176378,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.07190167803892353,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.15424087411311263,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.002506415686629554,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.3081385463599842,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00011756978302532878,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.19916342327210787,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.004935016622766852,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.33961791799675606,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.8138615581204948,
                     "threshold": 0.459,
                     "is_selected": True
                  },
                  "5402": {
                     "prediction": 0.27557938022816436,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.38774245315127903,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.0177625087755067,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.5569316670618344,
                     "threshold": 0.466,
                     "is_selected": True
                  },
                  "5601": {
                     "prediction": 0.4333097625661779,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.13525610370687677,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.0722832441077394,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.9781444695458483,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0044199379692350434,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.012275315766144362,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0080330405203576,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.0628108739467738,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.04046646777741209,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.07577592057701575,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.03041588833033299,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.06090539328391658,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.06082440506778286,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.15600187150941303,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.01623465838592227,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.03808934909070847,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0015400567766240179,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.26302306219864796,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.0744125587336811,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.0999207576287204,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.15615328835944337,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.10601730485047613,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.0441642683044914,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.15804356261461724,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.18200620819451446,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 1.2896965733535,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.3716568379608426,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.004453096035982202,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.03013519233302452,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.003675387108510514,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.015260102548475924,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.005347960091081402,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.006603740222545471,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.0032304426921265466,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.045717558760476985,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.020340949070317662,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.03367180090320847,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.12971302899329556,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.12172881426086261,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.03100264400831963,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.5777573122561557,
                     "threshold": 0.515,
                     "is_selected": True
                  },
                  "3403": {
                     "prediction": 0.7323447353326091,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.049662825308348,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.29890214676385396,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.27615793752762163,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.35747290923084174,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.011056834935314125,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.01855070737225038,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.02959022919336955,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.060442401725440485,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.05747696201576561,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.2615753342123593,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.005576538146524331,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.3494529851845332,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.11693884929021199,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0004307552113790404,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.7788332011462388,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.0034191675163660344,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.19208842346391738,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.061675135002709394,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.05271135738811588,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.2585625574912554,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.06347554533377937,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.3481789080101989,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.6170199173811645,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.08097079121235849,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.8947202064448672,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 1.06758587268176,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 1.057489247051711,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.4880110760336941,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.23886295516164072,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.2516125164487783,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.09714438168852178,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.24129380370331643,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.09957847594092345,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.02818301579624903,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.04952575783340298,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.006276175218562667,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.035351672816780665,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.15668902311821561,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.12799219684562219,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.02609028383738264,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.022990126760117163,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.09487734900580512,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.02161723947193086,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.08902863258182413,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.005080811414890309,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.012475757323431246,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.12818134015368432,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.13322483703314542,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.11099306458222344,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.40782971803798423,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.18420883837868185,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.013998316843872486,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.10042630447535565,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.2755368730835755,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.06353482196445799,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.714956324335207,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "1711": {
                     "prediction": 0.46809520241776864,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.08237286565009128,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.044197187695688415,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.03340648576562255,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.013051773472081708,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.008689560341519235,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.05072909980560033,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 206.48552703857422,
         "x1": 421.01690673828125,
         "y1": 277.593017578125,
         "rect": [
            0.0,
            206.48552703857422,
            421.01690673828125,
            277.593017578125
         ],
         "text": "Overcrowded camps also lead to increased levels of vulnerabilities for women and children, especially increasing risks of gender-based violence and abduction (OCHA SitRep 2 30/08/2019, OCHA 2016). Older people and people with disabilities also face greater risks of abuse in camps (OCHA 2019).",
         "textOrder": 3,
         "textCrop": [
            28.079999923706055,
            207.98300170898438,
            410.9438171386719,
            259.5880432128906
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.9431652496197472,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.4535551443534404,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.07695751264691353,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.5764504229383809,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.11633987712666272,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.5035670409346401,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.10591661953097604,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.08049192266506061,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.5070571716015155,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 1.6505731347137675,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.2590402413650414,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.0279650303804986,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.8930852314065841,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.20824768630783705,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.09140280017709643,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.051878847250150975,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.7636241344590261,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.19242924142193482,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.17196494978641777,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.6276455940190602,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.3847973338798084,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.060596317802396577,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.11437019715324426,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 1.5346731146631307,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 0.39595493982578145,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.1687315025434834,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.5771348329439555,
                     "threshold": 0.438,
                     "is_selected": True
                  },
                  "5306": {
                     "prediction": 0.6594139168847282,
                     "threshold": 0.424,
                     "is_selected": True
                  },
                  "5310": {
                     "prediction": 1.1931469500314242,
                     "threshold": 0.478,
                     "is_selected": True
                  },
                  "5302": {
                     "prediction": 0.6321225653995167,
                     "threshold": 0.44,
                     "is_selected": True
                  },
                  "5307": {
                     "prediction": 0.6081300657152554,
                     "threshold": 0.414,
                     "is_selected": True
                  },
                  "5309": {
                     "prediction": 0.5878933006897569,
                     "threshold": 0.512,
                     "is_selected": True
                  },
                  "5308": {
                     "prediction": 0.9852609508915952,
                     "threshold": 0.475,
                     "is_selected": True
                  },
                  "5301": {
                     "prediction": 0.9107120701524078,
                     "threshold": 0.488,
                     "is_selected": True
                  },
                  "5305": {
                     "prediction": 0.31107579042592387,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 1.3555552776869353,
                     "threshold": 0.444,
                     "is_selected": True
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.06469155277870939,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.624891616699454,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.03586353103476247,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.0077062913798064386,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.1492970508483699,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.14434925763803494,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.003370059099286161,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.4522417096181529,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.000398362271070632,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.15269415208909395,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.007531464798375964,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 1.1862246146113236,
                     "threshold": 0.483,
                     "is_selected": True
                  },
                  "5401": {
                     "prediction": 1.0119948641666918,
                     "threshold": 0.459,
                     "is_selected": True
                  },
                  "5402": {
                     "prediction": 0.43043817611450846,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.37475725015004474,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.014348503734384264,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.2726052004380287,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.43071179635941037,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.1146880894657073,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.12455950096502143,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.9300344767262093,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.009018383324613391,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.03492393623074541,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.00781516423550943,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.10354369156580172,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.04267924931829799,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.038058267997913675,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.07584673484265064,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.07890085305774439,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.588586708635983,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.06584413960331775,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.01949552991768209,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.07147748231428437,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0018337070489198798,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.03694595274696418,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.017844905133968518,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.005544115114828637,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.28599342331290245,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.10552841963039504,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.02525728605778701,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.06319682638184364,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.05004362803015669,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.31130162360285113,
                     "threshold": 0.417,
                     "is_selected": False
                  },
                  "3205": {
                     "prediction": 0.3236482540766398,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.000234336097313354,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.03380845571032157,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.0027716362746346983,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.010197790307474548,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.002965269137361124,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.0033530066333723302,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.00811262521892786,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.06500462239438837,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.006229741969800947,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.013633186909740587,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.029387502539632973,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.10468199753403919,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.005705894804314563,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.03660733911018927,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.4669082583295808,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.015438826535998085,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.04391813302760596,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.04677622003017822,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.03236128242721983,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.0016008028372501333,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.015005703877519677,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.011616253427096776,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.03804955673164436,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.037112834359534455,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.4099086452932919,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.01299214898389387,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.18470221180088664,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.08989992884942043,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.003069358035757296,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 1.5599299663616017,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.0047733929377145965,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.13823197498363268,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.025273008405764234,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.04363969953131497,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.08169437448183696,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.037092286958426667,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.2526901896644688,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.5209218514593024,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.10223295925476232,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.5949481106623048,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.7891298492969071,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.8260103077003637,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.2732838241799364,
                     "threshold": 0.412,
                     "is_selected": False
                  },
                  "4403": {
                     "prediction": 0.2021824099844502,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.25111979202312584,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.010407854475685067,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.07433840378663426,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.04558307653654317,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.08298616978477259,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.16573688137828627,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.01610514994424123,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.17834675326869262,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.23843975103341059,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.2493042694894891,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.015898703312131293,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.0423896520156902,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.18324469526608786,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.033137239696182874,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.07867065839248129,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.019535526225218668,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.07031632192207106,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.49058496952056885,
                     "threshold": 0.485,
                     "is_selected": True
                  },
                  "1702": {
                     "prediction": 0.09212870913815786,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.07691546994609474,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.05436570314470857,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.03358771695810206,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.04167496294215106,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.0395975124337532,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.06686878774910611,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.02071721768679191,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.44472963389955034,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "1711": {
                     "prediction": 0.8473140013053337,
                     "threshold": 0.507,
                     "is_selected": True
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.13458146975281532,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.053102982420365784,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.06534990156928551,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.02500845078864823,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.006775151235082291,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.06211040821083481,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 277.593017578125,
         "x1": 421.01690673828125,
         "y1": 314.8740234375,
         "rect": [
            0.0,
            277.593017578125,
            421.01690673828125,
            314.8740234375
         ],
         "text": "Impact on critical infrastructure",
         "textOrder": 4,
         "textCrop": [
            28.079999923706055,
            295.5979919433594,
            204.95309448242188,
            313.405029296875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 314.8740234375,
         "x1": 421.01690673828125,
         "y1": 356.8655242919922,
         "rect": [
            0.0,
            314.8740234375,
            421.01690673828125,
            356.8655242919922
         ],
         "text": "There are no reports on the overall extent to which the flooding has affected infrastructure and public facilities across the country. Still, roads across Nigeria lack effective drainage, making them prone to get submerged (African Arguments 2018).",
         "textOrder": 5,
         "textCrop": [
            28.079999923706055,
            316.343017578125,
            410.72430419921875,
            355.3680419921875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 356.8655242919922,
         "x1": 421.01690673828125,
         "y1": 406.91302490234375,
         "rect": [
            0.0,
            356.8655242919922,
            421.01690673828125,
            406.91302490234375
         ],
         "text": "Many flood-affected states and regions have reported infrastructure damages including roads submerged in water such as in Lagos, indicating severe temporary infrastructure impediments across the country (PM News 12/10/2019).",
         "textOrder": 6,
         "textCrop": [
            28.079999923706055,
            358.3630065917969,
            410.76177978515625,
            397.248046875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 406.91302490234375,
         "x1": 421.01690673828125,
         "y1": 435.8540344238281,
         "rect": [
            0.0,
            406.91302490234375,
            421.01690673828125,
            435.8540344238281
         ],
         "text": "Vulnerable groups affected",
         "textOrder": 7,
         "textCrop": [
            28.079999923706055,
            416.5780029296875,
            183.3896026611328,
            434.3850402832031
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 0.0,
         "y0": 435.8540344238281,
         "x1": 421.01690673828125,
         "y1": 595.3200073242188,
         "rect": [
            0.0,
            435.8540344238281,
            421.01690673828125,
            595.3200073242188
         ],
         "text": "IDPs: Nigeria has a large population of IDPs, mostly displaced due to the Boko Haram conflict in the northeastern states. At the end of 2018, around 2.2 million people in Nigeria were displaced of which over 90% live in the northeast (IDMC Special Report 2019). About 140,000 additional displacement cases were recorded between January and June 2019 across the country (IDMC). Displaced people in emergency and makeshift shelters face increased needs across all sectors due to the flooding including shelter, food, health and protection needs (OCHA 08/2019).",
         "textOrder": 8,
         "textCrop": [
            28.079999923706055,
            437.3230285644531,
            410.8822326660156,
            526.9940185546875
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 1.5194687862825296,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.36988913237143495,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.197213479421205,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.6116414442658424,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.04820265557344367,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 1.847731265003886,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.14128121745172154,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.05169153997772618,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.5475704814051534,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.5508827769668878,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.34370828524521563,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.196064820913511,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.8179639696248959,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.18993201896902293,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.6215985004718487,
                     "threshold": 0.533,
                     "is_selected": True
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.06637703114693318,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 1.234755537670511,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.13185555118797881,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 1.310425898665754,
                     "threshold": 0.486,
                     "is_selected": True
                  },
                  "2110": {
                     "prediction": 1.2536977322096596,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.17644568816222975,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.09296927413710167,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.0870161128636354,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.5944983637305638,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 1.1005567322517262,
                     "threshold": 0.464,
                     "is_selected": True
                  },
                  "2108": {
                     "prediction": 0.36712304541939184,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.1288940151940742,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.035144926821988706,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.17974382289782728,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.03178283487531272,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.16497685641482257,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.11534190707607195,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.31197340864884227,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.14119549486480776,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.11801409469110759,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.15554301910572224,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.05366854273237274,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 1.5071870734513069,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.012469117400136207,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.004017285108424907,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.0465383765681478,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.2092231554549627,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.004098918338484587,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.4343908913897281,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00023954688943448563,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.217532076304325,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.0038733379915356636,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.30967096487681073,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.11250931031044271,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.08914305016081385,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.3201235665215386,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.040874832442828586,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.46506552865065215,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.4484427984429415,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.07143739843110082,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.08943305208773937,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.0515707938825312,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.00041160753674127835,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.013308054829453787,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0010063822187355053,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.01827552342886686,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.00717758085809187,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.04210963025165665,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.008532637614692114,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.03326789379497915,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.057644015827844314,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.061743361756666976,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0007537318529879175,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.02559777779903026,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0005073780408161434,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.0955637509082731,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.03195323678569048,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.012849199039668873,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.37036991367737454,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.14776604930086742,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.10365071936458131,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.05978969230997463,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.07165855554453397,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.5304231632241814,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.13659711519573783,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.001448766271972263,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.025851354829382167,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.00340482081209711,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.017189949044379697,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.006424065798753469,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.0052765379454727855,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.0017457159369119576,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.024074558853180772,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.017628781922416542,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.011408438082495129,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.03363886524153792,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.08007672633297692,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.05723946123269566,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.96727638568693,
                     "threshold": 0.515,
                     "is_selected": True
                  },
                  "3403": {
                     "prediction": 1.782586153136616,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.04567694567475725,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.1904350797553639,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.0209281102598058,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.0893525984889636,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.004278443736472615,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.020499282551032526,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.026351139540710146,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.023324563432593207,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.04003689715974644,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.3384122778387631,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.01179715074781195,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.6210386981161273,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.2022461942684503,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0032425428459224013,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.6497891452075181,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.018577912350656926,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.26028463107490957,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.02723334602800156,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.08044605540515776,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.26131875107808367,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.011802588562494602,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.37675414945094593,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.7300942249647268,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.5240234390265973,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.531267838416693,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.7175319102587621,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.43370904996223053,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.44135094701665123,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.3961003836124174,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.25153539928735474,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.02983974309654923,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.6397411422437975,
                     "threshold": 0.458,
                     "is_selected": True
                  },
                  "4502": {
                     "prediction": 0.283202517728572,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.0523995898175435,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.052910745819680007,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.0074407332039509826,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.028799843988311823,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.383527864603055,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.16869061630264467,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.004059844807116472,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.010395309217165579,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.042945970263746046,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.008648024650953583,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.09695416924977067,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.005298240287852819,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.018169236077804757,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.0548375251981401,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.019919077854558646,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.0474823129388634,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.06643787644575777,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.023231981870006115,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.005938713371321775,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.016908938525964992,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.04561499218182936,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.015804469707693,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.13643570746164865,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.04406280345347741,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.29100152883636815,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.09407247009786587,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.07335275988957099,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.026811592523818432,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.015966726824739912,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.124689034527108,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 0.0,
         "x1": 842.0399780273438,
         "y1": 38.868499755859375,
         "rect": [
            421.01690673828125,
            0.0,
            842.0399780273438,
            38.868499755859375
         ],
         "text": "ACAPS Briefing Note: Floods in Nigeria",
         "textOrder": 9,
         "textCrop": [
            674.02001953125,
            22.557010650634766,
            814.0595703125,
            33.603973388671875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 38.868499755859375,
         "x1": 842.0399780273438,
         "y1": 84.65552520751953,
         "rect": [
            421.01690673828125,
            38.868499755859375,
            842.0399780273438,
            84.65552520751953
         ],
         "text": "Children: Children are especially vulnerable to the increased health risks due to the rainy season (MSF 12/08/2019). The deteriorating health situation can also worsen malnutrition (OCHA 08/2019).",
         "textOrder": 10,
         "textCrop": [
            431.0899963378906,
            44.133026123046875,
            813.8062744140625,
            83.15803527832031
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.37542893598903665,
                     "threshold": 0.489,
                     "is_selected": False
                  },
                  "2401": {
                     "prediction": 0.29976245767382376,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.21724868565797809,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.5659352588866438,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.07637698445620576,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.323988652837802,
                     "threshold": 0.431,
                     "is_selected": False
                  },
                  "2207": {
                     "prediction": 0.10883824676850587,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.10454846676765826,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.7620217380942879,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 1.4620596738782665,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.20486838938608024,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.0331249404176372,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 1.0280298718679308,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.21102876436633114,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.10449059069939447,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.08985057063058975,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.38211885357150144,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "2107": {
                     "prediction": 0.16091429457372547,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.41027241405636194,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 1.028348127501066,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.20039735971826367,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.060257177717489015,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 1.281680969091562,
                     "threshold": 0.624,
                     "is_selected": True
                  },
                  "2111": {
                     "prediction": 0.4280275010953506,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.07076104621178117,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.21740665156489117,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.578972710866362,
                     "threshold": 0.438,
                     "is_selected": True
                  },
                  "5306": {
                     "prediction": 0.09969117576783558,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.38351124799401193,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.07224219258535992,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.9380347198910184,
                     "threshold": 0.414,
                     "is_selected": True
                  },
                  "5309": {
                     "prediction": 0.7970606093294919,
                     "threshold": 0.512,
                     "is_selected": True
                  },
                  "5308": {
                     "prediction": 1.0007775457281816,
                     "threshold": 0.475,
                     "is_selected": True
                  },
                  "5301": {
                     "prediction": 1.1963913919495754,
                     "threshold": 0.488,
                     "is_selected": True
                  },
                  "5305": {
                     "prediction": 0.9927170013818215,
                     "threshold": 0.508,
                     "is_selected": True
                  },
                  "5304": {
                     "prediction": 0.2576422013409503,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.040327827144903086,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.2988632029898891,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.03039267823452086,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.00502975512670611,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.11796740944220183,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.12609103740190875,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.0067997109541233555,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.20812219974905624,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.000711019019390108,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.10015582491396072,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.011200697626918554,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 1.446932245732341,
                     "threshold": 0.483,
                     "is_selected": True
                  },
                  "5401": {
                     "prediction": 0.4357556956525981,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.28000889306372784,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.19655836953057182,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.03895458720979236,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.4119784791070504,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.3868297294334129,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.11665607249833704,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.15880461087671377,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.9719137825183014,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.007679753828805442,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.04552517421928783,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.004181640181859521,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.02853409575241255,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.01421865510815632,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.054791665677443604,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.010070611697346637,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.06799155700534393,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.034671700698790754,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.19047964357504643,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0027042688665593543,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.07554987061460124,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0013978887080965151,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.05977373058197058,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.007475978300098039,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.004352980036416958,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.3367653427024683,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.11835539240449194,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.2208695835764076,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.06277797774983054,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.06867942037218708,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.22774346941094892,
                     "threshold": 0.417,
                     "is_selected": False
                  },
                  "3205": {
                     "prediction": 0.23950266701574544,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0003149552700006934,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.020665421751375493,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.004263753616122887,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.012374983233367576,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.0022950425237236445,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.004614943024652234,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.0263483715908868,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.028333320449929634,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.011655597632375506,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.006614254400866156,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.030125312480157696,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.030692586998357505,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.006947743506252504,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.03694798978208338,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.34333650049805353,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.031086572856917554,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.11235776428992932,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.02058940492785735,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.056682162445568486,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.04057265059263618,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.0250762776920089,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.023773685097694397,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.06858399867078069,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.08676716386050475,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.8872647145215203,
                     "threshold": 0.425,
                     "is_selected": True
                  },
                  "3701": {
                     "prediction": 0.015776130860134706,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.350907140848588,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.1841955162860729,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.002745145654960259,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 1.3895427446229764,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.011122994905023218,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.10937346345225361,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.025993730804458486,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.058751019122000044,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.05518191267924054,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.019077726207889507,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.16547099099469137,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.5688995327502148,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.06609292886800461,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.6696306201009791,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.8060496650348052,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.6470858436269858,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.43782157805359484,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.18851340357815066,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.28473626383963757,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.00788964549297685,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.07807617136744953,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.03538347023018336,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.06092246240157573,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.0824235514853817,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.009684700769587204,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.06925429574292691,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.2387505259017365,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.2426068309830268,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.008055897937579588,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.02818035217050908,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.06645753979682922,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.018671010654717324,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.06948195324085726,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.21816412285423667,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.4745797978507148,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.14405951057512736,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.03996460911739304,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.05144493689367816,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.022488032105708225,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.008530711536021795,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.009075866040328276,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.013632755012670045,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.024084775573591316,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.021437961502200405,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.08341272414657118,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.08269428060604976,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.02849527080072446,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.04264800944953289,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.059103730694834156,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.01368294318166116,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.004335442659697983,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.04785305947618179,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 84.65552520751953,
         "x1": 842.0399780273438,
         "y1": 147.42302703857422,
         "rect": [
            421.01690673828125,
            84.65552520751953,
            842.0399780273438,
            147.42302703857422
         ],
         "text": "Gaps: While the humanitarian needs of vulnerable populations in northeastern camps are being assessed (OCHA 08/2019), there is a general lack of disaggregated information on flood-affected populations in Delta, Kebbi, and Kogi states. This makes it difficult to assess particular vulnerabilities there.",
         "textOrder": 11,
         "textCrop": [
            431.0899963378906,
            86.15301513671875,
            814.0199584960938,
            137.75804138183594
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 147.42302703857422,
         "x1": 842.0399780273438,
         "y1": 176.3640365600586,
         "rect": [
            421.01690673828125,
            147.42302703857422,
            842.0399780273438,
            176.3640365600586
         ],
         "text": "Humanitarian and operational constraints",
         "textOrder": 12,
         "textCrop": [
            431.0899963378906,
            157.0880126953125,
            668.072998046875,
            174.8950653076172
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 176.3640365600586,
         "x1": 842.0399780273438,
         "y1": 243.5655288696289,
         "rect": [
            421.01690673828125,
            176.3640365600586,
            842.0399780273438,
            243.5655288696289
         ],
         "text": "Humanitarian access to Borno state is severely limited. Due to the volatile security situation, movement restrictions and poor road infrastructure, people living in areas outside of military control can hardly be reached (MSF 13/08/2019). Over 800,000 people in Borno state cannot be accessed by humanitarian organisations (OCHA HNO",
         "textOrder": 13,
         "textCrop": [
            431.0899963378906,
            177.8330078125,
            813.9634399414062,
            242.0680389404297
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.6009340895709329,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.42073784189989666,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.092326152500593,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.6574487446674279,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.13368078545341647,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.5683648613931961,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 1.6003767726043936,
                     "threshold": 0.518,
                     "is_selected": True
                  },
                  "2204": {
                     "prediction": 0.1364027705501046,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.280507776763413,
                     "threshold": 0.455,
                     "is_selected": False
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.5746302730005354,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.41897739756442043,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.017118238400076,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.7535761553475818,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.13361489058313308,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.0879249446387586,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.03165887378224539,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 1.1813184294675916,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.17696317693076902,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.1704852276868781,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.30200870656867196,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.11591209444852002,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.38583102960221966,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.068086521843305,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.522174912950267,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 0.13103845914633108,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.1405340023275547,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.06928263852993648,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.01497623479907524,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.10614113484715818,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.010177980981428515,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.0723653837390568,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.0565611117053777,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.2075182607299403,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.0727652480489895,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.05569487927466866,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.09268502125868926,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.06973948639554148,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.5222045640063181,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.049926296580494856,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.011088839949478008,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.09962778863490827,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.1509846385178428,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.010866430053051483,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.2900897776437498,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00013432066667524022,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.1555267260985428,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.004969280562363565,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.20387037570432107,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.06075677399022387,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.06855546318470164,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.2962133288383484,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.013272081102643694,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.3240457036464511,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.5406974248154454,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.13624943368803194,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.168590774854361,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.1339693965010382,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0014931376261467283,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.01582174673346332,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0024586777510310935,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.01377531858416867,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.001204447326308001,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.0650361005818816,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.0069500588426001314,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.06031308787821715,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.0615178288712454,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.032216978881962746,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0019650755836287653,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.017590661082768487,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.00168246747812696,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.058706028837163304,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.018465503237742948,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.018473364541242866,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.33473571141560876,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.13317509243885675,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.06520090064530268,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.11622965993250119,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.19275016640707598,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.5763583331942844,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.11811014880964167,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.0015104293431858161,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.037472250111680795,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.01827181624504951,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.016863335823190623,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.010272125637665573,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.02028701939357241,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.004695225839636156,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.11730778465187987,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.028324589671517506,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.021133312096497527,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.04073342753817206,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.10437769635841729,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.019640741428654445,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.13757769054579502,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.6677603606161714,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 1.0989832009381129,
                     "threshold": 0.494,
                     "is_selected": True
                  },
                  "3502": {
                     "prediction": 1.355862142620506,
                     "threshold": 0.364,
                     "is_selected": True
                  },
                  "3504": {
                     "prediction": 0.4424505897569748,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.6662778667077391,
                     "threshold": 0.471,
                     "is_selected": True
                  },
                  "3503": {
                     "prediction": 0.019679315112255236,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.05242398215664757,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.23832110658524527,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.0814104690247734,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.17362516984099247,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.38204701507792754,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.021983427390203637,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.21236889748548973,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.13061877753999498,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.00025874794433945996,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.6664551406110067,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.00671072569736219,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.1924211399821275,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.12306201089801694,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.11883143735050856,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.3427898994198552,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.014263692824844864,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.125989224175987,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.9736904972477963,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.2826102035867292,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.29206077684148696,
                     "threshold": 0.466,
                     "is_selected": False
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.6889579045838414,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.34981781674414564,
                     "threshold": 0.388,
                     "is_selected": False
                  },
                  "4401": {
                     "prediction": 0.591401336262527,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.4554555841511296,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.11001872446607142,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.04547385683467796,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.08272472362330907,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.05212605785290849,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.061466381503421756,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.08714385753045548,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.0075512404481952,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.04144577745033141,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.16733821392576503,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.06623632512111896,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.001653720803483568,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.00956298446733472,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.03693425820933448,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.008360035694937153,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.40265495824341724,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.011311894996775575,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.011319941794029391,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.04876168425550166,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.06562616361911039,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.12104653428641142,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.16106009548407973,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.005793607629397336,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.0075593077834101696,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.036631340894341884,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.09782396977054142,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.045011582207627576,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.1533664955994008,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.0459893149208035,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.05337580033902372,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.019508772032353485,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.030179501157185245,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.0104562843815707,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.009177413781401732,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.06804690016260839,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 243.5655288696289,
         "x1": 842.0399780273438,
         "y1": 310.88551330566406,
         "rect": [
            421.01690673828125,
            243.5655288696289,
            842.0399780273438,
            310.88551330566406
         ],
         "text": "Kogi state has experienced violence in context of the Middle Belt in the past and so has Delta state to a smaller extent (Idakwoji et al. 2018). As the flooding and ensuing damage to crops and livestock can increase the land conflicts underlying the tensions and a recent government livestock plan has been rejected (SaharaReporters 27/09/2019), the security situation in Kogi should still be monitored.",
         "textOrder": 14,
         "textCrop": [
            431.0899963378906,
            245.06301879882812,
            813.8353271484375,
            309.3880310058594
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 310.88551330566406,
         "x1": 842.0399780273438,
         "y1": 345.4340362548828,
         "rect": [
            421.01690673828125,
            310.88551330566406,
            842.0399780273438,
            345.4340362548828
         ],
         "text": "Destroyed bridges and flooded roads can further constrain access but data on the infrastructural damages across the different states is lacking.",
         "textOrder": 15,
         "textCrop": [
            431.0899963378906,
            312.38299560546875,
            813.5042724609375,
            338.68804931640625
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 345.4340362548828,
         "x1": 842.0399780273438,
         "y1": 397.0940246582031,
         "rect": [
            421.01690673828125,
            345.4340362548828,
            842.0399780273438,
            397.0940246582031
         ],
         "text": "Aggravating factors Recurring flooding",
         "textOrder": 16,
         "textCrop": [
            431.0899963378906,
            352.1800231933594,
            572.7100830078125,
            395.6250305175781
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 397.0940246582031,
         "x1": 842.0399780273438,
         "y1": 439.06553649902344,
         "rect": [
            421.01690673828125,
            397.0940246582031,
            842.0399780273438,
            439.06553649902344
         ],
         "text": "Nigeria experiences flooding annually during the rainy season with Niger and Benue rivers frequently overflowing not only due to local rainfall but also because the country is located downstream of several neighbouring countries (IFRC 09/2019).",
         "textOrder": 17,
         "textCrop": [
            431.0899963378906,
            398.5630187988281,
            813.7708740234375,
            437.56805419921875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 2,
         "x0": 421.01690673828125,
         "y0": 439.06553649902344,
         "x1": 842.0399780273438,
         "y1": 569.6635437011719,
         "rect": [
            421.01690673828125,
            439.06553649902344,
            842.0399780273438,
            569.6635437011719
         ],
         "text": "In recent years, severe flooding has affected the country in 2012 and in 2018. In the past year, large parts of the country were flooded and the government declared a state of emergency in Kogi, Niger, Anambra and Delta (IFRC 09/2019). The 2018 flooding is estimated to have killed up to 200 people and displaced over half a million people (WHO 09/2019). The 2018 floods also caused widespread crop destruction of at least 150,000 hectares of agricultural land (OCHA 2018). Areas that are now affected by severe flooding for a second consecutive year face increased risks of reduced crop production that can impact the availability of produce in the region (Aljazeera 23/09/2019). In addition, there is a protracted risk of negative impacts on livelihoods of farmers and local populations\u2019 capacity to rebuild and repair their homes.",
         "textOrder": 18,
         "textCrop": [
            431.0899963378906,
            440.5630187988281,
            814.0977783203125,
            568.0340576171875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 421.0743103027344,
         "y1": 93.62402725219727,
         "rect": [
            0.0,
            0.0,
            421.0743103027344,
            93.62402725219727
         ],
         "text": "Rainy season",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            74.28800201416016,
            106.69536590576172,
            92.09503936767578
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 0.0,
         "y0": 93.62402725219727,
         "x1": 421.0743103027344,
         "y1": 183.55802154541016,
         "rect": [
            0.0,
            93.62402725219727,
            421.0743103027344,
            183.55802154541016
         ],
         "text": "The main rain season in the north of the country usually lasts from June until October while it can last until November in the south (FEWS NET). For 2019, the Nigeria Hydrological Services Agency (NIHSA) predicted flooding particularly from June throughout September (NNN 26/06/2019). Nevertheless, rainfall is likely to continue in the next days. For central Nigeria, heavy rainfall is expected in the upcoming week making further flooding likely (FEWS NET 11/10/2019).",
         "textOrder": 1,
         "textCrop": [
            28.079999923706055,
            95.15301513671875,
            411.0115051269531,
            171.9580535888672
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 0.0,
         "y0": 183.55802154541016,
         "x1": 421.0743103027344,
         "y1": 214.43402862548828,
         "rect": [
            0.0,
            183.55802154541016,
            421.0743103027344,
            214.43402862548828
         ],
         "text": "Conflicts",
         "textOrder": 2,
         "textCrop": [
            28.079999923706055,
            195.15798950195312,
            77.79168701171875,
            212.9650421142578
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 0.0,
         "y0": 214.43402862548828,
         "x1": 421.0743103027344,
         "y1": 332.2555236816406,
         "rect": [
            0.0,
            214.43402862548828,
            421.0743103027344,
            332.2555236816406
         ],
         "text": "Northeast: The three northeastern states Borno, Yobe and Adamawa continue to face a volatile security situation due to the Boko Haram conflict that has led to an ongoing humanitarian emergency. As of August 2019, over 7 million people are considered in need of humanitarian assistance in the northeast (OCHA 08/2019). The Boko Haram conflict is a key driver for displacement in Nigeria. Due to ongoing violence against civilians, around 42,000 new cases of displacement were reported in northeast states in the first half of 2019, with actual numbers likely to be even higher (IDMC 12/09/2019). The heavy rains and flooding during this rainy season have increased needs of IDPs and local farmers even further (OCHA 08/2019).",
         "textOrder": 3,
         "textCrop": [
            28.079999923706055,
            215.90301513671875,
            411.0586242675781,
            330.748046875
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 1.1087949778160922,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.30029136808730517,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.48724344621102017,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.9285765700042248,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.03594491721653357,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 1.713403692931421,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.4254854266247694,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.06756930317925779,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 1.0981449714073768,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.8007454114321684,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.3368153878473566,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 0.9515205415609841,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.9239900332400209,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.27653703679276337,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.2634014521933407,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.08925932263015607,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 1.572836866032892,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.10631303950895404,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.25005560414290723,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.33376736086119646,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.2646434195010008,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.042477648862650694,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.04082719067063851,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.5549764264912027,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 0.25096696255535916,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.1453523143038078,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.12645056496744286,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.040735170807478564,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.1499150961512801,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.027789596722207287,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.15364284964575284,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.11502028064569458,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.26610280338086584,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.1465937458589429,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.10677344187742142,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.10454887943761842,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.0871398284783425,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.6664468853484166,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.00986945448721957,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.005551625354183693,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.03758242866336899,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.1251165545597374,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.002056681006116436,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.316029947823014,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00012656540303898658,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.1500841188296843,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.002869440650101751,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.2672000948193157,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.08549403261255334,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.0571630855507039,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.20641053716341654,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.029031332759630112,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.500998048055837,
                     "threshold": 0.466,
                     "is_selected": True
                  },
                  "5601": {
                     "prediction": 0.324115610469586,
                     "threshold": 0.378,
                     "is_selected": False
                  },
                  "5603": {
                     "prediction": 0.047048493250598754,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.07937944067989366,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.9458889415608116,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0004053236639308145,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.0059611241070435346,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.001060415962230012,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.012124301068280163,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.0044229401353590506,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.032900919836773526,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.004400992846906777,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.017675002111440987,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.026926788133244183,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.04011546287054572,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0006994238214158431,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.014934296717935443,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0004661933922357599,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.15429167244671646,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.033404068722401134,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.015664852127946657,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.2894524484872818,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.21213278292663512,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.24231315606380735,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.1084672349716435,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.15054125401933316,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.8406954989444724,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.182493800728679,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.002690716618043513,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.029860576137951213,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.007469527991574018,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.031439937522699093,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.009964938490188308,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.00792892108903818,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.0029666455728667124,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.028734480893704138,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.036734751223837916,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.016470187345132965,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.03406907553258149,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.07038871404700922,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.030395374715066793,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.8877974112056991,
                     "threshold": 0.515,
                     "is_selected": True
                  },
                  "3403": {
                     "prediction": 1.4527041744666296,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.07951999392345367,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.32432872679207353,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.03091268499807126,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.19088515620322744,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.01096057153686329,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.02920164002312554,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.03670346997086964,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.04159149940915289,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.07459922831078045,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.9155511154847987,
                     "threshold": 0.425,
                     "is_selected": True
                  },
                  "3701": {
                     "prediction": 0.01645575254706564,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.934737069266183,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.3413314436688835,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.006798034675730535,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.7476454238756008,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.007252335131119985,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.18473698286832813,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.04672199077220115,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.08391073331273999,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.23928221790388288,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.029955747658791748,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.14251592399189308,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.4981400219199314,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.6855930536704773,
                     "threshold": 0.531,
                     "is_selected": True
                  },
                  "4301": {
                     "prediction": 0.60285608655905,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.8993595838546753,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.5048686235221391,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.3661334659289388,
                     "threshold": 0.412,
                     "is_selected": False
                  },
                  "4403": {
                     "prediction": 0.47181636816070927,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.31121761775484275,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.08836754404746734,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.2745347317129243,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.14708776258479403,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.02784037878584178,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.04933850919984095,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.0038899091752962424,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.030155342294653848,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.11179845077096769,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.10530063920175499,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.004150036107811462,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.011688840925780397,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.06764622198210822,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.016131555575868407,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.05939429865615203,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.005341303566920346,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.011344035767545604,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.03738770088584153,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.017091653208775693,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.03417948404782003,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.05897403771960579,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.008235550759469763,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.003901713500744191,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.007806779031450326,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.07463876005663747,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.010775831167298803,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.10061040134627584,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.03366877694101729,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.05100517627898227,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.011886782871866688,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.018975522190442382,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.016177347709384303,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.0037841748643592495,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.03716566962697253,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 3,
         "x0": 0.0,
         "y0": 332.2555236816406,
         "x1": 421.0743103027344,
         "y1": 498.1410217285156,
         "rect": [
            0.0,
            332.2555236816406,
            421.0743103027344,
            498.1410217285156
         ],
         "text": "Middle Belt: Kogi state is located in the Middle Belt area. In central Nigerian states, the violence between herders and farmers in central Nigerian states known as the Middle Belt conflict has displaced 23,000 people (IDMC 12/09/2019). The Middle Belt conflict mainly affects Benue, Nasarawa, Plateau, and Taraba states (CrisisGroup 26/07/2018) but there have been violent incidents in Kogi in the past (Idakwoji et al. 2018, HRW). The current extent of the humanitarian needs of conflict-affected people in the Middle Belt is under-reported and displacement numbers are likely to be higher (IDMC Special Report 05/2019). Insecurity and displacement have made farming and herding more difficult for communities (CrisisGroup 26/07/2018). This situation is likely to have increased in flooded areas where livestock and crops have been destroyed and can increase the risk of food insecurity. In addition, displaced people in emergency and makeshift shelters are likely to face increased needs due to the flooding.",
         "textOrder": 4,
         "textCrop": [
            28.079999923706055,
            333.76300048828125,
            410.93975830078125,
            486.55804443359375
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 1.0183669916203661,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.3825131634052301,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.308637869440847,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 1.2454045936465263,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.05856702270788875,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 1.368749445939562,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.4222874590789029,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.3591949087485932,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.6096943394168393,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.7770752994238893,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.42476490558352376,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 0.8980331019820454,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.8573236834369686,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.2541132834508661,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.34405872589204367,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.36798051191032477,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 1.230105834921407,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.13034528117896452,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.28368373834547195,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.2550602552775817,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.3587020379779613,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.09613219551157423,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.04305577096648705,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.8148225003030808,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 0.22754289916363254,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.1500788411988872,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.12822662688553604,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.027824357977875,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.15018697999511305,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.01914568922736428,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.1201430596591194,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.09242400847142562,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.23443568693964106,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.1386249071506203,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.1196357839572148,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.11384572733092953,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.06871126495756194,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 1.0495454991966617,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.007491684677641536,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.007467529960895625,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.036022265418797265,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.1506188963197653,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.003988608133364865,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.2912776042316959,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.00037349634341724957,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.1848054289371333,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.0036715963506139815,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.27238955532295117,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.07610787558399773,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.07866018630088645,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.3503301739692688,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.012368079097498031,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.5048211552042817,
                     "threshold": 0.466,
                     "is_selected": True
                  },
                  "5601": {
                     "prediction": 0.3692527454366129,
                     "threshold": 0.378,
                     "is_selected": False
                  },
                  "5603": {
                     "prediction": 0.09444628546877605,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.12122902829768295,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.0277564401057229,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0004899878471616808,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.008967816499522729,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.001050804866294206,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.01307389727509272,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.0032013360719510657,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.032580590673855374,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.003857921148019452,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.05032445833748542,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.03240532257232159,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.0440237300643504,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.000907084336731492,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.024851469003625917,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0009282420150056068,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.09586256862534166,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.02261741401114091,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.01829957332590531,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.45402844746907556,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.1919824807416825,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.10323470736191151,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.14159120932346633,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.2470623417678526,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 1.2670519540635803,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.4162491884547032,
                     "threshold": 0.393,
                     "is_selected": True
                  },
                  "3201": {
                     "prediction": 0.0033377319077269796,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.026803218947132293,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.015564065281335913,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.023251551942064845,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.004617240686660417,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.007534877444217878,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.006354122555681638,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.046443712953442066,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.02907523566665758,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.018765242171079725,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.06973279802047687,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.1025305905357418,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.09990493325810683,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.9242517855560896,
                     "threshold": 0.515,
                     "is_selected": True
                  },
                  "3403": {
                     "prediction": 1.416093067741856,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.09150664333389838,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.3677763372332185,
                     "threshold": 0.364,
                     "is_selected": True
                  },
                  "3504": {
                     "prediction": 0.0979505436268845,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.22572951268744823,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.012554580138789281,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.03874793786693502,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.11513896641277131,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.21767219574392774,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.2541779006113772,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.4064655303955078,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.012874444543248964,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.5641913763722595,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.1992081234484543,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0037258789538238794,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.8391814209273641,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.011835450627054874,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.3292760129047953,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.034027877504718126,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.14029622561021932,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.30065701944837847,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.07435045056584952,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.2494085759736707,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.7194517269832864,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.3243697677403969,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.630648862650466,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.84792983136783,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.5450574777175471,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.454041492013098,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.36879079115967595,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.3497307280115053,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.05702216614474047,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.4881972113551011,
                     "threshold": 0.458,
                     "is_selected": True
                  },
                  "4502": {
                     "prediction": 0.19548394192859053,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.01800944265283522,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.030928173117221347,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.00295978388749063,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.017753316886463567,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.09807341463395157,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.06709644487994885,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.006090127235836654,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.008753389554538114,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.05686383694410324,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.018027837706175037,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.08415199889995084,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.004653009901514644,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.009156248974378663,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.0612612544875784,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.023007038307477194,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.057603553373032176,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.08313661221593749,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.024859232499318967,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.0033337980562794037,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.014130142923016167,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.1021913048503124,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.04403277237123159,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.14248353289198998,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.059973834269850916,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.04214173120059324,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.012691781033300658,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.016895325586364716,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.007178492049443657,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.008945964702361862,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.050146525339372645,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 3,
         "x0": 0.0,
         "y0": 498.1410217285156,
         "x1": 421.0743103027344,
         "y1": 595.3200073242188,
         "rect": [
            0.0,
            498.1410217285156,
            421.0743103027344,
            595.3200073242188
         ],
         "text": "Border closure In August 2019, the Government of Nigeria unilaterally closed its borders with Benin and Niger to goods trade and effectively banned food imports from its neighbouring",
         "textOrder": 5,
         "textCrop": [
            28.079999923706055,
            509.7239990234375,
            410.7861022949219,
            556.7540283203125
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 0.0,
         "x1": 842.0399780273438,
         "y1": 38.868499755859375,
         "rect": [
            421.0743103027344,
            0.0,
            842.0399780273438,
            38.868499755859375
         ],
         "text": "ACAPS Briefing Note: Floods in Nigeria",
         "textOrder": 6,
         "textCrop": [
            674.02001953125,
            22.557010650634766,
            814.0595703125,
            33.603973388671875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 38.868499755859375,
         "x1": 842.0399780273438,
         "y1": 143.3040313720703,
         "rect": [
            421.0743103027344,
            38.868499755859375,
            842.0399780273438,
            143.3040313720703
         ],
         "text": "countries. According to the government, the decision was a step to counter smuggling (DW 17/09/2019) and is also part of a wider policy to strengthen local agricultural production. The shutdown has begun to impact food prices, which have been rising in September (Bloomberg 15/10/2019). Increased inflation can further limit access to food for poor people and people whose livelihoods have been reduced or destroyed by the floods and now rely on purchasing additional food. It also might aggravate the general availability of food items which has been strained by crop damage due to the flooding.",
         "textOrder": 7,
         "textCrop": [
            431.0899963378906,
            44.133026123046875,
            813.9660034179688,
            133.7980499267578
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 143.3040313720703,
         "x1": 842.0399780273438,
         "y1": 176.06900787353516,
         "rect": [
            421.0743103027344,
            143.3040313720703,
            842.0399780273438,
            176.06900787353516
         ],
         "text": "Key characteristics",
         "textOrder": 8,
         "textCrop": [
            431.0899963378906,
            152.8100128173828,
            568.7350463867188,
            173.4650115966797
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 176.06900787353516,
         "x1": 842.0399780273438,
         "y1": 269.87042236328125,
         "rect": [
            421.0743103027344,
            176.06900787353516,
            842.0399780273438,
            269.87042236328125
         ],
         "text": "Demographic profile (population/surface area): Country level: 193 million people / 909,890 square metres Borno: 5.7 million people / 72,000 square metres Delta: 3.9 million people / 17,108 square metres Kebbi: 4.4 million people / 36,985 square metres Kogi: 4.5 million people / 27,747 square metres (GoN National Bureau of Statistics 2011; population projection 2016)",
         "textOrder": 9,
         "textCrop": [
            431.0899963378906,
            178.67300415039062,
            734.4566650390625,
            268.3480224609375
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 269.87042236328125,
         "x1": 842.0399780273438,
         "y1": 349.81040954589844,
         "rect": [
            421.0743103027344,
            269.87042236328125,
            842.0399780273438,
            349.81040954589844
         ],
         "text": "Poverty statistics: Poverty gap at national poverty lines (%): 17 (2009) Rural poverty gap at national poverty lines (%): 20.1 (2009) Urban poverty gap at national poverty lines (%): 11.6 (2009) Poverty headcount ratio at USD 3.20 a day (2011 PPP) (% of population): 77.6 (2009) Poverty headcount ratio at USD 1.90 a day (2011 PPP) (% of population): 53.5 (2009)",
         "textOrder": 10,
         "textCrop": [
            431.0899963378906,
            271.392822265625,
            810.5216064453125,
            348.28802490234375
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 349.81040954589844,
         "x1": 842.0399780273438,
         "y1": 404.4104309082031,
         "rect": [
            421.0743103027344,
            349.81040954589844,
            842.0399780273438,
            404.4104309082031
         ],
         "text": "Food security figures: Most households outside northeast Nigeria face Minimal (IPC Phase 1) acute food insecurity. In Borno, Adamawa and Yobe states, Crisis (IPC Phase 3) and Emergency (IPC Phase 4) outcomes continue (FEWS NET 09/2019).",
         "textOrder": 11,
         "textCrop": [
            431.0899963378906,
            351.3327941894531,
            810.3082885742188,
            402.8880310058594
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 404.4104309082031,
         "x1": 842.0399780273438,
         "y1": 492.5535125732422,
         "rect": [
            421.0743103027344,
            404.4104309082031,
            842.0399780273438,
            492.5535125732422
         ],
         "text": "Nutrition levels: Prevalence of severe acute malnutrition, weight for height (% of children under 5): 2.9 Prevalence of acute malnutrition, weight for height (% of children under 5): 10.6 (2017) Prevalence of chronic malnutrition, height for age (% of children under 5): 43.6 (2017) Prevalence of undernourishment (% of population): 7.9 (2015)",
         "textOrder": 12,
         "textCrop": [
            431.0899963378906,
            405.9328308105469,
            813.2286987304688,
            482.718017578125
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.6977830440232603,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.4120223111030595,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.27126886157525915,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.8858683785157544,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.2073235809803009,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.6557786685961305,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.12012430139490075,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.32122769768823656,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.3468503991326133,
                     "threshold": 0.455,
                     "is_selected": False
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.7354586514983609,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.29162042341788436,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.5617628520894273,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.7222633438903244,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.12039272496818723,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.08113302052803827,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.06483368097095314,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.38599852144409336,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "2107": {
                     "prediction": 0.12715105554831935,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.5132890471215111,
                     "threshold": 0.486,
                     "is_selected": True
                  },
                  "2110": {
                     "prediction": 0.7155278943619638,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.17588461988267645,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.04114043454768912,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 1.3155330641147418,
                     "threshold": 0.624,
                     "is_selected": True
                  },
                  "2111": {
                     "prediction": 0.21050860188918474,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.07337473075965355,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.18274852395664856,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.4576596359139708,
                     "threshold": 0.438,
                     "is_selected": True
                  },
                  "5306": {
                     "prediction": 0.27815593441702285,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.5565849308189488,
                     "threshold": 0.478,
                     "is_selected": True
                  },
                  "5302": {
                     "prediction": 0.25551737370816147,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.5577781782058127,
                     "threshold": 0.414,
                     "is_selected": True
                  },
                  "5309": {
                     "prediction": 0.6464490434154868,
                     "threshold": 0.512,
                     "is_selected": True
                  },
                  "5308": {
                     "prediction": 0.5480707319159257,
                     "threshold": 0.475,
                     "is_selected": True
                  },
                  "5301": {
                     "prediction": 1.3647267564398344,
                     "threshold": 0.488,
                     "is_selected": True
                  },
                  "5305": {
                     "prediction": 1.2939158152407548,
                     "threshold": 0.508,
                     "is_selected": True
                  },
                  "5304": {
                     "prediction": 0.3709155428516972,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.1603146384912586,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.40800495294747374,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.15393440218109472,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.028914257714372883,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.5073179001242789,
                     "threshold": 0.447,
                     "is_selected": True
                  },
                  "5107": {
                     "prediction": 0.2393744106016605,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.03147683839531655,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.45138068837248935,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.0008553898663428296,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.1296516689245174,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.019287829054519534,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 1.3878728045193058,
                     "threshold": 0.483,
                     "is_selected": True
                  },
                  "5401": {
                     "prediction": 0.4777092819380085,
                     "threshold": 0.459,
                     "is_selected": True
                  },
                  "5402": {
                     "prediction": 0.3122096049024704,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.38992053932613796,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.08573725110008602,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.8972562817544896,
                     "threshold": 0.466,
                     "is_selected": True
                  },
                  "5601": {
                     "prediction": 0.6650388240814209,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.18589089556438168,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.05958883202303265,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.028890262788801,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0021498539736114885,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.07564851263073029,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0055671902009065905,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.01952871349256528,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.025839862709273836,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.09334260113624555,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.020273203127289526,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.08353940654254616,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.05801173663416574,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.23247285293099657,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0034265205968262223,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.05592743871528978,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0051329871995322825,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.1987910772104399,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.009191762885929626,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.0034444877107081746,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.8148143688837688,
                     "threshold": 0.48,
                     "is_selected": True
                  },
                  "3203": {
                     "prediction": 0.2364154520725447,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.06792682034024983,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.07280938233397588,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.21634149854466067,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.15813097965231332,
                     "threshold": 0.417,
                     "is_selected": False
                  },
                  "3205": {
                     "prediction": 0.2903245939249907,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.00012292541794556026,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.05124228030646621,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.011669240097318767,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.05727246532152439,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.004388548537081614,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.008521497486611953,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.00920877791941166,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.020819880082713335,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.021586911717408508,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.009128828304222004,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.026107011565371697,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.060493305995581746,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.008507242646852606,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.04087080726924452,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.6414331477721725,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.02243317030219414,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.046228856912681034,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.006994669933970263,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.04207744656601276,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.019833050599252736,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.049816979164326626,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.02322321580279441,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.043823152480509456,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.14095783966486572,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.26161937152638154,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.004967233067880018,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.18701871514928584,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.17634799451003838,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.010567976971882274,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.778914133519358,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.005354688657060652,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.20360627111773,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.13360646063576956,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.11924737855383286,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.13426542588712748,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.006265532093770477,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.1170932621825916,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.6561576638123536,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.4076746673009265,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 1.330719485303363,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.6403774846324605,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.49695722067479003,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.2407960738371877,
                     "threshold": 0.412,
                     "is_selected": False
                  },
                  "4403": {
                     "prediction": 0.3414415724335178,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.13593880130964167,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.008498766535037273,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.06022238819229551,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.04262558189825823,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.029401042590253668,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.07714904726497711,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.01541473723661441,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.07067473410670437,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.2366783917596697,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.46189506406243513,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.00396876020501258,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.04997082141502258,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.08726193673080868,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.04500659863683271,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.03253986487294187,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.11468724051063492,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.9898887138174037,
                     "threshold": 0.495,
                     "is_selected": True
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.10165503037344549,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.06159919213099652,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.06349578826437415,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.03892082851136095,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.017822188708712074,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.024360677470331608,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.03338477311441707,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.05177496742027843,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.012817098687788067,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.1262986328008879,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.08647445097007225,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.04068312936284569,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.04658195578936234,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.07414864548018057,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.13783542722787545,
                     "threshold": 0.046,
                     "is_selected": True
                  },
                  "1804": {
                     "prediction": 0.015283786747234547,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.08603164056099286,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 3,
         "x0": 421.0743103027344,
         "y0": 492.5535125732422,
         "x1": 805.2923583984375,
         "y1": 595.3200073242188,
         "rect": [
            421.0743103027344,
            492.5535125732422,
            805.2923583984375,
            595.3200073242188
         ],
         "text": "Health statistics: Mortality rate attributed to unsafe water, sanitation and lack of hygiene (per 100,000 population): 68.6 (2017) Incidence of malaria (per 1,000 population at risk): 380.8 (2015)",
         "textOrder": 13,
         "textCrop": [
            431.0899963378906,
            502.3890075683594,
            800.9447021484375,
            553.9940185546875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 421.04444885253906,
         "y1": 97.28042984008789,
         "rect": [
            0.0,
            0.0,
            421.04444885253906,
            97.28042984008789
         ],
         "text": "WASH statistics: People practicing open defecation (% of population): 25.5 (2015) People using at least basic drinking water services (% of population): 67.3 (2015) People using safely managed drinking water services (% of population): 19.4 (2015)",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            44.133026123046875,
            398.5422058105469,
            95.75804138183594
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.5338271215161907,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.4115646418159799,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.07231380247200529,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.3701171704701015,
                     "threshold": 0.448,
                     "is_selected": False
                  },
                  "2203": {
                     "prediction": 0.2250338836414058,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.331433113932333,
                     "threshold": 0.431,
                     "is_selected": False
                  },
                  "2207": {
                     "prediction": 0.03831708825347967,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 0.07693987470446971,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "2202": {
                     "prediction": 0.24540899219093743,
                     "threshold": 0.455,
                     "is_selected": False
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.4366235147187063,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.3430913192407101,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2305": {
                     "prediction": 1.7761366668148575,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.7743395641274045,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.12623778590630763,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.13385297936749055,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.03531601177443058,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.2842672323624705,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "2107": {
                     "prediction": 0.06732674305204557,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.5048713321057857,
                     "threshold": 0.486,
                     "is_selected": True
                  },
                  "2110": {
                     "prediction": 0.8262728870039966,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "2101": {
                     "prediction": 0.13991646402705032,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.043180364538246474,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.0891132065309928,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.16242003140787784,
                     "threshold": 0.437,
                     "is_selected": False
                  },
                  "2106": {
                     "prediction": 0.048384114553959204,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 1.4143220839961883,
                     "threshold": 0.589,
                     "is_selected": True
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.27819549384182446,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.13838984283073893,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.4516127343955898,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.14878645200621,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.268101764185993,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.32622157596051693,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.31948168026773555,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.36523143043283557,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.2332537574326898,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.3893335458931622,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.2559501946302967,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.32418940035782196,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.1759724862619335,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.027466720885524713,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.4808626385609842,
                     "threshold": 0.447,
                     "is_selected": True
                  },
                  "5107": {
                     "prediction": 0.35199788471638227,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.008029387669360384,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.6519929502020239,
                     "threshold": 0.482,
                     "is_selected": True
                  },
                  "5104": {
                     "prediction": 0.000493151040062896,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.28358885411466106,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.005952349747531116,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.6242731960170265,
                     "threshold": 0.483,
                     "is_selected": True
                  },
                  "5401": {
                     "prediction": 0.2534033523665534,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.19778300155984596,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.32256033685472274,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.002405397771369843,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.45831814855976677,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 1.1547296923935098,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.5153124409962476,
                     "threshold": 0.369,
                     "is_selected": True
                  },
                  "5605": {
                     "prediction": 0.09565987482161846,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 1.3167970809177378,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0013646717675228758,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.04211283306779678,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0015498714299992029,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.03124061544607837,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.004082356771071276,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.05289927491399109,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.014386660934751737,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.04209109422520402,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.05841321401619832,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.0461344768332219,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.005526644768329656,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.028133586135213773,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.003508607025853255,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.06650009973777979,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.006549655356340938,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.002132050275545696,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.2534270752221346,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.10995268230400389,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.038609036169308615,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.031244628006169776,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.06444377319540008,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.08168157270486406,
                     "threshold": 0.417,
                     "is_selected": False
                  },
                  "3205": {
                     "prediction": 0.22563203676359647,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.00010776849345024104,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.06716657086647412,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.002572722006760059,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.0184506434818794,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.0033602168932040603,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.008075103030021973,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.0011982540101079006,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.018450635083639415,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.00982280349635126,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.008601490880485193,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.017143841630414776,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.05361569818005572,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.0030092020384281087,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.024221542752483515,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.3326140867307169,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.004942945076476949,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.01863769260695675,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.01270214440247227,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.03864306901164369,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.0012677075574174523,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.026251070408357512,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.00965233360018049,
                     "threshold": 0.315,
                     "is_selected": False
                  },
                  "3603": {
                     "prediction": 0.026453801032814136,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.04098478887901932,
                     "threshold": 0.488,
                     "is_selected": False
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.1423508454771603,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.01099657814549861,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.2484459772097821,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.08524756556675757,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.012688387954191143,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.5491125922632444,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.008498858237131075,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.3151799709061303,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.2754285359422432,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.1064663627498465,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.2800848319697282,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.03712366510560547,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.6550623560851475,
                     "threshold": 0.477,
                     "is_selected": True
                  },
                  "4302": {
                     "prediction": 1.197461678179778,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.42261926916808507,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.9912691147030679,
                     "threshold": 0.466,
                     "is_selected": True
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.6125963277579671,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.6382609381503666,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.5399774651504258,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.4283026341469057,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.18673258669236129,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.07224504475121026,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.15158331485294357,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.08672736094047345,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.011725897030507932,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.04517987302912065,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.005707165781551829,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.023923703094026933,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.40369246502501843,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.6016535676925289,
                     "threshold": 0.494,
                     "is_selected": True
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.003480472012426115,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.049172691544707936,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.09903583261701795,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.02533790021773978,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.04033120625680036,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.017492402851218867,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.04124849131613067,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.07422405112649977,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.010551934141710581,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.02790755924762913,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.024888117484520616,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.009638590409475215,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.01431325909452162,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.02238313093106506,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.026954562995291996,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.0065923632780819546,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.06435694259837502,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.05516152336635063,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.03593127462971076,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.2417138334616874,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.3880765770194275,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.26699989710165106,
                     "threshold": 0.046,
                     "is_selected": True
                  },
                  "1804": {
                     "prediction": 0.12079654693208783,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.9284772318088989,
                     "threshold": 0.593,
                     "is_selected": True
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 97.28042984008789,
         "x1": 421.04444885253906,
         "y1": 139.38751983642578,
         "rect": [
            0.0,
            97.28042984008789,
            421.04444885253906,
            139.38751983642578
         ],
         "text": "Lighting and cooking sources: People using safely managed drinking water services (% of population): 19.4 (2015) Access to electricity (% of population): 59.3 (2016)",
         "textOrder": 1,
         "textCrop": [
            28.079999923706055,
            98.80281829833984,
            398.8687744140625,
            137.75804138183594
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 139.38751983642578,
         "x1": 421.04444885253906,
         "y1": 160.41698455810547,
         "rect": [
            0.0,
            139.38751983642578,
            421.04444885253906,
            160.41698455810547
         ],
         "text": "Source: World Bank 2015",
         "textOrder": 2,
         "textCrop": [
            28.079999923706055,
            141.01699829101562,
            119.28911590576172,
            152.06396484375
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 160.41698455810547,
         "x1": 421.04444885253906,
         "y1": 213.7740249633789,
         "rect": [
            0.0,
            160.41698455810547,
            421.04444885253906,
            213.7740249633789
         ],
         "text": "Response capacity Local and national response capacity",
         "textOrder": 3,
         "textCrop": [
            28.079999923706055,
            168.77000427246094,
            241.92799377441406,
            212.2450408935547
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 213.7740249633789,
         "x1": 421.04444885253906,
         "y1": 281.0055236816406,
         "rect": [
            0.0,
            213.7740249633789,
            421.04444885253906,
            281.0055236816406
         ],
         "text": "At a federal level, the National Emergency Management Agency (NEMA) is the coordinating agency for emergency management in Nigeria and operates in cooperation with the state emergency management agencies (SEMA). For 2019, the Nigeria Hydrological Services Agency (NIHSA) predicted flooding particularly from June throughout September (NNN 26/06/2019).",
         "textOrder": 4,
         "textCrop": [
            28.079999923706055,
            215.30300903320312,
            410.9477233886719,
            279.5080261230469
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 281.0055236816406,
         "x1": 421.04444885253906,
         "y1": 335.6255187988281,
         "rect": [
            0.0,
            281.0055236816406,
            421.04444885253906,
            335.6255187988281
         ],
         "text": "On the individual state level, the response and capacities of state governments vary. Kebbi government for instance announced in September to earmark 1.5 billion Nigerian naira for flood-related emergencies but it remains unclear what the operational response has been in each state (Guardian Nigeria 21/09/2019).",
         "textOrder": 5,
         "textCrop": [
            28.079999923706055,
            282.5030212402344,
            410.6949462890625,
            334.1280212402344
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 335.6255187988281,
         "x1": 421.04444885253906,
         "y1": 389.03076171875,
         "rect": [
            0.0,
            335.6255187988281,
            421.04444885253906,
            389.03076171875
         ],
         "text": "In the past, the national disaster management framework has been criticized for not clearly defining the role of local, state and government emergency management agencies and emergency response has been said to have been sub-optimal (Olanrewaju, Chitakira, Olanrewaju & Louw, 2019). This raises concerns about the",
         "textOrder": 6,
         "textCrop": [
            28.079999923706055,
            337.1230163574219,
            410.9607238769531,
            388.72802734375
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 389.03076171875,
         "x1": 421.04444885253906,
         "y1": 402.391845703125,
         "rect": [
            0.0,
            389.03076171875,
            421.04444885253906,
            402.391845703125
         ],
         "text": "government\u2019s response capacities regarding the current flooding.",
         "textOrder": 7,
         "textCrop": [
            28.079999923706055,
            389.33349609375,
            315.0956115722656,
            400.4606628417969
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 0.0,
         "y0": 402.391845703125,
         "x1": 421.04444885253906,
         "y1": 595.3200073242188,
         "rect": [
            0.0,
            402.391845703125,
            421.04444885253906,
            595.3200073242188
         ],
         "text": "The IFRC has launched an Emergency Plan of Action in October that is supposed to last until 4 February 2020 (IFRC EPoA 07/10/2019). National partner organisations involved in the implementation are the Nigerian Red Cross Society (NRCS), the National Emergency Management Agency (NEMA), and the State Emergency Management Agencies (SEMA). On 22 September, a State Emergency Operation Centre (EOC) was activated to coordinate this response. The IFRC disaster response aims to deliver WASH services in Cross River, Kogi, Niger and Taraba states and to support 6,000 persons through a cash transfer programme. Apart from the NRCS, there is no information on local and national NGOs responding to the flood-affected population.",
         "textOrder": 8,
         "textCrop": [
            28.079999923706055,
            404.3230285644531,
            410.9989013671875,
            519.1940307617188
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 0.0,
         "x1": 842.0399780273438,
         "y1": 38.69600296020508,
         "rect": [
            421.04444885253906,
            0.0,
            842.0399780273438,
            38.69600296020508
         ],
         "text": "ACAPS Briefing Note: Floods in Nigeria",
         "textOrder": 9,
         "textCrop": [
            674.02001953125,
            22.557010650634766,
            814.0595703125,
            33.603973388671875
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 38.69600296020508,
         "x1": 842.0399780273438,
         "y1": 63.97927474975586,
         "rect": [
            421.04444885253906,
            38.69600296020508,
            842.0399780273438,
            63.97927474975586
         ],
         "text": "International response capacity",
         "textOrder": 10,
         "textCrop": [
            431.0899963378906,
            43.78803253173828,
            610.9779663085938,
            61.595069885253906
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 63.97927474975586,
         "x1": 842.0399780273438,
         "y1": 92.45552825927734,
         "rect": [
            421.04444885253906,
            63.97927474975586,
            842.0399780273438,
            92.45552825927734
         ],
         "text": "International partners supporting the IFRC\u2019s Emergency Plan of Action are the ICRC and the British Red Cross (IFRC EPoA 07/10/2019).",
         "textOrder": 11,
         "textCrop": [
            431.0899963378906,
            66.36347961425781,
            813.3958129882812,
            90.95805358886719
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 92.45552825927734,
         "x1": 842.0399780273438,
         "y1": 172.37552642822266,
         "rect": [
            421.04444885253906,
            92.45552825927734,
            842.0399780273438,
            172.37552642822266
         ],
         "text": "Despite the concentration of operational presence of humanitarian actors in Maiduguri, the state capital of Borno, gaps remain across sectors in the city. Already in June, MSF reported that some the capacities of its feeding centre in Maiduguri were reached (MSF 13/08/2019). As of 4 October, the Camp Coordination and Camp Management site tracker reveals further gaps in shelter, food and WASH needs across camps in northeast Nigeria (CCCM MST report 3 04/10/2019).",
         "textOrder": 12,
         "textCrop": [
            431.0899963378906,
            93.9530029296875,
            813.954345703125,
            170.87803649902344
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 172.37552642822266,
         "x1": 842.0399780273438,
         "y1": 233.93402099609375,
         "rect": [
            421.04444885253906,
            172.37552642822266,
            842.0399780273438,
            233.93402099609375
         ],
         "text": "In the three states in northeast Nigeria, including Borno, the State Ministry of Health has launched an emergency response in cooperation with the WHO and other partners in order to provide medical services aiming to mitigate the spread of diseases (WHO",
         "textOrder": 13,
         "textCrop": [
            431.0899963378906,
            173.87301635742188,
            814.09912109375,
            225.50804138183594
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 233.93402099609375,
         "x1": 842.0399780273438,
         "y1": 265.67901611328125,
         "rect": [
            421.04444885253906,
            233.93402099609375,
            842.0399780273438,
            265.67901611328125
         ],
         "text": "Information gaps and needs",
         "textOrder": 14,
         "textCrop": [
            431.0899963378906,
            242.36000061035156,
            631.1800537109375,
            263.0150146484375
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 0.7090642895922826,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.2808790985260506,
                     "threshold": 0.461,
                     "is_selected": False
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.04225323856290844,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.73958673913564,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.23056391051145103,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.41395443083238714,
                     "threshold": 0.431,
                     "is_selected": False
                  },
                  "2207": {
                     "prediction": 0.12544526729344402,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 1.471181579849176,
                     "threshold": 0.456,
                     "is_selected": True
                  },
                  "2202": {
                     "prediction": 0.3553672478749202,
                     "threshold": 0.455,
                     "is_selected": False
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.36925846177966204,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "2303": {
                     "prediction": 0.5659443642099269,
                     "threshold": 0.463,
                     "is_selected": True
                  },
                  "2305": {
                     "prediction": 0.7009116984973444,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.6230693766481606,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.20170963286838572,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.30781650185361364,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.04848597246572511,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 0.8359345284150672,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.27840815360117044,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.3430763941733435,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.46107919586029694,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.4761854631710896,
                     "threshold": 0.452,
                     "is_selected": True
                  },
                  "2109": {
                     "prediction": 0.1679224897198514,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.11669237835284992,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.8065182229746943,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 0.32120191588484004,
                     "threshold": 0.464,
                     "is_selected": False
                  },
                  "2108": {
                     "prediction": 0.15085028620446275,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.2298770668027608,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.12470874056782363,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.387121132228165,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.11885947632518681,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.14920808050943457,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.29981628176756203,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.1983646499483209,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.2760555534089198,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.11833741762272017,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.23986058527821894,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.1412066123181482,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 0.24789937726726616,
                     "threshold": 0.454,
                     "is_selected": False
                  },
                  "5106": {
                     "prediction": 0.27319429114734717,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.06832113132531095,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.48979363452134783,
                     "threshold": 0.447,
                     "is_selected": True
                  },
                  "5107": {
                     "prediction": 0.34481426389817404,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.05199739194296776,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.43690736363042937,
                     "threshold": 0.482,
                     "is_selected": False
                  },
                  "5104": {
                     "prediction": 0.0010393852452124273,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.24020973216281846,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.056715840473771095,
                     "threshold": 0.05,
                     "is_selected": True
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.2544873681374465,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.4311970441169988,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.34792718101055065,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.2730330162578159,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "5202": {
                     "prediction": 0.015830958173388525,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.1443577810418452,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.4269215401518282,
                     "threshold": 0.378,
                     "is_selected": True
                  },
                  "5603": {
                     "prediction": 0.17871836902003302,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.05930690963010667,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.5661956039234181,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.003858228932283702,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.08339788682175528,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.024799799695261207,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.04914736372203549,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.010748124289179515,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.9185424733217762,
                     "threshold": 0.427,
                     "is_selected": True
                  },
                  "5706": {
                     "prediction": 0.5194595448728234,
                     "threshold": 0.403,
                     "is_selected": True
                  },
                  "5705": {
                     "prediction": 0.05900793675388393,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.19207385142776262,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.2318019206840918,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.0091792504507594,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.03898809152531486,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.016330466476372547,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.06642321927993784,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.04415456665518843,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.07854822123872823,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 1.0028945902983348,
                     "threshold": 0.48,
                     "is_selected": True
                  },
                  "3203": {
                     "prediction": 0.10445150768473034,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.04234397214607388,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.2621635481589983,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.10808935325782178,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.16418815874081436,
                     "threshold": 0.417,
                     "is_selected": False
                  },
                  "3205": {
                     "prediction": 0.20986293032575806,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.00991450731236876,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.049139280825751634,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.010840823327045923,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.07339821935727679,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.017087903370890296,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.029137121060738555,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.006688003694372518,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.03741596549807019,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.025046337750021495,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.06476248925914856,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.02957653402742268,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.24925703601612523,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.015128155753604674,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.02869339026872394,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.3573970990954531,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.06127818242499703,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.09491993626067927,
                     "threshold": 0.364,
                     "is_selected": False
                  },
                  "3504": {
                     "prediction": 0.07824329138950575,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.09031475950704765,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.013991298705891326,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.11395885850544328,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 1.883157661982945,
                     "threshold": 0.315,
                     "is_selected": True
                  },
                  "3603": {
                     "prediction": 0.3727595811455575,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "3604": {
                     "prediction": 0.6403659210830438,
                     "threshold": 0.488,
                     "is_selected": True
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.15192142304252176,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.04123285300538589,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.19487734807997334,
                     "threshold": 0.392,
                     "is_selected": False
                  },
                  "3704": {
                     "prediction": 0.14304405561199893,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0017433233058002278,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.20363925121971782,
                     "threshold": 0.422,
                     "is_selected": False
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.00927814088955328,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.3969291432942029,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "4201": {
                     "prediction": 0.047802611041148635,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.45045552556948765,
                     "threshold": 0.401,
                     "is_selected": True
                  },
                  "4206": {
                     "prediction": 0.2753877468069885,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "4205": {
                     "prediction": 0.018505246270501957,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.1098289695300896,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.5131759073423303,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.1350846246810956,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.19526508808647614,
                     "threshold": 0.466,
                     "is_selected": False
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.4850883263250741,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.45243896467169537,
                     "threshold": 0.388,
                     "is_selected": True
                  },
                  "4401": {
                     "prediction": 0.3510809060439323,
                     "threshold": 0.412,
                     "is_selected": False
                  },
                  "4403": {
                     "prediction": 0.08228186878465837,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.28675075109098475,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.03332993737212172,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.26709057683507426,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.175948687978159,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.04796337214161138,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.1880953810652908,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.0256090138394099,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.07617331818858189,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.4041692375361014,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.1571261840551971,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.004998352990081214,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.0357566531693275,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.32569067345725167,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.061956146330579435,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.12372998465405832,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.031104570152672505,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.03620614909162425,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.10879386177997,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.4750238484646901,
                     "threshold": 0.415,
                     "is_selected": True
                  },
                  "1703": {
                     "prediction": 0.5391981133837292,
                     "threshold": 0.479,
                     "is_selected": True
                  },
                  "1704": {
                     "prediction": 0.06625615060329437,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.07194637375719407,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.05445015495238097,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.1531864162729177,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.19566268836698567,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.03852835434531748,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.1907297868493925,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.09212944164313744,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.056394440739342334,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.05073042459858274,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.024217863075737582,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.028709099000400824,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.024255601047778762,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.08881895553201287,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 265.67901611328125,
         "x1": 842.0399780273438,
         "y1": 410.0255126953125,
         "rect": [
            421.04444885253906,
            265.67901611328125,
            842.0399780273438,
            410.0255126953125
         ],
         "text": "Most available information either summarises the impact of the flooding across Nigeria without providing a geographical breakdown of the displaced populations, fatalities, injuries, and houses damaged or focuses exclusively on humanitarian needs in the conflict-affected areas in northeast Nigeria. A clear breakdown of humanitarian needs by sector and state level is lacking. Moreover, there is a lack of information regarding the effect of the flooding on non-IDPs and on host communities. On the one hand, there is a detailed picture of sectoral needs of displaced people living in camps in north-east Nigeria through agencies involved with the Humanitarian Response Plan for north-east Nigeria, namely through the multi-sectoral site tracker of the CCCM (CCCM MST report 3 04/10/2019). On the other hand, similar granular information on flood-affected Delta, Kebbi, and Kogi states and local populations there does not exist.",
         "textOrder": 15,
         "textCrop": [
            431.0899963378906,
            268.343017578125,
            814.0428466796875,
            408.52801513671875
         ],
         "relevant": True,
         "classification": {
            "2": {
               "204": {
                  "2402": {
                     "prediction": 1.1961402824807508,
                     "threshold": 0.489,
                     "is_selected": True
                  },
                  "2401": {
                     "prediction": 0.8883611369805325,
                     "threshold": 0.461,
                     "is_selected": True
                  }
               },
               "202": {
                  "2206": {
                     "prediction": 0.32570996942619485,
                     "threshold": 0.576,
                     "is_selected": False
                  },
                  "2205": {
                     "prediction": 0.6811200375003474,
                     "threshold": 0.448,
                     "is_selected": True
                  },
                  "2203": {
                     "prediction": 0.08858189107925911,
                     "threshold": 0.492,
                     "is_selected": False
                  },
                  "2201": {
                     "prediction": 0.7027910369731434,
                     "threshold": 0.431,
                     "is_selected": True
                  },
                  "2207": {
                     "prediction": 0.3740580385716265,
                     "threshold": 0.518,
                     "is_selected": False
                  },
                  "2204": {
                     "prediction": 1.5468285010572065,
                     "threshold": 0.456,
                     "is_selected": True
                  },
                  "2202": {
                     "prediction": 0.7181528505388197,
                     "threshold": 0.455,
                     "is_selected": True
                  }
               },
               "203": {
                  "2302": {
                     "prediction": 0.7104910819046655,
                     "threshold": 0.409,
                     "is_selected": True
                  },
                  "2303": {
                     "prediction": 0.7941852249285571,
                     "threshold": 0.463,
                     "is_selected": True
                  },
                  "2305": {
                     "prediction": 0.7085236851300035,
                     "threshold": 0.428,
                     "is_selected": True
                  },
                  "2301": {
                     "prediction": 0.7608266543020552,
                     "threshold": 0.433,
                     "is_selected": True
                  },
                  "2304": {
                     "prediction": 0.2038559150232352,
                     "threshold": 0.463,
                     "is_selected": False
                  },
                  "2306": {
                     "prediction": 0.2900629564700386,
                     "threshold": 0.533,
                     "is_selected": False
                  }
               },
               "201": {
                  "2103": {
                     "prediction": 0.056872233201604366,
                     "threshold": 0.545,
                     "is_selected": False
                  },
                  "2104": {
                     "prediction": 1.1900939008732534,
                     "threshold": 0.386,
                     "is_selected": True
                  },
                  "2107": {
                     "prediction": 0.1476102945755939,
                     "threshold": 0.539,
                     "is_selected": False
                  },
                  "2105": {
                     "prediction": 0.18676402576175738,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "2110": {
                     "prediction": 0.44817088534996946,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "2101": {
                     "prediction": 0.13095309413903583,
                     "threshold": 0.452,
                     "is_selected": False
                  },
                  "2109": {
                     "prediction": 0.10720857042421997,
                     "threshold": 0.497,
                     "is_selected": False
                  },
                  "2102": {
                     "prediction": 0.04054822970945866,
                     "threshold": 0.624,
                     "is_selected": False
                  },
                  "2111": {
                     "prediction": 0.45565756152914644,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "2106": {
                     "prediction": 0.8612363117522206,
                     "threshold": 0.464,
                     "is_selected": True
                  },
                  "2108": {
                     "prediction": 0.24192837179213106,
                     "threshold": 0.589,
                     "is_selected": False
                  }
               }
            },
            "5": {
               "503": {
                  "5303": {
                     "prediction": 0.08913477431965745,
                     "threshold": 0.438,
                     "is_selected": False
                  },
                  "5306": {
                     "prediction": 0.04342958805555443,
                     "threshold": 0.424,
                     "is_selected": False
                  },
                  "5310": {
                     "prediction": 0.13380546013680464,
                     "threshold": 0.478,
                     "is_selected": False
                  },
                  "5302": {
                     "prediction": 0.042619539255445656,
                     "threshold": 0.44,
                     "is_selected": False
                  },
                  "5307": {
                     "prediction": 0.12314639049739654,
                     "threshold": 0.414,
                     "is_selected": False
                  },
                  "5309": {
                     "prediction": 0.08521872950950637,
                     "threshold": 0.512,
                     "is_selected": False
                  },
                  "5308": {
                     "prediction": 0.14331430196762085,
                     "threshold": 0.475,
                     "is_selected": False
                  },
                  "5301": {
                     "prediction": 0.1110734692851051,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "5305": {
                     "prediction": 0.09043778725496428,
                     "threshold": 0.508,
                     "is_selected": False
                  },
                  "5304": {
                     "prediction": 0.14050377046202753,
                     "threshold": 0.444,
                     "is_selected": False
                  }
               },
               "501": {
                  "5102": {
                     "prediction": 0.08323961479826908,
                     "threshold": 0.541,
                     "is_selected": False
                  },
                  "5109": {
                     "prediction": 1.0721900127007573,
                     "threshold": 0.454,
                     "is_selected": True
                  },
                  "5106": {
                     "prediction": 0.02616878569595457,
                     "threshold": 0.381,
                     "is_selected": False
                  },
                  "5108": {
                     "prediction": 0.008606928907886176,
                     "threshold": 0.527,
                     "is_selected": False
                  },
                  "5111": {
                     "prediction": 0.07068867518064426,
                     "threshold": 0.447,
                     "is_selected": False
                  },
                  "5107": {
                     "prediction": 0.20451014052520616,
                     "threshold": 0.449,
                     "is_selected": False
                  },
                  "5101": {
                     "prediction": 0.006640686138354718,
                     "threshold": 0.47,
                     "is_selected": False
                  },
                  "5103": {
                     "prediction": 0.5151613990300918,
                     "threshold": 0.482,
                     "is_selected": True
                  },
                  "5104": {
                     "prediction": 0.00042379368689034425,
                     "threshold": 0.786,
                     "is_selected": False
                  },
                  "5105": {
                     "prediction": 0.16833145576023428,
                     "threshold": 0.534,
                     "is_selected": False
                  },
                  "5110": {
                     "prediction": 0.004848436510656029,
                     "threshold": 0.05,
                     "is_selected": False
                  }
               },
               "504": {
                  "5403": {
                     "prediction": 0.20615941619280703,
                     "threshold": 0.483,
                     "is_selected": False
                  },
                  "5401": {
                     "prediction": 0.058562565830278496,
                     "threshold": 0.459,
                     "is_selected": False
                  },
                  "5402": {
                     "prediction": 0.05946573107800585,
                     "threshold": 0.47,
                     "is_selected": False
                  }
               },
               "502": {
                  "5201": {
                     "prediction": 0.9927776787016127,
                     "threshold": 0.45,
                     "is_selected": True
                  },
                  "5202": {
                     "prediction": 0.03088154253505525,
                     "threshold": 0.525,
                     "is_selected": False
                  }
               },
               "506": {
                  "5604": {
                     "prediction": 0.4496641553011063,
                     "threshold": 0.466,
                     "is_selected": False
                  },
                  "5601": {
                     "prediction": 0.26640278242883225,
                     "threshold": 0.378,
                     "is_selected": False
                  },
                  "5603": {
                     "prediction": 0.1093121926958968,
                     "threshold": 0.369,
                     "is_selected": False
                  },
                  "5605": {
                     "prediction": 0.32103658353878284,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "5602": {
                     "prediction": 0.7341569335899543,
                     "threshold": 0.402,
                     "is_selected": True
                  }
               },
               "507": {
                  "5703": {
                     "prediction": 0.0012581689001519385,
                     "threshold": 0.638,
                     "is_selected": False
                  },
                  "5709": {
                     "prediction": 0.046873478937008176,
                     "threshold": 0.677,
                     "is_selected": False
                  },
                  "5711": {
                     "prediction": 0.0019863997374738513,
                     "threshold": 0.639,
                     "is_selected": False
                  },
                  "5708": {
                     "prediction": 0.044825286732351644,
                     "threshold": 0.619,
                     "is_selected": False
                  },
                  "5713": {
                     "prediction": 0.0036048984987858287,
                     "threshold": 0.501,
                     "is_selected": False
                  },
                  "5712": {
                     "prediction": 0.0367493999018323,
                     "threshold": 0.427,
                     "is_selected": False
                  },
                  "5706": {
                     "prediction": 0.007724671950448239,
                     "threshold": 0.403,
                     "is_selected": False
                  },
                  "5705": {
                     "prediction": 0.01758882622323127,
                     "threshold": 0.473,
                     "is_selected": False
                  },
                  "5707": {
                     "prediction": 0.04150721235231704,
                     "threshold": 0.602,
                     "is_selected": False
                  },
                  "5701": {
                     "prediction": 0.0905906934230054,
                     "threshold": 0.549,
                     "is_selected": False
                  },
                  "5702": {
                     "prediction": 0.005060485450596344,
                     "threshold": 0.82,
                     "is_selected": False
                  },
                  "5710": {
                     "prediction": 0.04878432376880866,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "5704": {
                     "prediction": 0.0015785004102831914,
                     "threshold": 0.576,
                     "is_selected": False
                  }
               }
            },
            "3": {
               "301": {
                  "3102": {
                     "prediction": 0.11125530041224584,
                     "threshold": 0.422,
                     "is_selected": False
                  },
                  "3101": {
                     "prediction": 0.11835891922069676,
                     "threshold": 0.486,
                     "is_selected": False
                  },
                  "3103": {
                     "prediction": 0.09813503972415268,
                     "threshold": 0.29,
                     "is_selected": False
                  }
               },
               "302": {
                  "3206": {
                     "prediction": 0.42721709857384366,
                     "threshold": 0.48,
                     "is_selected": False
                  },
                  "3203": {
                     "prediction": 0.09198506761874471,
                     "threshold": 0.504,
                     "is_selected": False
                  },
                  "3208": {
                     "prediction": 0.14772520270790623,
                     "threshold": 0.409,
                     "is_selected": False
                  },
                  "3202": {
                     "prediction": 0.1368996288095202,
                     "threshold": 0.476,
                     "is_selected": False
                  },
                  "3207": {
                     "prediction": 0.1987242850206666,
                     "threshold": 0.472,
                     "is_selected": False
                  },
                  "3204": {
                     "prediction": 0.6080676468727972,
                     "threshold": 0.417,
                     "is_selected": True
                  },
                  "3205": {
                     "prediction": 0.257143025634853,
                     "threshold": 0.393,
                     "is_selected": False
                  },
                  "3201": {
                     "prediction": 0.009683029371902255,
                     "threshold": 0.652,
                     "is_selected": False
                  }
               },
               "303": {
                  "3304": {
                     "prediction": 0.052261811525341595,
                     "threshold": 0.586,
                     "is_selected": False
                  },
                  "3301": {
                     "prediction": 0.007996812501255798,
                     "threshold": 0.436,
                     "is_selected": False
                  },
                  "3303": {
                     "prediction": 0.039806181629156244,
                     "threshold": 0.58,
                     "is_selected": False
                  },
                  "3302": {
                     "prediction": 0.011483130676339364,
                     "threshold": 0.577,
                     "is_selected": False
                  },
                  "3305": {
                     "prediction": 0.009909961949942746,
                     "threshold": 0.613,
                     "is_selected": False
                  },
                  "3307": {
                     "prediction": 0.01176304982176849,
                     "threshold": 0.7,
                     "is_selected": False
                  },
                  "3309": {
                     "prediction": 0.02715149552091178,
                     "threshold": 0.517,
                     "is_selected": False
                  },
                  "3308": {
                     "prediction": 0.026859034971819178,
                     "threshold": 0.526,
                     "is_selected": False
                  },
                  "3306": {
                     "prediction": 0.06097700984088819,
                     "threshold": 0.631,
                     "is_selected": False
                  }
               },
               "304": {
                  "3405": {
                     "prediction": 0.06748884376408397,
                     "threshold": 0.552,
                     "is_selected": False
                  },
                  "3402": {
                     "prediction": 0.09192836648391707,
                     "threshold": 0.467,
                     "is_selected": False
                  },
                  "3404": {
                     "prediction": 0.04672631621360779,
                     "threshold": 0.456,
                     "is_selected": False
                  },
                  "3401": {
                     "prediction": 0.15483864592117014,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "3403": {
                     "prediction": 0.7732882915339805,
                     "threshold": 0.413,
                     "is_selected": True
                  }
               },
               "305": {
                  "3501": {
                     "prediction": 0.05681169886700055,
                     "threshold": 0.494,
                     "is_selected": False
                  },
                  "3502": {
                     "prediction": 0.5176884050552661,
                     "threshold": 0.364,
                     "is_selected": True
                  },
                  "3504": {
                     "prediction": 0.0849552739677172,
                     "threshold": 0.519,
                     "is_selected": False
                  },
                  "3505": {
                     "prediction": 0.31935760549678927,
                     "threshold": 0.471,
                     "is_selected": False
                  },
                  "3503": {
                     "prediction": 0.011495485280950863,
                     "threshold": 0.27,
                     "is_selected": False
                  }
               },
               "306": {
                  "3602": {
                     "prediction": 0.1665845513343811,
                     "threshold": 0.54,
                     "is_selected": False
                  },
                  "3601": {
                     "prediction": 0.4352053479542808,
                     "threshold": 0.315,
                     "is_selected": True
                  },
                  "3603": {
                     "prediction": 1.4192431298411665,
                     "threshold": 0.447,
                     "is_selected": True
                  },
                  "3604": {
                     "prediction": 0.8271668167387853,
                     "threshold": 0.488,
                     "is_selected": True
                  }
               },
               "307": {
                  "3703": {
                     "prediction": 0.35789016415091124,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "3701": {
                     "prediction": 0.018539224626766534,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "3702": {
                     "prediction": 0.8126383229177825,
                     "threshold": 0.392,
                     "is_selected": True
                  },
                  "3704": {
                     "prediction": 0.1607679106571056,
                     "threshold": 0.405,
                     "is_selected": False
                  }
               }
            },
            "4": {
               "401": {
                  "4102": {
                     "prediction": 0.0013149754173998752,
                     "threshold": 0.814,
                     "is_selected": False
                  },
                  "4101": {
                     "prediction": 0.694784084202554,
                     "threshold": 0.422,
                     "is_selected": True
                  }
               },
               "402": {
                  "4203": {
                     "prediction": 0.01868586412739831,
                     "threshold": 0.616,
                     "is_selected": False
                  },
                  "4204": {
                     "prediction": 0.601361303934644,
                     "threshold": 0.457,
                     "is_selected": True
                  },
                  "4201": {
                     "prediction": 0.05939599742276442,
                     "threshold": 0.599,
                     "is_selected": False
                  },
                  "4202": {
                     "prediction": 0.2611378890617827,
                     "threshold": 0.401,
                     "is_selected": False
                  },
                  "4206": {
                     "prediction": 0.5431439528249419,
                     "threshold": 0.486,
                     "is_selected": True
                  },
                  "4205": {
                     "prediction": 0.02673321464301451,
                     "threshold": 0.552,
                     "is_selected": False
                  }
               },
               "403": {
                  "4303": {
                     "prediction": 0.19392275897711828,
                     "threshold": 0.477,
                     "is_selected": False
                  },
                  "4302": {
                     "prediction": 0.6575153403205785,
                     "threshold": 0.437,
                     "is_selected": True
                  },
                  "4304": {
                     "prediction": 0.16765306281055659,
                     "threshold": 0.531,
                     "is_selected": False
                  },
                  "4301": {
                     "prediction": 0.36763649257979164,
                     "threshold": 0.466,
                     "is_selected": False
                  }
               },
               "404": {
                  "4402": {
                     "prediction": 0.5191247601535439,
                     "threshold": 0.362,
                     "is_selected": True
                  },
                  "4404": {
                     "prediction": 0.339974409218916,
                     "threshold": 0.388,
                     "is_selected": False
                  },
                  "4401": {
                     "prediction": 0.6497787329757099,
                     "threshold": 0.412,
                     "is_selected": True
                  },
                  "4403": {
                     "prediction": 0.05719877569185149,
                     "threshold": 0.496,
                     "is_selected": False
                  }
               },
               "405": {
                  "4501": {
                     "prediction": 0.3345749322690216,
                     "threshold": 0.408,
                     "is_selected": False
                  },
                  "4502": {
                     "prediction": 0.036263579989338775,
                     "threshold": 0.555,
                     "is_selected": False
                  }
               },
               "406": {
                  "4501": {
                     "prediction": 0.5140871330119636,
                     "threshold": 0.458,
                     "is_selected": True
                  },
                  "4502": {
                     "prediction": 0.10016284139367371,
                     "threshold": 0.531,
                     "is_selected": False
                  }
               }
            },
            "1": {
               "101": {
                  "1101": {
                     "prediction": 0.02184614050583761,
                     "threshold": 0.488,
                     "is_selected": False
                  },
                  "1102": {
                     "prediction": 0.033680488970003974,
                     "threshold": 0.441,
                     "is_selected": False
                  },
                  "1103": {
                     "prediction": 0.004718158071717391,
                     "threshold": 0.52,
                     "is_selected": False
                  },
                  "1104": {
                     "prediction": 0.011669214703698656,
                     "threshold": 0.402,
                     "is_selected": False
                  }
               },
               "102": {
                  "1201": {
                     "prediction": 0.26524338442953443,
                     "threshold": 0.461,
                     "is_selected": False
                  },
                  "1202": {
                     "prediction": 0.1050092370403923,
                     "threshold": 0.494,
                     "is_selected": False
                  }
               },
               "103": {
                  "1301": {
                     "prediction": 0.002291195622962031,
                     "threshold": 0.594,
                     "is_selected": False
                  },
                  "1302": {
                     "prediction": 0.010626351884389757,
                     "threshold": 0.343,
                     "is_selected": False
                  },
                  "1303": {
                     "prediction": 0.04322088840934965,
                     "threshold": 0.45,
                     "is_selected": False
                  },
                  "1304": {
                     "prediction": 0.010291621828627645,
                     "threshold": 0.413,
                     "is_selected": False
                  }
               },
               "104": {
                  "1401": {
                     "prediction": 0.16749178123946237,
                     "threshold": 0.505,
                     "is_selected": False
                  }
               },
               "106": {
                  "1601": {
                     "prediction": 0.005736095078939357,
                     "threshold": 0.493,
                     "is_selected": False
                  },
                  "1602": {
                     "prediction": 0.018191572767917556,
                     "threshold": 0.495,
                     "is_selected": False
                  }
               },
               "107": {
                  "1701": {
                     "prediction": 0.026198324852997494,
                     "threshold": 0.485,
                     "is_selected": False
                  },
                  "1702": {
                     "prediction": 0.018840579383344536,
                     "threshold": 0.415,
                     "is_selected": False
                  },
                  "1703": {
                     "prediction": 0.0695946912178167,
                     "threshold": 0.479,
                     "is_selected": False
                  },
                  "1704": {
                     "prediction": 0.014002135991399465,
                     "threshold": 0.458,
                     "is_selected": False
                  },
                  "1705": {
                     "prediction": 0.02065314308685415,
                     "threshold": 0.425,
                     "is_selected": False
                  },
                  "1706": {
                     "prediction": 0.003292630224124245,
                     "threshold": 0.345,
                     "is_selected": False
                  },
                  "1707": {
                     "prediction": 0.021075370692313758,
                     "threshold": 0.574,
                     "is_selected": False
                  },
                  "1708": {
                     "prediction": 0.023146975286941988,
                     "threshold": 0.538,
                     "is_selected": False
                  },
                  "1709": {
                     "prediction": 0.01643273543313765,
                     "threshold": 0.457,
                     "is_selected": False
                  },
                  "1710": {
                     "prediction": 0.054271939968198075,
                     "threshold": 0.386,
                     "is_selected": False
                  },
                  "1711": {
                     "prediction": 0.0416491092485789,
                     "threshold": 0.507,
                     "is_selected": False
                  }
               },
               "105": {
                  "1501": {
                     "prediction": 0.17725905675566597,
                     "threshold": 0.445,
                     "is_selected": False
                  }
               },
               "108": {
                  "1801": {
                     "prediction": 0.045700530404026066,
                     "threshold": 0.515,
                     "is_selected": False
                  },
                  "1802": {
                     "prediction": 0.05713121353810124,
                     "threshold": 0.542,
                     "is_selected": False
                  },
                  "1805": {
                     "prediction": 0.026817901728107878,
                     "threshold": 0.046,
                     "is_selected": False
                  },
                  "1804": {
                     "prediction": 0.04438000626319292,
                     "threshold": 0.604,
                     "is_selected": False
                  },
                  "1803": {
                     "prediction": 0.07613507707243626,
                     "threshold": 0.593,
                     "is_selected": False
                  }
               }
            }
         }
      },
      {
         "type": "text",
         "page": 4,
         "x0": 421.04444885253906,
         "y0": 410.0255126953125,
         "x1": 842.0399780273438,
         "y1": 504.550537109375,
         "rect": [
            421.04444885253906,
            410.0255126953125,
            842.0399780273438,
            504.550537109375
         ],
         "text": "Since flooding has been ongoing throughout the rainy season, information is also not always updated and may refer to previous weeks.",
         "textOrder": 16,
         "textCrop": [
            431.0899963378906,
            411.52301025390625,
            813.4745483398438,
            437.80804443359375
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 5,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 311.9906311035156,
         "y1": 842.0399780273438,
         "rect": [
            0.0,
            0.0,
            311.9906311035156,
            842.0399780273438
         ],
         "text": "Nigeria Reference Map Source: OCHA Reference Map 2016",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            80.20994567871094,
            197.041259765625,
            783.3399047851562
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 5,
         "x0": 311.9906311035156,
         "y0": 0.0,
         "x1": 594.9600219726562,
         "y1": 842.0399780273438,
         "rect": [
            311.9906311035156,
            0.0,
            594.9600219726562,
            842.0399780273438
         ],
         "text": "ACAPS Briefing Note: Floods in Nigeria",
         "textOrder": 1,
         "textCrop": [
            426.94000244140625,
            59.276981353759766,
            567.0302124023438,
            829.0839233398438
         ],
         "relevant": False
      },
      {
         "type": "image",
         "page": 5,
         "x0": 28.100000381469727,
         "y0": 107.49298095703125,
         "x1": 551.0699462890625,
         "y1": 763.4429931640625,
         "rect": [
            28.100000381469727,
            107.49298095703125,
            551.0699462890625,
            763.4429931640625
         ],
         "imageLink": "pic-7ca5e8c4-a517-40d0-bb63-3ec1ceeeceb3.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "text",
         "page": 6,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 585.7000122070312,
         "y1": 594.9600219726562,
         "rect": [
            0.0,
            0.0,
            585.7000122070312,
            594.9600219726562
         ],
         "text": "Flood-affected population per number and state (as of 27/09/2019) Source: IFRC EPoA 07/10/2019",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            43.49003601074219,
            497.5,
            564.0039672851562
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 6,
         "x0": 585.7000122070312,
         "y0": 0.0,
         "x1": 842.0399780273438,
         "y1": 594.9600219726562,
         "rect": [
            585.7000122070312,
            0.0,
            842.0399780273438,
            594.9600219726562
         ],
         "text": "ACAPS Briefing Note: Floods in Nigeria",
         "textOrder": 1,
         "textCrop": [
            673.9000244140625,
            22.437015533447266,
            813.990234375,
            582.0039672851562
         ],
         "relevant": False
      },
      {
         "type": "image",
         "page": 6,
         "x0": 106.75,
         "y0": 86.56402587890625,
         "x1": 735.22998046875,
         "y1": 551.8140258789062,
         "rect": [
            106.75,
            86.56402587890625,
            735.22998046875,
            551.8140258789062
         ],
         "imageLink": "pic-fce7650a-aa66-4982-9c06-0cc586966225.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      },
      {
         "type": "text",
         "page": 7,
         "x0": 0.0,
         "y0": 0.0,
         "x1": 528.6150360107422,
         "y1": 594.9600219726562,
         "rect": [
            0.0,
            0.0,
            528.6150360107422,
            594.9600219726562
         ],
         "text": "Seasonal calendar of Nigeria during a typical year Source: FEWS NET",
         "textOrder": 0,
         "textCrop": [
            28.079999923706055,
            43.49003601074219,
            383.3300476074219,
            497.739990234375
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 7,
         "x0": 528.6150360107422,
         "y0": 0.0,
         "x1": 842.0399780273438,
         "y1": 251.58551025390625,
         "rect": [
            528.6150360107422,
            0.0,
            842.0399780273438,
            251.58551025390625
         ],
         "text": "ACAPS Briefing Note: Floods in Nigeria",
         "textOrder": 1,
         "textCrop": [
            673.9000244140625,
            22.437015533447266,
            813.9395141601562,
            33.483978271484375
         ],
         "relevant": False
      },
      {
         "type": "text",
         "page": 7,
         "x0": 528.6150360107422,
         "y0": 251.58551025390625,
         "x1": 784.5990905761719,
         "y1": 594.9600219726562,
         "rect": [
            528.6150360107422,
            251.58551025390625,
            784.5990905761719,
            594.9600219726562
         ],
         "text": "p title",
         "textOrder": 2,
         "textCrop": [
            726.0999755859375,
            469.6870422363281,
            759.6781616210938,
            488.9779968261719
         ],
         "relevant": False
      },
      {
         "type": "image",
         "page": 7,
         "x0": 28.100000381469727,
         "y0": 70.70001220703125,
         "x1": 726.0699462890625,
         "y1": 484.6500244140625,
         "rect": [
            28.100000381469727,
            70.70001220703125,
            726.0699462890625,
            484.6500244140625
         ],
         "imageLink": "pic-7401e7de-52a1-4f8b-b0fd-a409d2da1668.png",
         "imageCaption": "undefined",
         "imageMeta": "undefined",
         "imageText": ""
      }
   ]
}
"""
