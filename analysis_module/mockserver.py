from typing import Any, List, Tuple
import os
import json
import requests
import logging
from random import shuffle
from math import ceil
from celery import shared_task
from sklearn.feature_extraction.text import CountVectorizer

from analysis_module.models import AnalysisModuleRequest
from core_server.settings import ENDPOINT_NAME
from .utils import send_callback_url_request

logging.getLogger().setLevel(logging.INFO)


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
    filepath_local = os.path.join('/tmp', filepath)

    with open(filepath_local, "w", encoding='utf-8') as f:
        f.write(json.dumps(data))
    return os.path.join(ENDPOINT_NAME, filepath)  # NOTE: this should be handled from external proxy server


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
            status=AnalysisModuleRequest.RequestStatus.PROCESS_INPUT_URL_FAILED,
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
        dir_name="ngrams", client_id=client_id, data=data,
    )

    send_callback_url_request(
        callback_url=callback_url,
        client_id=client_id,
        filepath=filepath,
        status=AnalysisModuleRequest.RequestStatus.SUCCESS,
    )


def ngramsmodel(body) -> Any:
    process_ngrams.delay(body)
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_summarization(body: dict) -> Any:
    request_body = body if isinstance(body, dict) else json.loads(body)

    client_id = request_body.get("client_id")
    entries_url = request_body.get("entries_url")
    callback_url = request_body.get("callback_url")

    excerpts = [x["excerpt"] for x in get_entries_data(entries_url)]
    try:
        excerpts = [x["excerpt"] for x in get_entries_data(entries_url)]
    except Exception:
        send_callback_url_request(
            callback_url=callback_url,
            client_id=client_id,
            filepath="",
            status=AnalysisModuleRequest.RequestStatus.PROCESS_INPUT_URL_FAILED,
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
        status=AnalysisModuleRequest.RequestStatus.SUCCESS,
    )


def summarizationmodel(body) -> Any:
    process_summarization.delay(body)
    return json.dumps({"status": "Successfully received the request."}), 200


@shared_task
def process_topicmodeling(body) -> Any:
    """topic modeling"""
    clusters = 5
    request_body = body if isinstance(body, dict) else json.loads(body)

    client_id = request_body.get("client_id")
    entries_url = request_body.get("entries_url")
    callback_url = request_body.get("callback_url")

    try:
        excerpt_ids = [x["entry_id"] for x in get_entries_data(entries_url)]
    except Exception:
        send_callback_url_request(
            callback_url=callback_url,
            client_id=client_id,
            filepath="",
            status=AnalysisModuleRequest.RequestStatus.PROCESS_INPUT_URL_FAILED,
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
        status=AnalysisModuleRequest.RequestStatus.SUCCESS,
    )


def topicmodelingmodel(body) -> Any:
    process_topicmodeling.delay(body)
    return json.dumps({"status": "Successfully received the request."}), 200
