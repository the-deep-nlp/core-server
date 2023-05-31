from typing import Any, List, Tuple
import os
import json
import requests
import logging
import random
import numpy as np
from random import shuffle
from math import ceil
from celery import shared_task
from sklearn.feature_extraction.text import CountVectorizer

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from core.models import NLPRequest
from core_server.settings import ENDPOINT_NAME
from .utils import send_callback_url_request

logging.getLogger().setLevel(logging.INFO)

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

MOCK_ENTRY_CLASSIFICATION = {
  "classifications": [
    {
      "client_id": "5",
      "model_preds": {
        "2": {
          "204": {
            "2402": {
              "prediction": 0.4069949281240046,
              "threshold": 0.489,
              "is_selected": False
            },
            "2401": {
              "prediction": 0.27091098129102825,
              "threshold": 0.461,
              "is_selected": False
            }
          }
        }
      }
    },
    {
      "client_id": "7",
      "model_preds": {
        "2": {
          "204": {
            "2402": {
              "prediction": 0.5442236220665992,
              "threshold": 0.489,
              "is_selected": True
            },
            "2401": {
              "prediction": 0.4262570897824335,
              "threshold": 0.461,
              "is_selected": False
            }
          },
          "202": {
            "2206": {
              "prediction": 0.25068859880169236,
              "threshold": 0.576,
              "is_selected": False
            },
            "2201": {
              "prediction": 0.5456802809044823,
              "threshold": 0.431,
              "is_selected": True
            }
          }
        },
        "5": {
          "503": {
            "5303": {
              "prediction": 0.12105567270217965,
              "threshold": 0.438,
              "is_selected": False
            },
            "5306": {
              "prediction": 0.0934217669913229,
              "threshold": 0.424,
              "is_selected": False
            },
            "5310": {
              "prediction": 0.2706523782039786,
              "threshold": 0.478,
              "is_selected": False
            },
            "5302": {
              "prediction": 0.10373815047470006,
              "threshold": 0.44,
              "is_selected": False
            },
            "5307": {
              "prediction": 0.10675184680643865,
              "threshold": 0.414,
              "is_selected": False
            },
            "5309": {
              "prediction": 0.15713495668023825,
              "threshold": 0.512,
              "is_selected": False
            },
            "5308": {
              "prediction": 0.2450807941587348,
              "threshold": 0.475,
              "is_selected": False
            },
            "5301": {
              "prediction": 0.16692731163052263,
              "threshold": 0.488,
              "is_selected": False
            },
            "5305": {
              "prediction": 0.09886651321893601,
              "threshold": 0.508,
              "is_selected": False
            },
            "5304": {
              "prediction": 0.18824445637496742,
              "threshold": 0.444,
              "is_selected": False
            }
          },
          "501": {
            "5102": {
              "prediction": 0.21789910171917756,
              "threshold": 0.541,
              "is_selected": False
            },
            "5109": {
              "prediction": 0.3480727123794051,
              "threshold": 0.454,
              "is_selected": False
            },
            "5106": {
              "prediction": 0.23486564947864202,
              "threshold": 0.381,
              "is_selected": False
            },
            "5108": {
              "prediction": 0.05966722541108756,
              "threshold": 0.527,
              "is_selected": False
            },
            "5111": {
              "prediction": 0.46915922655621894,
              "threshold": 0.447,
              "is_selected": True
            },
            "5107": {
              "prediction": 0.3090465321041693,
              "threshold": 0.449,
              "is_selected": False
            },
            "5101": {
              "prediction": 0.015221919587000888,
              "threshold": 0.47,
              "is_selected": False
            },
            "5103": {
              "prediction": 0.3523940058170018,
              "threshold": 0.482,
              "is_selected": False
            },
            "5104": {
              "prediction": 0.003284739766450025,
              "threshold": 0.786,
              "is_selected": False
            },
            "5105": {
              "prediction": 0.22805604930227613,
              "threshold": 0.534,
              "is_selected": False
            },
            "5110": {
              "prediction": 0.20070979371666908,
              "threshold": 0.05,
              "is_selected": True
            }
          }
        },
        "4": {
          "401": {
            "4102": {
              "prediction": 0.004212768160319299,
              "threshold": 0.814,
              "is_selected": False
            },
            "4101": {
              "prediction": 0.4228575605351778,
              "threshold": 0.422,
              "is_selected": True
            }
          }
        }
      }
    }
  ]
}


def get_entries_data(url: str) -> Any:
    """get data"""
    response = requests.get(url)
    entries_data = json.loads(response.text)
    return entries_data


def save_data_local_and_get_url(dir_name: str, client_id: str, data: Any) -> str:
    """save"""
    parent_dirpath = f"media/mock_responses/{dir_name}"
    if not os.path.exists(parent_dirpath):
        os.makedirs(parent_dirpath)

    filepath = os.path.join(parent_dirpath, f"{client_id}.json")
    filepath_local = os.path.join("/tmp", filepath)

    with open(filepath_local, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
    return os.path.join(
        ENDPOINT_NAME, filepath
    )  # NOTE: this should be handled from external proxy server


def get_ngrams(
    entries: list,
    ngram_from: int = 1,
    ngram_to: int = 1,
    n: int = 10,
    max_features: int = 20000,
) -> List[Tuple[str, int]]:
    vec = CountVectorizer(
        ngram_range=(ngram_from, ngram_to),
        max_features=max_features,
        stop_words="english",
    ).fit(entries)
    bag_of_words = vec.transform(entries)
    sum_words = bag_of_words.sum(axis=0).tolist()
    words_freq = [(word, sum_words[0][i]) for word, i in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
    return words_freq[:n]


@shared_task
def process_ngrams(body):
    request_body = body if isinstance(body, dict) else json.loads(body)

    client_id = request_body.get("client_id")
    entries_url = request_body.get("entries_url")
    callback_url = request_body.get("callback_url")

    unigrams = request_body.get("ngrams_config").get("generate_unigrams")
    bigrams = request_body.get("ngrams_config").get("generate_bigrams")
    trigrams = request_body.get("ngrams_config").get("generate_trigrams")
    max_items = request_body.get("ngrams_config").get("max_ngrams_items")

    try:
        excerpts = [x["excerpt"] for x in get_entries_data(entries_url)]
    except Exception:
        send_callback_url_request(
            callback_url=callback_url,
            client_id=client_id,
            filepath="",
            status=NLPRequest.RequestStatus.PROCESS_INPUT_URL_FAILED,
        )
        return

    data = {}
    if unigrams:
        data.update(
            {"unigrams": {k: v for k, v in get_ngrams(excerpts, 1, 1, max_items)}}
        )
    if bigrams:
        data.update(
            {"bigrams": {k: v for k, v in get_ngrams(excerpts, 2, 2, max_items)}}
        )
    if trigrams:
        data.update(
            {"trigrams": {k: v for k, v in get_ngrams(excerpts, 3, 3, max_items)}}
        )

    filepath = save_data_local_and_get_url(
        dir_name="ngrams",
        client_id=client_id,
        data=data,
    )

    send_callback_url_request(
        callback_url=callback_url,
        client_id=client_id,
        filepath=filepath,
        status=NLPRequest.RequestStatus.SUCCESS,
    )


def ngrams_mock_model(body) -> Any:
    process_ngrams.delay(body)
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_summarization(body: dict) -> Any:
    request_body = body if isinstance(body, dict) else json.loads(body)

    client_id = request_body.get("client_id")
    entries_url = request_body.get("entries_url")
    callback_url = request_body.get("callback_url")

    try:
        excerpts = [x["excerpt"] for x in get_entries_data(entries_url)]
    except Exception:
        send_callback_url_request(
            callback_url=callback_url,
            client_id=client_id,
            filepath="",
            status=NLPRequest.RequestStatus.PROCESS_INPUT_URL_FAILED,
        )
        return

    data = " ".join(["This is a fake response.\n"] + excerpts)
    filepath = save_data_local_and_get_url(
        dir_name="summarization", client_id=client_id, data=data
    )

    send_callback_url_request(
        callback_url=callback_url,
        client_id=client_id,
        filepath=filepath,
        status=NLPRequest.RequestStatus.SUCCESS,
    )


def summarization_mock_model(body) -> Any:
    process_summarization.delay(body)
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_topicmodeling(body) -> Any:
    """topic modeling"""
    request_body = body if isinstance(body, dict) else json.loads(body)

    client_id = request_body.get("client_id")
    entries_url = request_body.get("entries_url")
    callback_url = request_body.get("callback_url")
    clusters = request_body.get("max_clusters_num", 5)

    try:
        excerpt_ids = [x["entry_id"] for x in get_entries_data(entries_url)]
    except Exception:
        send_callback_url_request(
            callback_url=callback_url,
            client_id=client_id,
            filepath="",
            status=NLPRequest.RequestStatus.PROCESS_INPUT_URL_FAILED,
        )
        return

    shuffle(excerpt_ids)

    data = [
        excerpt_ids[x: x + ceil(len(excerpt_ids) / clusters)]
        for x in range(0, len(excerpt_ids), ceil(len(excerpt_ids) / clusters))
    ]

    data = {key: val for key, val in enumerate(data)}

    filepath = save_data_local_and_get_url(
        dir_name="topicmodel", client_id=client_id, data=data
    )

    send_callback_url_request(
        callback_url=callback_url,
        client_id=client_id,
        filepath=filepath,
        status=NLPRequest.RequestStatus.SUCCESS,
    )


def topicmodeling_mock_model(body) -> Any:
    process_topicmodeling.delay(body)
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_geolocation(body) -> Any:
    """geolocation extraction"""

    def shape_geo_entities(entity: dict, excerpt: str):
        ent = entity.copy()
        start = random.randint(0, len(excerpt) - len(ent["ent"]))
        ent.update({"offset_start": start, "offset_end": start + len(ent["ent"])})
        return ent

    request_body = body if isinstance(body, dict) else json.loads(body)

    client_id = request_body.get("client_id")
    entries_url = request_body.get("entries_url")
    callback_url = request_body.get("callback_url")

    try:
        excerpts = [
            (x["entry_id"], x["excerpt"]) for x in get_entries_data(entries_url)
        ]
    except Exception:
        send_callback_url_request(
            callback_url=callback_url,
            client_id=client_id,
            filepath="",
            status=NLPRequest.RequestStatus.PROCESS_INPUT_URL_FAILED,
        )
        return

    data = []
    for entry_id, excerpt in excerpts:
        entities = list(
            np.random.choice(
                MOCK_GEOLOCATION, size=random.randint(0, len(MOCK_GEOLOCATION))
            )
        )
        entities = [shape_geo_entities(x, excerpt) for x in entities]
        data.append({"entry_id": int(entry_id), "entities": entities})

    filepath = save_data_local_and_get_url(
        dir_name="geolocation", client_id=client_id, data=data
    )

    send_callback_url_request(
        callback_url=callback_url,
        client_id=client_id,
        filepath=filepath,
        status=NLPRequest.RequestStatus.SUCCESS,
    )


def geolocation_mock_model(body) -> Any:
    process_geolocation.delay(body)
    return json.dumps({"status": "Successfully received the request."}), 200


def text_extraction_mock(body) -> Any:
    return {}


TYPE_ACTIONS_MOCK = {
    "topicmodel": topicmodeling_mock_model,
    "summarization": summarization_mock_model,
    "summarization-v2": summarization_mock_model,
    "ngrams": ngrams_mock_model,
    "geolocation": geolocation_mock_model,
    "text_extraction": text_extraction_mock,
}


def process_mock_request(request: dict, request_type: str):
    action = TYPE_ACTIONS_MOCK.get(request_type)
    if action is None:
        raise ValidationError("Invalid request type")

    response, code = action(request)

    if code == 200:
        resp = {
            "client_id": request.get("client_id"),
            "type": request_type,
            "message": "Request has been successfully processed",
        }

        return Response(
            resp,
            status=status.HTTP_202_ACCEPTED,
        )

    else:
        return Response(
            {"message": response["status"]},
            status=status.HTTP_400_BAD_REQUEST,
        )
