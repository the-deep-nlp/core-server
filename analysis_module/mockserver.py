from typing import Any, List, Tuple
import os
import json
import requests
import logging
import random

from random import shuffle
from math import ceil
from celery import shared_task
from sklearn.feature_extraction.text import CountVectorizer

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from core.models import NLPRequest
from core_server.settings import ENDPOINT_NAME
from .mock_templates import MOCK_ENTRY_CLASSIFICATION, MOCK_ENTRY_CLASSIFICATION_FORMATTED, MOCK_GEOLOCATION  # noqa
from .utils import send_callback_url_request


logger = logging.getLogger("__name__")
logger.setLevel(logging.INFO)


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
def process_ngrams(body: dict):
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

    labels = [
        "Sudan Crisis 2022",
        "Earthquake of magnitude 7.2 in 2015",
        "Flood Disaster in Morocco",
        "Human Trafficking in African regions"
    ]

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

    data = {
        idx: {
            "entry_id": excerpt_ids[x:x + ceil(len(excerpt_ids) / clusters)],
            "label": labels[idx] if idx < len(labels) else "Random Cluster Topic"
        }
        for idx, x in enumerate(range(0, len(excerpt_ids), ceil(len(excerpt_ids) / clusters)))
    }

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
        ent = {}
        ent["entity"] = entity["ent"]
        start = random.randint(0, len(excerpt) - len(entity["ent"]))
        ent["meta"] = {
            "offset_start": start,
            "offset_end": start + len(entity["ent"]),
            "latitude": None,
            "longitude": None
        }
        ent["meta"].update({"latitude": None, "longitude": None})
        for geoid in entity["geoids"]:
            if entity["ent"] == geoid["match"]:
                ent["meta"].update({
                    "latitude": geoid["latitude"],
                    "longitude": geoid["longitude"]
                })
                break
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
    for idx, (entry_id, excerpt) in enumerate(excerpts):
        entities = MOCK_GEOLOCATION[idx]
        entities = [shape_geo_entities(entities, excerpt)]
        data.append({"entry_id": int(entry_id), "locations": entities})

    filepath = save_data_local_and_get_url(
        dir_name="geolocation",
        client_id=client_id,
        data=data
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
    process_extraction_mock.apply_async(
        args=(body,), countdown=2
    )  # Trigger task after 2 seconds
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_extraction_mock(body) -> Any:
    documents = body.get("documents") or []
    callback_url = body.get("callback_url")
    if not documents or not callback_url:
        return

    for document in documents:
        client_id = document["client_id"]
        text_extraction_id = "06b46e2a-00b6-4676-a375-8a7b938a17c6"
        random_extracted_text = """
            This is some random extracted text.
            On Human Rights Day, observed annually on December 10th, Palestinian human rights organizations—The Palestinian
            Center for Human Rights, Al Mezan, and Al-Haq—call on the international community to promptly intervene for an
            immediate ceasefire, pressure Israel to halt its aggression and genocide in the Gaza Strip and its violations
            in the entire occupied Palestinian territory, and ensure accountability and justice.
            As the world marks Human Rights Day today, commemorating the adoption of the Universal
            Declaration of Human Rights (UDHR) by the United Nations General Assembly in 1948;
            Israel blatantly and systematically violates the majority of the declaration's articles.
            It subjects 2.3 million Palestinians in Gaza to a genocidal campaign while
            enjoying complete immunity and support from the United States. Despite the US providing Israel with weapons and
            munitions and vetoing the UN Security Council resolution calling for an immediate ceasefire in Gaza, the
            international community has yet to take effective positions to halt the genocide of an entire people.
        """
        filepath = save_data_local_and_get_url(
            "extraction", client_id, random_extracted_text
        )
        callback_data = {
            "text_path": filepath,
            "images_path": [],
            "total_pages": 1,
            "total_words_count": 50,
            "status": NLPRequest.RequestStatus.SUCCESS,
            "client_id": client_id,
            "text_extraction_id": text_extraction_id
        }
        try:
            requests.post(
                callback_url,
                json=callback_data,
                timeout=30,
            )
            logger.info("Successfully send data on callback url for text extraction.")
        except Exception:
            logger.error("Could not send data to callback url", exc_info=True)


def entry_extraction_mock(body) -> Any:
    process_entry_extraction_mock.apply_async(
        args=(body,), countdown=2
    )  # Trigger task after 2 seconds
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_entry_extraction_mock(body) -> Any:
    documents = body.get("documents") or []

    callback_url = body.get("callback_url")
    if not documents or not callback_url:
        return

    for document in documents:
        client_id = document["client_id"]
        text_extraction_id = document["text_extraction_id"]
        # random_extracted_text = "This is some random entry extracted text"
        random_entry_extraction_classification = MOCK_ENTRY_CLASSIFICATION_FORMATTED
        random_entry_extraction_classification.update({
            "classification_model_info": {
                "name": "all_tags_model",
                "version": "1.0.0"
            },
            "client_id": client_id,
            "entry_extraction_id": "73f9ca13-deb2-4f39-8e86-a856490bfc0d",  # random
            "text_extraction_id": text_extraction_id
        })
        filepath = save_data_local_and_get_url(
            "entry_extraction", client_id, random_entry_extraction_classification
        )

        """
        the text_extraction_id is not something easy to retrieve in case the request is
        set with the "url". In both cases, with the url, or the textextractionid, the text
        was already extracted, and it's not (easily) to retrieve the id from the presigned url.
        In the case of a request with the id, is instead possible to get the right document.
        """
        callback_data = {
            "client_id": client_id,
            "entry_extraction_classification_path": filepath,
            "text_extraction_id": text_extraction_id,
            "status": 1
        }
        try:
            requests.post(
                callback_url,
                json=callback_data,
                timeout=30,
            )
            logger.info("Successfully send data on callback url for entry extraction.")
        except Exception:
            logger.error("Could not send data to callback url", exc_info=True)


def entry_classification_mock(body) -> Any:
    process_entry_classification_mock.apply_async(
        args=(body,), countdown=2
    )  # Trigger task after 2 seconds
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_entry_classification_mock(body) -> Any:
    callback_payload = MOCK_ENTRY_CLASSIFICATION
    callback_payload.update({
        "client_id": body["entries"][0]["client_id"],
        "model_info": {
            "id": "all_tags_model",
            "version": "1.0.0"
        },
        "prediction_status": True
    })
    callback_url = body["callback_url"]
    try:
        requests.post(
            callback_url,
            json=callback_payload,
            timeout=30
        )
        logger.info("Successfully send data on callback url for entry classification")
    except Exception:
        logger.error("Could not send data to callback url", exc_info=True)


TYPE_ACTIONS_MOCK = {
    "topicmodel": topicmodeling_mock_model,
    "summarization": summarization_mock_model,
    "summarization-v3": summarization_mock_model,
    "ngrams": ngrams_mock_model,
    "geolocation": geolocation_mock_model,
    "text-extraction": text_extraction_mock,
    "entry-extraction-classification": entry_extraction_mock,
    "entry-classification": entry_classification_mock
}


def process_mock_request(request: dict, request_type: str):
    action = TYPE_ACTIONS_MOCK.get(request_type)
    if action is None:
        raise ValidationError("Invalid request type")

    response, code = action(request)

    if code == 200:
        resp = {
            "client_id": request["documents"][0].get("client_id", "")
            if "documents" in request else request.get("client_id", ""),
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
