#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from freedan.adwords_objects.account import Account
from freedan.adwords_objects.adgroup import AdGroup
from freedan.adwords_objects.campaign import Campaign
from freedan.adwords_objects.campaign_budget import CampaignBudget
from freedan.adwords_objects.extended_text_ad import ExtendedTextAd
from freedan.adwords_objects.keyword import Keyword
from freedan.adwords_objects.keyword_final_url import KeywordFinalUrl
from freedan.adwords_objects.negative_keyword import NegativeKeyword
from freedan.adwords_objects.shared_set_overview import SharedSetOverview

from freedan.adwords_services.adwords import AdWords
from freedan.adwords_services.adwords_batch_uploader import AdWordsBatchJober
from freedan.adwords_services.adwords_standard_uploader import AdWordsStandardUploader
from freedan.adwords_services.adwords_error import AdWordsError
from freedan.adwords_services.adwords_label import AdWordsLabel
from freedan.adwords_services.report_normaliser import ReportNormaliser

from freedan.other_services.drive import Drive
from freedan.other_services.error_retryer import ErrorRetryer
from freedan.other_services.initiator import Initiator
from freedan.other_services.text_handler import TextHandler
from freedan.other_services.time_instance import TimeInstance


def from_json(json_path):
    """ Reads a json file and returns a dictionary with its content
    :param json_path: str, path of json file
    :return: dict
    """
    with open(json_path, mode="r") as json_file:
        return json.load(json_file)
